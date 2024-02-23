import random

def flipcoin():
    coin = ["Heads", "Tails"]
    result = random.choice(coin)
    return result
results = flipcoin()

print("results: ", results)