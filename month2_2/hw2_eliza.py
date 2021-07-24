current_year=2021

class Person:
    __total_persons=0
    """This is the Docstring """
    def __init__(self,name, birth_year,**kwargs):
        if birth_year>=current_year:
            raise Exception("Invalid year")
        else:
            self.__name=name
            self.__birth_year=birth_year
            self.__language=kwargs.get("language")
            self.inc()

    def get_language(self):
        return self.__language
    def get_name(self):
        return self.__name
    def get_birth_year(self):
        return self.__birth_year


    def is_adult(self):
        if current_year-self.__birth_year>=20:
            return True
        else:
            return "Stoooop!!!"




    @classmethod
    def inc(cls):
        cls.__total_persons+=1
    @classmethod
    def get_inc(cls):
        return cls.__total_persons

    def talk_hello(self):
        return f"Hello world! I am {self.__name}... "
print(Person.__doc__)


class Teacher(Person):

    def talk_hello(self):
        return f" Greetings, I'm your teacher "
    def teach(self):
        print("Lesson started by Teacher")




#print(Person.talk_hello())

p1=Person("Eliza",2001,language='spanish')
p2=Person("Bred",1998,language='kyrgyz')
p3=Person("Python",2011,language='enlish')
p4=Teacher("Aerika",1981,language='france')
p5=Teacher("Johnson",1669,language='chinese')
p6=Teacher("Mark",1898,language='kazak')
print("UURRRAAAAHH!!! There are created ",Teacher.get_inc(),"persons")
print("---------------------------------------------------")
print("Name: ",p1.get_name(),",","Language: ",p1.get_language(),",",p1.talk_hello())
print("---------------------------------------------------")
print("Name: ",p2.get_name(),",","Language: ",p2.get_language(),p2.is_adult(),",",p2.talk_hello())
print("---------------------------------------------------")
print("Name: ",p3.get_name(),",","Language: ",p3.get_language(),p3.is_adult(),",",p3.talk_hello())
print("---------------------------------------------------")
print("Name: ",p4.get_name(),",","Language: ",p4.get_language(),",",p4.talk_hello())
print("---------------------------------------------------")
print("Name: ",p5.get_name(),",","Language: ",p5.get_language(),",",p5.talk_hello())
print("---------------------------------------------------")
print("Name: ",p6.get_name(),",","Language: ",p6.get_language(),",",p6.talk_hello())
print("---------------------------------------------------")