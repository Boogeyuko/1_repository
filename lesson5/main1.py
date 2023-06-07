
def print_name(print_text, tyyyyy, is_print=False):
    if is_print == True:
        print(print_text, tyyyyy)
    else:
        print('прінтить заборонено')

print_name(input('введіть ім\'я  '), input('введіть свій вік  '), True)