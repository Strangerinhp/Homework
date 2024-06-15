import math
def exercise2():

    def sigmoid(x):
        return 1/(1+math.e**(-x))
    
    def relu(x):
        if x <= 0:
            return 0
        if x > 0:
            return x
        
    def elu(x):
        if x <= 0:
            return 0.01*(math.e**x-1)
        if x > 0:
            return x
        
    def is_number(x):
        try: 
            float(x)
        except ValueError:
            return False
        return True
    
    x = input("Input x = ")
    if is_number(x) == True:
        x = float(x)
        func = input('Input activation Function ( sigmoid | relu | elu ) : ')
        if func == "sigmoid":
            print(f'sigmoid: f({x})={sigmoid(x)}')
        elif func == "relu":
            print(f'relu: f({x})={relu(x)}')
        elif func == "elu":
            print(f' elu: f({x})={elu(x)}')
        else:
            print(f'{func} is not supported')
    else:
        print("X must be a number")
    
exercise2()