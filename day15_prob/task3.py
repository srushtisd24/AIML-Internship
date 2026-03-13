import random

trials = 100000
success = 0

for i in range(trials):
    
    bag = ["Red"]*5 + ["Blue"]*5
    
    first = random.choice(bag)
    bag.remove(first)
    
    second = random.choice(bag)
    
    if first == "Red" and second == "Red":
        success += 1

probability = success / trials

print("Experimental Probability:", probability)
print("Theoretical Probability:", 2/9)