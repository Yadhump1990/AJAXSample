from django.urls import path

from ajapp import views

urlpatterns=[
    path('',views.main,name='main'),
    path('log',views.log,name='log'),
    ############## admin #########################
    path('AdminHome',views.AdminHome,name='AdminHome'),
    path('manage_dep',views.manage_dep,name='manage_dep'),
    path('add_dep',views.add_dep,name='add_dep'),
    path('addDep',views.addDep,name='addDep'),
    path('edit_dep/<int:id>',views.edit_dep,name='edit_dep'),
    path('delDep/<int:id>',views.delDep,name='delDep'),
    path('updateDep',views.updateDep,name='updateDep'),
    path('manageCourse',views.manageCourse,name='manageCourse'),
    path('add_course',views.add_course,name='add_course'),
    path('addCourse',views.addCourse,name='addCourse'),
    path('editCourse/<int:id>',views.editCourse,name='editCourse'),
    path('delCourse/<int:id>',views.delCourse,name='delCourse'),
    path('updateCourse',views.updateCourse,name='updateCourse'),
    path('manageSubject',views.manageSubject,name='manageSubject'),
    path('addSubject',views.addSubject,name='addSubject'),
    path('add_subject',views.add_subject,name='add_subject'),
    path('updateSubject',views.updateSubject,name='updateSubject'),
    path('editSubject/<int:id>',views.editSubject,name='editSubject'),
    path('delSub/<int:id>',views.delSub,name='delSub'),
    path('manageStudent',views.manageStudent,name='manageStudent'),
    path('addStudent',views.addStudent,name='addStudent'),
    path('searchCrs',views.searchCrs,name='searchCrs'),
    path('updateStudent',views.updateStudent,name='updateStudent'),
    path('add_student',views.add_student,name='add_student'),
    path('studExist',views.studExist,name='studExist'),
    path('editStudent/<int:id>',views.editStudent,name='editStudent'),
    path('delStudent/<int:id>',views.delStudent,name='delStudent'),
    path('searchstud',views.searchstud,name='searchstud'),
    path('serch_student',views.serch_student,name='serch_student'),
    path('viewAttendance',views.viewAttendance,name='viewAttendance'),
    path('markAttendance/<int:id>',views.markAttendance,name='markAttendance'),
    path('absent/<int:id>',views.absent,name='absent'),
    path('attendancePercentage',views.attendancePercentage,name='attendancePercentage'),
    ########### student ##########################
    path('studentHome', views.studentHome, name='studentHome'),
    path('studentDash', views.studentDash, name='studentDash'),
    path('searchDep', views.searchDep, name='searchDep'),
    path('viewSubjects/<int:id>', views.viewSubjects, name='viewSubjects'),

]