from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from applications.globals.models import (Designation, ExtraInfo,
                                         HoldsDesignation, DepartmentInfo)
from applications.academic_information.models import *

# Create your views here.

@login_required
def view_alloted_room(request):
    hall_1_student = Student.objects.filter(hall_no=1)
    hall_3_student = Student.objects.filter(hall_no=3)
    hall_4_student = Student.objects.filter(hall_no=4)[:10]                        

    context = {
        'hall_1_student': hall_1_student,
        'hall_3_student': hall_3_student,
        'hall_4_student': hall_4_student
    }

    return render(request, 'hostelmanagement/hostel.html', context)