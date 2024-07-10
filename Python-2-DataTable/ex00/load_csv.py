import pandas as pd


def load(path: str):
    try:
        return pd.read_csv(path)
    except Exception:
        return None
