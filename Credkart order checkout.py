

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("headless")
driver=webdriver.Chrome(options=chrome_options)

#-----------------------open browser-----------

# driver = webdriver.Chrome()
driver.maximize_window()

#----------------go to url----------------------

driver.get("https://automation.credence.in/login")

#------------------Enter Email------------------

driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Credencetest@test.com")

#------------------Enter password---------------
driver.find_element(By.CSS_SELECTOR, "input[id='password']").send_keys("Credence@123")

# --------------Click Login button----------------
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)


#----------------click on product macbook---------------
driver.find_element(By.XPATH,"//img[@src='https://automation.credence.in/img/macbook-pro.jpg']").click()

#------------Add to cart product macbook------------------
driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
time.sleep(5)

#---------------click on continouse shopping-----------
driver.find_element(By.XPATH,"//a[normalize-space()='Continue Shopping']").click()

#------------click on headphone-----------------
driver.find_element(By.XPATH,"//img[@src='https://automation.credence.in/img/headphones.jpg']").click()

#----------------click on add to cart-------------
driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
time.sleep(5)

#-----------proceed to checkout ------------------------
driver.find_element(By.XPATH,"//a[normalize-space()='Proceed to Checkout']").click()
time.sleep(2)

#------------Enter first name------------------
driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys("Anuradha")

#------------Enter last name------------------
driver.find_element(By.XPATH,"//input[@id='last_name']").send_keys("Pawar")

#------------Enter phone---------------
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("8937237233")


#------------Enter address------------------
driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("Satara")

#------------Enter zip code------------------
driver.find_element(By.XPATH,"//input[@id='zip']").send_keys("415004")


time.sleep(2)
#------------Enter state------------------
state=Select(driver.find_element(By.XPATH,"//select[@id='state']"))
state.select_by_visible_text("Pune")

#------------Enter owner------------------
driver.find_element(By.XPATH,"//input[@id='owner']").send_keys("Anuradha")


time.sleep(2)
#------------Enter CVV------------------
driver.find_element(By.XPATH,"//input[@id='cvv']").send_keys("567")

time.sleep(2)
#------------Enter card no------------------5281 0370 4891 6168
driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("5281")
driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("0370")
driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("4891")
driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("6168")

#------------Enter year------------------
year=Select(driver.find_element(By.XPATH,"//select[@id='exp_year']"))
year.select_by_visible_text("2027")

#------------Enter month------------------
year=Select(driver.find_element(By.XPATH,"//select[@id='exp_month']"))
year.select_by_visible_text("March")
time.sleep(2)

# ---click on checkout button
driver.find_element(By.XPATH,"//button[@id='confirm-purchase']").click()

print(driver.find_element(By.XPATH, "//p[@class='lead w-lg-50 mx-auto']").text)

time.sleep(10)



