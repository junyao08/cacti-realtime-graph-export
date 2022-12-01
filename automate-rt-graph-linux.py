from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Cacti Credential
username = "admin"
password = "Monash123!!"

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')
# Initialize the chrome driver
driver = webdriver.Chrome('/usr/lib/chromedriver', chrome_options=chrome_options)

# Get the cacti login page
driver.get("https://10.158.65.227/cacti/index.php")

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