#1.WAP to remove the item present at index 4 and add it to the 2nd position and at the list 
#Items[3,5,7,9,11,13]
items = [3, 5, 7, 9, 11, 13]
x = items.pop(4)
items.insert(1, x)
items.append(x)
print(items)

#2. WAP to find the intersection (common) of two sets and remove those elements from 
# the first set.
A = {1, 2, 3, 4}
B = {3, 4, 5}
common = A.intersection(B)
A -= common
print(A)

#3. first_set = {23, 42, 65, 57, 78, 83, 29} second_set = {57, 83, 29, 67, 73, 43, 48} 
# Write a code to checks if one set is a subset or superset of another set. If found, delete all 
# elements from that set. first_set = {27, 43, 34} second_set = {34, 93, 22, 27, 43, 53, 48}
first_set ={27,43,34}
second_set ={34,93,22,27,43,53.48}
if first_set.issubset(second_set):
    first_set.clear()
elif first_set.issuperset(second_set):
    second_set.clear()
print(first_set,second_set)

#4.Write a code to get all values from the dictionary and add them to a list but don’t add 
# duplicates
#month = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54,
#'Aug': 44, 'Sept': 54}
month = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44,
         'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
result = list(set(month.values()))
print(result)

#5.Write a code to remove duplicates from a list and create a tuple and find the minimum and 
# maximum number sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
unique = list(set(sample_list))
t = tuple(unique)
print("Tuple:", t)
print("Min:", min(t))
print("Max:", max(t))

#6.Consider the following code:


#7 Write a Python program that defines two sets: club_A containing the members "Alice", "Bob", 
# and "Charlie" and club_B containing the members "David", "Eve",and "Bob". The program should 
# check whether the two clubs have any members in common. If they do, 
# print "There is an overlap!" If they have no common members,print "No overlap between clubs."
club_A = {"Alice", "Bob", "Charlie"}
club_B = {"David", "Eve", "Bob"}
if club_A & club_B:
    print("There is an overlap!")
else:
    print("No overlap between clubs.")

#8 Consider the following code


#9 Write a Python program that checks whether a student is eligible to enroll in a
# requested course based on course availability and minimum grade requirements.You are given: 
student = {"name": "Ram", "course": "Math", "grade": 75}
valid_courses = {"Science", "Math", "English"}
min_grades = {
    "Science": 70,
    "Math": 60,
    "English": 65
}
course = student["course"]
grade = student["grade"]
if course not in valid_courses:
    print("Invalid course.")
elif grade < min_grades[course]:
    print(f"Grade too low for {course}.")
else:
    print(f"{student['name']} approved for {course}.")

#10 Write a Python program that defines two sets:
required_tasks = {"Email", "Report", "Meeting"}
completed_tasks = {"Email", "Report"}
if required_tasks.issubset(completed_tasks):
    print("All tasks done!")
else:
    print("Some tasks pending.")

#11 Write a Python program that stores student contact information using a dictionary
contacts = {
    "Ram Sharma": "ram@gmail.com",
    "Sita Thapa": "sita@gmail.com"
}
name = input("Enter student name: ")
if name in contacts:
    print("Email:", contacts[name])
else:
    print("Contact not found.")

#12 Write a Python program that defines two sets: shopping_list containing "Milk","Bread", 
# and "Eggs". bought_containing "Bread" and "Eggs"
shopping_list = {"Milk", "Bread", "Eggs"}
bought = {"Bread", "Eggs"}
remaining = shopping_list - bought
if remaining:
    print("Still need to buy:", remaining)
else:
    print("Shopping complete!")

#13 Write a Python program that adds a new student to a class list only if they are not already 
# enrolled.
class_list = ["ram", "sita", "laxman"]
new_student = "ram"
if new_student not in class_list:
    class_list.append(new_student)
    print("Added ram.")
else:
    print("ram is already in class.")

#14 votes = ["Blue", "Red", "Blue", "Green", "Blue"] Count how many voted "Blue".
votes = ["Blue", "Red", "Blue", "Green", "Blue"]
count = votes.count("Blue")
if count >= 3:
    print("Blue wins!")
else:
    print("Blue did not win.")

#15  Write a Python program that checks whether a student’s grade exists in a given dictionary 
# and prints an appropriate message.
grades = {"Ram": 92, "Sita": 88}
student = "Laxman"
if student in grades:
    print(f"{student}'s grade is {grades[student]}.")
else:
    print(f"Grade not available for {student}.")

#16 Write a Python program that checks whether a student is eligible to enroll in an elective 
# course based on the following school rules:
student = {"name": "Hari", "course": "Robotics", "grade": 9}
valid_courses = {"Creative Writing", "Robotics", "Digital Art"}
name = student["name"]
course = student["course"]
grade = student["grade"]
if course not in valid_courses:
    print(f"{name} selected an invalid course.")
elif grade < 9 or grade > 12:
    print(f"{name} is not eligible for {course} (grade too low).")
elif course == "Robotics" and grade == 9:
    print(f"{name} is not eligible for {course} (grade too low).")
else:
    print(f"{name} is approved for {course}.")

#17 A company accepts an application only if: The candidate knows Python or Java, and
applicant = {
    "name": "Priya",
    "skills": ["Java", "SQL"],
    "experience_years": 1
}
required_skills = {"Python", "Java"}
has_skill = bool(set(applicant["skills"]) & required_skills)
has_experience = applicant["experience_years"] >= 2
if has_skill and has_experience:
    print("Priya qualifies.")
else:
    print("Priya does not qualify.")

#18 Write a Python program that determines whether an airline passenger’s cabin baggage is 
# allowed based on two rules:
banned_items = {"scissors", "knife", "lighter"}
weight = float(input("Enter baggage weight: "))
item = input("Enter item: ").lower()
if weight <= 7 and item not in banned_items:
    print("Bag accepted.")
else:
    print("Bag not allowed.")

#19 A teacher created two quiz groups, but accidentally put the same student in both.
# You need to detect if any student appears in both groups.
group1 = {"Ram", "Sita", "Hari"}
group2 = {"Gita", "Sita", "Ramesh"}
if group1.isdisjoint(group2):
    print("Groups are OK – no overlap.")
else:
    print("Warning: Groups share at least one student!")

#20 Write a program to change shyam salary to 8500 in the following dictionary. Given:
salary = {"ram": 5000, "shyam": 6000, "hari": 7000}
salary["shyam"] = 8500
print(salary)

#21 Riya bought: "bread", "butter", "jam", "tea" and Anjali bought: "butter", "jam",
#"coffee", "eggs". Write a Python program that stores their items in two sets called 
# riya and anjali.\
riya = {"bread", "butter", "jam", "tea"}
anjali = {"butter", "jam", "coffee", "eggs"}
result = riya - anjali
if result:
    print("Riya has extra items:", result)
else:
    print("Riya has no extra items.")

#22  Write a Python program that: Stores Alice’s and Bob’s items in two sets: alice_items and 
# bob_items. 
alice_items = {"Milk", "Eggs"}
bob_items = {"Juice", "Bread"}
if alice_items.isdisjoint(bob_items):
    print("They picked completely different items.")
else:
    print("They have some common items.")
