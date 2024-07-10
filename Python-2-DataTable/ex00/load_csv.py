import pandas as pd


def load(path: str):
    '''
    Take a path to load a csv file
    '''
    try:
        return pd.read_csv(path)
    except Exception:
        return None
