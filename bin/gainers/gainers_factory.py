"""
Factory to return the correct Gainer class based on source string.
"""

from bin.gainers.yahoo import YahooGainer
from bin.gainers.wsj import WSJGainer


def get_gainer(source):
    """Return an instance of a Gainer class based on source name."""
    if source == "yahoo":
        return YahooGainer()
    if source == "wsj":
        return WSJGainer()
    raise ValueError("Unsupported source")
