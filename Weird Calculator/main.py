import random
import math
import matplotlib.pyplot as plt
import functions
import login
import game


login.sign_up()

while True:
  iflogin = input("Do you want to login? (y/n) ")
  if iflogin == "y":
    break
  elif iflogin == 'n':
    print("Okay, bye!")
    quit()
  else:
    print('Invalid input')

functions.block_sign_up()

login.login()

while True:
  ifoptions = input("Type 'o' for options ")

  if ifoptions == "o":
    while True:
      print(
          "Type 'g' to generate a random number, type 'c' to \ncalculate the area of a \ncircle, Type 'graph' to create a graph,Type 'game' \nto open the game interface 'x' \nto exit"
      )

      userintent = input("What would you like to do? ")
      if userintent == "g":

        while True:
          try:
            functions.generate_num(input("How many characters would you like your number to be? "))
          except:
            print("Invalid input")
          else:
            break

      elif userintent == "c":
        while True:
          try:
            functions.calc_pi(input("What is the radius of the circle? "))
          except:
            print("Invalid input")
          else:
            break
      elif userintent == "x":
        exit()

      elif userintent == "graph":

        x = []
        y = []
        while True:
          x1 = input("What is the 1st x value? ")
          x2 = input("What is the 2nd x value? ")
          x3 = input("What is the 3rd x value? ")

          y1 = input("what is the 1st y value? ")
          y2 = input("What is the 2nd y value? ")
          y3 = input("What is the 3rd y value? ")

          try:
            x.append(float(x1))
            x.append(float(x2))
            x.append(float(x3))

            y.append(float(y1))
            y.append(float(y2))
            y.append(float(y3))
          except:
            print('Invald input')
          else:
            break

        xlabel = input("What is the x label? ")
        ylabel = input("What is the y label? ")
        title = input("What is the title? ")

        functions.create_graph(x, y, str(xlabel), str(ylabel), str(title))

        print('Invalid input')

      elif userintent == "game":
        game.dice_game(input("How many rounds would you \nlike to play? "))

      else:
        print("Invalid input")
