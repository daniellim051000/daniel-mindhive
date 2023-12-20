import time
from selenium.webdriver.chrome import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scrapers.website import WebsiteSource
from scrapers.selenium import SeleniumChrome
from scrapers.models import CoffeeShop
from scrapers.location import get_coordinates

class CoffeeShopUtils:
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
        print("All State Name :", states_name)
        return states_name

    def scrape_address(self, driver: webdriver):
        """
        Website: Zus Coffee Store
        Formula: All coffee shop address
        """
        print("Scrape State: ", driver.current_url)
        body_data = driver.find_elements(
            By.XPATH, "/html/body/div[1]/main/div/div/div/div/section/div/div/div/div/div/div[2]/div/div")

        zus_coffee_array = []

        for header in body_data:
            header_data = header.find_elements(By.TAG_NAME, "p")
            # print("Print Text",header_data.get_attribute("innerText"))
            for x in header_data:
                shop_info = x.get_attribute("innerText")
                zus_coffee_array.append(shop_info)

            # Filter out empty items
        data = [item for item in zus_coffee_array if item]

        # Create a list of tuples containing shop name and address
        shops = [(data[i], data[i + 1]) for i in range(0, len(data), 2)]
        print("Current Shops :", shops)
        return shops

    def next_page(self, driver: webdriver):
        # Find Next Button
        try:
            next_button = driver.find_element(
                By.XPATH, "//*[contains(text(), 'Next')]")
            # Check is Next Button is clickable or not
            href_data = next_button.get_attribute('href')
            if href_data:
                print("Next Page Button is clicked")
                driver.execute_script("arguments[0].click();", next_button)
                has_next = True
            else:
                has_next = False

            print("Next Button :", has_next)
            return has_next
        except NoSuchElementException:
            print("Element not found")
            has_next = False

    def save_data(self,shop_array):
        # Shop array format: (name, address)
        for shop_name, shop_address in shop_array:
            try:
                coffee_shop = CoffeeShop.objects.get(shop_name=shop_name, shop_address=shop_address)
                if coffee_shop.shop_coordinate_latitude is None or coffee_shop.shop_coordinate_longitude is None:
                    latitude, longitude = get_coordinates(shop_address)
                    coffee_shop.shop_coordinate_latitude = latitude
                    coffee_shop.shop_coordinate_longitude = longitude
                    coffee_shop.save()
                
            except CoffeeShop.DoesNotExist:
                # get_coordinate (Latitude and longitude) from a function
                latitude, longitude = get_coordinates(shop_address)
                # Save Coffee Shop Data
                coffee_shop = CoffeeShop(shop_name=shop_name, shop_address=shop_address, shop_coordinate_latitude=latitude, shop_coordinate_longitude=longitude)
                coffee_shop.save()

    def scrape_data(self):
        base_url = WebsiteSource.ZUS_COFFEE.value
        driver = SeleniumChrome.chrome_setting(base_url)
        driver.get(base_url)

        # Declare Array to store coffee shop and name
        # format: [(coffee_shop,address)]
        zus_coffee_array_tuples = []

        states_name = self.get_state(driver)

        # states_name = ["Melaka"]

        for x in states_name:
            time.sleep(5)
            driver.implicitly_wait(5)
            # if x not in visited_states:
            if x == "Kedah" or x == "Pahang":
                pass
            else:
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, x))
                ).click()

                run = True
                while run:
                    print("Start Scrapping again")
                    # time.sleep(5)
                    driver.implicitly_wait(2)
                    
                    # Scrape Current Data
                    current_page_data = self.scrape_address(driver)
                    zus_coffee_array_tuples.extend(current_page_data)

                    # Next Page
                    has_next_page = self.next_page(driver)

                    run = has_next_page
        
        driver.quit()
        # Save Data into database
        self.save_data(shop_array=zus_coffee_array_tuples)
