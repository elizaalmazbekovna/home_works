
import datetime
dt=datetime.datetime.now()
print(dt)

def writefile():
    file = open("data1.txt", "a+", encoding="UTF-8")
    file.write(f"Последние действие:  {dt}\n")
    file.close()

def readfile():
    file=open("data1.txt","r+",encoding="UTF-8")
    lines=file.readlines()
    for i in lines:
        print(i[:-1])
    file.close()
    writefile()
print(readfile())





def drawFild():
    for i in range(3):
        print()
        print(str(game_field[i][0])+'  ' +
              str(game_field[i][1])+'  '+str(game_field[i][2]))


order = 'x'


def change_order():
    global order
    if order == 'x':
        order = 'o'
    else:
        order = 'x'


game_field_template = [
    ['*', '*', '*'],
    ['*', '*', '*'],
    ['*', '*', '*']
]
game_field = game_field_template[:]

win_templates = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1),
                                            (2, 0)], [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)]]


def check_field():
    for template in win_templates:
        p1, p2, p3 = template
        if game_field[p1[0]][p1[1]] == game_field[p2[0]][p2[1]] == game_field[p3[0]][p3[1]] != '*':
            return game_field[p1[0]][p1[1]]
    for row in range(3):
        for column in range(3):
            if game_field[row][column] == '*':
                return False
    return None


while True:
    winner = check_field()
    if winner:
        print("Победитель: ", winner)
        game_field = game_field_template[:]
        print('-----------------------------------------------------------')

    elif winner is None:
        print("Ничья")
        game_field = game_field_template[:]
        print('-----------------------------------------------------------')

    drawFild()
    row, column = input(
        f'Куда будем ставить {order}? Введите 2 числа через пробел (строку и колонку)').split(' ')
    row, column = int(row), int(column)
    try:
        game_field[row][column] = order
        change_order()
    except:
        print('Вы ввели неверные значения')