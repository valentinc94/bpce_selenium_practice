import unittest
from unittest.mock import Mock, call

from client import FrenchPopularBank
from selenium.webdriver.common.by import By


class TestFrenchPopularBank(unittest.TestCase):
    def setUp(self):
        self.mock_driver = Mock()
        self.bank = FrenchPopularBank(street="MockStreet", zip_code="MockZip", position_on_map=4)
        self.bank.driver = self.mock_driver

    def test_open_website(self):
        self.bank.open_website()
        self.mock_driver.get.assert_called_with("https://www.banquepopulaire.fr/")

    def test_accept_cookies(self):
        self.bank.accept_cookies()
        self.mock_driver.find_element.assert_called_with(By.CSS_SELECTOR, "#consent_prompt_submit")
        self.mock_driver.find_element.return_value.click.assert_called()
        self.mock_driver.save_screenshot.assert_called()

    def test_find_agency(self):
        self.bank.find_agency()
        self.mock_driver.find_element.assert_called_with(
            By.XPATH, "//p[@class='font-text-body-bold' and contains(text(), 'Trouver une agence')]"
        )
        self.mock_driver.find_element.return_value.click.assert_called()
        self.mock_driver.save_screenshot.assert_called()

    def test_close_browser(self):
        self.bank.close_browser()
        self.mock_driver.quit.assert_called()


if __name__ == "__main__":
    unittest.main()
