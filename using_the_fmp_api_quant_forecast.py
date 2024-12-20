# -*- coding: utf-8 -*-
"""Using the FMP API-Quant Forecast.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1m57cGuZjX5pfaCSgBLtJIqpD6IPqicXw
"""

#!/usr/bin/env python
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import certifi
import json

def get_jsonparsed_data(url):
    response = urlopen(url, cafile=certifi.where())
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("https://financialmodelingprep.com/api/v3/search?query=AA&apikey=qVXvjPhg98aEFqlvCHfmX1lBWWoXbYF4")
print(get_jsonparsed_data(url))

type(url)

"""Code to search Ticker"""

url = ("https://financialmodelingprep.com/api/v3/search-ticker?query=META&exchange=NASDAQ&apikey=qVXvjPhg98aEFqlvCHfmX1lBWWoXbYF4")
print(get_jsonparsed_data(url))

"""Code to search Name of the Company"""

url = ("https://financialmodelingprep.com/api/v3/search-name?query=META&limit=1&exchange=NASDAQ&apikey=qVXvjPhg98aEFqlvCHfmX1lBWWoXbYF4")
print(get_jsonparsed_data(url))

url = ("https://financialmodelingprep.com/api/v3/search-name?query=Meta&limit=1&exchange=NASDAQ&apikey=qVXvjPhg98aEFqlvCHfmX1lBWWoXbYF4")
print(get_jsonparsed_data(url))

"""Searching for a particular stock ticker"""

url = ("https://financialmodelingprep.com/api/v3/profile/AAPL?apikey=qVXvjPhg98aEFqlvCHfmX1lBWWoXbYF4")
print(get_jsonparsed_data(url))

"""FMP's Income Statement API provides access to real-time income statement data for a wide range of companies, including public companies, private companies, and ETFs. This data can be used to track a company's profitability over time, to compare a company to its competitors, and to identify trends in a company's business."""

inst = get_jsonparsed_data(f"https://financialmodelingprep.com/api/v3/income-statement/{'AAPL'}?period=annual&apikey=qVXvjPhg98aEFqlvCHfmX1lBWWoXbYF4")

inst

import pandas as pd
df1 = pd.DataFrame(inst)
df1 = df1.set_index(['date'])
df1

df1.isnull().sum()

"""preparing the dataset for annual prediction of a stock"""

import pandas as pd
import requests

# List of NASDAQ 100 companies (only symbols are needed for API requests)
nasdaq_100_companies = [
    "AAPL", "MSFT", "AMZN", "NVDA", "GOOGL", "META", "TSLA", "AVGO", "PEP", "COST",
    "ADBE", "CSCO", "TXN", "CMCSA", "NFLX", "AMD", "INTC", "CHTR", "QCOM", "PYPL",
    "SBUX", "ISRG", "BKNG", "GILD", "REGN", "ADI", "TEAM", "DOCU", "ZM", "AMGN",
    "ILMN", "CSX", "MAR", "CTAS", "DXCM", "WDAY", "MNST", "NXPI", "LULU", "EBAY",
    "ORLY", "MELI", "KDP", "ROST", "MCHP", "PCAR", "PANW", "CDNS", "VRTX", "LRCX",
    "KLAC", "ADP", "BIIB", "AMAT", "SNPS", "XLNX", "IDXX", "SPLK", "ALGN", "HOLX",
    "CDNS", "ILMN", "ADSK", "SGEN", "ZBRA", "NTES", "DOCU", "FTNT", "VRSK", "TMUS",
    "CHTR", "CTSH", "XEL", "LBTYA", "TTWO", "EXPE", "EA", "LUMN", "SWKS", "MTCH",
    "MRNA", "OKTA", "ZM", "CMG", "BMRN", "SNOW", "ODFL", "DDOG", "TTD", "PDD",
    "CSGP", "MRVL", "ZS", "CRWD", "EPAM", "PAYX", "FAST", "CERN", "SIRI", "ATUS",
    "NTAP"
]

# Define a function to get JSON data from the API
def get_jsonparsed_data(url):
    response = requests.get(url)
    return response.json()

# Initialize an empty DataFrame
df = pd.DataFrame()

# API key for Financial Modeling Prep
api_key = "qVXvjPhg98aEFqlvCHfmX1lBWWoXbYF4"

# Fetch data for each company and concatenate into the main DataFrame
for symbol in nasdaq_100_companies:
    url = f"https://financialmodelingprep.com/api/v3/balance-sheet-statement/{symbol}?period=annual&apikey={api_key}"
    try:
        data = get_jsonparsed_data(url)
        df_temp = pd.DataFrame(data)
        df_temp['symbol'] = symbol
        df = pd.concat([df, df_temp], ignore_index=True)
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

# Set the 'date' column as the index
df.set_index('date', inplace=True)

# Display the DataFrame
print(df)

df

df.columns

import pandas as pd

# List of NASDAQ 100 companies (only symbols are needed for API requests)
nasdaq_100_companies = [
    "AAPL", "MSFT", "AMZN", "NVDA", "GOOGL", "META", "TSLA", "AVGO", "PEP", "COST",
    "ADBE", "CSCO", "TXN", "CMCSA", "NFLX", "AMD", "INTC", "CHTR", "QCOM", "PYPL",
    "SBUX", "ISRG", "BKNG", "GILD", "REGN", "ADI", "TEAM", "DOCU", "ZM", "AMGN",
    "ILMN", "CSX", "MAR", "CTAS", "DXCM", "WDAY", "MNST", "NXPI", "LULU", "EBAY",
    "ORLY", "MELI", "KDP", "ROST", "MCHP", "PCAR", "PANW", "CDNS", "VRTX", "LRCX",
    "KLAC", "ADP", "BIIB", "AMAT", "SNPS", "XLNX", "IDXX", "SPLK", "ALGN", "HOLX",
    "CDNS", "ILMN", "ADSK", "SGEN", "ZBRA", "NTES", "DOCU", "FTNT", "VRSK", "TMUS",
    "CHTR", "CTSH", "XEL", "LBTYA", "TTWO", "EXPE", "EA", "LUMN", "SWKS", "MTCH",
    "MRNA", "OKTA", "ZM", "CMG", "BMRN", "SNOW", "ODFL", "DDOG", "TTD", "PDD",
    "CSGP", "MRVL", "ZS", "CRWD", "EPAM", "PAYX", "FAST", "CERN", "SIRI", "ATUS",
    "NTAP"
]

# Initialize an empty DataFrame
df = pd.DataFrame()

# API key for Financial Modeling Prep
api_key = "qVXvjPhg98aEFqlvCHfmX1lBWWoXbYF4"

# Fetch data for each company and concatenate into the main DataFrame
for symbol in nasdaq_100_companies:
    url = f"https://financialmodelingprep.com/api/v3/income-statement/{'AAPL'}?period=annual&apikey=qVXvjPhg98aEFqlvCHfmX1lBWWoXbYF4"
    try:
        data = get_jsonparsed_data(url)
        if isinstance(data, list) and data:
            df_temp = pd.DataFrame(data)
            df_temp['symbol'] = symbol
            df = pd.concat([df, df_temp], ignore_index=True)
        else:
            print(f"No data returned for {symbol}")
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

# Set the 'date' column as the index
if not df.empty:
    df.set_index('date', inplace=True)

# Display the DataFrame
print(df)

df1

