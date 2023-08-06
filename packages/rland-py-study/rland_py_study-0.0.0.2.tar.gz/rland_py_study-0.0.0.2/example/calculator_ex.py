from rland_py_study import *

_cal = calculator.Calculator()
while(1):
    _input = str(input("Please insert number and operator\nPresent value : "+str(_cal.result())+"\n(ex. +10 or -10, quit:q, reset:r)\ninput : "))
    if _input[0] == '+':
        print("Add")
        _input=_input[1:]
        _cal.add(float(_input))
    elif _input[0] == '-':
        print("Sub")
        _input=_input[1:]
        _cal.sub(float(_input))
    elif _input[0] == '*':
        print("mul")
        _input=_input[1:]
        _cal.mul(float(_input))
    elif _input[0] == '/':
        print("Div")
        _input=_input[1:]
        if(float(_input)==0):
            print("can't divided by 0")
        else:
            _cal.div(float(_input))
    elif _input[0] == 'r':
        _cal.reset()
        print("Calculator is reset")
    elif _input[0] == 'q':
        exit()
    else:
        print("Wrong input. Please insert right direction.")
