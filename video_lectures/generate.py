from random import choice
from random import randint
from random import shuffle

def main():
    coin = coin_flipper()
    print(coin)
    hand = card_shuffler()
    for card in hand:
        print(card)
    rng = random_number_generator()


def coin_flipper():
    coin = choice(["heads", "tails"])
    if coin == "heads":
        return """  
          ████████████            
      ████░░░░░░░░░░░░████        
    ██░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░██      
  ██░░░░▒▒░░░░░░░░░░░░▒▒░░░░██    
  ██░░▒▒░░░░      ░░░░░░  ░░██    
██░░▒▒░░░░░░  ░░░░▒▒░░░░░░  ░░██  
██░░▒▒░░      ░░░░░░  ░░░░  ░░██  
██░░▒▒░░  ░░░░░░░░░░░░▒▒░░  ░░██  
██░░▒▒░░  ░░░░░░░░░░░░▒▒░░  ░░██  
██░░▒▒░░░░▒▒░░░░░░▒▒▒▒▒▒░░  ░░██  
██░░▒▒░░░░░░  ░░░░▒▒░░░░░░  ░░██  
  ██░░▒▒░░░░░░▒▒▒▒▒▒░░░░  ░░██    
  ██░░░░  ░░░░░░░░░░░░  ░░░░██    
    ██░░░░            ░░░░██      
      ████░░░░░░░░░░░░████        
          ████████████ 
"""
       
    else:
        return "tails"

def card_shuffler():
    cards = ["jack", "queen", "king"]
    hand = []
    shuffle(cards)
    for card in cards:
        hand.append(card)

    return hand

def random_number_generator():
    number = randint(1, 10)
    return print(f"{number}")

main()