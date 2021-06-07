from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import mobi
import random
import http.client
from django.conf import settings
# Create your views here.
def send_otp(mobile , otp):
    conn = http.client.HTTPSConnection("api.msg91.com")
    authkey = settings.AUTH_KEY
    sendid = "smsind"
    headers = {'content-type': "application/json"}
    url = "http://control.msg91.com/api/sendotp.php?otp="+otp+"&sender="+sendid+"&message="+"otpis"+otp+"&mobile="+mobile+"&authkey="+authkey+"&country=91"
    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    return None

def log(request):
    return render(request, 'log.html')

def ver(request):
    if request.method =="POST":
        name = request.POST["name"]
        mobile = request.POST["mobile"]
        otp = str(random.randint(1000, 9999))

        user1 =User(username=name)
        user1.save()
        mobi1 = mobi(user=user1, mobile=mobile, otp=otp)
        mobi1.save()
        send_otp(mobile, otp)
        request.session['mobile']= mobile
        request.session['otp'] = otp
        return redirect('otp')

def otp(request):
    otp = request.session['otp']
    mobile = request.session['mobile']
    if request.method == 'POST':
        otpu = request.POST.get('otp')
        if otp == otpu :
            return render(request,"sucess.html",{"mobi": mobile})
        else:
            return render(request, "otp.html", {"mess": "Otp is wrong", "mobi": mobile})


    else:
         return render(request, "otp.html", {"mobi": mobile})

