"""
Market data loaders for the Institutional Markets Lab.

This module keeps external data-fetching logic out of the Streamlit pages.
The Volatility Lab uses this to load SPX, VIX, and VVIX market data.
"""

from __future__ import annotations

import pandas as pd
import yfinance as yf


MARKET_TICKERS = {
    "^GSPC": "spx",
    "^VIX": "vix",
    "^VVIX": "vvix",
}


def load_spx_vix_vvix_data(
    period: str = "1y",
    interval: str = "1d",
) -> pd.DataFrame:
    """
    Load SPX, VIX, and VVIX OHLC market data from Yahoo Finance.

    Parameters
    ----------
    period:
        Yahoo Finance lookback period. Examples: "6mo", "1y", "2y", "5y".

    interval:
        Yahoo Finance data interval. For this lab, "1d" is the default.

    Returns
    -------
    pd.DataFrame
        A clean dataframe indexed by date with columns such as:
        spx_open, spx_high, spx_low, spx_close,
        vix_open, vix_high, vix_low, vix_close,
        vvix_open, vvix_high, vvix_low, vvix_close.
    """

    raw_data = yf.download(
        tickers=list(MARKET_TICKERS.keys()),
        period=period,
        interval=interval,
        auto_adjust=False,
        progress=False,
    )

    if raw_data.empty:
        raise ValueError("No market data returned from Yahoo Finance.")

    fields_to_keep = ["Open", "High", "Low", "Close"]

    cleaned_data = pd.DataFrame(index=raw_data.index)

    for yahoo_ticker, clean_name in MARKET_TICKERS.items():
        for field in fields_to_keep:
            cleaned_column_name = f"{clean_name}_{field.lower()}"
            cleaned_data[cleaned_column_name] = raw_data[(field, yahoo_ticker)]

    cleaned_data.index.name = "date"

    return cleaned_data.dropna()
