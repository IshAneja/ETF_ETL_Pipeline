import requests
import pandas as pd
from sqlalchemy import create_engine
import time
import logging
from dotenv import load_dotenv
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Alpha Vantage config
load_dotenv()
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY') # Ensure you have an .env file with this key
BASE_URL = 'https://www.alphavantage.co/query'
ETF_SYMBOLS = ['SPY', 'QQQ', 'VTI']  # You can customize this list

# Step 1: Extract
def extract_etf_data(symbol):
    logging.info(f"Extracting data for {symbol}")
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': symbol,
        'apikey': API_KEY,
        'outputsize': 'compact',  # 'full' gets all data
        'datatype': 'json'
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

# Step 2: Transform
def transform_data(symbol, data):
    logging.info(f"Transforming data for {symbol}")
    time_series = data.get('Time Series (Daily)', {})
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df = df.rename(columns={
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. adjusted close': 'adjusted_close',
        '6. volume': 'volume'
    })
    df.index = pd.to_datetime(df.index)
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'date'}, inplace=True)
    df['symbol'] = symbol
    df = df[['date', 'symbol', 'open', 'high', 'low', 'close', 'adjusted_close', 'volume']]
    return df

# Step 3: Load
def load_data(df, db_engine):
    logging.info(f"Loading data for {df['symbol'].iloc[0]}")
    df.to_sql('etf_prices', db_engine, if_exists='append', index=False)

# Main ETL Runner
def run_etl():
    engine = create_engine('sqlite:///etf_prices.db')
    for symbol in ETF_SYMBOLS:
        try:
            raw_data = extract_etf_data(symbol)
            transformed_df = transform_data(symbol, raw_data)
            load_data(transformed_df, engine)
            time.sleep(12)  # Alpha Vantage rate limit: 5 requests/minute
        except Exception as e:
            logging.error(f"Error processing {symbol}: {e}")

if __name__ == "__main__":
    run_etl()
