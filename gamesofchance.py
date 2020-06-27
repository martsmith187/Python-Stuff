import random

#Game of Chance.

money = 100
#Write your game of chance functions here
def game_of_chance(bet, amount):
    global money
    num = random.randint(1, 10)
    if bet == num:
        money += amount
        print("Congralutions You won ! Your picked number was: " + str(bet) + " and the picked numbers was :" + str(num) + " Your pot is now: £" + str(money))
    if bet != num:
        money -= amount
        print("Whoops! You lost ! Your picked number was: " + str(bet) + " and the picked numbers was :" + str(num) + " Your pot is now: £" + str(money))
    
print("""
Testing Game of Chance Function
=====================================
""")
print("Test 1=============================")
game_of_chance(5, 10)
print("Test 2=============================")
game_of_chance(3, 10)
print("Test 3=============================")
game_of_chance(7, 10)
print("Test 4=============================")
game_of_chance(1, 10)
print("Test 5=============================")
game_of_chance(2, 10)

#Head or Tails

money = 100

def heads_of_tails(bet, amount):
    global money
    num = random.randint(1, 2)
    if num == 1 and bet == "Heads":
        money += amount
        print("Congratulations !! Your bet was " + str(bet) + " which is correct, for the amount of " + str(amount) + " Your pot is now "+ str(money))
    if num == 2 and bet == "Heads":
        money -= amount
        print("Sorry !! Your bet was " + str(bet) + " which is wrong, for the amount of " + str(amount) + " Your pot is now "+ str(money))
    if num == 2 and bet == "Tails":
        money += amount
        print("Congratulations !! Your bet was " + str(bet) + " which is correct, for the amount of " + str(amount) + " Your pot is now "+ str(money))
    if num == 1 and bet == "Tails":
        money -= amount
        print("Sorry !! Your bet was " + str(bet) + " which is wrong, for the amount of " + str(amount) + " Your pot is now "+ str(money))

print("""

Testing Heads or Tails Function
=====================================
""")
print("Test 1=============================")
heads_of_tails("Heads", 10)
print("Test 2=============================")
heads_of_tails("Heads", 10)
print("Test 3=============================")
heads_of_tails("Heads", 10)
print("Test 4=============================")
heads_of_tails("Heads", 10)
print("Test 5=============================")
heads_of_tails("Heads", 10)
print("Test 6=============================")
heads_of_tails("Tails", 10)

#Cho-Han Game

money = 100

def chohan(bet, amount):
    global money
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    if bet == "Odd":
        output = 1
    if bet == "Even":
        output =  0
    if (dice1 + dice2) % 2 == 1 and output == 1:
        money += amount
        print("Congrats !! You bet '" + str(bet) +"' :the two dice values " + str(dice1) + " + " + str(dice2) + " equal Odd.")
    if (dice1 + dice2) % 2 == 0 and output == 0:
        money += amount
        print("Congrats !! You bet '" + str(bet) +"' :the two dice values " + str(dice1) + " + " + str(dice2) + " equal Even.")
    if (dice1 + dice2) % 2 == 1 and output == 0:
        money += amount
        print("Sorry !! You bet '" + str(bet) +"' :the two dice values " + str(dice1) + " + " + str(dice2) + " equal Odd.")
    if (dice1 + dice2) % 2 == 0 and output == 1:
        money += amount
        print("Sorry !! You bet '" + str(bet) +"' :the two dice values " + str(dice1) + " + " + str(dice2) + " equal Even.")

print("""

Testing Cho-Han Function
=====================================
""")
print("Test 1=============================")        
chohan("Odd", 10)
print("Test 2=============================")
chohan("Odd", 10)
print("Test 3=============================")
chohan("Odd", 10)
print("Test 4=============================")
chohan("Even", 10)
print("Test 5=============================")
chohan("Even", 10)
print("Test 6=============================")
chohan("Even", 10)

#Pick a Card

money = 100

def deck_of_cards(bet, amount):
    global money
    num = random.randint(2,10)
    if bet < num:
        money -= amount
        print("The house Wins, you Lost :( Your card was " + str(bet) + " of Hearts and the House had " + str(num)+ " of Diamonds. Your pot is now " + str(money))
    if bet > num:
        money += amount
        print("The house Loses, you Won !! Your card was " + str(bet) + " of Hearts and the House had " + str(num)+ " of Diamonds. Your pot is now " + str(money))
    if bet == num:
        print("Its a Tie !! Your card was " + str(bet) + " of Hearts and the House had " + str(num)+ " of Diamonds. Your pot is still " + str(money))

print("""

Testing Deck of Cards Function
=====================================
""")
print("Test 1=============================")  
deck_of_cards(3,10)
print("Test 2=============================")  
deck_of_cards(2,10)
print("Test 3=============================")  
deck_of_cards(5,10)
print("Test 4=============================")  
deck_of_cards(7,10)
print("Test 5=============================")  
deck_of_cards(9,10)
print("Test 6=============================")  
deck_of_cards(8,10)


#Roulette
# Create a function that simulates some of the rules of roulette. A random number should be generated that determines which space the ball lands on.
# When we wrote our function, we allowed the user to guess "Odd", "Even", or a specific number. We also implemented the logic associated with the 0 and 00 spots. 
# For example, the player loses if they guess either "Odd" or "Even" and either 0 or 00 comes up.
# Implement as many rules of roulette as you’d like. Make sure to consider the different ways roulette rewards a win. Check the hint to see more about this!

money = 100

def roulette(bet, amount):
    global money
    house_wins = random.randint(1,100)
    num = random.randint(1,100)
    if num % 2 == 0 and bet % 2 == 0 and num == house_wins:
        money -= amount
        print("You bet Even: " + str(bet) + " The number it landed on was: 0 The House wins !! You have decreased your Pot by £ " + str(amount) + ", Your pot is now £ " + str(money))
    if num % 2 == 1 and bet % 2 == 1 and num == house_wins:
        money -= amount
        print("You bet Odd: " + str(bet) + " The number it landed on was: 00 YThe House wins !! You have decreased your Pot by £ " + str(amount) + ", Your pot is now £ " + str(money))
    if num % 2 == 0 and bet % 2 == 0:
        money += amount
        print("You bet Even: " + str(bet) + " The number it landed on was: " + str(num) + " You have increased your Pot by £ " + str(amount) + ", Your pot is now £ " + str(money))
    if num % 2 == 1 and bet % 2 == 1:
        money += amount
        print("You bet Odd: " + str(bet) + " The number it landed on was: " + str(num) + " You have increased your Pot by £ " + str(amount) + ", Your pot is now £ " + str(money))
    if num % 2 == 1 and bet % 2 == 0:
        money -= amount
        print("You bet Even: " + str(bet) + " The number it landed on was: " + str(num) + " Odd, You have decreased your Pot by £ " + str(amount) + ", Your pot is now £ " + str(money))
    if num % 2 == 0 and bet % 2 == 1:
        money -= amount
        print("You bet Odd: " + str(bet) + " The number it landed on was: " + str(num) + "  Even, You have decreased your Pot by £ " + str(amount) + ", Your pot is now £ " + str(money))
    


print("""

Testing Roulette Function
=====================================
""")
print("Test 1=============================")  
roulette(3,10)
print("Test 2=============================")  
roulette(2,10)
print("Test 3=============================")  
roulette(5,10)
print("Test 4=============================")  
roulette(7,10)
print("Test 5=============================")  
roulette(9,10)
print("Test 6=============================")  
roulette(8,10)
