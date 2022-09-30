"""Entry point."""

from loan import Loan

MY_LOAN: Loan = Loan("Fastforrentet lån med afdrag", True, 5, 99.14)


def main():
    """Execute the main function."""
    print("hey there")


if __name__ == "__main__":
    main()
