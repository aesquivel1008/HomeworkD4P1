#1

def calculate(num1,num2,op):
    if op == "+":
        result=num1+num2
    elif op =='-':
        result=num1-num2
    elif op =='*':
        result=num1*num2
    elif op == '/':
        result=num1/num2
        return result
        
    
num1=int(input("Please enter first number" ))
op=input("Enter the operator you would like to use(-,+,*,/)" )
num2=int(input("Please enter your second number" ))

result=calculate(num1,num2,op)
print(result)

#2



def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"{item} is now in shopping list.")


def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")

def print_list(shopping_list):
    print("Shopping List:")
    if shopping_list:
        print("You do not have anything in list")
    

def full_list():
    shopping_list = []

    while True:
       
        print("1. Add item to list")
        print("2. Remove item from list")
        print("3. Print the list")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item you want to add: ")
            add_item(shopping_list, item)
        elif choice == '2':
            item = input("Enter the item you want remove: ")
            remove_item(shopping_list, item)
        elif choice == '3':
            print_list(shopping_list,item)
        elif choice == '4':
            print("Bye")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

full_list()


#3 
def calculate(average_grade,grade):
    average_grade.average(grade) 
    print(f"{average_grade} is the average grade")

def highest_grade(highest,grade):
    highest.max(grade)
    print(f"The highest grade is{highest}")

def lowest_grade(lowest,grade):
    lowest.min(grade)
    print(f"The lowest grade is {lowest}")

def grades_sorted(sorted,grades):
    sorted.sort(grades)
    (f"These {sorted} are your grades sorted by letter")
def all_grades():
    grades=[]
    while True:
        grades=input("Please enter all grades: ")
        print("1. Would you like to find the average grade?")
        print("2. Would you like to find the highest grade?")
        print("3. Would you like to find the lowest grade?")
        print("4. Would you like to sort all the grades?")
        print("5. Quit")