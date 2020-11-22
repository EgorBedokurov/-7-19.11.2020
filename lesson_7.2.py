# рабочая функция, с декоратором на ввод данных не получается

type_t = input('enter type temperature C, F or K - ') #исходная шкала температур
val_t = int(input('enter value of temperature  - ')) #температура по исходной шкале

def calc_temp():
    if type_t == 'C':
        print('in Farengate - ', + int(9/5*val_t+32))
        print('in Kelvin - ', + int(val_t+273))
    elif type_t == 'F':
        print('in Celsium - ', + int(5/9*(val_t-32)))
        print('in Kelvin - ', + int(5/9*(val_t-32)+273))
    else:
        print('in Farengate - ', + int(9/5*(val_t-273)+32))
        print('in Celsium - ', + int(val_t-273))

calc_temp()



# черновой лог. операция
# type_t = input('enter type temperature C, F or K - ')
# val_t = int(input('enter temperature value - '))
#
# if type_t == 'C':
#     print('in Farengate - ', + int(9/5*val_t+32))
#     print('in Kelvin - ', + int(val_t+273))
# elif type_t == 'F':
#     print('in Celsium - ', + int(5/9*(val_t-32)))
#     print('in Kelvin - ', + int(5/9*(val_t-32)+273))
# else:
#     print('in Farengate - ', + int(9/5*(val_t-273)+32))
#     print('in Celsium - ', + int(val_t-273))
