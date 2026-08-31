import streamlit as st
from pandas import DataFrame


def show_player_metrics(player: str, players: DataFrame, mode: int):
    stats = (players.loc[players['Player'] == player]).iloc[0]
    if mode == 1:
        pts, ast = st.columns(2)
        trb, mpg = st.columns(2)
        games, fg = st.columns(2)
        threep, ft = st.columns(2)

    elif mode == 2:
        pts, ast, trb, mpg = st.columns(4)
        games, fg, threep, ft = st.columns(4)
    else:
        return None
    with pts:
        st.metric(
            label='Points per game',
            value=stats['PTS']
        )
    with ast:
        st.metric(
            label='Assists per game',
            value=stats['AST']
        )
    with trb:
        st.metric(
            label='Rebounds per game',
            value=stats['TRB']
        )
    with mpg:
        st.metric(
            label='Minutes per game',
            value=stats['MPG']
        )
    with games:
        st.metric(
            label='Games played',
            value=stats['Games']
        )
    with fg:
        st.metric(
            label='Field goal percentage',
            value=f'{stats['FG%']}%'
        )
    with threep:
        st.metric(
            label='Three point percentage',
            value=f'{stats['3P%']}%'
        )
    with ft:
        st.metric(
            label='Free throw percentage',
            value=f'{stats['FT%']}%'
        )

