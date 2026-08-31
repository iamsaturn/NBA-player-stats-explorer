import pandas as pd
import sqlite3
import streamlit as st

from src.data import (
    aggregate_players,
    clean_data,
    load_data,
    games_by_date,
)

from player import show_player_metrics


df = load_data('data/nbadata.csv')
df = clean_data(df)
players = aggregate_players(df)

connection = sqlite3.connect(':memory:')

players.to_sql(
    'Players',
    connection,
    if_exists='replace',
    index=False,
)

player_list = sorted(players['Player'].tolist())

metric_options = {
    'Points': 'PTS',
    'Assists': 'AST',
    'Rebounds': 'TRB',
}

ranking_metric_options = {
    'Points': 'PTS',
    'Assists': 'AST',
    'Rebounds': 'TRB',
    'Minutes': 'MPG',
}


st.title('NBA Player Stats Explorer 2026')

(
    player_expl_tab,
    player_comparison_tab,
    performance_history_tab,
    league_rankings_tab,
) = st.tabs(
    [
        'Player Explorer',
        'Compare Players',
        'Performance History',
        'League Rankings',
    ]
)


with player_expl_tab:

    selected_player = st.selectbox(
        'Select player',
        options=player_list,
        index=None,
        placeholder='Type player name...',
    )

    if selected_player:

        show_player_metrics(
            player=selected_player,
            players=players,
            mode=2,
        )


with player_comparison_tab:

    player1, player2 = st.columns(2)

    with player1:

        selected_player1 = st.selectbox(
            'Select player 1',
            options=player_list,
            index=None,
            placeholder='Type player name...',
        )

        if selected_player1:

            show_player_metrics(
                player=selected_player1,
                players=players,
                mode=1,
            )

    with player2:

        selected_player2 = st.selectbox(
            'Select player 2',
            options=player_list,
            index=None,
            placeholder='Type player name...',
        )

        if selected_player2:

            show_player_metrics(
                player=selected_player2,
                players=players,
                mode=1,
            )


with performance_history_tab:

    select_player_performance, select_metric = st.columns(2)

    with select_player_performance:

        selected_player_performance = st.selectbox(
            label='Select player for chart',
            options=player_list,
            index=None,
            placeholder='Type player name...',
        )

    with select_metric:

        selected_metric = st.selectbox(
            label='Select metric',
            options=metric_options.keys(),
            index=None,
            placeholder='Type metric...',
        )

    if selected_player_performance and selected_metric:

        history = games_by_date(
            selected_player_performance,
            df,
            metric_options[selected_metric],
        )

        st.line_chart(
            data=history,
            x='Date',
            x_label='Date',
            y=metric_options[selected_metric],
            y_label=selected_metric,
        )


with league_rankings_tab:

    st.subheader('League Rankings')

    ranking_metric = st.selectbox(
        'Select ranking metric',
        options=ranking_metric_options.keys(),
    )

    ranking_column = ranking_metric_options[ranking_metric]

    page_size = 10

    page = st.number_input(
        'Page',
        min_value=1,
        value=1,
        step=1,
    )

    offset = (page - 1) * page_size

    query = f"""
    SELECT Player, {ranking_column}, Games
    FROM Players
    WHERE Games >= 20
    ORDER BY {ranking_column} DESC
    LIMIT {page_size}
    OFFSET {offset}
    """

    ranking = pd.read_sql_query(
        query,
        connection,
    )

    st.dataframe(
        ranking,
        hide_index=True,
        use_container_width=True,
    )