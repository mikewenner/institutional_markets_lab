"""
Realized volatility calculations for the Institutional Markets Lab.

This module contains reusable volatility functions that can be imported
by Streamlit pages, notebooks, tests, or future analytics modules.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def calculate_realized_volatility(
    prices: pd.Series,
    window: int = 20,
    annualization_factor: int = 252,
) -> pd.Series:
    """
    Calculate rolling annualized realized volatility from a price series.

    Parameters
    ----------
    prices:
        A pandas Series of asset prices indexed by date or observation order.

    window:
        The rolling window size used to calculate realized volatility.
        For example, 20 means 20 trading days.

    annualization_factor:
        Number of trading periods in one year. For daily data, this is
        typically 252.

    Returns
    -------
    pd.Series
        Rolling annualized realized volatility as a decimal.
        For example, 0.20 means 20% annualized realized volatility.
    """

    if prices.empty:
        raise ValueError("prices cannot be empty.")

    if window <= 1:
        raise ValueError("window must be greater than 1.")

    if annualization_factor <= 0:
        raise ValueError("annualization_factor must be positive.")

    returns = prices.pct_change()

    realized_vol = returns.rolling(window=window).std() * np.sqrt(
        annualization_factor
    )

    return realized_vol
