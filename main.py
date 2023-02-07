from ast import While
from turtle import clear
from art import logo,vs
from dataset import data
import random

def formating(acct):
#formating the acct to print
    acct_name = acct["name"]
    acct_desc = acct["description"]
    acct_country = acct["country"]
    return(f"{acct_name},a {acct_desc}, from {acct_country} ")

#Comparing the accounts
def compare(guess,a_follower,b_follower):
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"





# print logo
print(logo)
score = 0
game_should_start = True
acct_b = random.choice(data)

 #repeat till loose
while game_should_start:

    #random generate the accounts 
    
    acct_a = acct_b
    acct_b = random.choice(data)
    while acct_a == acct_b:
        acct_b = random.choice(data)

    print(f"account A: {formating(acct_a)}")
    print(vs)
    print(f"Compare B: {formating(acct_b)}")

    #guess the number 
    guess = input("Who has more Followers? Type 'A' or 'B': ").lower()

    a_follower = acct_a["follower_count"]
    b_follower = acct_b["follower_count"]

    is_correct = compare(guess,a_follower,b_follower)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"You are right! current score: {score}")
    else:
        game_should_start = False
        print(f"You Guessed wrong, Your score is {score}")