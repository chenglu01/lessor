# -*- coding: utf-8 -*-
#fibonacci series 
import sys
def fibo(n):
    a , b = 0 ,1
    while a < n:
        print a,
        a , b = b , a+b
def fibo1(n):
    result = []
    a, b = 0 , 1
    while a < n:
        result.append(a)
        a , b = b , a+b
    return result

if __name__ == '__main__':
    fibo(int(sys.argv[1]))
