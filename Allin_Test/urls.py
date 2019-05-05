from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('',views.homepage,name='homepage'),
path('login/', auth_views.LoginView.as_view(template_name='Allin_Test/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(template_name='Allin_Test/logout.html'), name='logout'),
path('register/',views.register,name='register'),
path('register/guidelines/',views.guidelines,name='guidelines'),
path('register/guidelines/coding/',views.coding,name='coding'),
path('register/guidelines/coding/result',views.result,name='result'),
path('send/',views.send,name='send'),
]



if settings.DEBUG :
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)