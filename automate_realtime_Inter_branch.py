from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os

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

# Get the cacti login page
driver.get("https://10.158.65.227/cacti/")

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

# Select Tree
driver.find_element(By.ID, 'treeview').click()

# # Delay for login to finished
# WebDriverWait(driver, 120).until(
#     EC.presence_of_all_elements_located(('xpath', '//*[@id="tree_anchor-1_anchor"]'))
# )

time.sleep(20)

if driver.find_element('xpath', '//*[@id="tree_anchor-1"]').get_attribute('class') == 'jstree-node  jstree-closed jstree-last':
    # Click dropdown to display all branches 
    driver.find_element('xpath', '//*[@id="tree_anchor-1"]/i').click()

# Delay for login to finished
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.ID, 'tbranch-6_anchor'))
)

# Click on Inter-Branch
driver.find_element(By.ID, 'tbranch-6_anchor').click()

time.sleep(10)

# Realtime Graph for all graphs
# NOTE: GRAPH WILL NOT WORK IF THE TEMPLATE ID IS CHANGED
driver.find_element('xpath','//*[@id="graph_523_realtime"]').click()
driver.find_element('xpath','//*[@id="graph_1281_realtime"]').click()

time.sleep(3000)