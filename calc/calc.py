
a = 0
b = 0

def get_a():
    global a
    try:
        a = float(input('введіть число a '))
    except:
        print('введіть число!!!')
        get_a()

get_a()


def get_b():
    global b
    try:
        b = float(input('введіть число b '))
    except:
        print('введіть число!!!')
        get_b()

get_b()



def arifmatic():
    c = input('введіть арифметичну дію: + - * /')

    if c == '+':
        result = a + b
        print(result)

    elif c == '-':
        result = a - b
        print(result)


    elif c == '/':
        if b != 0:
            result = a / b 
            print(result)
        else:
            print('На нуль ділити  не можна!')
            get_b()
            arifmatic()

    elif c == '*':
        result = a * b
        print(result)

    else:
        print('введіть коректне значення')
        arifmatic()
    

arifmatic()
 