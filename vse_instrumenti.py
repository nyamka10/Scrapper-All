import time
from extension import proxies
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from proxy_auth import *


proxies_extension = proxies(PROXY_USER, PROXY_PASS, PROXY_HOST, PROXY_PORT)


def pars_vse(ids_vse):
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

    result_vse = []
    count_vse = []
    res_vse_instrumenti = []

    try:
        print(f'[!] Старт парсинга Все Инструменты')
        for id in ids_vse:
            driver.get(id)
            time.sleep(1.5)
            try:
                driver.find_element(By.CLASS_NAME, 'HjW-1Z')
                result_vse.append('В наличии')
                count = driver.find_element(By.CLASS_NAME, 'nkoaBr').text
                count_vse.append(count)
                print(f'[+] ВсеИнтрументы {id} : В наличии : {count}')
            except NoSuchElementException:
                result_vse.append('Нет в наличии')
                count_vse.append(' ')
                print(f'[-] ВсеИнтрументы {id} : Нет в наличии')

        print(f'[!] Все Интрументы Конец парсинга')
        res_vse_instrumenti.append(result_vse)
        res_vse_instrumenti.append(count_vse)
        return res_vse_instrumenti

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        times = datetime.now() - start_time
        print(f'Время парсинга Все Инструменты : {times}')
