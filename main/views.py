from django.shortcuts import render, redirect

from main.forms import (StudentForm,CourseForm,InstructorForm,CourseScheduleForm,ScheduleDayForm,EnrollmentForm,)
from .models import (
    Student,
    Course,
    Instructor,
    CourseSchedule,
    ScheduleDay,
    Enrollment,
)
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime


@login_required(login_url="login")
def admin_dashboard(request):

    context = {
        "students": Student.objects.count(),
        "courses": Course.objects.count(),
        "instructors": Instructor.objects.count(),
        "schedules": CourseSchedule.objects.count(),
        "schedule_days": ScheduleDay.objects.count(),
        "enrollments": Enrollment.objects.count(),
    }

    return render(
        request,
        "main/admin/dashboard.html",
        context,
    )

def home(request):
    schedules = CourseSchedule.objects.select_related("course").all()
    return render(request, "main/home.html", {"schedules": schedules})


def student_create(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Student added successfully."
            )

            next_url = request.GET.get("next")

            if next_url:
                return redirect(next_url)

            return redirect("home")

    else:
        form = StudentForm()

    return render(
        request,
        "main/students/create.html",
        {"form": form},
    )

def course_create(request):

    if request.method == "POST":

        form = CourseForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Course added successfully."
            )

            return redirect("admin_dashboard")

    else:

        form = CourseForm()

    return render(
        request,
        "main/courses/create.html",
        {"form": form}
    )

def instructor_create(request):

    if request.method == "POST":

        form = InstructorForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Instructor added successfully."
            )

            return redirect("admin_dashboard")

    else:

        form = InstructorForm()

    return render(
        request,
        "main/instructors/create.html",
        {"form": form}
    )


def schedule_create(request):

    if request.method == "POST":

        form = CourseScheduleForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Course schedule added successfully."
            )

            return redirect("admin_dashboard")

    else:

        form = CourseScheduleForm()

    return render(
        request,
        "main/schedules/create.html",
        {"form": form}
    )


def schedule_day_create(request):

    if request.method == "POST":

        schedule = CourseSchedule.objects.get(
            id=request.POST.get("schedule")
        )

        days = request.POST.getlist("day[]")
        starts = request.POST.getlist("start_time[]")
        ends = request.POST.getlist("end_time[]")

        for day, start, end in zip(days, starts, ends):

            ScheduleDay.objects.create(
                schedule=schedule,
                day=day,
                start_time=datetime.strptime(
                    start,
                    "%H:%M"
                ).time(),
                end_time=datetime.strptime(
                    end,
                    "%H:%M"
                ).time(),
            )

        messages.success(
            request,
            "Schedule days added successfully."
        )

        return redirect("admin_dashboard")

    schedules = CourseSchedule.objects.all()

    return render(
        request,
        "main/schedule_days/create.html",
        {
            "schedules": schedules
        }
    )

def enrollment_create(request):

    if request.method == "POST":

        form = EnrollmentForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Student enrolled successfully."
            )

            return redirect("admin_dashboard")

    else:

        form = EnrollmentForm()

    return render(
        request,
        "main/enrollments/create.html",
        {"form": form}
    )
def schedule_details(request, id):

    schedule = get_object_or_404(
        CourseSchedule,
        id=id
    )

    days = ScheduleDay.objects.filter(
        schedule=schedule
    )

    context = {
        "schedule": schedule,
        "days": days,
    }

    return render(
        request,
        "main/details.html",
        context
    )