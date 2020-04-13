from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Studentregister
from .models import Facultyregister
from django .views.generic import UpdateView
from django.views.generic import ListView

def register1(request):
    return render(request,"register.html")


def about1(request):
    return render(request,"about.html")

def courses1(request):
    return render(request,"courses.html")


def blog1(request):
    return render(request,"blog.html")


def contact1(request):
    return render(request,"contact.html")


def index1(request):
    return render(request,"index.html")


def categories1(request):
    return render(request,"course-single.html")


def blogsingle1(request):
    return render(request,"blog-single.html")


def login2(request):
    return render(request,"facultylogin.html")


def studenlogin(request):
    suname = request.POST.get("suname")
    spassw = request.POST.get("spassw")
    sd = Studentregister.objects.filter(email=suname, password=spassw)
    if sd:
        name = Studentregister.objects.get(email=suname)
        return render(request, "studenthome.html",{"student":name})
    else:
        return render(request,"login.html",{"msg":"You Are Not A Valid User Register First"})



def login1(request):
    return render(request,"login.html")


def facultylogin(request):
    funame = request.POST.get("funame")
    fpassw = request.POST.get("fpassw")
    facult = Facultyregister.objects.filter(email=funame, password=fpassw)
    if facult:
        name=Facultyregister.objects.get(email=funame)
        return render(request, "facultyhome.html",{"faculty":name})
    else:
        return render(request, "facultylogin.html",{"messg":"You Are Not A Valid User Register First"})


def studentregister(request):
    s_name=request.POST.get("sname")
    s_contact=request.POST.get("scnum")
    s_email=request.POST.get("semail")
    s_department=request.POST.get("sdepart")
    s_password=request.POST.get("spassword")

    student=Studentregister(name=s_name,contact=s_contact,email=s_email,department=s_department,password=s_password)
    student.save()

    return render(request,"login.html")


def studreg(request):
    return render(request,"register.html")


def facultyregister(request):
    f_name=request.POST.get("fname")
    f_contact=request.POST.get("fcontact")
    f_age=request.POST.get("fage")
    f_email=request.POST.get("femail")
    f_password=request.POST.get("fpassword")

    faculty=Facultyregister(name=f_name,contact=f_contact,age=f_age,email=f_email,password=f_password)
    faculty.save()

    return render(request,"facultylogin.html")


def faculreg(request):
    return render(request,"facultyregister.html")


def studprofile(request):
    type=request.GET.get("type")
    std=Studentregister.objects.get(email=type)
    return render(request,"studenthome.html",{"student":std,"viewprofile":std})


def facultprofile(request):
    type=request.GET.get("type")
    facult=Facultyregister.objects.get(name=type)
    return render(request,"facultyhome.html",{"faculty":facult,"viewprofile":facult})




def studenthome(request):
    type = request.GET.get("type")
    std = Studentregister.objects.get(name=type)
    return render(request, "studenthome.html",{"student":std})


def update(request):
    email = request.GET.get("email")
    res = Studentregister.objects.filter(email=email)
    type='result'
    return render(request, "studenthome.html", {"type": type, "res": res})


def admin1(request):
    return render(request,"index2.html")


def adminlogin1(request):
    username = request.POST.get("user")
    password = request.POST.get("pass")
    if username == "college" and password == "student@1234":
        return render(request,"adminhome.html")
    else:
        return render(request,"index2.html")#{"message":"Wrong Username And Password"})


def studupdate(request):
    name = request.POST.get("t1")
    cno = request.POST.get("t2")
    email = request.POST.get("t3")
    department = request.POST.get("t4")
    password = request.POST.get("t5")
    stud=Studentregister(name=name,contact=cno,email=email,department=department,password=password)
    stud.save()
    type="result"
    res = Studentregister.objects.filter(email=email)

    return render(request,"studenthome.html",{"msg":"updated","type":type,"res":res})


def facupdate(request):
    email = request.GET.get("email")
    res = Facultyregister.objects.filter(email=email)
    type = 'result'
    return render(request,"facultyhome.html",  {"type": type, "res": res})


def facultyupdate(request):
    name = request.POST.get("a1")
    cno = request.POST.get("a2")
    age = request.POST.get("a3")
    email = request.POST.get("a4")
    password = request.POST.get("a5")
    facult = Facultyregister(name=name, contact=cno, age=age, email=email, password=password)
    facult.save()
    type = "result"
    res = Facultyregister.objects.filter(email=email)

    return render(request, "facultyhome.html", {"masg": "Updated", "type": type, "res": res})


def adminhome(request):
    return render(request,"adminhome.html")


class AllStudent(ListView):
    context_object_name = "student"
    model = Studentregister
    template_name = "elen/student list.html"

class Adminstudupdate(UpdateView):
    model = Studentregister
    fields = {'name','contact','email','department','password'}
    template_name = "elen/student list.html"
    context_object_name = "studentupdate"
    success_url = reverse_lazy("satwant")

