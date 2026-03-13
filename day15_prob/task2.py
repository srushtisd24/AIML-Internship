import random
trials = 100000
success = 0

for i in range(trials):
    
    coin = random.choice(["Heads", "Tails"])
    die = random.randint(1,6)
    
    if coin == "Heads" and die == 6:
        success += 1

probability = success / trials

print("Experimental Probability:", probability)
print("Theoretical Probability:", 1/12)