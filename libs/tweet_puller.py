from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from libs.tweet_formatter import outputData
from libs.proxy_provider import get_proxy
import time
from libs.proxy_provider import get_proxy
from chromedriver_py import binary_path

PROXY = get_proxy()
options = Options()
options.add_argument(f'--proxy-server={PROXY}')
options.add_argument(f'--start-maximized')
webdriver_service = Service(executable_path=binary_path)
driver = webdriver.Chrome(service=webdriver_service, options=options)

def login(username,password):
    url = 'https://www.twitter.com/login'
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[autocomplete="username"]'))).send_keys(username)
    driver.find_element(By.XPATH, "//span[text()='Next']").click()
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[autocomplete="current-password"]'))).send_keys(password)
    driver.find_element(By.XPATH, "//span[text()='Log in']").click()

def puller(duration,username,password):
    login(username,password)
    pulled_tweets = []
    start_time = time.time()
    duration = 60
    while time.time() - start_time < duration:
        elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-testid="cellInnerDiv"]'))
        )
        tweets = driver.find_elements(By.XPATH, '//*[@data-testid="cellInnerDiv"]')
        for t in tweets:
            try:
                pulled_tweets.append(t.text)
            except:
                pass
        outputData(pulled_tweets)
        pulled_tweets.clear()
        time.sleep(4)
        driver.refresh()
    driver.quit()   
