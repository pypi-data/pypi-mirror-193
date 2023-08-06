import random
import pandas as pd
import numpy as np
import yfinance
import matplotlib.lines as mlines
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
plt.rcParams['axes.facecolor'] = 'lightblue'


def create_ts(params={'data': np.array([]), 'timestamps': pd.Series([1])}):
    '''
    Input paramters:
    ------------------------------------------------
    params: dict (dictionary) containing the dates with column named "timestamps"
            and the data containing the data corresponding to the dates.

    >>> Example:
    >>> create_ts(params={'data': np.array([1, 2, 3]), 'timestamps': pd.Series(['2017-01-01', '2018-02-01', '2016-05-07'])})

    Returns: pd.Series with date as index and data.
    '''
    return pd.Series(params['data'], index=params['timestamps'].values)


def get_signal_strategy(stock_short, stock_long):
    '''
    Input: Takes 2 parameters : short time period moving average, long time period moving average.

    Returns: Digital Signal of the Strategy
    '''
    arr = stock_short - stock_long
    signal = np.sign(arr)
    signal = np.nan_to_num(signal)

    return signal


def split_func(X, test_size=0.2):
    '''
    Input: An array or list
    test_size = 0.2 (the size of test set)
                default value is 20%.
    '''
    train_size = 1 - test_size
    return X[:int(train_size*len(X))], X[int(train_size*len(X)):]


def get_strategy_aroon(up, down):
    '''
    Input: up , down signals of Aroon indicator
    ---------------------------------------------------------------
    Parameters:
              up: Array Like
              down: Array Like
    Returns: digital output of the signal .
    '''

    signal = [0, 0]
    count = 0

    for i in range(2, len(up)):
        if up[i-2] < down[i-2] and up[i] > down[i]:
            signal.append(1)
        elif down[i-2] < up[i-2] and down[i] > up[i]:
            signal.append(-1)
        elif up[i] > 50 and down[i] < 50:
            signal.append(1)
        elif up[i] < 50 and down[i] > 50:
            signal.append(-1)
        else:
            signal.append(0)

    return signal


def sigmoid(x):
    '''
    input: Accepts a list or array like input
    outputs: scaled value between 0 and 1.

    >>> Example:
    >>> sigmoid([1])
    >>> [0.73]
    '''
    return np.around(1/(1 + np.e**(-x)), 2)


def digital_signal(super_indicator):
    '''
    Input: Given a list or array like input converts it into a digital output

    Example:
    >>> digital_signal([1, 2, 3, 4, 5, 6, 7])
    >>> [1, 1, 1, 1, 1, 1, 1]
    '''
    signal = []

    for i in super_indicator:
        j = sigmoid(i)
        if j >= 0.5:
            signal.append(1)
        else:
            signal.append(-1)

    return signal


def signal_strategy_bollb(up, down, price):
    '''
    Input: Takes 3 parameters : up, down and price (list or array)
    The 3 bands of the bollinger band
    ---------------------------------------------------------------
    Parameters:
              up: Array Like
              down: Array Like
              price: Array Like

    Returns: Digital Signal of the Strategy
    '''

    signal = []

    for i in range(len(price)):
        if (up[i] - price[i]) > (price[i] - down[i]):
            signal.append(1)
        elif (up[i] - price[i]) - (price[i] - down[i]) < 1:
            signal.append(0)
        else:
            signal.append(-1)

    return signal


