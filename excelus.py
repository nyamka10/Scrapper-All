from openpyxl import load_workbook


def r_excel():
    fn = 'attachments/pars_result.xlsx'
    wb = load_workbook(fn, data_only=True)

    ids_all = []
    sheets = ['mvideo', 'eldorado', 'vse_instrumenti', 'ozon', 'wb']

    for sht in sheets:
        sheet = wb[sht]
        max_rows = sheet.max_row
        # max_rows = 2
        ids = []
        for i in range(2, max_rows + 1):
            value = sheet.cell(row=i, column=3).value
            ids.append(value)
        ids_all.append(ids)

    wb.close()
    return ids_all


def w_excel(res_all):
    print(f'[!] Начало заполнение файла')
    fn = 'attachments/pars_result.xlsx'
    wb = load_workbook(fn, data_only=True)

    sheets = ['mvideo', 'vse_instrumenti', 'ozon']
    j = 0
    o = 0
    colls = ['C', 'E', 'F']

    for sht in sheets:

        sheet = wb[sht]
        sht = wb['all']
        max_rows = sheet.max_row
        # max_rows = 2

        res_ava = res_all[j][0]
        res_cou = res_all[j][1]

        for i in range(2, max_rows + 1):
            col_avaible = 'D' + str(i)
            col_count = 'E' + str(i)
            collos = colls[o] + str(i)
            print(collos)
            sheet[col_avaible] = res_ava[i - 2]
            sheet[col_count] = res_cou[i - 2]
            sht[collos] = res_cou[i - 2]
            o = o + 1


        j = j + 1

    wb.save(fn)
    wb.close()
    print(f'[!] Запись окончена')
