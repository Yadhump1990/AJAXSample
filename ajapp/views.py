from datetime import datetime
from pprint import pprint

from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render, redirect

# Create your views here.
from ajapp.models import *


def main(request):
    return render(request, 'loginIndex.html')

def log(request):
    username = request.POST['uname']
    password = request.POST['password']
    try:
        logOb = login.objects.get(username=username, password=password)
        if logOb.type == 'admin':
            return HttpResponse('''<script>alert("welcome admin");window.location='/AdminHome'</script>''')
        elif logOb.type == 'student':
            return HttpResponse('''<script>alert("welcome student");window.location='/studentHome'</script>''')
        else:
            return HttpResponse('''<script>alert("invalid username or password ");window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert("invalid username or password ");window.location='/'</script>''')


######### ADMIN ################
def AdminHome(request):
    return render(request,'ADMININDEX.html')

def manage_dep(request):
    ob = department.objects.all()
    return render(request,'admin/manage_department.html',{'val':ob})

def add_dep(request):
    return render(request,'admin/ADD_DEPARTMENT.html')

def addDep(request):
    depName = request.POST['textfield']
    desc = request.POST['textarea']
    ob = department()
    ob.name = depName
    ob.description = desc
    ob.save()
    return HttpResponse('''<script>alert("department added ");window.location='manage_dep'</script>''')


def edit_dep(request,id):
    request.session['did'] = id
    ob = department.objects.get(id=id)
    return render(request,'admin/EDIT_DEPARTMENT.html',{'val':ob})

def updateDep(request):
    depName = request.POST['textfield']
    desc = request.POST['textarea']
    ob = department.objects.get(id=request.session['did'])
    ob.name = depName
    ob.description = desc
    ob.save()
    return HttpResponse('''<script>alert("department update ");window.location='/manage_dep'</script>''')

def delDep(request,id):
    ob = department.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("department deleted ");window.location='/manage_dep'</script>''')


def manageCourse(request):
    ob = course.objects.all()
    return render(request,'admin/MANAGE_COURSE.html',{'val':ob})

def addCourse(request):
    dob = department.objects.all
    return render(request,'admin/ADD_COURSE.html',{'val':dob})

def add_course(request):
    cname = request.POST['textfield']
    dep = request.POST['select']
    desc = request.POST['textarea']
    ob = course()
    ob.name = cname
    ob.depId = department.objects.get(id=dep)
    ob.description = desc
    ob.save()
    return HttpResponse('''<script>alert("course added ");window.location='/manageCourse'</script>''')



def editCourse(request,id):
    request.session['cid'] = id
    ob = course.objects.get(id=id)
    dob= department.objects.all()
    return render(request,'admin/EDIT_COURSE.html',{'val':ob,'val2':dob})

def updateCourse(request):
    try:
        cname = request.POST['textfield']
        desc = request.POST['textarea']
        dep = request.POST['select']
        ob = course.objects.get(id=request.session['cid'])
        ob.name = cname
        ob.depId = department.objects.get(id=dep)
        ob.description = desc
        ob.save()
        return HttpResponse('''<script>alert("course updated ");window.location='/manageCourse'</script>''')
    except:
        cname = request.POST['textfield']
        desc = request.POST['textarea']
        # dep = request.POST['select']
        ob = course.objects.get(id=request.session['cid'])
        ob.name = cname
        # ob.depId = department.objects.get(id=dep)
        ob.description = desc
        ob.save()
        return HttpResponse('''<script>alert("course updated ");window.location='/manageCourse'</script>''')

def delCourse(request,id):
    ob = course.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("course deleted ");window.location='/manageCourse'</script>''')


def manageSubject(request):
    ob = subject.objects.all()
    return render(request,'admin/MANAGE_SUBJECT.html',{'val':ob})

def addSubject(request):
    dob = department.objects.all()
    cob= course.objects.all()
    return render(request,'admin/ADD_SUBJECT.html',{'val':dob,'val2':cob})

def add_subject(request):
    dep = request.POST['select2']
    crs = request.POST['select']
    subname = request.POST['textfield']
    desc = request.POST['textarea']
    ob = subject()
    ob.depId = department.objects.get(id=dep)
    ob.cid = course.objects.get(id=crs)
    ob.name = subname
    ob.description = desc
    ob.save()
    return HttpResponse('''<script>alert("subject added ");window.location='/manageSubject'</script>''')


def editSubject(request,id):
    sob = subject.objects.get(id=id)
    dob = department.objects.all()
    cob = course.objects.all()
    request.session['sid'] = id
    return render(request,'admin/EDIT_SUBJECT.html',{'val':sob,'val2':dob,'val3':cob})

def updateSubject(request):
    dep = request.POST['select']
    crs = request.POST['select2']
    sname = request.POST['textfield']
    desc = request.POST['textarea']
    ob = subject.objects.get(id=request.session['sid'])
    ob.name = sname
    ob.depId = department.objects.get(id=dep)
    ob.cid = course.objects.get(id=crs)
    ob.description = desc
    ob.save()
    return HttpResponse('''<script>alert("subject updated ");window.location='/manageSubject'</script>''')


