from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,"index.html")
def deals(request):
    return render(request,"deals.html")
def about(request):
    return render(request,"about.html")
'''def reservation(request):
    
    finalans=0
   
    try:
       n1=request.GET['Name']
       num=request.GET['Number']
       guests=request.GET['Guests']
       date=request.GET['date']
       place=request.GET['Destination']
       print(n1+' '+num+' '+guests+' '+date+' '+place )

       finalans=n1+' '+num+' '+guests+' '+date+' '+place      
    except:
        pass

    return render(request,"reservation.html",{'output':finalans})'''

def reservation(request):
    
    finalans=0
    data={}
   
    try:
        if request.method=="POST":
         n1=request.POST['Name']
        ''' num=request.POST['Number']
       guests=request.POST['Guests']
       date=request.POST['date']
       place=request.POST['Destination']'''
        finalans=n1
        data={
            'n1':n1,
            'output':finalans
        }
       
    except:
        pass

    return render(request,"reservation.html",data)

def signup(request):



















































































































    
    return render(request,"signup.html")
