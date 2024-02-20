from django.shortcuts import render
from students.models import register1

# Create your views here.
def stuform(request):
    if request.method=="POST":
        obj=register1()
        obj.name=request.POST.get("name")
        obj.age=request.POST.get("age")
        obj.std=request.POST.get("std")
        obj.division=request.POST.get("division")
        obj.save()
    return render(request,"student.html")

def stureg(request):
    obj=register1.objects.all()
    return render(request,"studentview.html",{"sdata":obj})
def stuupdate(request,pk):
    obj=register1.objects.get(id=pk)
    if request.method=="POST":
        obj=register1.objects.get(id=pk)
        obj.name=request.POST.get("name")
        obj.age=request.POST.get("age")
        obj.std=request.POST.get("std")
        obj.division=request.POST.get("division")
        obj.save()
    return render(request,"update.html",{'data':obj})
def delete(request,pk):
    obj=register1.objects.get(id=pk)
    obj.delete()
    return stureg(request)


