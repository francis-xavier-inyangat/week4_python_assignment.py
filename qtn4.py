# Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
# percentage less than 50 (Grade C)
# percentage equal to 50 and less than 80 (Grade B)
# percentage equal to 80 and more than 80 (Grade A)

def totalMarks(marks):
    total = 0
    for i in marks:
        total = total + i
    print(total)
    return total

def percentage(marks):
    average = str(totalMarks(marks)/len(marks))

    print(average + '%' + "is the average percantage mark")

    return float(average)

def grade(marks):
    if percentage(marks) >= 80:
        print('Grade A')
    elif percentage(marks) >= 50 and percentage(marks) <= 80:
        print('Grade B')
    
    else:
        print('Grade C')

def main():
    print('Enter Marks')
math = int(input('Enter math marks: '))
english = int(input('Enter english marks: '))
sst = int(input('Enter sst marks: '))
science = int(input('Enter science marks: '))
re = int(input('Enter RE marks: '))

marks = []

marks.append(math)
marks.append(english)
marks.append(sst)
marks.append(science)
marks.append(re)

print("Total Mark, press: t \n" + "Avarage % Mark, press: a \n" + "Grade, press: g \n")
choice = input("Choose Operation: ")

if choice == "t":
    totalMarks(marks)

if choice == "a":
    percentage(marks)

if choice == "g":
    grade(marks)



main()


