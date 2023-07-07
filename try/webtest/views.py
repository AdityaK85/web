from cmath import log
from email import message
from unicodedata import name
from xml.dom.domreg import registered
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from webtest.admin import login_password
from webtest.forms import *
from webtest.models import *
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
import math, random
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .serializer import *
from rest_framework.generics import (CreateAPIView)
import json
import traceback
# login user modules
from django.contrib.auth.models import User
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from Utilities.HandleFunctions import getData

# --------------------------------------- Advanced Ajax Function-----------------------------------
@csrf_exempt
@login_required(login_url='/login')
def  form_aj(request):
    return render(request, 'form_aj.html')

@csrf_exempt
def form_save_aj(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    profile_img = request.FILES.get('profile_img')

    print('...........proifel ', profile_img)

    advancedAjax.objects.create(username = username, password = password, email = email, profile_img = profile_img)
    return JsonResponse({'status':'1'})

# --------------------------------------FETCH DATA THORUGH API----------------------------------------------

def fetch_api(request):
    resp = requests.get('https://randomuser.me/api/?results=5000').json()
    context = { 'response' : resp }
    return render(request, 'fetch_api.html', context)

# --------------------------------------LOGIN---------------------------------------------------------------
# User Auth Login

@csrf_exempt
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            return redirect('/signup')
        
        user_obj = authenticate(username=username, password=password)
        print('..............user', user_obj)
        request.session['user_id'] = str(user_obj.id)
        if user_obj:
            print('..............user obj', user_obj)
            login(request, user_obj)
            return redirect('/')

    return render(request, 'login.html')

# --------------------------------------SIGN UP---------------------------------------------------------------

@csrf_exempt
def user_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            return redirect('/signup')
       
        user_obj = User(username=username, email=email , password=password)
        user_obj.set_password(password)
        user_obj.save()
        print("account created")
        print(f'{username}, email : {email}, password : {password}')
        return redirect('/login')

    return render(request, 'signup.html')

def logout_page(request):
    logout(request)
    return redirect('/login')

# --------------------------------------REST API---------------------------------------------------------------

# Rest API
@csrf_exempt
@api_view(['POST'])
def api_home(request):
    obj = testmod.objects.all()
    serializer = studentSerializer(obj, many=True)
    return Response({'status':200, 'payload': serializer.data})

# upload image through API

class ImageCreateAPIView(CreateAPIView):
	serializer_class = imageSerializer
	# queryset = login.objects.all()

# ---------------------------------------PASS DATA------------------------------------------------------------------

@login_required(login_url='/login')
def home(request):

    
    data = {
        
        'data':'welcome to TestWebsite',
        
        'how' : 'hello how are you',
        
        'table': ['aditya','ashok','kothekar'] ,
        
        'stu':[
            {
                'Name':'aditya','course':'BCCA'
            },
            {
                'Name':'vedant','course':'BBA'
            },
            {
                'Name':'adarsh','course':'b.com'
            },
            {
                'Name':'Jayshu','course':'BBA'
            }
        ]
        
    }
    
    new = news.objects.all()
    data = {
        'new':new
    }
    
    return render(request, 'index.html',data)

# -----------------------------------------FETCH DATA -----------------------------------------------------------------

# @login_required(login_url='/login')
def modeltesting(request):
    if request.session.get('user_id'):
    
        sendData = testmod.objects.all()
        paginator = Paginator(sendData,2)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)
        total_page = page_obj.paginator.num_pages
        
        
        data = {
            'sendData':page_obj,
                }
        
        if request.method == "POST":
            sd = request.POST.get('sdata')
            if sd != None:
                sendData = testmod.objects.filter(name__icontains=sd)
                data = {
                    'sendData':sendData,
                    'total_page':[n+1 for n in range(total_page)]
                } 
                
       
    return render(request,'model.html',data)

# -------------------------------------USE PARAMETER---------------------------------------------------------
def naMe(request, couserid):
    return HttpResponse(couserid)

# ---------------------------------------RENDER HTML PAGE----------------------------------------------------

@login_required(login_url='/login')
def contact(request):
    return render(request, 'contact.html')

# ------------------------------------------------------------------------------------------------------------

def passPara(request, couserid):
    return HttpResponse(couserid)

# -------------------------------------------GET METHOD-------------------------------------------------------

@login_required(login_url='/login')
def about(request):
#   using GET method
    if request.method == "GET":
        data = request.GET.get('total')
    return render(request,'about.html',{'data': data})

# ------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
def form(request):
    total = 0
    try:
        if request.method == "GET":
            n1 = request.GET.get('num1')
            n2 = request.GET.get('num2')
            total = n1+n2
    except : 
        pass
    return render(request, 'form.html',{'total': total})

# --------------------------------------------POST METHOD-----------------------------------------------------------

@login_required(login_url='/login')
def formPost(request):
    total = 0
    
    try:
        if request.method == "POST":
            n1 = request.POST['num1']
            n2 = request.POST['num2']
            totalData = {
                'total': n1 + n2               
                }
            url = "/about/?total={}".format(total)
            return HttpResponseRedirect(url)
        # This url data will be send to about page 
    except :
        pass
    
    return render(request,'post.html',{'total': total})

