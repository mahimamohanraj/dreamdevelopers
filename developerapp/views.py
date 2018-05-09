from django.shortcuts import render,redirect
from django.http import HttpResponse

def index(request):
    return render(request,'developerapp/index.html')

def homepage(request):
    return render(request,'developerapp/homepage.html')

def loginpage(request):
        if request.method=='POST':
                user_name = request.POST.get('user_name')
                password = request.POST.get('password')	
                f =  open('files\\signup.txt','r+')
                users = f.readlines()
                for user in users:
                        details = user.split('|')
                        if details[0] == user_name :
                        		if details[4].strip() == password:
                        				return render(request,'developerapp/homepage.html')
                return HttpResponse("You are not authenticated")
        return render(request,'developerapp/loginpage.html')

def signuppage(request):
        if request.method=='POST':
                user_name = request.POST.get('user_name')
                address= request.POST.get('address')
                mobile_number = request.POST.get('mobile_number')
                email = request.POST.get('email')
                password = request.POST.get('password')
                confirm_password = request.POST.get('confirm_password')
                file = open('files\\signup.txt','a')
                file.write(user_name+'|'+address+'|'+mobile_number+'|'+email+'|'+password)
                file.write('\n')
                file.close()
                return redirect('loginpage')
        return render(request,'developerapp/signuppage.html')
