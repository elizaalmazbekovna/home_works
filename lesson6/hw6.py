import  random

num=random.randint(1,16)

print(num)
while True:
    run=input("Хотите играть? ")
    if run=="да":

        user_num=int(input("Введите цифру от 1 до 15: "))
        if num==user_num:
            print("Урраа, вы победили!")
        elif num-3<=user_num<=num+3:
            print("горячо")

        elif num-5<=user_num<=num+5:
            print("тепло")

        else:
            print("холодно")

    if run=="нет":
        print("Остановилось")