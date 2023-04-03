cou_mv = [' ', ' ', '11 990 ₽', ' ', ' ']
cou_vi = ['10 648 р.', '5 590 р.', '11 990 р.', '1 022 р.', ' ']
cou_oz = ['10 989 ₽ ', '5 590 ₽ ', '11 990 ₽ ', '1 290 ₽ ', ' ']
max_rows = 6

print(cou_mv)
print(cou_vi)
print(cou_oz)

for r in range(2, max_rows + 1):
    col_m = 'C' + str(r)
    col_v = 'E' + str(r)
    col_o = 'F' + str(r)
    print(f'{cou_mv[r - 2]} : {cou_vi[r - 2]} : {cou_oz[r - 2]}')