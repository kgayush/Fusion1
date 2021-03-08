import datetime
from django.db import models
from applications.globals.models import ExtraInfo, Staff
from applications.academic_information.models import Student
from applications.office_module.models_office_students import (hostel_allotment, hostel_capacity, Constants)

ROOM_NO = (
    ('A101', 'A101'),
    ('A102', 'A102'),
    ('A103', 'A103'),
    ('A104', 'A104'),
    ('B101', 'B101'),
    ('B102', 'B102'),
    ('B103', 'B103'),
    ('B104', 'B104'),
    ('C101', 'C101'),
    ('C102', 'C102'),
    ('C103', 'C103'),
    ('C104', 'C104'),
    ('D101', 'D101'),
    ('D102', 'D102'),
    ('D103', 'D103'),
    ('D104', 'D104'),

    ('A201', 'A201'),
    ('A202', 'A202'),
    ('A203', 'A203'),
    ('A204', 'A204'),
    ('B201', 'B201'),
    ('B202', 'B202'),
    ('B203', 'B203'),
    ('B204', 'B204'),
    ('C201', 'C201'),
    ('C202', 'C202'),
    ('C203', 'C203'),
    ('C204', 'C204'),
    ('D201', 'D201'),
    ('D202', 'D202'),
    ('D203', 'D203'),
    ('D204', 'D204'),

    ('A301', 'A301'),
    ('A302', 'A302'),
    ('A303', 'A303'),
    ('A304', 'A304'),
    ('B301', 'B301'),
    ('B302', 'B302'),
    ('B303', 'B303'),
    ('B304', 'B304'),
    ('C301', 'C301'),
    ('C302', 'C302'),
    ('C303', 'C303'),
    ('C304', 'C304'),
    ('D301', 'D301'),
    ('D302', 'D302'),
    ('D303', 'D303'),
    ('D304', 'D304'),

    ('A401', 'A401'),
    ('A402', 'A402'),
    ('A403', 'A403'),
    ('A404', 'A404'),
    ('B401', 'B401'),
    ('B402', 'B402'),
    ('B403', 'B403'),
    ('B404', 'B404'),
    ('C401', 'C401'),
    ('C402', 'C402'),
    ('C403', 'C403'),
    ('C404', 'C404'),
    ('D401', 'D401'),
    ('D402', 'D402'),
    ('D403', 'D403'),
    ('D404', 'D404'),
)


class Hostel(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, choices=Constants.HALL_NO)

    def __str__(self):
        return self.name


class HostelStaff(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)                   # onetoonefield is more appropriate here
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self):
        return self.staff_id.id.user.username + "-" + self.hostel.name


# room no of a student can be shown on the profile
class HostelStudent(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)               # onetoonefield is more appropriate here
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_id.id.id + self.student_id.id.user.username + self.hostel.name
    

class HostelRoom(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_no = models.CharField(max_length=15, unique=True, blank=False, choices=ROOM_NO, default='')

    def __str__(self):
        return self.hostel.name + self.room_no
    

class AllotedHostelRoom(models.Model):                                              # didn't need to create this table, but roomno and studentid not mentioned in the main table
    id = models.ForeignKey(hostel_allotment, on_delete=models.CASCADE)
    hostel_room = models.ForeignKey(HostelRoom, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)