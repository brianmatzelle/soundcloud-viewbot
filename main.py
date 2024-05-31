import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint

# Replace 'path/to/your/webdriver' with the actual path to your WebDriver executable
options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(
    options=options
)

try:
    # Navigate to SoundCloud
    driver.get("https://soundcloud.com/")

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/span/span/form/input')))
    search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/span/span/form/input')
    # Find the search box and search for the song
    search_box.send_keys("hypochondriac brakence/jersey remix x shameless + blanc")
    r  = randint(2, 5)
    print(f"Sleeping for {r} seconds...")
    time.sleep(r)
    search_box.send_keys(Keys.RETURN)
    print("Search results loaded...")

    # Wait for search results to load
    r  = randint(2, 4)
    time.sleep(r)

    # Click on the first result
    first_result = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/div/div[3]/div/div/div/ul/li/div/div/div/div[2]/div[1]/div/div/div[1]/a')
    first_result.click()
    r = randint(90, 115)
    time.sleep(r)  # Adjust this time according to the song length
    print(f"Song loaded, now playing for {r} seconds...")
    # Wait for the song to finish playing (set this to the length of the song)
    print("Song finished playing, quitting!")

finally:
    # Close the browser
    driver.quit()