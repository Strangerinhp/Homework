import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        exp_x = torch.exp(x)
        return exp_x / exp_x.sum()


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x)
        exp_x = torch.exp(x - x_max)
        return exp_x / exp_x.sum()


# Test
data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(output)

softmax_stable = SoftmaxStable()
output_stable = softmax_stable(data)
print(output_stable)
