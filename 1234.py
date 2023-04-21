import os

import pandas as pd

import config as cfg


def read_prc_csv(tic):
    file = os.path.join(cfg.DATADIR, tic.lower() + '_prc.csv')
    df_r = pd.read_csv(file, parse_dates=['Date'], index_col='Date')
    df = cfg.standardise_colnames(df_r)
    df.sort_index(inplace=True)
    return df


""" This function creates a data frame with the contents of a CSV file 
    containing stock price information for a given ticker. 

    Parameters
    ----------
    tic : str
        String with the ticker (can include lowercase and/or uppercase
        characters)

    Returns
    -------
    df 
        A Pandas data frame containing the stock price information from the CSV
        containing the stock prices for the ticker `tic`.

        This data frame must meet the following criteria:

        - df.index: `DatetimeIndex` with dates, matching the dates contained in
          the CSV file. The labels in the index must be `datetime` objects.

        - df.columns: each column label will be a column in the CSV file, 
          with the exception of 'Date'. Column names will be formatted
          according to the `standardise_colnames` function included in the
          `project2.config.py` module.

    Examples
    --------
    IMPORTANT: The examples below are for illustration purposes. Your ticker/sample
    period may be different.

        >> tic = 'AAPL'
        >> tic_df = read_prc_csv(tic)
        >> tic_df.info()

        DatetimeIndex: 252 entries, 2010-01-04 to 2010-12-31
        Data columns (total 6 columns):
         #   Column     Non-Null Count  Dtype
        ---  ------     --------------  -----
         0   open       252 non-null    float64
         1   high       252 non-null    float64
         2   low        252 non-null    float64
         3   close      252 non-null    float64
         4   adj_close  252 non-null    float64
         5   volume     252 non-null    int64
        dtypes: float64(5), int64(1)

     Hints
     -----
     - Remember that the ticker `tic` in `<tic>`_prc.csv is in lower case.
       File names in non-windows systems are case sensitive (so 'AAA.csv' and
       'aaa.csv' are different files). 

    """


def mk_prc_df(tickers, prc_col='adj_close'):
    df_raw = pd.DataFrame()

    for tic in tickers:
        df_tic = read_prc_csv(tic)
        df_tic_prc = df_tic.loc[:, [prc_col]]
        df_tic_prc.columns = [tic.lower()]
        df_raw = df_raw.join(df_tic_prc, how='outer')
    df = df_raw.dropna(axis=0, how="all")
    return df


""" This function creates a data frame containing price information for a
    list of tickers and a given type of quote (e.g., open, close, ...)

    This function uses the `read_prc_csv` function in this module to read the
    price information for each ticker in `tickers`.

    Parameters
    ----------
    tickers : list
        List of tickers

    prc_col: str, optional
        String with the name of the column we will use to compute returns. The
        column name must conform with the format in the `standardise_colnames`
        function defined in the config.py module.  
        Defaults to 'adj_close'.

    Returns
    -------
    df
        A Pandas data frame containing the `prc_col` price for each stock
        in the `tickers` list:

        - df.index: DatetimeIndex with dates. The labels in this index must
          include all dates for which there is at least one valid price quote
          for one ticker in `tickers`.  


        - df.columns: each column label will contain the ticker code (in lower
          case). The number of columns in this data frame must correspond to
          the number of tickers in the ``tickers` parameter. 

    Notes
    -----
    - If the price is not available for a given ticker and date, its value
      will be a NaN, as long as there is a price available for another ticker
      on the same date.

    Examples
    --------
    Note: The examples below are for illustration purposes only and will
    **not** necessarily represent the actual contents of the data frame you
    create).

    Example 1: Suppose there are two tickers in `tickers`, "tic1" and "tic2".
    Suppose the following information is available for each ticker: 

      tic1:
          | <date col> | <prc_col> |
          |------------+-----------|
          | 2020-01-02 | 1.0       |

      tic2:
          | <date col> | <prc_col> |
          |------------+-----------|
          | 2020-01-10 | 2.0       |
          | 2020-03-10 | NaN       |

    Then the output data frame should include the following information:

          |            | tic1 | tic2 |
          |------------+------+------|
          | 2020-01-02 | 1.0  | NaN  |
          | 2020-01-10 | NaN  | 2.0  |

    The DatetimeIndex will include objects representing the dates 2020-01-02
    and 2020-01-10. The reason 2020-03-10 is not included is because there is
    no price information (for any ticker in `tickers`) on that date.

    Example 2:    

        >> tickers = ['AAPL', 'TSLA']
        >> prc_df = mk_prc_df(tickers, prc_col='adj_close')
        >> prc_df.info()

        <class 'pandas.core.frame.DataFrame'>
        DatetimeIndex: 252 entries, 2010-01-04 to 2010-12-31
        Data columns (total 2 columns):
         #   Column  Non-Null Count  Dtype
        ---  ------  --------------  -----
         0   aapl    252 non-null    float64
         1   tsla    130 non-null    float64
        dtypes: float64(2)

        >> print(prc_df)
                         aapl   tsla
        Date
        2010-01-04   6.604801    NaN
        2010-01-05   6.616219    NaN
        ...               ...    ...
        2010-12-30   9.988830  5.300
        2010-12-31   9.954883  5.326


    """


# ----------------------------------------------------------------------------
#   Test functions
# ----------------------------------------------------------------------------


def _test_print(obj, msg=None):
    import pprint as pp
    sep = '-'*40
    if isinstance(obj, str):
        prt = obj
    else:
        prt = pp.pformat(obj)
        prt = f'{prt}\n\nObj type is: {type(obj)}'
    if msg is not None:
        prt = f'{msg}\n\n{prt}'
    to_print = [
        '',
        sep,
        prt,
        ]
    print('\n'.join(to_print))
    if isinstance(obj, pd.DataFrame):
        print('')
        obj.info()
    print(sep)


def _test_read_prc_csv():
    tic = 'TSLA'
    df = read_prc_csv(tic)
    _test_print(df)


def _test_mk_prc_df():
    tickers = ['AAPL', 'TSLA']
    prc_df = mk_prc_df(tickers, prc_col='adj_close')
    _test_print(prc_df)


if __name__ == "__main__":
    pass
    _test_read_prc_csv()
    _test_mk_prc_df()