# ------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
def output(request):
    total = 0
    try:
        if request.method == "POST":
            n1 = request.POST['num1']
            n2 = request.POST['num2']
            total = n1 + n2 
    except :
        pass
    return HttpResponse(f"Total is : {total}")

# ------------------------------------------PASS MODEL -----------------------------------------------------------

@login_required(login_url='/login')
def testform(request):
    data = inputform()
    fn = {'data': data}
    
    return render(request,'form.html',{'update': fn})


# ------------------------------------------USE TRY CATCH-------------------------------------------------------------

def getData (**kwargs):
    kwargsData = requests.POST.get( f'{kwargs}'  )
    print('get Data', kwargsData)
    return kwargsData

@login_required(login_url='/login')
def cal(request):
    num1 = ''
    num2 = ''  
    c = ''
    clear = ''
    try:
        if request.method == "POST":
            # num1 = eval(request.POST.get('num1'))
            # num2 = eval(request.POST.get('num2'))
            use_func = getData(num1, num2)
            print('user funct.......................',use_func)
            opr = request.POST.get('opt')
            
            if opr == "+":
                c = num1+num2
            elif opr == "-":
                c = num1-num2
            elif opr == "*":
                c = num1*num2
            elif opr == "/":
                c = num1/num2
            else:
                return "Invalid Input"
    except Exception as e:
        print (e)
    return render(request, 'cal.html',{'c':c,'n1':num1,'n2':num2})

# -------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
def evenodd(request):
    n1 = ''
    c = ''
    
    if request.method ==  "POST":
        if request.POST.get('num') == "":
            return render(request, 'oddeven.html',{'error': True})
        
        
        n1 = eval(request.POST.get('num'))
        
        if n1 % 2 ==  0:
            c = "Even Number"
        else:
            c = "Odd Number"
            
    return render(request, 'oddeven.html',{'c': c,'n1':n1})

# --------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
def marksheet(request):
    vb = ''
    tally = ''
    cost = ''
    sad = ''
    total = 600
    percentage = 0
    
    try:
        if request.method  == "POST":
            vb = eval(request.POST.get('vb'))
            tally = eval(request.POST.get('tally'))
            cost = eval(request.POST.get('cost'))
            sad = eval(request.POST.get('sad'))
            
            subtotal = vb + tally + cost + sad
            percentage = subtotal/total * 100
            
    except:
        pass
    return render(request, 'marksheet.html',{'vb':vb,'tally': tally,'cost': cost,'sad': sad,'perc': percentage})

# -------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
def newupdate(request,slug):
    data = news.objects.get(new_slug=slug)
    new_data = {
                'id': data
            }
    if request.method == "POST": 
        news_search =  request.POST.get('sdata')
        if news_search != None:
            new_data = {
                'id': data
            }
            
    return render(request,'newsdata.html',new_data)

# -------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
def addDetails(request):
    
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        course = request.POST.get('course')
        year = request.POST.get('year')
        
        send = testmod(name = name, subject = subject, course = course, year = year)
        send.save()
    return render(request, 'details.html')

# -------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
def gmailVerify(request):
    if request.method == "POST":
        subject = request.POST.get('subject','')
        message = request.POST.get('message','')
        to_email = request.POST.get('to_email','')
        if subject and message and to_email:
            try:
                send_mail(subject, message,'vedantkothekar85@gmail.com',[to_email])
            except BadHeaderError:
                return HttpResponse('<h1>Invalid Mail</h1>')
            return HttpResponseRedirect('/email_Verifications/')
        else:
            return HttpResponse('<h2>Make sure all fields are entered and valid</h2>')
    return render(request,'gmail_Send.html')

# -------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
def otp_Verify(request):
    global registered
    global ul
    registered = True
    if (request.method == "POST"):
        login_form = login_password(request.POST, request.FILES)
        if login_form.is_valid():
            user = login_form.save()
            username = request.POST.get('username')
            ul = username
            email    = request.POST.get('email')
            password = request.POST.get('password')
            user.save()
            user = authenticate(request ,username = username,password = password)
            
            if user is None:
                user = get_user_model().objects.create_user(username=username, password=password, email=email)
                user.save()
        
        else:
            print('user_form.error')
        return redirect('/otp.html/')
    else:
        login = login_password()
        return render(request, 'otp.html',{'sign':login,'registered':registered})

# -------------------------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
@csrf_exempt
def drop_select(request):
    context ={}
 
    # create object of form
    form = selections(request.POST or None, request.FILES or None)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
 
    context['form']= form
    return render(request, "checker.html", context)

# -------------------------------------------------------------------------------------------------------------------

def select_multiple(request):
    obj = select_muliple.objects.all()
    for i in obj:
        print(i.option)
        # print('...................',obj])
    return render(request, 'select_multiple.html')

@csrf_exempt
def send_multiple(request):
    if request.POST:
        select = request.POST.getlist('select')
        print('...............option', select)
        select_muliple.objects.create(option = select)
        return HttpResponse(select)