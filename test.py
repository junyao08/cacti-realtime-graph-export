from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Cacti Credential
username = "admin"
password = "Monash123!!"

chrome_options = Options()
chrome_options.binary_location = '/usr/bin/google-chrome'
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--ignore-certificate-errors')
# Initialize the chrome driver
driver = webdriver.Chrome(executable_path='/usr/lib/chromedriver', chrome_options=chrome_options)

time.sleep(5)

# Get the cacti login page
driver.get("https://10.158.65.227/cacti/")

print(driver.find_element('xpath', '/html/body').text)

driver.close()