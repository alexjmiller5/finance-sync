"""Fidelity 401k scraper package.

Captures biweekly payroll contributions (+ fund exchanges, fees, dividends) from
the Capital One 401k via Fidelity's JSON activity API. Account Type = "401k".
"""

from finance_sync.banks.fidelity.scraper import FidelityScraper

__all__ = ["FidelityScraper"]
