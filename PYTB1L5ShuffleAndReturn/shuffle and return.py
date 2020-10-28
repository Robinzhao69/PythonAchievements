import random


def shuffle(randomised):
    
    randomised = ''.join(random.sample(randomised,  len(randomised)))
    return str(randomised)
    

print(shuffle("oke"))
print(shuffle("banaan"))
print(shuffle("auto"))
