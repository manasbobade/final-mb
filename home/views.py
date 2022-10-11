
from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
def index(request):
    context={"variable":"this is sent"}
    return render(request,'index.html',context)
    #return HttpResponse("this is home page")
def about(request):
    context={}
    return render(request,'about.html',context) 
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        problem=request.POST.get("problem")
        contact=Contact(name=name,phone=phone,email=email,problem=problem,date=datetime.today())
        contact.save()
    context={}
    return render(request,'contact.html',context)


