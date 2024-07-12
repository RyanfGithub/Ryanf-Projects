import random
import math
import matplotlib.pyplot as plt
import os


def block_sign_up():
  os.system('cls')

def generate_num(characters):
  num = ""
  for i in range(int(characters)):
    num = num + str(random.randint(0, 9))
  print(num)


def calc_pi(r):
  area = math.pi * int(r)**2
  print("A = " + str(area))
  

def create_graph(x, y, xlabel, ylabel, title):

  plt.plot(x, y)

  plt.xlabel(xlabel)
  plt.ylabel(ylabel)
  plt.title(title)

  plt.show()
