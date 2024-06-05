import math
import random

def exercise3():
    def MAE(x):
        final_MAE = 0
        for i in range(x+1):
            pred = random.uniform(0,10)
            target = random.uniform(0,10)
            loss = pred - target
            final_MAE += loss
            print(f'loss name : MAE , sample : {i} , pred : {pred} , target : {target} , loss : {loss}')
        print(f'final_MAE = {final_MAE}')

    def MSE(x):
        final_MSE = 0
        for i in range(x+1):
            pred = random.uniform(0,10)
            target = random.uniform(0,10)
            loss = (pred - target)**2
            final_MAE += loss
            print(f'loss name : MSE , sample : {i} , pred : {pred} , target : {target} , loss : {loss}')
        print(f'final_MSE = {final_MSE}')
        
    def RMSE(x):
        final_RMSE = 0
        for i in range(x+1):
            pred = random.uniform(0,10)
            target = random.uniform(0,10)
            temp = (pred - target)**2
            loss = math.sqrt(temp)
            final_RMSE += loss
            print(f'loss name : RMSE , sample : {i} , pred : {pred} , target : {target} , loss : {loss}')
        print(f'final_RMSE = {final_RMSE}')

    num_samples = input('Input number of samples ( integer number ) which are generated :')
    if num_samples.isnumeric() == False:
        return 'number of samples must be an integer number'
    else:
        num_samples = int(num_samples)
        loss_func = input('Input loss name :')
        if loss_func == "MAE":
            MAE(num_samples)
        elif loss_func == "MSE":
            MSE(num_samples)
        elif loss_func == "RMSE":
            RMSE(num_samples)
        else:
            print(f'{loss_func} is not supported')
            
exercise3()