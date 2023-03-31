res_all = [[['В наличии', 'Нет в наличии', 'В наличии', 'Нет в наличии', 'Нет в наличии'], ['9 010 ₽', ' ', '11 990 ₽', ' ', ' ']], [['Нет в наличии', 'В наличии', 'В наличии', 'В наличии', 'Нет в наличии'], [' ', '4 216 р.', '11 990 р.', '1 049 р.', ' ']], [['В наличии', 'В наличии', 'В наличии', 'В наличии', 'В наличии', 'Нет в наличии'], ['10 990 ₽', '5 590 ₽', '11 990 ₽', '1 290 ₽', ' ']]]

sheets = ['mvideo', 'vse_instrumenti', 'ozon']

j = 0
for sht in sheets:

    # sheet = wb[sht]
    # max_rows = sheet.max_row
    max_rows = 6

    res_ava = res_all[j][0]
    print(f'res_ava : {res_ava}')
    res_cou = res_all[j][1]

    for i in range(2, max_rows + 1):
        col_avaible = 'D' + str(i)
        col_count = 'E' + str(i)
        # sheet[col_avaible] = res_ava[i - 2]
        # sheet[col_count] = res_cou[i - 2]
        print(f'наличие: {res_ava[i - 2]}, стоимость: {res_cou[i - 2]}')
    print(j)
    j = j + 1