def financial_summary(df_rets, frequency='D'):
    '''
    Must supply a dataframe with date and daily retruns as columns
    Note - Don't supply daily returns as % . Keep the date column at the beginning.
    Example:
    date           returns
    2018-02-09     0.25
    2018-02-10     0.29

    frequency : Daily (D), Monthly(M) or Weekly(W), default - 'D'.
                Describes the frequency of data provided.

    Outputs: pd.DataFrame()
    '''
    if frequency == 'D':
        df_rets['c_ret'] = (1 + df_rets['returns']).cumprod() - 1
        days = (pd.to_datetime(df_rets.iloc[len(df_rets)-1, 0]) - pd.to_datetime(df_rets.iloc[0, 0])) // np.timedelta64(1, 'D')
        volatility = np.std(df_rets['returns']) * np.sqrt(252)
        returns = ((df_rets['c_ret'].values[-1])/(days)) * 252
        sharpe = returns/volatility
        sortino = returns / (np.std(df_rets[df_rets['returns'] < 0]['returns']) * np.sqrt(252))

        return pd.DataFrame(data=[df_rets.iloc[0, 0],
                           df_rets.iloc[len(df_rets)-1, 0],
                           days,
                           np.around(returns*100, 2),
                           np.around(volatility*100, 2),
                           np.around(sharpe, 2),
                           np.around(kurtosis(df_rets['returns'], fisher=False), 2),
                           np.around(drawdown(df_rets['returns'])['Drawdown'].min()*100, 2),
                           np.around(sortino, 2)],

                          columns=['Summary'],
                          index=['Start Date', 'End Date', 'Time Period (in Days)', 'Annual Return %',
                                 'Annual Volatility %', 'Sharpe Ratio', 'Kurtosis', 'Max Drawdown %', 'Sortino Ratio'])

    elif frequency == 'M':
        df_rets['c_ret'] = (1 + df_rets['returns']).cumprod() - 1
        months = (pd.to_datetime(df_rets.iloc[len(df_rets)-1, 0]) - pd.to_datetime(df_rets.iloc[0, 0])) // np.timedelta64(1, 'M')
        volatility = np.std(df_rets['returns']) * np.sqrt(12)
        returns = ((df_rets['c_ret'].values[-1])/(months)) * 12
        sharpe = returns/volatility
        sortino = returns / (np.std(df_rets[df_rets['returns'] < 0]['returns']) * np.sqrt(12))

        return pd.DataFrame(data=[df_rets.iloc[0, 0],
                           df_rets.iloc[len(df_rets)-1, 0],
                           months,
                           np.around(returns*100, 2),
                           np.around(volatility*100, 2),
                           np.around(sharpe, 2),
                           np.around(kurtosis(df_rets['returns'], fisher=False), 2),
                           np.around(drawdown(df_rets['returns'])['Drawdown'].min()*100, 2),
                           np.around(sortino, 2)],

                          columns=['Summary'],
                          index=['Start Date', 'End Date', 'Time Period (in Months)', 'Annual Return %',
                                 'Annual Volatility %', 'Sharpe Ratio', 'Kurtosis', 'Max Drawdown %', 'Sortino Ratio'])

    elif frequency == 'W':
        df_rets['c_ret'] = (1 + df_rets['returns']).cumprod() - 1
        weeks = (pd.to_datetime(df_rets.iloc[len(df_rets)-1, 0]) - pd.to_datetime(df_rets.iloc[0, 0])) // np.timedelta64(1, 'W')
        volatility = np.std(df_rets['returns']) * np.sqrt(52)
        returns = ((df_rets['c_ret'].values[-1])/(weeks)) * 52
        sharpe = returns/volatility
        sortino = returns / (np.std(df_rets[df_rets['returns'] < 0]['returns']) * np.sqrt(52))

        return pd.DataFrame(data=[df_rets.iloc[0, 0],
                           df_rets.iloc[len(df_rets)-1, 0],
                           weeks,
                           np.around(returns*100, 2),
                           np.around(volatility*100, 2),
                           np.around(sharpe, 2),
                           np.around(kurtosis(df_rets['returns'], fisher=False), 2),
                           np.around(drawdown(df_rets['returns'])['Drawdown'].min()*100, 2),
                           np.around(sortino, 2)],

                          columns=['Summary'],
                          index=['Start Date', 'End Date', 'Time Period (in Weeks)', 'Annual Return %',
                                 'Annual Volatility %', 'Sharpe Ratio', 'Kurtosis', 'Max Drawdown %', 'Sortino Ratio'])


def drawdown(return_series: pd.Series):
    """Takes a time series of asset returns.
       returns a DataFrame with columns for
       the wealth index,
       the previous peaks, and
       the percentage drawdown
    """
    wealth_index = 1000*(1+return_series).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    return pd.DataFrame({"Wealth": wealth_index,
                         "Previous Peak": previous_peaks,
                         "Drawdown": drawdowns})

