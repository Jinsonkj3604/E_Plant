from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


def usersign(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['passwd']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"The Credenials Are Worngggg")
            return redirect('sign')
        
    else:
        return render(request,'signin.html')




def register(request):
    print("the  functioonnn")
    if request.method == 'POST':
        print("tge method is possstts")
        firstname = request.POST['firstname']
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['psw']
        confirm = request.POST['psw-repeat']

        if password == confirm:
            print("condition satisfiedddd")
            if User.objects.filter(username=username).exists():
                print("user anmejjjjs alesysys")
                messages.info(request,"UserName Already Taken")
                return redirect('register')
            elif User.objects.filter(email = email).exists():
                print("emillssjsjsjsj")
                messages.info(request,"EMAIL iS allready in use")
                return redirect('register')
            else:
                print("sucesssssssss")
                user = User.objects.create_user(username=username,first_name=firstname,password=password,email=email)
                user.save()
                return redirect('/')
        else:
            print("Errorrrrrr password")
            messages.info(request,"Password is incorrect !!")
            return redirect('register')
    else:
        print("redirectionnnnnn")
        return render(request,'register.html')

def signout(request):
    auth.logout(request)
    return redirect('sign')
