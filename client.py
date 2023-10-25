import time
import logging
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class NoSuchElementException(Exception):
    pass

# Configure logging
logging.basicConfig(
    filename="french_popular_bank_selenium.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

class FrenchPopularBank:
    def __init__(self, street: str = "Lyon Perrache", zip_code: str = "69000", position_on_map: int = 4):
        """
        Initializes an instance of FrenchPopularBank.

        :param street: The street for agency search (default is "Lyon Perrache").
        :param zip_code: The postal code for agency search (default is "69000").
        :param position_on_map: The position on the map to capture (default is 4).
        """
        # Initialize the Selenium WebDriver (Ensure Selenium and the driver are installed)
        self.driver = webdriver.Chrome()
        self.street = street
        self.zip_code = zip_code
        self.position_on_map = position_on_map

    def open_website(self):
        """
        Opens the Banque Populaire web page.
        """
        # Open the web page
        self.driver.get("https://www.banquepopulaire.fr/")
        # Wait for the page to fully load (you can adjust the wait time as needed)
        self.driver.implicitly_wait(10)

    def accept_cookies(self):
        """
        Accepts cookies on the web page.
        """
        # Locate the "Tout accepter" (Accept All) button by its CSS selector and click it
        cookie_button = self.driver.find_element(By.CSS_SELECTOR, "#consent_prompt_submit")
        time.sleep(1)
        self.driver.save_screenshot("step_zero.png")
        cookie_button.click()
        self.driver.save_screenshot("step_one.png")
        logging.info("Accepted cookies")

    def find_agency(self):
        """
        Finds the "Trouver une agence" (Find an agency) section and clicks on it.
        """
        # Locate the "Trouver une agence" (Find an agency) element by its <p> tag text
        find_agency_element = self.driver.find_element(
            By.XPATH, "//p[@class='font-text-body-bold' and contains(text(), 'Trouver une agence')]"
        )
        # Click on the element
        find_agency_element.click()
        self.driver.save_screenshot("step_two.png")
        logging.info("Clicked on 'Trouver une agence'")

    def fill_address(self):
        """
        Fills in the address (Rue) and postal code fields in the agency search form.
        """
        # Locate and fill in the street (Rue) input field
        street_input = self.driver.find_element(By.ID, "em-search-form__searchstreet")
        street_input.send_keys(self.street)
        # Locate and fill in the postal code input field
        postal_code_input = self.driver.find_element(By.ID, "em-search-form__searchcity")
        postal_code_input.send_keys(self.zip_code)
        self.driver.save_screenshot("step_three.png")
        logging.info("Filled in address information")

    def search_agency(self):
        """
        Clicks the "Rechercher" (Search) button and waits for the redirection.
        """
        # Click the "Rechercher" button
        search_button = self.driver.find_element(By.CLASS_NAME, "em-search-form__submit")
        search_button.click()
        # Wait for the URL to change, indicating redirection
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_changes(self.driver.current_url))
        time.sleep(1)
        self.driver.save_screenshot("step_four.png")
        logging.info("Clicked on 'Rechercher'")

    def collect_agency_elements(self):
        """
        Collects agency elements on the search results page.
        """
        # Collect agency elements
        agency_elements = self.driver.find_elements(By.CLASS_NAME, "em-results__item")
        return agency_elements

    def capture_specific_agency(self):
        """
        Captures a specific agency by its position on the map.

        This function collects agency elements, hovers over the specified agency, and captures a screenshot.

        :raises NoSuchElementException: If the specified agency is not found.
        """
        agency_elements = self.collect_agency_elements()
        if len(agency_elements) >= self.position_on_map:
            element_to_hover = self.driver.find_element(
                By.XPATH, f"//td[text()='{self.position_on_map}']"
            )
            self.hover_and_capture(element_to_hover, "step_five.png")
        else:
            raise NoSuchElementException("The specified agency was not found.")

    def hover_and_capture(self, element, filename):
        """
        Hovers over an element and captures a screenshot.

        :param element: The element to hover over.
        :param filename: The filename for the screenshot.
        """
        # Move the mouse to the center of the element
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(element).perform()
        time.sleep(1)
        action_chains.move_by_offset(10, 0).perform()
        action_chains.move_by_offset(0, 10).perform()
        action_chains.move_by_offset(-10, 0).perform()
        action_chains.move_by_offset(0, -10).perform()
        time.sleep(1)
        # Capture a screenshot before clicking the button
        self.driver.save_screenshot(filename)
        logging.info(f"Hovered over the element and captured a screenshot: {filename}")

    def close_browser(self):
        # Close the browser
        self.driver.quit()
        logging.info("Closed the browser")

if __name__ == "__main__":
    bank = FrenchPopularBank()
    try:
        bank.open_website()
        bank.accept_cookies()
        bank.find_agency()
        bank.fill_address()
        bank.search_agency()
        bank.capture_specific_agency()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    finally:
        bank.close_browser()
