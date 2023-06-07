
turists = []


def poll():
    name = input('введіть ім\'я  ')
   
    def get_age():
        global age 
        try:
            age = int(input('введіть вік '))
        except:
            print('введіть вік числом!!!!!!!!!!!')
            get_age()

    get_age()
    

    prof = input('введіть професію ')


    

    def get_the_next():
        global the_next
        the_next = input('це остання людина? : введіть так або ні')
        if the_next == 'так':
            the_next = True
        elif the_next == 'ні':
            the_next = False
        else:
            print('введіть так або ні !!!!!!')
            get_the_next()

    get_the_next()
    

    turist = {
    'name': name,
    'age': age,
    'prof': prof,
    }

    turists.append(turist)

    if the_next == False:
        poll()

poll()


for tourist in turists:
    name = tourist['name']
    age = tourist['age']
    prof = tourist['prof']
    print(f'З нами в групі {name}, якому {age} років, професія якого {prof}')