def analyze_strategy(actions, df, frequency='D', plot=False):
    '''
    actions: a list , np.array or series of actions .
    plot: default-False, boolean
    df: prices_with_dates - a list of prices along with their respective dates (pd.DataFrame)
                            name of the price column should be "prices"
                            Example :
                            Date           prices
                            "2017-01-09"   22.87

    frequency : Daily (D), Monthly(M) or Weekly(W), default - 'D'.
                Describes the frequency of data provided.

    Example:
    >>> analyze_strategy([1, 1, 1, ..-1], df, 'D', True)
    actions : +1 , 0 or -1 . (Buy, Hold or Sell)

    outputs summary for the actions taken .
    '''

    df['actions'] = actions
    df['returns'] = df['prices'].pct_change() * df['actions'].shift(1)
    df['c_ret'] = (1 + df['returns']).cumprod() - 1
    df.fillna(0, inplace=True)

    if frequency == 'D':
        days = (pd.to_datetime(df.iloc[len(df)-1, 0]) - pd.to_datetime(df.iloc[0, 0]))//np.timedelta64(1, 'D')
        volatility = np.std(df['returns']) * np.sqrt(252)
        returns = ((df['c_ret'].values[-1])/(days)) * 252
        sharpe = returns/volatility
    elif frequency == 'M':
        months = (pd.to_datetime(df.iloc[len(df)-1, 0]) - pd.to_datetime(df.iloc[0, 0]))//np.timedelta64(1, 'M')
        volatility = np.std(df['returns']) * np.sqrt(12)
        returns = ((df['c_ret'].values[-1])/(months)) * 12
        sharpe = returns/volatility
    elif frequency == 'W':
        weeks = (pd.to_datetime(df.iloc[len(df)-1, 0]) - pd.to_datetime(df.iloc[0, 0]))//np.timedelta64(1, 'W')
        volatility = np.std(df['returns']) * np.sqrt(52)
        returns = ((df['c_ret'].values[-1])/(weeks)) * 52
        sharpe = returns/volatility

    if plot:
        dq = df.set_index(df.columns[0])
        plt.title("Returns over the years")
        dq['c_ret'].plot(figsize=(12, 6))
        plt.xlabel("Days")
        plt.ylabel("Returns (Compounded)")


    return pd.DataFrame(data=[df.iloc[0, 0],
                           df.iloc[len(df)-1, 0],
                           days,
                           np.around(returns*100, 2),
                           np.around(volatility*100, 2),
                           np.around(sharpe, 2),
                           np.around(kurtosis(df['returns'], fisher=False), 2),
                           np.around(drawdown(df['returns'])['Drawdown'].min()*100, 2)],

                          columns=['Summary'],
                          index=['Start Date', 'End Date', f'Time Period (in ({frequency}))', 'Annual Return %',
                                 'Annual Volatility %', 'Sharpe Ratio', 'Kurtosis', 'Max Drawdown %'])


