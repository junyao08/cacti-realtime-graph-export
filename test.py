from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Cacti Credential
username = "admin"
password = "Monash123!!"

chrome_options = Options()
chrome_options.binary_location = '/usr/bin/google-chrome'
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
# Initialize the chrome driver
driver = webdriver.Chrome(executable_path='/usr/lib/chromedriver', chrome_options=chrome_options)

# Get the cacti login page
driver.get("https://www.google.com")

print(driver.find_element('xpath', '/html/body/div[1]/div[5]/div[1]'))