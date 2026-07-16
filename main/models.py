from django.db import models

from django.core.exceptions import ValidationError
from datetime import date
######### Student model to store student information ###########

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    college = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


    
########## Course model to store course information ###########
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    learning_outcomes = models.TextField()
    # instructor = models.CharField(max_length=100)
    duration_hours = models.PositiveIntegerField()
    # days_per_week = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title
    

############ Instructor model to store instructor information ###########
class Instructor(models.Model):

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    field  = models.CharField(max_length=100)
    def __str__(self):
        return self.full_name
    
########### CourseSchedule model to store course schedule information ###########
class CourseSchedule(models.Model):

    STATUS_CHOICES = [
        ("Upcoming", "Upcoming"),
        ("Running", "Running"),
        ("Finished", "Finished"),
    ]

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )
    instructor = models.ForeignKey(
    Instructor,
    on_delete=models.SET_NULL,
    null=True,
    blank=True
)

    start_date = models.DateField()
    end_date = models.DateField()

    room_number = models.CharField(max_length=20)

    capacity = models.PositiveIntegerField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Upcoming"
    )

    def save(self, *args, **kwargs):

        today = date.today()

        if today < self.start_date:
            self.status = "Upcoming"

        elif self.start_date <= today <= self.end_date:
            self.status = "Running"

        else:
            self.status = "Finished"

        super().save(*args, **kwargs)


    @property
    def enrolled_count(self):
        return self.enrollment_set.count()

    @property
    def remaining_seats(self):
        return max(0, self.capacity - self.enrolled_count)

    @property
    def is_full(self):
        return self.enrolled_count >= self.capacity

    def __str__(self):
        return f"{self.course.title} ({self.start_date})"



############ Enrollment model to store student enrollment information ###########


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    schedule = models.ForeignKey(
        CourseSchedule,
        on_delete=models.CASCADE
    )

    enrollment_date = models.DateField(auto_now_add=True)

    def clean(self):
        if self.schedule.is_full:
            raise ValidationError(
                "This course is full. No more students can be enrolled."
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.full_name} - {self.schedule.course.title}"

########### ScheduleDay model to store the days and times of the course schedule ###########

class ScheduleDay(models.Model):

    DAY_CHOICES = [
    ("Sunday", "Sunday"),
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
]
    schedule = models.ForeignKey(
        CourseSchedule,
        on_delete=models.CASCADE
    )

    day = models.CharField(
        max_length=10,
        choices=DAY_CHOICES
    )

    start_time = models.TimeField()

    end_time = models.TimeField()
    def __str__(self):
        return f"{self.schedule.course.title} - {self.day}"

