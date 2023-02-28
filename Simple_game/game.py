"""
This is a small game program for scissors and stone cloth, 
in which you can play with the scissors and the computer to play with the scissors and will record the win
"""


import random




def subfunction():
  global userpoints, tie, rounds
  
  userpoints = 0
  tie = 0
  rounds = 0

def games():
  global userpoints, tie, rounds

  dict_game = {
    1: "rock",
    2: "paper",
    3: "scissors",
  }
  while True:    
    user = input("Please choose one in the rock scissors paper, and if you don't want to play, you can enter the quit game: ")
    if user.lower() == "quit":
      break

    if user.lower() not in dict_game.values():
      print("Invalid selection")
      continue

    i = random.randint(1,3)

    print("You chose: ", user)
    print("Computer chose: ", dict_game.get(i))

    if user.lower() == dict_game.get(i):
      print("It is a tie!")
      tie = tie + 1


    elif (user.lower() == "scissors" and i == 2) or (user.lower() == "rock" and i == 3) or (user.lower() == "paper" and i == 1):

      print("You WIN!")
      userpoints = userpoints + 1


    else:
      print("You LOSE!")
    
    rounds = rounds + 1
  
def main():
  subfunction()
  games()
  return f"You played {rounds} rounds, you win {userpoints} round, It was tied for {tie} rounds"


if __name__ == "__main__":
  print(main())

