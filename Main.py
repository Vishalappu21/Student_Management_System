Student = []

def add_students(lst):
    StudentID = int(input('Please Enter Your ID Number: '))
    Name = input('Please Enter Your Name: ').lower()
    Age = int(input('Please Enter Your Age: '))
    Marks = int(input('Please Enter Your Mark: '))
    
    student = {
        "id": StudentID,
        "name": Name,
        "age": Age,
        "marks": Marks
    }

    lst.append(student)
    print('Student added successfully.')

def view_students(data):
    if not data:
        print('No students found')  
        return
    for student in data:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Marks: {student['marks']}"
        )
def search_students(data):
    Name_of_the_student = input('Please Enter the student Name: ').lower()
    found = False
    for i in data:
        if i['name'] == Name_of_the_student:
            print("\nStudent Found:")
            print(f"ID: {i['id']}")
            print(f"Name: {i['name']}")
            print(f"Age: {i['age']}")
            print(f"Marks: {i['marks']}")
            
            found = True
            break
        if not found:
            print('Student Not Found...')
            
def update_marks(data):
    student_id = int(input("Please enter Student ID: "))
    change_the_marks = int(input('Enter the marks to update: '))
    found = False
    for i in data:
        if i['id'] == student_id:
            i['marks'] = change_the_marks
            print("Marks updated successfully.")
            
            found = True
            break
        if not found:
            print('Student Not Found...')    

def delete_students(data):
    delete_the_student = input('Please enter the name of the student to delete: ')
    found = False
    for index in data:
        if index['name']== delete_the_student:
            data.remove(index)
            print('Student Deleted Successfully')
            found = True
            break
        if not found:
            print('Student Not Found...') 

def topper_data(data):
    if not data:
        print('Student Not Found...')
        return
        
    topper = data[0]
    for index in data:
        if index['marks'] > topper['marks']:
            topper = index
    print('\nTopper: ')   
    print(f"ID: {topper['id']}")
    print(f"Name: {topper['name']}")
    print(f"Age: {topper['age']}")
    print(f"Marks: {topper['marks']}")



def avergae(data):
    if not data:
        print('Student Not Found...')
        return
    count = 0
    sum_marks = 0
    for index in data:
        count += 1
        sum_marks += index['marks']
    Average_Marks = sum_marks / count
    print(f'Avg-Mark: {Average_Marks}')
        
    

print("===Student Management System===")

while True:
    user_need = int(
                input(
                    '1. Add Student\n'
                    '2. View All Students\n'
                    '3. Search Student\n'
                    '4. Update Marks\n'
                    '5. Delete Student\n'
                    '6. Show Topper\n'
                    '7. Show Average Marks\n'
                    '8. Exit\n'
                    'Please select the Option : '
        )
    )
    if user_need == 1:
        add_students(lst = Student)
    elif user_need == 2:
        view_students(data = Student)
    elif user_need == 3:
        search_students(data=Student)  
    elif user_need == 4:
        update_marks(data= Student)
    elif user_need == 5:
        delete_students(data = Student)
    elif user_need == 6:
        topper_data(data= Student)
    elif user_need == 7:
        avergae(data= Student)
    elif user_need == 8:
        print('Please enter one again...')
        break
        