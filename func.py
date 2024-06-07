import requests
import os
import psycopg2
import pandas as pd
from datetime import datetime
from airflow.hooks.postgres_hook import PostgresHook

df = pd.DataFrame()

def extract():        # Extract phase

    pairs = ["BTC", "ETH", "LTC", "XRP", "SOL"]
    exchange_rates = []
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for pair in pairs:
        url = "https://alpha-vantage.p.rapidapi.com/query"

        querystring = {"from_currency":pair,"function":"CURRENCY_EXCHANGE_RATE","to_currency":"USD"}

        headers = {
            "x-rapidapi-key": "#############################",
            "x-rapidapi-host": "alpha-vantage.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        json_response = response.json()
        if "Realtime Currency Exchange Rate" in json_response:
            currency_data = json_response["Realtime Currency Exchange Rate"]
            exchange_rate = round(float(currency_data["5. Exchange Rate"]), 3)
            exchange_rates.append(exchange_rate)
        else:
            print(f"API response for {pair} is missing expected data.")
            break

    df = pd.DataFrame({
        "Timestamp": [current_time],
        "BTC": float(exchange_rates[0]),
        "BTC_change": 0.0,
        "ETH": float(exchange_rates[1]),
        "ETH_change": 0.0,
        "LTC": float(exchange_rates[2]),
        "LTC_change": 0.0,
        "XRP": float(exchange_rates[3]),
        "XRP_change": 0.0,
        "SOL": float(exchange_rates[4]),
        "SOL_change": 0.0
    })

    df.head()
    print(df)
    df.to_csv('table1.csv', mode='a', header=not os.path.exists('table1.csv'), index=False)
    return df

def transform_s(df):
    df = pd.read_csv('table.csv')           # Read the CSV file into a DataFrame
    last_row = df.iloc[-1]                  # Store the last row in a variable
    df = df.iloc[:-1]                       # Remove the last row from the DataFrame
    df.to_csv('table.csv', index=False)
    df = pd.read_csv('table.csv')

    # Check the data types of the columns
    print(df.dtypes)

    # Convert non-numeric columns to numeric
    for col in df.columns[1:]:
        if df[col].dtype != 'float64':
            for col in df.columns[1:]:
                df[f"{col}_change"] = df[col].diff()
                df.loc[0, f"{col}_change"] = 0
                df[f"{col}_change"] = df[f"{col}_change"].apply(lambda x: f"+{round(abs(x), 7)}" if x >= 0 else f"-{round(abs(x), 5)}")

    # Reorder the columns
    reorder_columns = ['Timestamp', 'BTC', 'BTC_change', 'ETH', 'ETH_change', 'LTC', 'LTC_change', 'XRP', 'XRP_change', 'SOL', 'SOL_change']
    df = df[reorder_columns]

    # Append the last row to the DataFrame
    df = pd.concat([df, pd.DataFrame([last_row])], ignore_index=True)

    # Write the DataFrame to a CSV file
    df.to_csv('table.csv', mode='w', header=True, index=False)

    print(df)
    return df

def transform():
    df = pd.read_csv('table1.csv')
    last_row = df.iloc[-1]
    df = df[:-1]
    #df.to_csv('table2.csv', mode='w', header=not os.path.exists('table2.csv'), index=False)
    df.to_csv('table2.csv', mode='w', index=False)
    df = pd.read_csv('table2.csv')

    changes = {}

    # Iterate through the columns to calculate the changes
    for col in ["BTC", "ETH", "LTC", "XRP", "SOL"]:
        if df.empty:    # Check if previous price exists and is not null
            previous_price = 0  # Set previous_price to 0 if missing
        else:
            previous_price = df.iloc[-1][col]

        current_price = last_row[col]
        price_change = round(current_price - previous_price, 7)
        if price_change > 0:
            changes[f"{col}_change"] = f"+{price_change:.7f}"
        else:
            changes[f"{col}_change"] = f"{price_change:.7f}"

    # Assign the calculated changes to the last row
    for key, value in changes.items():
        last_row[key] = value

    # Append the updated last row back to the DataFrame
    last_row_df = pd.DataFrame([last_row])
    df = pd.concat([df, last_row_df], ignore_index=True)

    # Save the updated DataFrame back to 'table.csv'
    rows_to_drop = len(df) - 1  # drop all rows except last
    df = df.iloc[rows_to_drop:]
    df.to_csv('table.csv', mode='a', index=False, header=False)

    return df


def load():
    df = pd.read_csv('table.csv')
    last_row = df.iloc[-1]

    # Connect to PostgreSQL using Airflow's PostgresHook
    pg_hook = PostgresHook(postgres_conn_id='postgres_default')
    conn = pg_hook.get_conn()
    cur = conn.cursor()

    # SQL Insert Statement
    sql = """
    INSERT INTO prices_and_change (
        Timestamp,
        BTC, BTC_change,
        ETH, ETH_change,
        LTC, LTC_change,
        XRP, XRP_change,
        SOL, SOL_change
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        last_row['Timestamp'], 
        last_row['BTC'], last_row['BTC_change'],
        last_row['ETH'], last_row['ETH_change'],
        last_row['LTC'], last_row['LTC_change'],
        last_row['XRP'], last_row['XRP_change'],
        last_row['SOL'], last_row['SOL_change']
    )

    cur.execute(sql, values)
    conn.commit()

    print("Uploaded to database")

    cur.close()
    conn.close()

load()
