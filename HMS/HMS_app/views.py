from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
from HMS_app.models import Table
#from Menuapp.models import RMenu
# Create your views here.
def index(request):
    content={
        'var':'i am a variable'
    }
    return render(request,'index.html',content)
def login(request):
    return render(request,'index.html')
def auth(request):
    if request.method== "POST":
        nm=request.POST.get('username')
        pwd=request.POST.get('password')
        if nm=="aaa" and pwd=="123":
            mymembers = Table.objects.all().values()
            template = loader.get_template('emp.html')
            context = {
            'mymembers': mymembers,
            }
            return HttpResponse(template.render(context, request))
def add(request):
    return render(request,'add.html')
    #return HttpResponse("Hello add:>")
def addrecord(request):
    nm=request.POST['name']
    age=request.POST['age']
    add=request.POST['address']
    mnum=request.POST['mobile_number']
    desg=request.POST['designation']
    sal=request.POST['salary']
    leave=request.POST['leaves']
    m=Table(name=nm,age=age,address=add,mobile_number=mnum,designation=desg,salary=sal,leaves=leave)
    m.save()
    return HttpResponse("Added")

def update(request,id):
    mymember = Table.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
    'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request,id):
    nm=request.POST['name']
    age=request.POST['age']
    add=request.POST['address']
    mnum=request.POST['mobile_number']
    desg=request.POST['designation']
    sal=request.POST['salary']
    leave=request.POST['leaves']
    member = Table.objects.get(id=id)
    member.name = nm
    member.age = age
    member.address = add
    member.mobile_number = mnum
    member.designation = desg
    member.salary = sal
    member.leaves = leave
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request,id):
    member =Table.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))