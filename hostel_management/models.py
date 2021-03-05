import datetime
from django.db import models
from applications.globals.models import ExtraInfo, Staff
from applications.academic_information.models import Student

HOSTELS = (
    ('Hall-1', 'Hall-1'),
    ('Hall-3', 'Hall-3'),
    ('Hall-4', 'Hall-4')
)

class Hostel(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, choices=HOSTELS)

    def __str__(self):
        return self.name

class HostelStaff(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self):
        return self.staff_id.id.user.username + "-" + self.hostel.name

class HostelStudent(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id.id.id + self.student_id.id.user.username + self.hostel.name
    