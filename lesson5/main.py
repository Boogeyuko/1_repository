def plus(a, b):

    def arithmatic():

        c = input('введіть арифметичну дію ( + ) ( - ) ( * ) ( / ) ')

        if c == '/':

            if b != 0:
                result = a / b
                print(result) 

            else:
                j = input('\tна нуль ділить не можна \n\tщоб змінити дію натисніть + ')
                if j =='+':
                    arithmatic()
                    
                
        elif c == '*':
            result = a * b
            print(result)

        elif c == '-':
            result = a - b
            print(result)

        else:
            print('введіть коректне значення')
            arithmatic()

    arithmatic()



def get_a():
    global a
    try:
        a = int(input('введіть число а '))
    except:
        print('введіть число!!!')
        get_a()
    
get_a()

def get_b():
    global b
    try:
        b = int(input('введіть число b '))
    except:
        print('введіть число!!!')
        get_b()
    
get_b()


plus(a, b)

