"""Loan module."""


class Loan:
    """Loan class."""

    name: str
    years: int
    is_fixed: bool
    interest_rate: float
    bond_rate: float | None

    def __init__(
        self,
        name: str,
        years: int,
        is_fixed: bool,
        interest_rate: float,
        bond_rate: float | None = None,
    ) -> None:
        self.name = name
        """Loan name."""

        self.years = years
        """Number of years."""

        self.is_fixed = is_fixed
        """Either fixed or variable rate."""

        self.interest_rate = interest_rate
        """Interest rate."""

        self.bond_rate = bond_rate
        """If it's a fixed interest rate, the bond rate that comprises the loan."""

    def __str__(self) -> str:
        if self.is_fixed:
            return f"Fixed interest rate loan: {self.name} at {self.interest_rate}%"
        else:
            return f"Variable interest rate loan: {self.name} at {self.interest_rate}%"
