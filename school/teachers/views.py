from django.shortcuts import redirect, render
from teachers.models import register2

# Create your views here.
def teaform(request):
    if request.method=="POST":
        obj=register2()
        obj.name=request.POST.get("name")
        obj.age=request.POST.get("age")
        obj.subject=request.POST.get("subject")
        obj.save()
    return render(request,"teachers.html")

def teareg(request):
    obj=register2.objects.all()
    return render(request,"teachersview.html",{"data":obj})
def teaupdate(request,pk):
    obj=register2.objects.get(id=pk)
    if request.method=="POST":
        obj=register2.objects.get(id=pk)
        obj.name=request.POST.get("name")
        obj.age=request.POST.get("age")
        obj.subject=request.POST.get("subject")
        obj.save()
        return redirect("viewst")
    return render(request,"tupdate.html",{'data':obj})
def delete(request,pk):
    obj=register2.objects.get(id=pk)
    obj.delete()
    return teareg(request)