def delSub(request,id):
    ob = subject.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("subject deleted ");window.location='/manageSubject'</script>''')


def manageStudent(request):
    ob = student.objects.all()
    return render(request,'admin/manageStudent.html',{'val':ob})

def addStudent(request):
    dob = department.objects.all()
    cob = course.objects.all()
    return render(request,'admin/ADD_STUDENTS.html',{'val':dob,'val2':cob})

def searchCrs(request):
    dep = request.GET['dep']
    cob = course.objects.filter(depId=dep)
    data = []
    for i in cob:
        row = {"id" : i.id, "course":i.name}
        data.append(row)
    res = {"res" : data}
    pprint(res)
    return JsonResponse(res)


def add_student(request):
    dep = request.POST['select']
    crs = request.POST['select2']
    sname = request.POST['textfield']
    age = request.POST['number']
    uname = request.POST['uname']
    password = request.POST['password']
    lob = login()
    lob.username = uname
    lob.password = password
    lob.type = 'student'
    lob.save()
    ob = student()
    ob.name = sname
    ob.depId = department.objects.get(id=dep)
    ob.cid = course.objects.get(id=crs)
    ob.age = age
    ob.lid = lob
    ob.save()
    return HttpResponse('''<script>alert("student added ");window.location='/manageStudent'</script>''')

def studExist(request):
    username = request.GET['uname']
    data = {
        'is_taken': student.objects.filter(lid__username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = "a user with username already exists"

    return JsonResponse(data)


def editStudent(request,id):
    sob = student.objects.get(id=id)
    dob = department.objects.all()
    cob = course.objects.all()
    request.session['std'] = id
    return render(request,'admin/EDIT_STUDENT.html',{'val':sob,'val2':dob,'val3':cob})

def updateStudent(request):
    dep = request.POST['select']
    crs = request.POST['select2']
    sname = request.POST['textfield']
    age = request.POST['number']
    ob = student.objects.get(id=request.session['std'])
    ob.name = sname
    ob.depId = department.objects.get(id=dep)
    ob.cid = course.objects.get(id=crs)
    ob.age = age
    ob.save()
    return HttpResponse('''<script>alert("student updated ");window.location='/manageStudent'</script>''')

def delStudent(request,id):
    ob = student.objects.get(lid__id=id)
    ob.delete()
    ob = login.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("student deleted ");window.location='/manageStudent'</script>''')

def searchstud(request):
    ob = course.objects.all()
    return render(request,'admin/searchStud.html',{'val':ob})

def serch_student(request):
    cob = request.POST['select']
    sob = student.objects.filter(cid=cob)
    ob = course.objects.all()
    return render(request, 'admin/searchStud.html', {'val': ob,'val2':sob,'s':cob})


# def viewAttendance(request):
#     if request.method == 'POST':
#         selected_date = request.POST.get('date')
#         try:
#             date_obj = datetime.strptime(selected_date, '%Y-%m-%d').date()
#         except ValueError:
#             return render(request, 'admin/STUDENT_ATTENDENCE.html', {'error': 'Invalid date format'})
#
#         students = student.objects.all()
#         return render(request, 'admin/STUDENT_ATTENDENCE.html', {'students': students, 'selected_date': selected_date})
#
#     return render(request, 'admin/STUDENT_ATTENDENCE.html', {'selected_date': None})



# def viewAttendance(request):
#     if request.method == 'POST':
#         selected_date = request.POST.get('date')
#         try:
#             date_obj = datetime.strptime(selected_date, '%Y-%m-%d').date()
#         except ValueError:
#             return render(request, 'admin/STUDENT_ATTENDENCE.html', {'error': 'Invalid date format'})
#
#         students = student.objects.all()
#         attendance_dict = {}  # Dictionary to store attendance values
#
#         # Retrieve attendance values for selected date
#         for student_obj in students:
#             try:
#                 attendance = studentAttendence.objects.get(sid=student_obj, date=date_obj)
#                 attendance_dict[student_obj.id] = attendance.attendence
#             except studentAttendence.DoesNotExist:
#                 attendance_dict[student_obj.id] = None
#
#         return render(request, 'admin/STUDENT_ATTENDENCE.html', {'students': students, 'selected_date': date_obj, 'attendance_dict': attendance_dict})
#
#     return render(request, 'admin/STUDENT_ATTENDENCE.html')
#

