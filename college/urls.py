"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from CLG.views import AllStudent
from CLG.views import Adminstudupdate
from CLG import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="index.html")),
    path('register1/',views.register1),
    path('about1/',views.about1),
    path('courses1/',views.courses1),
    path('blog1/',views.blog1),
    path('index1/', views.index1),
    path('contact1/',views.contact1),
    path('categories1/',views.categories1),
    path('blogsingle1/',views.blogsingle1),
    path('login2/',views.login2),
    path('studentlogin/',views.studenlogin),
    path('login1/',views.login1),
    path('facultylogin/',views.facultylogin),
    path('studentregister/',views.studentregister),
    path('studreg/',views.studreg),
    path('facultyregister/',views.facultyregister),
    path('faculreg/',views.faculreg),
    path('studprofile/',views.studprofile),
    path('facultprofile/',views.facultprofile),
    path('studenthome/',views.studenthome),
    path('update/',views.update),
    path('admin1/',views.admin1),
    path('adminlogin1/',views.adminlogin1),
    path('studupdate/',views.studupdate),
    path('facupdate/',views.facupdate),
    path('facultyupdate/',views.facultyupdate),
    path('adminhome/',views.adminhome),
    path('studentview/',AllStudent.as_view()),
    path('studentupdate/' , Adminstudupdate.as_view() , name = 'satwant' ),
    path('studupdate/<str:pk>',Adminstudupdate.as_view()),
]

