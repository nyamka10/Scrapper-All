import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from extension import proxies
from selenium_stealth import stealth
from captcha_solver import CaptchaSolver

# данные прокси
PROXY_HOST = '91.188.243.162'
PROXY_PORT = 9434
PROXY_USER = 'E8Wmqg'
PROXY_PASS = 'ZgUf8X'

proxies_extension = proxies(PROXY_USER, PROXY_PASS, PROXY_HOST, PROXY_PORT)
solver = CaptchaSolver('rucaptcha', api_key='45fe483c082a3c39258b5bcf92a21622')


def pars_eldo():
    start_time = datetime.now()

    options = webdriver.ChromeOptions()
    # options.add_extension(proxies_extension)
    options.add_argument('--no-sandbox')
    # options.add_argument("--headless=new")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    driver.maximize_window()

    stealth(driver,
            languages=["ru-RU", "ru"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )

    result_eldorado = []
    count_eldorado = []
    res_eldorado = []

    ids_eldorado = ['74385701', '590002138', '590035269', '74471647', '590016106']

    try:
        print(f'[!] Старт парсинга Эльдорадо')
        driver.get('https://www.eldorado.ru/')
        time.sleep(2)

        try:
            # проверка на капчу
            driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/footer/div[2]')
            time.sleep(2)
            for id in ids_eldorado:
                # переход на карточку товара
                driver.get(f'https://www.eldorado.ru/search/catalog.php?q={id}&utf')
                try:
                    # проверка наличия товара по кнопке
                    driver.find_element(By.CLASS_NAME, 'KM')
                    try:
                        driver.find_element(By.CLASS_NAME, 'Sv')
                        result_eldorado.append('Витринный образец')
                        count = driver.find_element(By.CLASS_NAME, 'JQ').text
                        count_eldorado.append(count)
                        print(f'[+] Eldo {id} : Витринный образец : {count}')
                    except NoSuchElementException:
                        result_eldorado.append('В наличии')
                        count = driver.find_element(By.CLASS_NAME, 'JQ').text
                        count_eldorado.append(count)
                        print(f'[+] Eldo {id} : В наличии : {count}')
                except NoSuchElementException:
                    result_eldorado.append('Нет в наличии')
                    print(f'[-] Eldo {id} : Нет в наличии')

        except NoSuchElementException:
            # получаем капчу
            captcha = driver.find_element(By.CLASS_NAME, 'capture')
            src = captcha.get_attribute('src')
            img_captcha = captcha.screenshot_as_png
            with open('captcha.jpg', 'wb') as f:
                f.write(img_captcha)
            # решаем капчу
            raw_data = open('captcha.jpg', 'rb').read()
            caps = solver.solve_captcha(raw_data)
            print(caps)
            # вписываем капчу
            search_input = driver.find_element(By.CLASS_NAME, 'input-ru')
            search_input.clear()
            search_input.send_keys(caps)
            time.sleep(3)
            search_input.send_keys(Keys.ENTER)

            time.sleep(8)

        finally:
            pass
        print(f'[!] Eldo Конец парсинга')
        res_eldorado.append(result_eldorado)
        res_eldorado.append(count_eldorado)
        return res_eldorado

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        times = datetime.now() - start_time
        print(f'Время парсинга Эльдорадо : {times}')


def main():
    pars_eldo()


if __name__ == '__main__':
    main()