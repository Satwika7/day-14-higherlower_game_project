import random
from replit import clear
from values import dict
from art import *
print(logo1)
score=0
list_of_keys=list(dict.keys())
A=random.choice(list_of_keys)
def higher_lower(score,A,list_of_keys):
  print("\n")
  #random.shuffle(list_of_keys)
  B=random.choice(list(dict.keys()))
  while A==B:
    B=random.choice(list(dict.keys()))  
  if A>B:
    greater="A"
  else:
    greater="B"
  print(f"Compare A: {dict[A]}\n\n {logo2} \n\nagainst B: {dict[B]}")
  user_choice=input("\nwho has more followers on Instagram? Type 'A' or 'B': ").upper()
  if user_choice==greater:
    score+=1
    A=B
    #list_of_keys.remove(B)
    clear()
    print(f"you are correct,current score is {score}")
    higher_lower(score,A,list_of_keys)
  else:
    print(f"you are wrong,total score is {score}\n game ended.")
    
higher_lower(score,A,list_of_keys)