class Student:
    all_courses=['python','java','cpp','c','mySQL','digital marketing','SAP','cloud computing','DBMS','DSA']
    def __init__(self,id_p,name_p,email_p):
        self.id=id_p
        self.name=name_p
        self.email=email_p
        self.courses=[]
    def show_all_courses(self):
        print('\n**AVAILABLE COURSES**')
        for i in range(len(self.all_courses)):
            print(f'{i+1}.{self.all_courses[i]}')
        choice=int(input('Number of courses you wnat enroll:'))
        for i in range(choice):
            course=input('enter the course you want to enroll:')
            if course not in self.all_courses:
                print('Invalid Input!!Please check the avaliable courses')
            else:
                self.courses.append(course)
        print(f'\nYou enroll for the following courses')


    def remove_course(self):
        print(self.courses,'\n')
        choice=int(input('enter the number of courses you want to remove:'))
        for i in range(choice):
            course = input('enter the course you want to remove:')
            if course not in self.courses:
                print('Invalid Input!!Please check the enrolled courses')

            else:
                self.courses.remove(course)
                print(f'you removed {course} course')

    def get_issued_courses(self):
        for i in range(len(self.courses)):
            print(f'{i+1}.{self.courses[i]}\n')


    def show_details(self):
            print('\nStudent Details:')
            print(f'Student Id: {self.id}')
            print(f'Name: {self.name}')
            print(f'Email: {self.email}')
            print(f'courses: {self.courses}\n')

a=Student(101,'renu','abc@gmail.com')
a.show_all_courses()
a.get_issued_courses()
a.remove_course()
a.show_details()





