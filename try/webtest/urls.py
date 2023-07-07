
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


urlpatterns = [

    
    path("login/",views.user_login,name="userLogin"),
    path("signup/",views.user_signup,name="userSignup"),
    path("logout/",views.logout_page,name="logout"),


    path("",views.home,name="home"),
    path('about/',views.about ,name="about"),
    path('aboutus/<slug:couserid>',views.naMe),
    path('contact/',views.contact, name="contact"),
    path('contact/<couserid>',views.passPara),
    path('form/',views.form,name= "form"),
    path('calculator',views.cal ,name="cal"),
    path('post/',views.formPost, name="post"),
    path('checkvalue/',views.evenodd,name = "evenodd"),
    path('output/',views.output,name="output"),
    path('testform/',views.testform,name="testform"),
    path('model/',views.modeltesting,name="model"),
    path('marksheet/',views.marksheet,name= "marksheet"),
    path('newsdata/<slug>',views.newupdate ,name='news'),
    path('details/',views.addDetails,name="details"),
    path('email_Verifications/',views.gmailVerify,name='gmailVerify'),
    path('Login/',views.otp_Verify,name='otpverify'),
    path('drop_select/',views.drop_select,name='checker'),
    path('mulitple_select/',views.select_multiple,name='select_multiple'),
    path('send_multiple/',views.send_multiple,name='send_multiple'),
    path('form_aj/',views.form_aj,name='form_aj'),
    path('form_save_aj/',views.form_save_aj,name='form_save_aj'),
    path('fetch_api/',views.fetch_api,name='fetch_api'),
    
    
    path('api/', views.api_home, name="api"),
    path('upload/', views.ImageCreateAPIView.as_view()),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)