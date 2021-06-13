eng_to_russ={"dog":"собака","cat":"кошка",
             "book":"книга",
             "table":"стол",
             "simple":"простой"}

russ_to_eng={"dog":"собака",

             "кошка":"cat",
             "книга":"book",
             "стол":"table",
             "простой":"simple"}

eng_to_kir={"tv":"сыналгы",

             "mother":"апа",
             "door":"эшик",
             "short":"кыска",
             "fine":"сонун"}
while True:
    lang=input("Язык для перевода: ")
    if lang=="eng":

        word=input("Слово для перевода: ")
        try:
            print(eng_to_russ[word])
        except KeyError:
            for i in eng_to_kir:

                if eng_to_russ[word]==eng_to_kir[i]:
                    print("Слова есть в другом словаре,хотите ли увидеть?")
                    option=input()
                    if option=="yes":
                        print(eng_to_kir[i])
            print("Слова нету в словаре,хотите добавить?")
            option=input()
            if option=="yes":
                eng_to_russ[word]=input(f"Перевод для слово:{word} ")

    if lang=="russ":
        word=input("Слово для перевода: ")
        try:
            print(russ_to_eng[word])

        except KeyError:
            print("Слова нету в словаре,хотите добавить?")
            option = input()
            if option == "yes":
                eng_to_russ[word] = input(f"Перевод для слово:{word} ")

    if lang=="kir":
        word=input("Слово для перевода: ")
        try:
            print(eng_to_kir[word])

        except KeyError:
            print("Слова нету в словаре,хотите добавить?")
            option = input()
            if option == "yes":
                eng_to_kir[word] = input(f"Перевод для слово:{word} ")