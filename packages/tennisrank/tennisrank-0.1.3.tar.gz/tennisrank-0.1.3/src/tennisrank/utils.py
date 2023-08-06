import difflib
import pandas as pd

from tennisrank.model import Player, Match


def df_to_matches(df):
    df['point_diff'] = (df['w_1stWon'] + df['w_2ndWon']) - (
        df['l_1stWon'] + df['l_2ndWon'])
    for idx, row in df.iterrows():
        winner = Player(id=row['winner_id'], name=row['winner_name'])
        loser = Player(id=row['loser_id'], name=row['loser_name'])
        surface = row['surface'].lower()
        point_diff = row['point_diff']
        yield Match(winner=winner, loser=loser, point_diff=point_diff, surface=surface)


def fuzzy_match(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


def load_matches(urls):
    def iter_matches():
        for url in urls:
            df = pd.read_csv(url)
            yield from df_to_matches(df)
    return list(iter_matches())


def load_atp(*years):
    urls = [(
            'https://raw.githubusercontent.com/JeffSackmann/'
            f'tennis_atp/master/atp_matches_{year}.csv'
            )
            for year in years
            ]
    return load_matches(urls)


def load_wta(*years):
    urls = [(
            'https://raw.githubusercontent.com/JeffSackmann/'
            f'tennis_wta/master/wta_matches_{year}.csv'
            )
            for year in years
            ]
    return load_matches(urls)
