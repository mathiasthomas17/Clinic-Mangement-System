from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,'home.html')



# Doctor Login
def doctor_login(request):
    return render(request,'login.html')

# Doctor Pass Reset
def doctor_pass_reset(request):
    return render(request,'reset_password.html')