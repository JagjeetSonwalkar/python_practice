from django.db import models

# Create your models here.
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self)->str:
        return self.department
    
    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=50)

    def __str__(self)->str:
        return self.student_id                          

'''
StudentManager - the heart of soft delete
What Django normally does
models.Manager().get_queryset() → returns ALL rows from DB

What YOU changed:
You overrode get_queryset():
.filter(is_deleted=False)
Result: Every query through Student.objects automatically hides deleted rows & Also, No need to write .filter(is_deleted=False) every time
'''
class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE )
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    # Soft delete flag
    # False → active record, True → logically deleted
    # Record still exists in DB
    is_deleted = models.BooleanField(default=False)

    '''
    Custom Object Manager
    This becomes the default queryset: Student.objects.all()
    '''
    objects = StudentManager()  # Default manager

    '''
    Admin / raw manager
    This gives unfiltered access to the database: Student.admin_objects.all()
    '''
    admin_objects = models.Manager()


    def __str__(self)->str:
        return self.student_name
    
    class Meta:
        ordering = ['student_name']
        verbose_name = "student"

class Subject(models.Model):
    subject_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.subject_name

class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="studentmarks")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField(default=None)

    def __str__(self) -> str:
        return f"{self.student.student_name} {self.subject.subject_name}"

    class Meta:
        unique_together = ['student', 'subject']