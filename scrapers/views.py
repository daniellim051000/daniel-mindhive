import time
from selenium.webdriver.chrome import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from scrapers.website import WebsiteSource
from scrapers.selenium import SeleniumChrome

# Create your views here.


class ZusCoffeeView:
    def __init__(self):
        return None

    def get_state(self, driver):
        states_name = []
        map_data = driver.find_element(
            By.ID, "Layer_1"
        )
        states = map_data.find_elements(By.CLASS_NAME, "state")
        for x in states:
            states_name.append(x.get_attribute("id"))
            # states_webelement.append(x)
        return states_name

    def scrape_address(self, driver: webdriver):
        """
        Website: Zus Coffee Store
        Formula: All coffee shop address
        """
        print("Scrape State: ", driver.current_url)
        body_data = driver.find_elements(
            By.XPATH, "/html/body/div[1]/main/div/div/div/div/section/div/div/div/div/div/div[2]")

        zus_coffee_array = []

        for header in body_data:
            header_data = header.find_elements(By.TAG_NAME, "p")
            for x in header_data:
                zus_coffee_array.append(x.text)

            # Filter out empty items
        data = [item for item in zus_coffee_array if item]

        # Create a list of tuples containing shop name and address
        shops = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]

        return shops

    def next_page(self, driver: webdriver):
        # Find Next Button
        try:
            next_button = driver.find_element(
                By.XPATH, "//*[contains(text(), 'Next')]")
            # Check is Next Button is clickable or not
            href_data = next_button.get_attribute('href')
            print("Next Button :", href_data)
            if href_data:
                print("Next Page Button is clicked")
                driver.execute_script("arguments[0].click();", next_button)
                has_next = True
            else:
                has_next = False
            return has_next
        except NoSuchElementException:
            print("Element not found")
            has_next = False

    def scrape_data(self):
        base_url = WebsiteSource.ZUS_COFFEE.value
        driver = SeleniumChrome.chrome_setting(base_url)
        driver.get(base_url)

        # Declare Array to store coffee shop and name
        # format: [(coffee_shop,address)]
        zus_coffee_array_tuples = []
        visited_states = set()

        states_name = self.get_state(driver)

        for x in states_name:
            time.sleep(2)
            driver.implicitly_wait(2)
            if x not in visited_states:
                if x =="Kedah" or x=="Pahang":
                    pass
                else:
                    visited_states.add(x)
                    element = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.ID, x))
                    ).click()
                    run = True
                    while run:
                        print("Start Scrapping again")
                        time.sleep(2)
                        driver.implicitly_wait(2)
                        print(visited_states)
                        # Scrape Current Data
                        current_page_data = self.scrape_address(driver)
                        zus_coffee_array_tuples.extend(current_page_data)

                        # Next Page
                        has_next_page = self.next_page(driver)

                        run = has_next_page

        for x,shop in enumerate(zus_coffee_array_tuples):
            print(x, shop)