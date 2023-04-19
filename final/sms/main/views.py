from django.shortcuts import render, redirect

from main.form import MarkForm
from .models import  Student, Teacher,Mark
from rest_framework.decorators import api_view
from rest_framework import status,generics
from rest_framework.response import Response
from.serializers import studentSerializer,StaffSerializer
from django.db.models import Avg




def home(request):
    return render(request, 'home.html')

def adminPanel(request):
    if 'admin_user' in request.session:
        all_students = Student.objects.all()
        all_teachers = Teacher.objects.all()
        data = {'students': all_students, 'teachers': all_teachers}
        return render(request, 'admin/admin_panel.html', data)
    else:
        return redirect('admin_login')


def adminLogin(request):
    if request.method == 'POST':
        admin_email = request.POST['email']
        admin_pwd = request.POST['pwd']

        if admin_email == "admin@gmail.com" and admin_pwd == "admin@123":
            request.session['admin_user'] = admin_email
            return redirect('admin_panel')
        else:
            return redirect('admin_login')

    return render(request, 'admin/admin_login.html')

def adminLogout(request):
    del request.session['admin_user']
    return redirect('admin_login')


def addStudent(request):
    if request.method == 'POST':
        School_de=request.POST['school']
        Clas=request.POST['Class']
        Section=request.POST['section']
        fullName = request.POST['full_name']
        fatherName = request.POST['f_name']
        gender = request.POST['gender']
        city = request.POST['city']
        stuEmail = request.POST['stu_email']
        contactNum = request.POST['contact_number']
        dob = request.POST['dob']
        studentId = request.POST['stu_id']
        studentUserName = request.POST['stu_user_name']
        studentPassword = request.POST['stu_pwd']

        add_student = Student.objects.create(school=School_de, Class=Clas,section=Section,full_name=fullName, father_name=fatherName, gender=gender, city=city,email=stuEmail, contact_num=contactNum, date_of_birth=dob, stu_id=studentId, user_name=studentUserName, password=studentPassword)

        add_student.save()
    return render(request, 'admin/new_student.html')

def manageStudent(request):
    all_students = Student.objects.all()
    data = {"students": all_students}
    return render(request, 'admin/manage_students.html', data)


def updateStudent(request, id):
    if request.method == 'POST':
        student_obj = Student.objects.get(id=id)
        School=request.POST['school']
        Clas=request.POST['Class']
        Section=request.POST['section']
        fullName = request.POST['full_name']
        fatherName = request.POST['f_name']
        gender = request.POST['gender']
        city = request.POST['city']
        stuEmail = request.POST['stu_email']
        contactNum = request.POST['contact_number']
        dob = request.POST['dob'] or student_obj.date_of_birth
        studentId = request.POST['stu_id']
        studentUserName = request.POST['stu_user_name']
        studentPassword = request.POST['stu_pwd']


        student_obj.school=School
        student_obj.Class=Clas
        student_obj.section=Section
        student_obj.full_name = fullName
        student_obj.father_name = fatherName
        student_obj.gender = gender
        student_obj.city = city
        student_obj.email = stuEmail
        student_obj.contact_num = contactNum
        student_obj.date_of_birth = dob
        student_obj.stu_id = studentId
        student_obj.user_name = studentUserName
        student_obj.password = studentPassword

        student_obj.save()
    return redirect('manage_students')

def deleteStudent(request, id):
    if 'admin_user' in request.session:
        stu_obj = Student.objects.get(id=id)
        stu_obj.delete()
    return redirect('manage_students')




def addTeacher(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        gender = request.POST['gender']
        email = request.POST['email']
        contact_num = request.POST['contact_number']
        qualification = request.POST['qualification']
        add_teacher = Teacher.objects.create(full_name=full_name, gender=gender, email=email,contact_num=contact_num, qualification=qualification)
        add_teacher.save()
    return render(request, 'admin/add_teacher.html')

def manageTeachers(request):
    all_teachers = Teacher.objects.all()
    data = {"teachers": all_teachers}
    return render(request, 'admin/manage_teachers.html', data)

def deleteTeacher(request, id):
    teacher_obj = Teacher.objects.get(id=id)
    teacher_obj.delete()
    return redirect('manage_teachers')

def studentLogin(request):
    if 'student_user' not in request.session:
        if request.method == "POST":
            user_name = request.POST['userName']
            student_pwd = request.POST['stuPwd']

            stu_exists = Student.objects.filter(user_name=user_name, password=student_pwd).exists()
            if stu_exists:
                request.session['student_user'] = user_name
                return redirect('student_dashboard')

        return render(request, 'student/student_login.html')
    else:
        return redirect('student_dashboard')



def studentDashboard(request):
    if 'student_user' in request.session:
        student_in_session = Student.objects.get(user_name=request.session['student_user'])
        data  = {"student": student_in_session}
       
        return render(request, 'student/student_dashboard.html', data,)
    else:
        return redirect('student_login')


def studentLogout(request):
    del request.session['student_user']
    return redirect('student_login')


def updateFaculty(request, id):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        contactNumber = request.POST['contact_number']
        gender = request.POST['gender']
        qualification = request.POST['qualification']
        teacher_obj = Teacher.objects.get(id=id)
        teacher_obj.full_name = full_name
        teacher_obj.email = email
        teacher_obj.contact_num = contactNumber
        teacher_obj.gender = gender
        teacher_obj.qualification = qualification
        teacher_obj.save()
    return redirect('manage_teachers')

def subject_ranking(request, subject):
    marks = Mark.objects.filter(subject=subject).order_by('mark')
    context = {'subject': subject, 'marks': marks}
    return render(request, 'subject_ranking.html', context)

def add_mark(request):
    if request.method == 'POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_ranking', subject=form.cleaned_data['subject'])
    else:
        form = MarkForm()
    context = {'form': form}
    return render(request, 'add_mark.html', context)

# API VIEW
@api_view(['GET','POST'])
def studentlist(request,format=None):
    if request.method=='GET':
        stu=Student.objects.all()
        serializer=studentSerializer(stu,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def stafflist(request,format=None):
    if request.method=='GET':
        staf=Teacher.objects.all()
        serializers=StaffSerializer(staf,many=True)
        return Response(serializers.data)
    if request.method=='POST':
        serializers=StaffSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def studentdetails(request,pk,format=None):
    try:
        stud=Student.objects.get(pk=pk)
    except stud.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=studentSerializer(stud)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=studentSerializer(Student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        
    elif request.method=='DELETE':
        Student.delete(stud)
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['GET','PUT','DELETE'])
def staffdetails(request,pk,format=None):
    try:
        staff=Teacher.objects.get(pk=pk)
    except staff.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializers=StaffSerializer(staff)
        return Response(serializers.data)

    elif request.method=='PUT':
        serializers=StaffSerializer(Teacher,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_404_NOT_FOUND)
        
    elif request.method=='DELETE':
        Teacher.delete(staff)
        return Response(status=status.HTTP_404_NOT_FOUND)
    



