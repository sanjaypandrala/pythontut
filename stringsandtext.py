# assign 10 to types_of_people;
types_of_people = 10

# assign the f-string to x (insert types_of_people);
x = f"There are {types_of_people} types of people."

# assing binary to binary;
binary = "binary"
# assign don't to do_not;
do_not = "don't"

# assign f-string "{binary}" "{do_not} " to y ;
y = f"those who know {binary} and those who {do_not} "
# print x;
print(x)
# print y;
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
