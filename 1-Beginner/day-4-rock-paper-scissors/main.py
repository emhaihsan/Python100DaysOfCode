rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
                  
computer_choice = random.randint(0,2)
                  

# if user_choice == 0:
#     if computer_choice == 1:
#         print(f"You chose {rock}\nComputer chose {paper}\nYou lose")
#     elif computer_choice == 2:
#         print(f"You chose {rock}\nComputer chose {scissors}\nYou win")
#     else:
#         print(f"You chose {rock}\nComputer chose {rock}\nIt's a draw")
# elif user_choice == 1:
#     if computer_choice == 0:
#         print(f"You chose {paper}\nComputer chose {rock}\nYou win")
#     elif computer_choice == 2:
#         print(f"You chose {paper}\nComputer chose {scissors}\nYou lose")
#     else:
#         print(f"You chose {paper}\nComputer chose {paper}\nIt's a draw")
# else:
#     if computer_choice == 0:
#         print(f"You chose {scissors}\nComputer chose {rock}\nYou lose")
#     elif computer_choice == 1:
#         print(f"You chose {scissors}\nComputer chose {paper}\nYou win")
#     else:
#         print(f"You chose {scissors}\nComputer chose {scissors}\nIt's a draw")
