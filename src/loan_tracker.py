"""Entry point."""

from loan import Loan
from loan_scraper import LoanScraper

MY_LOAN: Loan = Loan("Fastforrentet lån med afdrag", True, 5, 99.14)


def main():
    """Execute the main function."""
    scraper: LoanScraper = LoanScraper()
    scraper.run()


if __name__ == "__main__":
    main()
