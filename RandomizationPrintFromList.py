import random
from random import choice
#list
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#hardest
random_friend = friends[random.randint(0,4)]
print(random_friend)

#medium
random_number = random.randint(0,4)
print(friends[random_number])

#easiest
print(choice(friends))