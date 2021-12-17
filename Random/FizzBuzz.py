'''
FizzBuzz

Output numbers from 1 to x. If the number is divisable by 3,replace it with "Fizz". If it is divisable by 5,
replace it with "Buzz". If it is divisable by 3 and 5 replace it with "FizzBuzz".

eg:

1
2
Fizz
4
Buzz 
Fizz 
7
8
Fizz
...
14
FizzBuzz
16

'''

def fizzBuzz(x):
    for i in range(1, x + 1):  
        toPrint = i
        if (i % 3 == 0):
            toPrint = "Fizz"

        if (i % 5 == 0):
            toPrint = "Buzz"

        if (i % 3 == 0 and i % 5 == 0):
            toPrint = "FizzBuzz"
        print(toPrint)

fizzBuzz(81)