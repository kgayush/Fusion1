from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from applications.globals.models import (Designation, ExtraInfo,
                                         HoldsDesignation, DepartmentInfo)
from .models import AllotedHostelRoom


# Create your views here.

@login_required
def alloted_room(request):
    hall_1_boys_student = AllotedHostelRoom.objects.filter(id__hall_no="HALL-1-BOYS")
    hall_1_girls_student = AllotedHostelRoom.objects.filter(id__hall_no="HALL-1-GIRLS")
    hall_3_student = AllotedHostelRoom.objects.filter(id__hall_no="HALL-3")
    hall_4_student = AllotedHostelRoom.objects.filter(id__hall_no="Hall-4")
    context = {
        'hall_1_boys_student', hall_1_boys_student,
        'hall_1_girls_student', hall_1_girls_student,
        'hall_3_student', hall_3_student,
        'hall_4_student', hall_4_student
    }
    
    return render(request, 'hostelmanagement/hostel.html', context)