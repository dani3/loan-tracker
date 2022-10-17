"""Loan scraper module."""

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from loan import Loan

import time


class LoanScraper:
    """Class that represent a loan scraper."""

    NUM_LOANS: int = 8
    URL: str = "https://rd.dk/kurser-og-renter"

    def __init__(self) -> None:
        pass

    def run(self) -> list[Loan]:
        """
        Execute the scraper and return a list of loans.

        :return: list of `Loan`.
        """
        driver: WebDriver = webdriver.Chrome()
        driver.get(self.URL)
        time.sleep(2)
        cookies_button: WebElement = driver.find_element(
            "xpath", '//*[@id="root"]/div[4]/div/div/div[3]/button[1]'
        )
        cookies_button.click()
        time.sleep(1)

        loans: list[Loan] = list()
        for i in range(1, self.NUM_LOANS + 1):
            loan_element: WebElement = driver.find_element(
                "xpath",
                f'//*[@id="root"]/div[3]/div[2]/div/div[3]/div/div/div/table/tbody/tr[{i}]/td[1]',
            )

            current_course: WebElement = driver.find_element(
                "xpath",
                f'//*[@id="root"]/div[3]/div[2]/div/div[3]/div/div/div/table/tbody/tr[{i}]/td[3]/span',
            )

            name: str = loan_element.find_element("class name", "prefix").text
            years: int = int(
                loan_element.find_element("class name", "value").text.split(" ")[0]
            )
            rate: float = float(
                loan_element.find_element("class name", "value")
                .text.split(" ")[3]
                .replace(",", ".")
            )
            loan: Loan = Loan(
                name, years, True, rate, float(current_course.text.replace(",", "."))
            )

            loans.append(loan)

        return loans
