from django.shortcuts import render

from .models import Student

# Create your views here.

def student_home(request):
    
    students_data = Student.objects.all()

    print(students_data)

    data={
        "students_data": students_data 
    }
    return render(request,"student/student_home.html",data)

def add_student(request):

    if request.method == "POST" :
        #yaha hoga database me student save
        student_name = request.POST.get("input_name")
        student_email = request.POST.get("input_email")
        student_phone_number = request.POST.get("input_phone_number")

        Student.objects.create(
            name = student_name,
            email = student_email,
            phone_number = student_phone_number
        )

    return render(request, "student/add_student.html")