import sys
sys.path.append('.')

from bin.gainers.yahoo import YahooGainer

def test_yahoo_parse_html():
    """Test that YahooGainer parses a valid HTML file correctly."""
    gainer = YahooGainer()
    data_frame = gainer.parse_html()
    assert not data_frame.empty
    assert "Symbol" in data_frame.columns or "Name" in data_frame.columns

