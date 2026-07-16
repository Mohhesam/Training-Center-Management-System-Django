# Training Center Management System

A full-stack web application built with Django, following the MVT (Model-View-Template) architecture, for managing the daily operations of a physical training center. Receptionists register students and administrators manage courses, instructors, schedules, and enrollments.

This project demonstrates backend development, database design, authentication, CRUD operations, business logic, and responsive frontend design using Bootstrap.

## Technologies Used

- Python 3
- Django
- SQLite
- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons
- JavaScript (dynamic Schedule Day form)
- Git / GitHub

## Project Purpose

The application manages the daily operations of an offline training center.

**Administrators can:**
- Manage courses
- Manage instructors
- Create course schedules
- Define weekly class sessions
- Enroll students
- Prevent overbooking
- Track schedules automatically

**Receptionists can:**
- View available courses
- Register new students
- Enroll students into available schedules

## Database Design

The database follows normalization principles, separating entities into reusable models connected via Foreign Keys.

### Student
Stores student information.
- Full Name
- Email (unique)
- Phone
- College
- Specialty
- Date of Birth

*Relationship: one student can have many enrollments.*

### Course
Represents the course itself (e.g. Python Programming, Networking Fundamentals, Cyber Security, Data Science).
- Title
- Description
- Learning Outcomes
- Duration Hours

> A Course does **not** contain an instructor, since multiple instructors can teach the same course at different times.

### Instructor
Stores instructor information.
- Full Name
- Email
- Phone
- Field / Specialization (e.g. Programming, Networking, Cyber Security, AI, Data Science)

### CourseSchedule
Represents one actual running class (e.g. Python Programming, July 20 → August 20, Instructor Ahmed, Room 301, Capacity 20).
- Course (ForeignKey)
- Instructor (ForeignKey)
- Start Date
- End Date
- Room Number
- Capacity
- Status *(calculated automatically)*

### ScheduleDay
Each `CourseSchedule` can contain multiple weekly sessions. Rather than storing something like "Monday, Wednesday, Thursday" in a single field, every day is stored as a separate row.
- Course Schedule
- Day
- Start Time
- End Time

The frontend allows adding multiple `ScheduleDay` records on one page using JavaScript.

### Enrollment
Represents the relationship between Students and Course Schedules.
- Student
- Schedule
- Enrollment Date *(auto-generated)*

### Relationships

```
Course
  └── CourseSchedule
        └── ScheduleDay

Student
  └── Enrollment
        └── CourseSchedule

Instructor
  └── CourseSchedule
```

## Business Logic

### Automatic Schedule Status
Course schedules automatically determine their status (`Upcoming`, `Running`, `Finished`) inside the model's `save()` method, by comparing today's date with the schedule dates. No manual selection is required.

### Capacity Management
Every `CourseSchedule` tracks capacity dynamically via computed properties:
- `enrolled_count`
- `remaining_seats`
- `is_full`

### Enrollment Validation
Validation is implemented inside the `Enrollment` model. Before saving, `full_clean()` calls `clean()`, which raises a `ValidationError` if `schedule.is_full` — students cannot enroll in full courses.

## Authentication

The application uses Django's built-in authentication system.
- The Admin Dashboard is protected with `@login_required`
- Unauthenticated users are redirected to the login page
- Only authenticated users can access administrative pages

## Frontend

Built with Bootstrap 5 for a responsive interface. Pages include:
- Home Page
- Admin Dashboard
- Login Page
- Student Registration
- Course Creation
- Instructor Creation
- Course Schedule Creation
- Schedule Day Creation
- Student Enrollment
- Course Details

### Admin Dashboard
A custom dashboard built without Django Admin, displaying statistics for Students, Courses, Instructors, Schedules, Schedule Days, and Enrollments, along with quick action buttons for every management page.

### Home Page
The receptionist-facing interface, displaying available courses (status, instructor, capacity, remaining seats, room, start/end dates) and allowing new students to be registered directly.

### JavaScript Features
The Schedule Day page allows dynamically adding multiple weekly sessions without leaving the page — each new block creates another `ScheduleDay` object on submit.

## Features

- ✅ Student Management
- ✅ Course Management
- ✅ Instructor Management
- ✅ Course Scheduling
- ✅ Multiple Weekly Sessions
- ✅ Student Enrollment
- ✅ Capacity Validation
- ✅ Automatic Schedule Status
- ✅ Login Authentication
- ✅ Responsive Bootstrap UI
- ✅ Dynamic Schedule Day Form

## Project Structure

```
Training Center Management System
├── Student Management
├── Course Management
├── Instructor Management
├── Course Scheduling
├── Schedule Days
├── Enrollment Management
├── Authentication
├── Admin Dashboard
└── Receptionist Interface
```

## Design Decisions

- **Course** is separated from **Instructor** because a course may be taught multiple times by different instructors.
- **CourseSchedule** acts as the link between Courses and Instructors.
- **ScheduleDay** is separated from **CourseSchedule** to support multiple weekly sessions.
- **Enrollment** is implemented as a separate model to represent the many-to-many relationship between Students and CourseSchedules.
- Business rules are implemented inside Django models rather than templates.
- ModelForms are used to simplify CRUD operations and leverage Django's built-in validation.
- Bootstrap provides a responsive, modern UI.
- JavaScript is used only where it improves UX without affecting backend logic.

## Future Improvements

- Student profiles
- Attendance tracking
- Certificate generation
- Search and filtering
- Edit/Delete pages
- Email notifications
- Dashboard charts
- PDF reports
- Instructor availability checking
- AJAX enrollment without page refresh
- Role-based permissions
- PostgreSQL deployment
- REST API for mobile applications
