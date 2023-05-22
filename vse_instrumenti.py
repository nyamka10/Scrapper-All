import time
from extension import proxies
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from proxy_auth import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


proxies_extension = proxies(PROXY_USER, PROXY_PASS, PROXY_HOST, PROXY_PORT)


def pars_vse(ids_vse):
    start_time = datetime.now()

    options = webdriver.ChromeOptions()
    # options.add_extension(proxies_extension)
    options.add_argument('--no-sandbox')
    options.add_argument("--headless=new")
    options.add_argument("--disable-blink-features=AutomationControlled")

    s = Service(executable_path='path_to_chromedriver')
    # driver = webdriver.Chrome(service=s, options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

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

    driver.get('https://www.vseinstrumenti.ru/product/termopot-gfgril-gf-tp015-6864355/')
    time.sleep(5)
    driver.get('https://www.vseinstrumenti.ru/product/ultratonkaya-vibroplatforma-trenazher-dlya-pohudeniya-planta-vibra-slim-vp-02-2948156/')
    time.sleep(5)
    driver.get('https://www.vseinstrumenti.ru/view_goods_by_id_redirect.php?id=2925524')
    time.sleep(5)

    try:
        print(f'[!] Старт парсинга Все Инструменты')
        for id in ids_vse:
            driver.get(id)
            time.sleep(1.5)
            try:
                driver.find_element(By.CLASS_NAME, 'FBhpWG')
                result_vse.append('В наличии')
                count = driver.find_element(By.CLASS_NAME, 'df5X3i').text
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
