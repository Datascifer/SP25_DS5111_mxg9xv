"""
Yahoo Gainer module for scraping stock gainers from Yahoo Finance.
"""

import pandas as pd
import requests
from bin.gainers.base import GainerBase


class YahooGainer(GainerBase):
    """Yahoo implementation of the GainerBase abstract class."""

    def get_html(self):
        """Download HTML content from Yahoo Finance gainers page."""
        url = "https://finance.yahoo.com/gainers"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        with open("ygainers.html", "w", encoding="utf-8") as file:
            file.write(response.text)

    def parse_html(self):
        """Parse gainers table from saved HTML."""
        data_frame = pd.read_html("ygainers.html")[0]
        return data_frame

    def save_csv(self, data_frame, output_file):
        """Save the DataFrame to a CSV file."""
        data_frame.to_csv(output_file, index=False)
