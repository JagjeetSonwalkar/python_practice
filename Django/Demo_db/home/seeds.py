from .models import Student, Department, Course
from faker import Faker
import random
from datetime import date, timedelta
from django.core.validators import MinValueValidator, MaxValueValidator

fake = Faker()

# ---------------------------
# Seed Departments
# ---------------------------
def seed_departments():
    department_names = ["IT", "CSE", "Mechanical", "Civil", "E & TC"]
    for name in department_names:
        Department.objects.get_or_create(name=name)
    print("Departments seeded!")


# ---------------------------
# Seed Courses
# ---------------------------
def seed_courses():
    course_names = [
        "Software Engineering", "Operating Systems", 
        "Networking", "AI & ML", "Structural Analysis"
    ]
    for name in course_names:
        Course.objects.get_or_create(name=name)
    print("Courses seeded!")


# ---------------------------
# Seed Students
# ---------------------------
def seed_students(n=10):
    """
    Generate n fake students using existing Departments and Courses
    """
    print(f"Creating {n} fake students...")

    departments = list(Department.objects.all())
    courses = list(Course.objects.all())

    if not departments:
        print("No Departments found! Run seed_departments() first.")
        return

    if not courses:
        print("No Courses found! Run seed_courses() first.")
        return

    for _ in range(n):
        name = fake.name()
        email = fake.unique.email()
        address = fake.address()
        age = random.randint(18, 25)
        gpa = round(random.uniform(2.0, 4.0), 2)
        dob = date.today() - timedelta(days=age*365 + random.randint(0, 364))
        is_active = random.choice([True, False])
        dept = random.choice(departments)

        student = Student.objects.create(
            name=name,
            address=address,
            age=age,
            gpa=gpa,
            date_of_birth=dob,
            is_active=is_active,
            email=email,
            department=dept,
            user=None  # No auth user
        )

        # Assign 1–3 random courses
        student_courses = random.sample(courses, k=random.randint(1, min(3, len(courses))))
        student.courses.set(student_courses)

        student.save()

    print(f"{n} fake students created successfully!")
