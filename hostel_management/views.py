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


    def add_hall_room(request):
    if request.method == "GET":
        files = request.FILES['hallroom']
        excel = pd.read_csv(files)
        roll_no = excel['ROLL NO.']
        hall_no = excel['Hall']
        room_no = excel['ROOM NO']
        for roll, hall, room in zip(roll_no,hall_no,room_no):
            student = Student.objects.get(id__id=roll)
            student.hall_no = hall
            student.room_no = room
            print("success GM==")
    return render(request, 'hostelmanagement/hall_upload.html')