def get_benchmark_result(ticker, start, end, price_col='Adj Close', frequency='D', plot=False):
    '''
    start: start date
    end: end date
    ticker: symbol (of Benchmark index eg: ^NSEI for NIFTY)
    plot: default-False, boolean

    frequency : Daily (D), Monthly(M) or Weekly(W), default - 'D'.
                Describes the frequency of data provided.

    price : Open, High , Low or Close . Default = 'Close' .

    returns summary for the benchmark
    '''
    data = yfinance.download(tickers=ticker, start=start, end=end, interval='1d', progress=False)
    mapper = {"D": "Days", "M": "Monthly", "W": "Weeks"}

    if frequency == 'D':
        df = data.loc[:, price_col].reset_index().rename(columns={price_col: "prices"})
        df['returns'] = df['prices'].pct_change()
        df['c_ret'] = (1 + df['returns']).cumprod() - 1
        df.fillna(0, inplace=True)

        days = (pd.to_datetime(df.iloc[len(df)-1, 0]) - pd.to_datetime(df.iloc[0, 0]))//np.timedelta64(1, 'D')
        volatility = np.std(df['returns']) * np.sqrt(252)
        returns = ((df['c_ret'].values[-1])/(days)) * 252
        sharpe = returns/volatility

    elif frequency == 'M':
        data = data.resample('M').last()
        df = data.loc[:, price_col].reset_index().rename(columns={price_col: "prices"})
        df['returns'] = df['prices'].pct_change()
        df['c_ret'] = (1 + df['returns']).cumprod() - 1
        df.fillna(0, inplace=True)

        days = (pd.to_datetime(df.iloc[len(df)-1, 0]) - pd.to_datetime(df.iloc[0, 0]))//np.timedelta64(1, 'M')
        volatility = np.std(df['returns']) * np.sqrt(12)
        returns = ((df['c_ret'].values[-1])/(days)) * 12
        sharpe = returns/volatility

    elif frequency == 'W':
        data = data.resample('W').last()
        df = data.loc[:, price_col].reset_index().rename(columns={price_col: "prices"})
        df['returns'] = df['prices'].pct_change()
        df['c_ret'] = (1 + df['returns']).cumprod() - 1
        df.fillna(0, inplace=True)

        days = (pd.to_datetime(df.iloc[len(df)-1, 0]) - pd.to_datetime(df.iloc[0, 0]))//np.timedelta64(1, 'W')
        volatility = np.std(df['returns']) * np.sqrt(52)
        returns = ((df['c_ret'].values[-1])/(days)) * 52
        sharpe = returns/volatility

    if plot:
        dq = df.set_index("Date")
        plt.title("Returns over the years")
        dq['c_ret'].plot(figsize=(12, 6))
        plt.xlabel("Days")
        plt.ylabel("Returns (Compounded)")


    return pd.DataFrame(data=[str(df.iloc[0, 0])[:10],
                           str(df.iloc[len(df)-1, 0])[:10],
                           days,
                           np.around(returns*100, 2),
                           np.around(volatility*100, 2),
                           np.around(sharpe, 2),
                           np.around(kurtosis(df['returns'], fisher=False), 2),
                           np.around(drawdown(df['returns'])['Drawdown'].min()*100, 2)],

                          columns=['Summary'],
                          index=['Start Date', 'End Date', f'Time Period (in ({frequency}))', 'Annual Return %',
                                 'Annual Volatility %', 'Sharpe Ratio', 'Kurtosis', 'Max Drawdown %'])


def MDD(rets):
    '''
    Input: Takes a return series and returns the maximum drawdown.
    '''
    final = rets
    maxdrwdn = (1+final).cumprod().diff().min()

    return maxdrwdn


