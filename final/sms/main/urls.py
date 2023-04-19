from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin_panel/dashboard', views.adminPanel, name="admin_panel"),
    path('admin_panel/login/', views.adminLogin, name="admin_login"),
    path('admin_panel/logout/', views.adminLogout, name="admin_logout"),
    path('student/login/', views.studentLogin, name="student_login"),
    path('admin_panel/add_student/', views.addStudent, name="add_student"),
    path('admin_panel/manage_students/', views.manageStudent, name="manage_students"),
    path('admin_panel/update_student/<str:id>/', views.updateStudent, name="update_student"),
    path('admin_panel/delete_student/<str:id>/', views.deleteStudent, name="delete_student"),
    path('admin_panel/add_teacher/', views.addTeacher, name="add_teacher"),
    path('admin_panel/manage_teacher/', views.manageTeachers, name="manage_teachers"),
    path('admin_panel/delete_teacher/<str:id>/', views.deleteTeacher, name="delete_teacher"),
    path('student/dashboard/', views.studentDashboard, name="student_dashboard"),
    path('student/logout/', views.studentLogout, name="student_logout"),
    path('student/update_teacher/<str:id>/', views.updateFaculty, name="update_teacher"),
    path('ranking/<str:subject>/', views.subject_ranking, name='subject_ranking'),
    path('addmark', views.add_mark, name='add_mark'),
]