from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("students/create/", views.student_create, name="student_create"),
    path("courses/create/", views.course_create, name="course_create"),
    path("instructors/create/", views.instructor_create, name="instructor_create"),
    path("schedules/create/", views.schedule_create, name="schedule_create"),
    path("schedule-days/create/", views.schedule_day_create, name="schedule_day_create"),
    path("enrollments/create/", views.enrollment_create, name="enrollment_create"),
    path("admin-dashboard/",views.admin_dashboard,name="admin_dashboard",),
    path("schedule/<int:id>/",views.schedule_details,name="schedule_details",),
]