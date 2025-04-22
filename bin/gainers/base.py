"""Abstract base class for all stock gainer scrapers."""

from abc import ABC, abstractmethod


class GainerBase(ABC):
    """Defines the required interface for any stock gainer implementation."""

    @abstractmethod
    def get_html(self):
        """Download and save HTML data."""
        raise NotImplementedError

    @abstractmethod
    def parse_html(self):
        """Parse HTML and return a DataFrame."""
        raise NotImplementedError

    @abstractmethod
    def save_csv(self, data_frame, output_file):
        """Save DataFrame to CSV."""
        raise NotImplementedError
