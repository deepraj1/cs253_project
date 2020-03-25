from django.urls import path

from . import views

appname = "myapp"

urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('student/<int:student_id>', views.student, name='student')

]

