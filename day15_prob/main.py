import random
trials = 1000

count_sum7 = 0

for i in range(trials):
    
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    
    total = dice1 + dice2
    
    if total == 7:
        count_sum7 += 1
probability = count_sum7 / trials

print("Number of trials:", trials)
print("Number of times sum = 7:", count_sum7)
print("Experimental Probability of sum = 7:", probability)