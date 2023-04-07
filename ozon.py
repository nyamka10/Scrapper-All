import time
from extension import proxies
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from proxy_auth import *


proxies_extension = proxies(PROXY_USER, PROXY_PASS, PROXY_HOST, PROXY_PORT)


def pars_ozon(ids_ozon):
    start_time = datetime.now()
    options = webdriver.ChromeOptions()
    options.add_extension(proxies_extension)
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

    try:
        print(f'[!] Старт парсинга OZON')
        for id in ids_ozon:
            driver.get(f'https://www.ozon.ru/product/{id}')
            time.sleep(1.5)
            try:
                try:
                    count = driver.find_element(By.CLASS_NAME, 'n1q').text
                except NoSuchElementException:
                    count = driver.find_element(By.CLASS_NAME, 'q0n').text

                result_ozon.append('В наличии')
                count = count.replace('\u2009', ' ')
                count_ozon.append(count)
                print(f'[+] OZON {id} : В наличии : {count}')

            except NoSuchElementException:
                result_ozon.append('Нет в наличии')
                count_ozon.append(' ')
                print(f'[-] OZON {id} : Нет в наличии')

        print(f'[!] OZON Конец парсинга')
        res_ozon.append(result_ozon)
        res_ozon.append(count_ozon)
        return res_ozon

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        times = datetime.now() - start_time
        print(f'Время парсинга OZON : {times}')
