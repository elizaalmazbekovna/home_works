todos=[]

while True:
    print("1)Добавить задачу")
    print("2) Показать задачи")
    option= int(input())

    if option==1:
        task=input()
        deadline=input()
        date_add=input()
        todo=[task,deadline,date_add]
        todos.append(todo)
        print("Задача добавлено")


    if option==2:
        print("------------------------")
        for i in todos:
            print(i[0],i[1],i[1])

        print("------------------------")
