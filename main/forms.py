from django import forms
from .models import Course, CourseSchedule, Enrollment, Instructor, ScheduleDay, Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'full_name',
            'email',
            'phone',
            'college',
            'specialty',
            'date_of_birth',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email Address'
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),

            'college': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'College'
            }),

            'specialty': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Specialty'
            }),

            'date_of_birth': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
class CourseForm(forms.ModelForm):

    class Meta:
        model = Course

        fields = [
            "title",
            "description",
            "learning_outcomes",
            "duration_hours",
        ]

        widgets = {

            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Course Title"
            }),

            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Course Description"
            }),

            "learning_outcomes": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Learning Outcomes"
            }),

            "duration_hours": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Duration (Hours)"
            }),

        }
        
class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor

        fields = "__all__"

        widgets = {

            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Instructor Name"
            }),

            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email Address"
            }),

            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone Number"
            }),

            "field": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Specialization"
            }),

        }

class CourseScheduleForm(forms.ModelForm):

    class Meta:
        model = CourseSchedule

        exclude = ["status"]

        widgets = {

            "course": forms.Select(attrs={
                "class": "form-select"
            }),

            "instructor": forms.Select(attrs={
                "class": "form-select"
            }),

            "start_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "end_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),

            "room_number": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Room Number"
            }),

            "capacity": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Capacity"
            }),

        }
class ScheduleDayForm(forms.ModelForm):

    class Meta:
        model = ScheduleDay

        fields = "__all__"

        widgets = {

            "schedule": forms.Select(attrs={
                "class": "form-select"
            }),

            "day": forms.Select(attrs={
                "class": "form-select"
            }),

            "start_time": forms.TimeInput(attrs={
                "class": "form-control",
                "type": "time"
            }),

            "end_time": forms.TimeInput(attrs={
                "class": "form-control",
                "type": "time"
            }),

        }

class EnrollmentForm(forms.ModelForm):

    class Meta:
        model = Enrollment

        fields = "__all__"

        widgets = {

            "student": forms.Select(attrs={
                "class": "form-select"
            }),

            "schedule": forms.Select(attrs={
                "class": "form-select"
            }),

        }