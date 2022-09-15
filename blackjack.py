import os
import random
from re import L
import sys

deck = {
    "1": ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "2": ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "3": ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    "4": ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
}

usedCards = {
    "1": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "2": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "3": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "4": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

# after players finish, dealer hits until the sum is equal or greater than 17

def aceDeal():
    res = int(input("You were dealt an ace. 1 or 11? "))

    
    while res != 1 and res != 11:
        os.system("clear")
        res = int(input("Invalid input. 1 or 11? "))
    
    os.system("clear")
    return res


def dealCards(cards):
    
    cardIndex = random.randint(0, 12)
    faceIndex = str(random.randint(1, 4))
    
    while usedCards[faceIndex][cardIndex] == 1:
        cardIndex = random.randint(0, 12)
        faceIndex = str(random.randint(1, 4))
        
    if deck[faceIndex][cardIndex] == "ace":
        card = aceDeal()
    else:
        card = deck[faceIndex][cardIndex]
    
    cards.append(card)
    usedCards[faceIndex][cardIndex] = 1
        
    return cards

def getSum(cards):
    sum = 0
    for i in cards:
        sum += i
    return sum
    

dealerCards = []
playerCards = []
for i in range(2):
    dealerCards = dealCards(dealerCards)
for i in range(2):
    playerCards = dealCards(playerCards)
    
playerSum = getSum(playerCards)
dealerSum = getSum(dealerCards)

print(f"Your cards: {playerCards}. Total: {playerSum}")

if playerSum > 21:
    print("You lose.")
    sys.exit()

hit = 0
stand = False

while stand == False:
    os.system("clear")
    
    print(f"Your cards: {playerCards}. Total: {playerSum}")
    
    move = input("Hit or Stand? (H/S): ")
    while move not in ["h", "H", "s", "S"]:
        os.system("clear")
        move = input("Invalid input. Hit or Stand? (H/S): ")
    
    if move in ["h", "H"]:
        playerCards = dealCards(playerCards)
    else:
        stand = True;
    
    playerSum = getSum(playerCards)
    print(f"Your cards: {playerCards}. Total: {playerSum}")
    
    if playerSum > 21:
        print("You lose.")
        sys.exit()

while dealerSum < 17:
    dealerCards = dealCards(dealerCards)
    dealerSum = getSum(dealerCards)
    
os.system("clear")
print(f"Your cards: {playerCards}. Total: {playerSum}")
print(f"Dealer's cards: {dealerCards}. Total: {dealerSum}")

if dealerSum > 21:
    print("You win!")
    sys.exit()
elif playerSum == dealerSum:
    print("Tie!")
    sys.exit()
elif playerSum < dealerSum:
    print("You lose!")
    sys.exit()
else:
    print("You Win!")
    sys.exit()
    
    
    


