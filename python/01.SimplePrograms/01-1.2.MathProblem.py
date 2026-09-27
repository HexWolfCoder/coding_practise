from math import *

print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("▌                                                 ▐")
print("▌       Задача 1.2. Вариант 17                    ▐")
print("▌                                                 ▐")
print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")

print("Составить прграмму вычисления таблицы значений функции f(x) из задачи 1.1 для n значений аргумента x,равномерно распределенных на отрезке [a,b]. Для проверки программы задать n=10, a=0.50, b=1.00. Результаты выдать в виде таблицы, в каждой строке - соответственно порядковый номер, значение аргумента и значение функции с шестью знаками после запятой")

print("-------------------------------------------------------")

#ToDo ===>
# зададим переменные
check_res=2.36642
x = 0.5

a = 0.50
b = 1.00
n = 10

# посчитаем результат
# Здесь надо использовать цикл(!) Но! для достоверности - реши "линейно"
print("ТАБЛИЦА ФУНКИИ")
print("n \t X \t Y \t")
print("---------------------------------")
delta = (b-a)/n

index=0
x=a+delta*index
result=abs(7.2 - 10*x)/(x/9 + e**(2*x))**(1/3)
result= round(result * atan((4 * tan(2*x))/(sqrt(1.1*x**3))), 6)
print(f"|{index + 1}\t| {x} \t| {result}\t|")
print("---------------------------------")

index=1
x=a+delta*index
result=abs(7.2 - 10*x)/(x/9 + e**(2*x))**(1/3)
result= round(result * atan((4 * tan(2*x))/(sqrt(1.1*x**3))), 6)
print(f"|{index + 1}\t| {x} \t| {result}\t|")
print("---------------------------------")

index=2
x=a+delta*index
result=abs(7.2 - 10*x)/(x/9 + e**(2*x))**(1/3)
result= round(result * atan((4 * tan(2*x))/(sqrt(1.1*x**3))), 6)
print(f"|{index + 1}\t| {x} \t| {result}\t|")
print("---------------------------------")

index=3
x=a+delta*index
result=abs(7.2 - 10*x)/(x/9 + e**(2*x))**(1/3)
result= round(result * atan((4 * tan(2*x))/(sqrt(1.1*x**3))), 6)
print(f"|{index + 1}\t| {x} \t| {result}\t|")
print("---------------------------------")

index=4
x=a+delta*index
result=abs(7.2 - 10*x)/(x/9 + e**(2*x))**(1/3)
result= round(result * atan((4 * tan(2*x))/(sqrt(1.1*x**3))), 6)
print(f"|{index + 1}\t| {x} \t| {result}\t|")
print("---------------------------------")

index=5
x=a+delta*index
result=abs(7.2 - 10*x)/(x/9 + e**(2*x))**(1/3)
result= round(result * atan((4 * tan(2*x))/(sqrt(1.1*x**3))), 6)
print(f"|{index + 1}\t| {x} \t| {result}\t|")
print("---------------------------------")

index=6
x=a+delta*index
result=abs(7.2 - 10*x)/(x/9 + e**(2*x))**(1/3)
result= round(result * atan((4 * tan(2*x))/(sqrt(1.1*x**3))), 6)
print(f"|{index + 1}\t| {x} \t| {result}\t|")
print("---------------------------------")

index=7
x=a+delta*index
result=abs(7.2 - 10*x)/(x/9 + e**(2*x))**(1/3)
result= round(result * atan((4 * tan(2*x))/(sqrt(1.1*x**3))), 6)  #<==== ERORR for View!
print(f"|{index + 1}\t| {x:.2} \t| {result}\t|")
print("---------------------------------")

index=8
x=a+delta*index
result=abs(7.2 - 10*x)/(x/9 + e**(2*x))**(1/3)
result= round(result * atan((4 * tan(2*x))/(sqrt(1.1*x**3))), 6)
print(f"|{index + 1}\t| {x} \t| {result}\t|")
print("---------------------------------")

index=9
x=a+delta*index
result=abs(7.2 - 10*x)/(x/9 + e**(2*x))**(1/3)
result= round(result * atan((4 * tan(2*x))/(sqrt(1.1*x**3))), 6)
print(f"|{index + 1}\t| {x} \t| {result}\t|")
print("---------------------------------")


