#как на уроке
def fun_list(fun):
    def f_n():
        print(fun().split())
    return f_n

@fun_list
def ent_list():
    return str(input('enter some string: '))

ent_list()

#так тоже работает
def fun_list(fun):
      return print(fun().split())

@fun_list
def ent_list():
    return str(input('enter some string: '))