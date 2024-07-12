class user():

  def __init__(self, username, password):
    self.username = username
    self.password = password


def sign_up():
  username = input("What is your username? ")
  password = input("What is your password? ")

  global user1
  user1 = user(username, password)
  print("Your username is " + user1.username + " and your password is " +
        user1.password)


def login():
  for i in range(5):
    user_name = input("Username: ")
    passkey = input('Password: ')
    if user_name == user1.username and passkey == user1.password:
      print("You have successfully logged in!")
      break

    else:
      print("Incorrect username or password \nTry again")

    if i == 5:
      print('Too many failed attempts \nTry again later')
