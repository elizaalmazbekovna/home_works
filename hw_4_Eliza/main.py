

from hw_4_Eliza.calculator import Calculator
from random import randint, choices

rand_list = []
for i in range(20):
    rand_list.append(randint(0, 100))

obj=Calculator()

num1 = choices(rand_list,k=3)

print(choices(rand_list, k=3))
print(obj.addit(num1[0],num1[1], num1[2]))

print(choices(rand_list, k=3))
print(obj.comp(num1[0],num1[1], num1[2]))

print(choices(rand_list, k=2))
print(obj.mult(num1[0],num1[1]))

print(choices(rand_list, k=2))
print(obj.div(num1[0],num1[1]))
