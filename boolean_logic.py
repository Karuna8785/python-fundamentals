age = int(input("Enter your age: "))

can_vote = age >= 18

print("Eligible for voting:", can_vote)

print(age > 18 and age < 60)
print(age < 18 or age > 60)
print(not can_vote)