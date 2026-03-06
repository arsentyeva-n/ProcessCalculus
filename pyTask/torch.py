import torch
import time


def multy(N,M):
  for _ in range(1):  # Многократные умножения для точности измерения
    AB = torch.mm(a, b)


# Размеры матриц
N = 1000
M = 1000
# Создание матриц и перенос их на GPU
a = torch.ones(N, M).cuda()
b = torch.ones(N, M).cuda()


# Замер времени умножения
start_time = time.time()
multy(N,M)
end_time = time.time()

print("Время умножения матриц с использованием PyTorch GPU: ", end_time - start_time)
