import time
from extension import proxies
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from proxy_auth import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


proxies_extension = proxies(PROXY_USER, PROXY_PASS, PROXY_HOST, PROXY_PORT)


def pars_mvideo(ids_mvideo):
    start_time = datetime.now()

    options = webdriver.ChromeOptions()
    # options.add_extension(proxies_extension)
    options.add_argument('--no-sandbox')
    options.add_argument("--headless=new")
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(2)
    driver.maximize_window()

    result_mvideo = []
    count_mvideo = []
    res_mvideo = []

    try:
        print(f'[!] Старт парсинга Mvideo')
        driver.get('https://www.mvideo.ru/')
        time.sleep(1)

        for id in ids_mvideo:
            search_input = driver.find_element(By.CLASS_NAME, 'input__field')
            search_input.clear()
            search_input.send_keys(id)
            search_input.send_keys(Keys.ENTER)
            time.sleep(2)

            try:
                # driver.find_element(By.CLASS_NAME, 'price__main-value')
                # result_mvideo.append('В наличии')
                cou = driver.find_element(By.CLASS_NAME, 'price--pdp-emphasized-personal-price')
                count = cou.find_element(By.CLASS_NAME, 'price__main-value').text
                result_mvideo.append('В наличии')
                count_mvideo.append(count)
                print(f'[+] Mvideo {id} : В наличии : {count}')

            except NoSuchElementException:
                result_mvideo.append('Нет в наличии')
                count_mvideo.append(' ')
                print(f'[-] Mvideo {id} : Нет в наличии')

        print(f'[!] Mvideo Конец парсинга')
        res_mvideo.append(result_mvideo)
        res_mvideo.append(count_mvideo)
        return res_mvideo

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        times = datetime.now() - start_time
        print(f'Время парсинга М Видео : {times}')
