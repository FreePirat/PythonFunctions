import math

def performOperation(num1, num2, operation='sum'): # default operation of sum
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
    else:
        return 'Not a valid operation'
    
print(performOperation(2, 3))
print(performOperation(5, 7, operation='multiply'))

def perfomPrint(*args, **kwargs):
    print(args)
    print(kwargs)

perfomPrint(1, 2, 3, operation='sum')

def performOperationFlex(*args, operation='sum'):
        if operation == 'sum':
            return math.sum(args)
        if operation == 'multiply':
            return math.prod(args)
        else:
            return 'Not a valid operation'
        
print(performOperationFlex(2, 6, 8, operation='multiply'))

def performOperationLocal(num1, num2, operation='sum'):
    print(locals())

performOperationLocal(1, 2, operation='multiply')

def function1(varA, varB):
    print(locals())

def function2(varC, varB):
    print(locals())

function1(1, 2)
function2(2, 4)