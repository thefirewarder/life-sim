import random
def update_grade():
    if grade_num > 100:
        grade_num = 100
    if grade_num >= 90:
        grade = "A"
    elif grade_num >= 80:
        grade = "B"
    elif grade_num >= 70:
        grade = "C"
    elif grade_num >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade
righteousness = random.randint(50,100)
happiness = random.randint(25,100)
health = random.randint(75,100)
social_intelligence = random.randint(50,100)
def print_stats():
    print("Stats: ")
    print("Righteousness: "+str(righteousness))
    print("Happiness: "+str(happiness))
    print("Health: "+str(health))
    print("Social Intelligence: "+str(social_intelligence))
grade_num = random.randint(60,100)
grade = "C"
print("Welcome to python life simulator!")
print("To avoid anything unusual, you will be single your whole life, and your life will start at age 14.")
print("Have fun!")
if random.randint(1,3) == 1:
    choice1 = int(input("Let's begin. You are taking a math test in your 9th grade algebra class. Solve for x to see if you pass. 2x - 5 = 9 "))
    if choice1 == 7:
        grade_num += 20
        
    else:
        grade_num-=10
        if grade_num > 100:
            grade_num = 100
        grade = update_grade()
    print("Your grade has been updated. You currently have a "+grade+" on your high school transcript!")
elif random.randint(1,2) == 1:
    choice1 = input("You see someone being bullied in the hallways. What do you do? (help/ignore)").lower()
    if choice1 == "ignore":
        social_intelligence += random.randint(1,10)
        righteousness -= random.randint(1,10)
        if social_intelligence > 100:
            social_intelligence = 100
        if righteousness < 0:
            righteousness
