""" yf_example2.py

Example of a function to download stock prices from Yahoo Finance.
"""

import yfinance as yf


def yf_prc_to_csv(tic, pth, start=None, end=None):
    """ Downloads analysts recommendation from Yahoo Finance and saves the
    information in a CSV file

    Parameters
    ----------
    tic : str
        Ticker

    路径 pth : str
        Location of the output CSV file

    起始日期 start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    终止日期 end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)


# this will print the value of __name__
print(f"The value of __name__ is: '{__name__}'")


# Example
if __name__ == "__main__":
    tic = 'QAN.AX'
    datadir = '/Users/panqiaoyi/PycharmProjects/5546/toolkit/data'
    pth = f'{datadir}/qan_stk_prc.csv'
    yf_prc_to_csv(tic, pth)

import os

tic = 'QAN.AX'
datadir = '/Users/panqiaoyi/PycharmProjects/5546/toolkit/data'
path = os.path.join(datadir ,'qan_stk_prc.csv')

datadir = '/Users/panqiaoyi/PycharmProjects/5546/toolkit/data'
pth = f'{datadir}/qan_stk_prc.csv'