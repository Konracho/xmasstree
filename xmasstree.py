"""H - высота елки
   I - интервал украшений,
   L - Строка
   C - Столбец - координаты, где начиналась верхушка елки"""

def base_el(args_list):
    H, I = map(int, args_list)
    position = 0
    print('X'.center(H * 2, ' '), '^'.center(H * 2, ' '), sep='\n')
    for i in range(0, H * 2 - 2, 2):
        quantity = '*' * (i + 1)
        quantity_list = list(quantity)

        for j in range(len(quantity)):
            if j % 2 != 0:
                position += 1
                if position == I or i == 2:
                    quantity_list[j] = 'O'
                    position = 0
        quantity = ''.join(quantity_list)

        stroka = '/' + quantity + '\\'
        print(stroka.center(H * 2, ' '))

    print('| |'.center(H * 2, ' '))

def parse_input(args_list):
    args_one_el = 4
    parse_args_list = []
    for start_arg in range(0, len(args_list), args_one_el):
        H, I, L, C = map(int, args_list[start_arg: start_arg + args_one_el])
        parse_args_list.append([H, I, L, C])
    return parse_args_list

def otkritka(parsed):
    X = 50
    Y = 30
    matr = []
    for i in range(Y):
        matr.append([' '] * X)

    for i in range(len(matr)):
        for j in range(len(matr[i])):

            matr[i][0] = '|'
            matr[i][49] = '|'
            matr[0][j] = '-'
            matr[29][j] = '-'
            # matr[L + H + 1][C - 1: C + 2] = '| |'

            print(matr[i][j], end='')
        print()
        signature = 'Merry Xmas'

        matr[Y - 3][(X // 2) - (len(signature) // 2): (X // 2) + (len(signature) // 2)] = signature

        print_el1(parsed, matr, Y)

def print_el1(parsed, matr, Y):
    for args in parsed:
        H, I, L, C = args[: len(args)]
        position = 0
        next_stolb = 2
        matr[L][C] = 'X'
        matr[L + 1][C] = '^'
        for i in range(0, H * 2 - 2, 2):
            quantity = '*' * (i + 1)
            quantity_list = list(quantity)

            for j in range(len(quantity)):
                if j % 2 != 0:
                    position += 1

                    if position == I or i == 2:
                        quantity_list[j] \
                            = 'O'
                        position = 0
            quantity = ''.join(quantity_list)
            stroka = '/' + quantity + '\\'

            if (L + next_stolb) >= (Y - 3):
                break
            else:
                matr[L + next_stolb][C - (len(stroka) // 2): C + (len(stroka) // 2) + 1] = stroka
                next_stolb += 1

        matr[L + H + 1][C - 1: C + 2] = '| |'
def main():
    args = input()
    args_list = list(args.split(' '))
    if len(args_list) == 2:
        base_el(args_list)
    else:
        parsed = parse_input(args_list)
        otkritka(parsed)

main()
