class Calculator:


    @staticmethod
    def addit(*args):
        return sum(args)

    @staticmethod
    def comp(*args):
        num = 0
        for n in args:
            num -= n
        return  num
    @staticmethod
    def mult(a,b):
        return a*b

    @staticmethod
    def div(x,y):
        return x/y


