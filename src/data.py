import pandas as pd


def minutes_to_decimal(time: str) -> float:
    parts = time.split(':')
    minutes = int(parts[0])
    seconds = int(parts[1]) / 60

    return round(minutes+seconds, 2)


def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.loc[df['MP'] != '0:00'].copy()
    df = df.dropna(axis=1, how='all')
    df['MP_minutes'] = df['MP'].apply(minutes_to_decimal)

    return df


def aggregate_players(df: pd.DataFrame) -> pd.DataFrame:
    players = (
        df.groupby('Player')[['PTS', 'AST', 'TRB']]
        .mean()
        .round(2)
    )
    players['Games'] = df.groupby('Player').size()

    fg = df.groupby('Player')['FG'].sum()
    fga = df.groupby('Player')['FGA'].sum()

    players['FG%'] = (fg / fga * 100).round(2)
    three_p = df.groupby('Player')['3P'].sum()
    three_pa = df.groupby('Player')['3PA'].sum()
    players['3P%'] = (three_p / three_pa * 100).round(2)

    ft = df.groupby('Player')['FT'].sum()
    fta = df.groupby('Player')['FTA'].sum()

    players['FT%'] = (ft / fta * 100).round(2)

    players['MPG'] = (df.groupby('Player')['MP_minutes'].mean().round(2))
    players = players.reset_index()

    return players


def games_by_date(player: str, df: pd.DataFrame, metric: str) -> pd.DataFrame:
    player_games_by_date = df.loc[
        df['Player'] == player, ['Date', metric]
    ].sort_values(by='Date')

    player_games_by_date['Date'] = pd.to_datetime(
        player_games_by_date['Date']
    )
    return player_games_by_date
