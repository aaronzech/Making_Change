# [2021-06-07] Challenge #393 [Easy] Making change
import math


def change(number):
    #Coins
    coin_500 = 0
    coin_100 = 0
    coin_25 = 0
    coin_10 = 0
    coin_5 = 0
    coin_1 = 0
    balance = int(number)
    sum = 0

    # Check the amount of 500 coins that can be given out
    if (balance >=500):
        coin_500 = math.floor(balance / 500)
        balance = number % 500
        sum = coin_500
    # Check the amount of 100 coins that can be given out
    if (balance>=100):
        coin_100 = math.floor(balance / 100)
        balance = number % 100
        sum += coin_100
    # Check the amount of 25 coins that can be given out    
    if(balance >=25):
        coin_25 = math.floor(balance / 25)
        balance = (balance % 25)
        sum += coin_25
    if(balance >=10):
            coin_10 = math.floor(balance/10)
            balance = (balance % 10)
            sum += coin_10
    if(balance>=5):
        coin_5 = math.floor(balance/5)
        balance = (balance % 5)
        sum += coin_5
    if(balance>=1):
        coin_1 = math.floor(balance/1)
        balance = (balance % 1)
        sum += coin_1
    if(balance == 0):
        return sum   
    


print(change(0))
print(change(12))
print(change(468))
print(change(123456))

money = input("Enter how much cash you have? (whole numbers only)")
print(change(int(money)))