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

# Delay for login to finished
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.ID, 'graph_template_id_ms'))
)

# Click dropdown to display all branches 
driver.find_element('xpath', '//*[@id="tree_anchor-1"]/i').click()

# Click on Inter-Branch
driver.find_element('xpath', '//*[@id="tbranch-6_anchor"]').click()
# Realtime Graph for all graphs
# NOTE: GRAPH WILL NOT WORK IF THE TEMPLATE ID IS CHANGED
driver.find_element('xpath','//*[@id="graph_523_realtime"]').click()
driver.find_element('xpath','//*[@id="graph_255_realtime"]').click()


#Click on Core Infrastructure
driver.find_element('xpath', '//*[@id="tbranch-5_anchor"]').click()
# Realtime Graph for all graphs
driver.find_element('xpath', '//*[@id="graph_514_realtime"]').click()
driver.find_element('xpath', '//*[@id="graph_512_realtime"]').click()
driver.find_element('xpath', '//*[@id="graph_515_realtime"]').click()
driver.find_element('xpath', '//*[@id="graph_513_realtime"]').click()
driver.find_element('xpath', '//*[@id="graph_508_realtime"]').click()
driver.find_element('xpath', '//*[@id="graph_507_realtime"]').click()
driver.find_element('xpath', '//*[@id="graph_510_realtime"]').click()


# Close browser
#driver.close()