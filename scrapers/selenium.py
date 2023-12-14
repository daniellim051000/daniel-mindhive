from selenium import webdriver
import time
from django.conf import settings


class SeleniumChrome:
    def chrome_setting(base_url):
        base_url = base_url
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--incognito")
        options.add_argument("--ignore-ssl-errors=yes")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--start-maximized")

        connected = False

        while not connected:
            try:
                if settings.USE_DOCKER_SELENIUM_DRIVER == True:
                    driver = webdriver.Remote(
                        command_executor=settings.SELENIUM_DRIVER,
                        options=options,
                    )
                else:
                    driver = webdriver.Chrome(options=options)
                connected = True
            except Exception as e:
                print(f"Unable to connect to the hub. Error: {str(e)}")
                time.sleep(5)

        return driver
