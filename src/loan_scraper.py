from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

import time


class LoanScraper:
    """Class that represent a loan scraper."""

    URL: str = "https://rd.dk/kurser-og-renter"

    def __init__(self) -> None:
        pass

    def run(self) -> None:
        driver = webdriver.Chrome()
        driver.get(self.URL)
        time.sleep(2)
        cookies_button: WebElement = driver.find_element(
            "xpath", '//*[@id="root"]/div[4]/div/div/div[3]/button[1]'
        )
        cookies_button.click()
        time.sleep(1)
        loan: WebElement = driver.find_element(
            "xpath",
            '//*[@id="root"]/div[3]/div[2]/div/div[3]/div/div/div/table/tbody/tr[1]/td[1]',
        )

        current_course: WebElement = driver.find_element(
            "xpath",
            '//*[@id="root"]/div[3]/div[2]/div/div[3]/div/div/div/table/tbody/tr[1]/td[3]/span',
        )

        print(f"Prefix: {loan.find_element('class name', 'prefix').text}")
        print(f"Value: {loan.find_element('class name', 'value').text}")
        print(f"Current course: {current_course.text}")
