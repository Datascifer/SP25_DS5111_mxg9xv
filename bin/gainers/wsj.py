"""
WSJ Gainer module for scraping stock gainers from Wall Street Journal.
"""

import pandas as pd
import requests
from bin.gainers.base import GainerBase


class WSJGainer(GainerBase):
    """WSJ implementation of the GainerBase abstract class."""

    def get_html(self):
        """Download HTML content from WSJ gainers page."""
        url = "https://www.wsj.com/market-data/stocks/us/movers"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        with open("wjsgainers.html", "w", encoding="utf-8") as file:
            file.write(response.text)

    def parse_html(self):
        """Parse gainers table from saved HTML."""
        data_frame = pd.read_html("wjsgainers.html")[0]
        return data_frame

    def save_csv(self, data_frame, output_file):
        """Save the DataFrame to a CSV file."""
        data_frame.to_csv(output_file, index=False)
