from faker import Faker 
from .models import *
import random

fake = Faker()

def seed_db(n = 50)-> None:
    try:
        derpartment_obj = Department.objects.all()
        for _ in range(0, n):
            derpartment_index = random.randint(0, (len(derpartment_obj)-1))
            derpartment = derpartment_obj[derpartment_index]

            student_id = f"STU-0{random.randint(100, 999)}"
            student_name = fake.name()
            student_email = fake.unique.email()
            student_age = random.randint(18, 30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Student.objects.create(
                department = derpartment,
                student_id = student_id_obj,
                student_name = student_name,
                student_email = student_email,
                student_age = student_age,
                student_address = student_address,
            )
    except Exception as e:
        print(e)

def create_subject(n = 10)->None:
    try:
        students = Student.objects.all()
        subjects = Subject.objects.all()

        for student in students:
            for subject in subjects:
                SubjectMarks.objects.get_or_create(
                    subject = subject,
                    student = student,
                    marks = random.randint(0, 100)
                )
    except Exception as e:
        print(e)