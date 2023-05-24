import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def set_test_web_driver():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    return driver


def set_web_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1400,2100")
    chrome_options.add_argument('--disable-gpu')

    preferences = {'download.prompt_for_download': False,
                   'download.directory_upgrade': True,
                   'safebrowsing.enabled': False,
                   'safebrowsing.disable_download_protection': True,
                   'download.default_directory': os.path.abspath(os.getcwd()) + '/'
                   }

    driver = webdriver.Chrome(chrome_options=chrome_options)
    chrome_options.add_experimental_option('prefs', preferences)

    return driver


BASE_URL = 'https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/'
REQUEST_FORM_NAME = ''
REQUEST_FORM_TYPE = ''
REQUEST_FORM_BUSINESS_UNIT = ''  # REQUIRED IN REQUEST FORM AND GENERAL USE FORM, ARE THEY THE SAME?

GENERAL_FORM_USERNAME = ''
GENERAL_FORM_REQUESTERS_EMAIL = ''
GENERAL_FORM_MANAGERS_EMAIL = ''
GENERAL_FORM_TEAM_DL = ''
GENERAL_FORM_CO_OWNERS = ''
GENERAL_FORM_BUSINESS_UNIT = ''

CLICKABLE_WAIT_TIME = 10
LOAD_WAIT_TIME = 10
