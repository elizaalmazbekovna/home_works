todos = []

while True:
    print('1) вывести все задачи')
    print("2) добавить задачу\n")

    option = int(input("Выберит что вам нужно? "))

    if option == 2:
        newTodo = [input("Введите задачу: ")]
        todos.append(newTodo)
    elif option == 1:
        for i in range(len(todos)):
            for j in todos[i]:
                print(str(i+1) + ": " + j)
        print()
    else:
        print("Такого варианта нету :(")
