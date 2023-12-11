# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


'''def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.'''
import sys
import time
import types
import math
from threading import Thread
def countup(N):
    n = 0
    while n < N:
        n += 1

def get_key_in_dict(k, dict):
    is_key = k in dict.keys()
    k_res = None
    if is_key == False:
        # check int values
        try:
            is_key = int(k) in dict.keys()
            k_res = int(k)
        except:
            ValueError
    else:
        k_res = k
    return k_res

def test_func():
    a = 1
    b = 2
    c = 3
    return a

def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

def f4(x=5):
    print(x)
    x += 1
    return x + 1

def switch_light(x):
    return not x

def print_light_state(light):
    if light:
        print("on")
    else:
        print("off")

def encrypt_letter(char, key_int):
    if not char.isalpha():
        return char
    r = "abcdefghijklmnopqrstuvwxyz"
    index = r.index(char) + int(key_int)
    leng = len(r)
    if index > len(r):
        index = index - leng
    result = r[index]
#    l = 26 - int(key_int)
#    if char in r[l:26]:
#        delta = 26
#    else:
#        delta = 0
#    result = chr((ord(char) + int(key_int))) # - delta))
    return result

def calculate_shifts(char):
    if not char.isalpha():
        return char
    return "abcdefghijklmnopqrstuvwxyz".index(char)

def encrypt_text(text, keyword):
    text_l = text.lower()
    keyw_l = keyword.lower()
    i = 0
    result = str()
    for letter in text_l:
        if i > len(keyw_l) - 1:
            i = 0
        result += encrypt_letter(letter, calculate_shifts(keyw_l[i]))
        i += 1
    return result


def is_prime(num):
    for i in range(2, int(num)):
        if num % i == 0:
            return False
    return True

def sum_even_numbers(n):
#    even_list = list()
    tmp = 0
    result = 0
    i = 0
    while i < int(n):
        i += 1
        tmp += 2
        result += tmp
    return result

def prime_list(num):
    result = []
    for i in range(2, int(num) + 1):
        if is_prime(i):
            result.append(i)
    return result

def ispronic(n: int):
    sq = math.sqrt(n)
    sq_f = math.floor(sq)
    sq_c = math.ceil(sq)
    if sq_f * (sq_f+1) == n or sq_c * (sq_c+1) == n:
        return True
    return False

def isabundant(n: int):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
           sum += i
    if sum > n:
        return True
    return False

def isnarcisstic(n: int):
    # get degree
    n_str = str(n)
    dig = len(n_str)
    result = 0
    for s in n_str:
        result += math.pow(int(s),dig)
    if n == result:
        return True
    return False

def print_pascal_triangle(n: int):
    lines = [[1],[1,1]]
    i = 1
    while i < int(n):
        new_line = [1,1]
        k = 1
        while k < len(lines):
            new = lines[len(lines)-1][k-1]+lines[len(lines)-1][k]
            new_line.insert(k,new)
            k+=1
        i+=1
        lines.append(new_line)
    i = 0
    while i < len(lines):
        print(lines[i])
        i+=1

# Press the green button in the gutter to run the script.'''
if __name__ == '__main__':
    print_pascal_triangle(input("NUmber of lines: "))
#    print(prime_list(int(input("Enter any number: "))))
#    print(encrypt_text(input("Enter text to be encrypted: "), input("Enter keyword: ")))

    '''    mass_list = tuple(range(50,105,5))
    height_list = tuple(range(150, 205, 5))

    #print(mass_list)
    #print(height_list)

    header_cols =f"{'h[m] / w[kg]':>13s}"
    for m in mass_list:
        header_cols+=f"{m:5d}"
    print(header_cols)
    print("-"*68)

    for h in height_list:
        var = f"{h/100:1.2f}"
        mass_var = f"{var:>13s}"
        for m in mass_list:
            mass_var += f" {m/((h/100)**2):2.1f}"
        print(mass_var)'''
