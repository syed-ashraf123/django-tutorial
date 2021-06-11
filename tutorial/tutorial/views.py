from django.shortcuts import HttpResponse,render,redirect
from tutorial.models import Contact
def home(request):
    # print(request)
    # return HttpResponse("You are on Home Page")
    return render(request,"home.html")
def about(request):
    # print(request)
    # return HttpResponse("You are on About Page")
    return render(request,"about.html")

def services(request):
    # print(request)
    # return HttpResponse("You are on Services Page")
    return render(request,"services.html")


def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,phone=phone,message=message)
        contact.save()
        return redirect('home')

    return render(request,"contact.html")