import time
from extension import proxies
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from proxy_auth import *



options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--headless=new")
options.add_argument("--disable-blink-features=AutomationControlled")

s = Service(executable_path='path_to_chromedriver')
driver = webdriver.Chrome(service=s, options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
  '''
})

count_ozon = []
res_ozon = []
result_ozon = []
ids_ozon = [232219844, 638292146, 730058045, 228322840, 858028699, 311476945, 176402627, 590911498]


for id in ids_ozon:
    driver.get(f'https://www.ozon.ru/product/{id}')
    time.sleep(1.5)
    counts = driver.find_element(By.CLASS_NAME, 'nq0').text
    print(counts)
    # count = count.replace('\u2009', ' ')
    # print(f'[+] OZON {id} : В наличии : {count}')
