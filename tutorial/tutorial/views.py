from django.shortcuts import HttpResponse,render,redirect
from tutorial.models import Contact

def index(request):
    # return HttpResponse("Hello")


    return render(request,"index.html")

    return render(request,"index.html")
def about(request):
    # return HttpResponse("You're on about page")
    if request.method== "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        return redirect("index")
    return render(request,"about.html")
def services(request):
    return HttpResponse("You're on Services Page")