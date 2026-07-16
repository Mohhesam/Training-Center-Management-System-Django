from django.contrib import admin


from .models import (
    Student,
    Course,
    CourseSchedule,
    Enrollment,
    Instructor,
    ScheduleDay,
)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "college",
        "specialty",
    )

    search_fields = (
        "full_name",
        "email",
    )
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        # "instructor",
        "duration_hours",
        # "days_per_week",
    )

    search_fields = (
        "title",
        # "instructor",
    )


@admin.register(CourseSchedule)
class CourseScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "course",
        "start_date",
        "end_date",
        "room_number",
        "capacity",
        "enrolled_count",
        "remaining_seats",
        "is_full",
        "status",
    )

    search_fields = (
        "course__title",
        "room_number",
    )

    list_filter = (
        "status",
    )
    
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "schedule",
        "enrollment_date",
    )

    search_fields = (
        "student__full_name",
        "schedule__course__title",
    )
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "phone",
        "field",
    )

    search_fields = (
        "full_name",
        "email",
    )
@admin.register(ScheduleDay)
class ScheduleDayAdmin(admin.ModelAdmin):
    list_display = (
        "schedule",
        "day",
        "start_time",
        "end_time",
    )

    list_filter = (
        "day",
    )