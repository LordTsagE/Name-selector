# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
a = int(len(names))
b = random.randint(0, a-1)
c = names[b]
print(c)


#Write your code below this line 👇



