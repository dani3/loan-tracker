"""Loan module."""

from typing import Optional


class Loan:
    """Loan class."""

    name: str
    is_fixed: bool
    interest_rate: float
    bond_rate: Optional[float]

    def __init__(
        self,
        name: str,
        is_fixed: bool,
        interest_rate: float,
        bond_rate: Optional[float] = None,
    ) -> None:
        self.name = name
        """Loan name."""

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