def detailed_summary(excelSheet, sheets, period=12, prev_yr='2017'):
    '''
    Provides an year-wise summary of portfolio, baseline and the individual stocks.

    excelSheet: Name of the ExcelSheet with the details.
    sheets: A list with sheet Names - ["Portfolio", "Baseline", "Prices"]
    period: Data details, whether monthly, daily or quarterly data. Default is 12 i.e. monthly, change it to 4 if quarterly or 252 if daily.
    prev_yr: last year preceeding the first date. For Ex: if first date is "2018-03-01", prev_yr = 2017

    Note: "Provide the entire path to the excelsheet if it is inside a folder."
          All sheets must have a column named "date" for dates.
          "invested" - Investments in portfolio (in Portfolio sheet).
          "Adj Close" - In Baseline Sheet.(In Baseline sheet)
    '''

    def individual_etfs(df):
        Y = list(df.columns[1:len(df.columns)-1])
        dfx = pd.DataFrame()

        # for all etfs in the portfolio
        for etf in Y:
            tf = pd.DataFrame()
            prev_date = prev_yr
            for date in df['year'].unique():
                y = df[(df_port.date>=prev_date+'-12-31') & (df_port.date<=date+'-12-31')].loc[:, [etf]]
                y.reset_index(drop=True, inplace=True)

                # Date update
                prev_date = date

                # Log Returns
                lgrets = np.diff(np.log(y[etf]))
                lgrets = np.insert(lgrets, 0, np.nan)
                y['log_returns'] = lgrets
                y['log_returns'].fillna(0, inplace=True)

                # Volatility
                vol = np.std(y.loc[1:, 'log_returns'], ddof=1) * np.sqrt(period)

                # Annual Return
                ret = (y.loc[len(y)-1, etf] / y.loc[0, etf]) - 1

                # Max Drawdown
                inv = y[etf]
                z = pd.Series(index=range(len(inv)))
                z.iloc[0] = inv.iloc[0]

                for i in range(1, len(inv)):
                    z.iloc[i] = max(inv[i], z[i-1])

                maxdrwdn = (inv - z).min()/z[0]

                # Sharpe ratio
                sharpe = ret / vol

                new_df = pd.DataFrame(data=[ret, vol, sharpe, maxdrwdn], columns=[date], index=['Return', 'Volatility', 'Sharpe Ratio', 'Max Drawdown'])
                tf = pd.concat([tf, new_df], axis=1)

            tf.columns.name = etf
            tf['Security Name'] = etf
            dfx = pd.concat([dfx, tf])

        return dfx


    # Read the entire excel sheet
    result = pd.ExcelFile(excelSheet)
    df = pd.DataFrame()
    prev_date = prev_yr

    for ticker in sheets:
        df_port = pd.read_excel(result, ticker)
        df_port['year'] = df_port['date'].apply(lambda x: x[:4])
        tf = pd.DataFrame()

        if ticker == 'Portfolio':
            for date in df_port['year'].unique():
                y = df_port[(df_port.date>=prev_date+'-12-31') & (df_port.date<=date+'-12-31')]
                y.reset_index(drop=True, inplace=True)

                # Date update
                prev_date = date

                # Log Returns
                lgrets = np.diff(np.log(y['invested']))
                lgrets = np.insert(lgrets, 0, np.nan)
                y['log_returns'] = lgrets
                y['log_returns'].fillna(0, inplace=True)

                # Volatility
                vol = np.std(y.loc[1:, 'log_returns'], ddof=1) * np.sqrt(period)

                # Annual Return
                ret = (y.loc[len(y)-1, 'invested'] / y.loc[0, 'invested']) - 1

                # Max Drawdown
                inv = y['invested']
                z = pd.Series(index=range(len(inv)))
                z.iloc[0] = inv.iloc[0]

                for i in range(1, len(inv)):
                    z.iloc[i] = max(inv[i], z[i-1])

                maxdrwdn = (inv - z).min()/z[0]

                # Sharpe ratio
                sharpe = ret / vol

                new_df = pd.DataFrame(data=[ret, vol, sharpe, maxdrwdn], columns=[date], index=['Return', 'Volatility', 'Sharpe Ratio', 'Max Drawdown'])
                tf = pd.concat([tf, new_df], axis=1)

            tf.columns.name = ticker
            tf['Security Name'] = ticker
            df = pd.concat([df, tf])

        elif ticker == 'Baseline':
            prev_date = prev_yr

            for date in df_port['year'].unique():
                y = df_port[(df_port.date>=prev_date+'-12-31') & (df_port.date<=date+'-12-31')]
                y.reset_index(drop=True, inplace=True)

                # Date update
                prev_date = date

                # Log Returns
                lgrets = np.diff(np.log(y['Adj Close']))
                lgrets = np.insert(lgrets, 0, np.nan)
                y['log_returns'] = lgrets
                y['log_returns'].fillna(0, inplace=True)

                # Volatility
                vol = np.std(y.loc[1:, 'log_returns'], ddof=1) * np.sqrt(period)

                # Annual Return
                ret = (y.loc[len(y)-1, 'Adj Close'] / y.loc[0, 'Adj Close']) - 1

                # Max Drawdown
                inv = y['Adj Close']
                z = pd.Series(index=range(len(inv)))
                z.iloc[0] = inv.iloc[0]

                for i in range(1, len(inv)):
                    z.iloc[i] = max(inv[i], z[i-1])

                maxdrwdn = (inv - z).min()/z[0]

                # Sharpe ratio
                sharpe = ret / vol

                new_df = pd.DataFrame(data=[ret, vol, sharpe, maxdrwdn], columns=[date], index=['Return', 'Volatility', 'Sharpe Ratio', 'Max Drawdown'])
                tf = pd.concat([tf, new_df], axis=1)

            tf.columns.name = ticker
            tf['Security Name'] = ticker
            df = pd.concat([df, tf])

        else:
            tf = individual_etfs(df_port)
            df = pd.concat([df, tf])

    df.columns.name = 'Metric'
    return df
