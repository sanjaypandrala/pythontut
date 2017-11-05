print("how old are you?", end=' ')
age = input()
print(">>>>>> age=", repr(age))
# in interger format
print ("please confirm the age?", end=' ')

age = int(input())
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weigh = input()

print(f"So, you're {age} old, {height} tall and {weigh} heavy.")
