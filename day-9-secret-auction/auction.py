# from replit import clear
from art import logo
import os
print(logo)
print("Welcome to the secret auction program.")
auction = {}
finish = False
while not finish:
  bidder = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  auction[bidder] = bid
  another = input("Another bidder? Type 'yes' or 'no'.\n")
  if another.lower() == "no":
    finish = True
#   clear()
  os.system('cls' if os.name == 'nt' else 'clear') # alternative for clear()
winner = ""
max_bid = 0

for bidder in auction:
  if auction[bidder] > max_bid:
    winner = bidder
    max_bid = auction[bidder]
print(f"The winner is {winner} with a bid of ${max_bid}.")