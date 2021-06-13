eng_to_russ={"dog":"собака","cat":"кошка","book":"книга","table":"стол","simple":"простой"}

while True:
    word=input("Слова для перевода")
    try:
        print(eng_to_russ[word])

    except KeyError:
        print("Такого нету")