# def markAttendance(request, id):
#     if request.method == 'POST':
#         selected_date = request.POST.get('date')
#         try:
#             date_obj = datetime.strptime(selected_date, '%Y-%m-%d').date()
#         except ValueError:
#             return render(request, 'admin/STUDENT_ATTENDENCE.html', {'error': 'Invalid date format'})
#
#         studentz = student.objects.get(id=id)
#         attendance, created = studentAttendence.objects.get_or_create(sid=studentz, date=date_obj)
#         attendance.attendence = 1  # Correct the field name to "attendence" instead of "attendance"
#         attendance.save()
#
#         return redirect('viewAttendance')
#
#     return redirect('viewAttendance')
def viewAttendance(request):
    if request.method == 'POST':
        selected_date = request.POST.get('date')
        try:
            date_obj = datetime.strptime(selected_date, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'admin/STUDENT_ATTENDENCE.html', {'error': 'Invalid date format'})

        students = student.objects.all()
        student_attendance_dict = {}
        for student_obj in students:
            attendance = studentAttendence.objects.filter(sid=student_obj, date=date_obj).first()
            student_attendance_dict[student_obj.id] = attendance
        return render(request, 'admin/STUDENT_ATTENDENCE.html', {'students': students, 'selected_date': selected_date, 'student_attendance_dict': student_attendance_dict})

    return render(request, 'admin/STUDENT_ATTENDENCE.html', {'selected_date': None})

# def markAttendance(request, id):
#     if request.method == 'POST':
#         selected_date = request.POST.get('date')
#         try:
#             date_obj = datetime.strptime(selected_date, '%Y-%m-%d').date()
#             pprint(date_obj)
#         except ValueError:
#             return render(request, 'admin/STUDENT_ATTENDENCE.html', {'error': 'Invalid date format'})
#
#         studentz = student.objects.get(id=id)
#         attendance, created = studentAttendence.objects.get_or_create(sid=studentz, date=date_obj)
#
#         # Check the value of the "attendance" field in the POST data
#         attendance_value = request.POST.get('attendance')
#         if attendance_value == '1':
#             attendance.attendence = 1
#         elif attendance_value == '0':
#             attendance.attendence = 0
#         else:
#             return render(request, 'admin/STUDENT_ATTENDENCE.html', {'error': 'Invalid attendance value'})
#
#         attendance.save()
#
#         return redirect('viewAttendance')
#
#     return redirect('viewAttendance')
def markAttendance(request, id):
    if request.method == 'POST':
        selected_date = request.POST.get('date')
        try:
            date_obj = datetime.strptime(selected_date, '%Y-%m-%d').date()
            pprint(date_obj)
        except ValueError:
            return render(request, 'admin/STUDENT_ATTENDENCE.html', {'error': 'Invalid date format'})

        studentz = student.objects.get(id=id)
        attendance, created = studentAttendence.objects.get_or_create(sid=studentz, date=date_obj)
        attendance.attendence = 1  # Correct the field name to "attendence" instead of "attendance"

        # # Check the value of the "attendance" field in the POST data
        # attendance_value = request.POST.get('attendance')
        # if attendance_value == '1':
        #     attendance.attendence = 1
        # elif attendance_value == '0':
        #     attendance.attendence = 0
        # else:
        #     return render(request, 'admin/STUDENT_ATTENDENCE.html', {'error': 'Invalid attendance value'})

        attendance.save()

        return redirect('viewAttendance')

    return redirect('viewAttendance')

def absent(request, id):
    if request.method == 'POST':
        selected_date = request.POST.get('date')
        try:
            date_obj = datetime.strptime(selected_date, '%Y-%m-%d').date()
            pprint(date_obj)
        except ValueError:
            return render(request, 'admin/STUDENT_ATTENDENCE.html', {'error': 'Invalid date format'})

        studentz = student.objects.get(id=id)
        attendance, created = studentAttendence.objects.get_or_create(sid=studentz, date=date_obj)
        attendance.attendence = 0  # Correct the field name to "attendence" instead of "attendance"
        attendance.save()

        return redirect('viewAttendance')

    return redirect('viewAttendance')


def attendancePercentage(request):
    students = student.objects.all()
    attendance_percentages = {}

    for student_obj in students:
        total_attendance = studentAttendence.objects.filter(sid=student_obj).count()
        present_attendance = studentAttendence.objects.filter(sid=student_obj, attendence=1).count()

        if total_attendance == 0:
            attendance_percentage = 0
        else:
            attendance_percentage = (present_attendance / total_attendance) * 100

        attendance_percentages[student_obj.id] = attendance_percentage

    return render(request, 'admin/attendance_percentage.html', {'students': students, 'attendance_percentages': attendance_percentages})



#################### student ##########################

def studentDash(request):
    return render(request,'STUDENTINDEX.html')

def studentHome(request):
    dob = department.objects.all()
    return render(request,'student/studentHome.html',{'val':dob})

def searchDep(request):
    depOb = request.POST['select']
    cob = course.objects.filter(depId=depOb)
    dob = department.objects.all()
    return render(request,'student/studentHome.html',{'val2':cob,'val':dob,'s':depOb})


def viewSubjects(request,id):
    sob = subject.objects.filter(cid=id)
    return render(request,'student/subjects.html',{'val':sob})