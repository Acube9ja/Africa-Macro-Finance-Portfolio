import wbgapi as wb
import pandas as pd
from fredapi import Fred
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_wb(indicators: dict, countries: list, start: int, end: int) -> pd.DataFrame:
    frames = []
    for name, code in indicators.items():
        df = wb.data.DataFrame(code, countries, range(start, end + 1))
        df = df.stack().reset_index()
        df.columns = ['country', 'year', name]
        df['year'] = df['year'].str.replace('YR', '').astype(int)
        frames.append(df)

    result = frames[0]
    for df in frames[1:]:
        result = result.merge(df, on=['country', 'year'], how='outer')

    return result.sort_values(['country', 'year']).reset_index(drop=True)


def fetch_fred(series: dict, start: str = '2000-01-01') -> pd.DataFrame:
    fred = Fred(api_key=os.getenv('FRED_API_KEY'))
    frames = {name: fred.get_series(code, observation_start=start)
              for name, code in series.items()}
    return pd.DataFrame(frames)


def save_data(df: pd.DataFrame, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"Saved: {path}")