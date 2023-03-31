from datetime import datetime

# Подключение внутрених модулей
import excelus
import mvideo
import eldorado
import vse_instrumenti
import ozon
import wb
import send_email


def main():
    start_time = datetime.now()

    # Получение всех ids
    ids_all = excelus.r_excel()
    ids_mvideo = ids_all[0]
    ids_eldorado = ids_all[1]
    ids_vse_instrumenti = ids_all[2]
    ids_ozon = ids_all[3]
    ids_wb = ids_all[4]

    # Парсинг МВидео
    res_mvideo = mvideo.pars_mvideo(ids_mvideo)

    # Парсинг ВсеИнструменты
    res_vse_instrumenti = vse_instrumenti.pars_vse(ids_vse_instrumenti)

    # Парсинг OZON
    res_ozon = ozon.pars_ozon(ids_ozon)

    # Запить полученных данных
    res_all = []
    res_all.append(res_mvideo)
    res_all.append(res_vse_instrumenti)
    res_all.append(res_ozon)

    excelus.w_excel(res_all)

    send_email.send_email()

    print(datetime.now() - start_time)


if __name__ == '__main__':
    main()