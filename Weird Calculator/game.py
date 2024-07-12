import random



def dice_game(rounds):
  print("Welcome to the dice game!")
  print('The rules are simple, you will roll a dice and guess if it will \nbe higher or lower than 3')
  print('If you guess correctly, you will get a point')
  print('if you guess incorrectly, you \nwill lose a point')
  print('You will play againts the computer')
  print('Who ever has the most points after ' + rounds + ' \nrounds wins')
  print('goodluck')

  points = 0
  comp_points = 0

  for i in range(int(rounds)):
    
    print('Round ' + str(i + 1))
    print('You have ' + str(points) + ' points')
    print('The computer has ' + str(comp_points) + ' points')

    dice_roll = random.randint(1, 6)
    comp_rand = random.randint(0, 1)
    


    while True:
      guess = input('Do you think the dice will be \nhigher or lower than 3? ')
      if guess == 'higher' and dice_roll > 3:
        print('You guessed correctly!')
        points += 1
        break
      
      elif guess == 'lower' and dice_roll < 3:
        print('You guessed correctly!')
        points += 1
        break
      
      elif guess == 'higher' and dice_roll < 3:
        print('You guessed incorrectly!')
        points -= 1
        break
      
      elif guess == 'lower' and dice_roll > 3:
        print('You guessed incorrectly!')
        points -= 1
        break

      elif dice_roll == 3:
        break
      else:
        print('Invalid input')

    if comp_rand == 0:
      print('Computer guessed correctly! \nThe dice rolled ' + str(dice_roll))
      comp_points = comp_points + 1
    elif dice_roll == 3:
      print('Dice landed on 3, Tie')
    else: 
      print('Computer guessed incorrectly! \nThe dice rolled ' + str(dice_roll))
      comp_points = comp_points - 1
      
  if points > comp_points:
    print('You won!')
  else:
    print('You lost')
    

  
  
