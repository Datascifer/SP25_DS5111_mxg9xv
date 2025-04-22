"""Main runner for scraping and saving stock gainers."""

import sys
from bin.gainers.gainers_factory import get_gainer


def main():
    """Main function that selects gainer class and runs it."""
    if len(sys.argv) < 2:
        print("Usage: python get_gainer.py <source>")
        return

    source = sys.argv[1]
    gainer = get_gainer(source)
    gainer.get_html()
    data_frame = gainer.parse_html()
    gainer.save_csv(data_frame, f"{source}_gainers.csv")


if __name__ == "__main__":
    main()
