from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Cacti Credential
username = "admin"
password = "Monash123!!"

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# # Initialize the chrome driver
# driver = webdriver.Chrome("chromedriver")

# Get the cacti login page
driver.get("https://netmon.monash.edu.my/cacti/index.php")

httpConnection = driver.find_element(By.ID, 'details-button')
if httpConnection.text != "":
    httpConnection.click()
    # Proceed to localhost
    driver.find_element('xpath', '//*[@id="proceed-link"]').click()

# Get the cacti username and password html tag ID and populate username and password
driver.find_element(By.ID, 'login_username').send_keys(username)
driver.find_element(By.ID, 'login_password').send_keys(password)

# Get login button
driver.find_element("xpath", '//*[@id="login"]/div[2]/table/tbody/tr[4]/td/input').click()

# Delay for login to finished
WebDriverWait(driver, 3).until(
    EC.presence_of_all_elements_located((By.ID, 'tab-graphs'))
)

# Open Graph page
driver.find_element('xpath', '//*[@id="tab-graphs"]').click()


# Select Preview
driver.find_element('xpath', '//*[@id="preview"]').click()

# Delay for login to finished
WebDriverWait(driver, 40).until(
    EC.presence_of_all_elements_located((By.ID, 'graph_template_id_ms'))
)

# Search for device to generate realtime graphs
filter = driver.find_element('xpath', '//*[@id="rfilter"]')

if filter.text == "":
    filter.send_keys('maxis')

# Delay for login to finished
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, 'graph_template_id_ms'))
)

# Hit go button to search
driver.find_element('xpath', '//*[@id="go"]').click()


# Delay for login to finished
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, 'graph_145_realtime'))
)

# Hit the realtime button to generate realtime graph
driver.find_element(By.ID, 'graph_145_realtime').click()
# Close browser

#driver.close()