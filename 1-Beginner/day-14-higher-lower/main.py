import art
from game_data import data
import random
import os

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  return f" {account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, first_account, second_account):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if first_account["follower_count"] > second_account["follower_count"]:
    return guess == "a"
  else:
    return guess == "b"

def game(first_account, score):
  cur_score = score
  first_account = first_account
  second_account = get_random_account()
  
  while first_account == second_account:
    second_account= get_random_account()
  
  print(art.logo)
  if cur_score > 0:
    print("Compare A: " + format_data(first_account) + ",Current Socre: " + str(cur_score))
  else:
    print("Compare A: " + format_data(first_account))
  print(art.vs)
  print("Againts B: " + format_data(second_account))

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  if check_answer(guess, first_account, second_account):
    cur_score += 1
    os.system('clear')
    print(f"You're right! Current score: {cur_score}")
    game(second_account, cur_score)
  else:
    os.system('clear')
    print(art.logo)
    print(f"Sorry, that's wrong. Final score: {cur_score}")
    
account_a = get_random_account()
game(account_a, 0)