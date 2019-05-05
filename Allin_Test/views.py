from django.shortcuts import render ,redirect
from django.core.files.storage import FileSystemStorage
from .forms import SolutionForm
from .models import Questions,Solution
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('guidelines')
    else:
        form = UserRegisterForm()
    return render(request, 'Allin_Test/register.html', {'form': form})


def send(request):
    res= Solution.objects.all()
    for i in res:
        if i.result =='A':
            subj ='Accepted'
            mess ='You are selected. Congrats'
            recip = i.email

        elif i.result=='R':

            subj = 'Rejected'
            mess = 'You are rejected.Sorry try again next time'
            recip = i.email

        send_mail(subject=subj,message=mess,from_email='jainhardik256@gmail.com',recipient_list =[recip],fail_silently=False,)



    return render(request,'Allin_Test/send.html',{'title':'Sending Mail'})





def homepage(request):
    return render(request,'Allin_Test/homepage.html',{'title':'Homepage'})




def guidelines(request):
    return render(request,'Allin_Test/guidelines.html',{'title':'Test Guidelines'})




def coding(request):
    if request.method=='POST':
        form = SolutionForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('result')
    else:
        form =SolutionForm()
        value = Questions.objects.all()
    return render(request,'Allin_Test/coding.html',{'value':value,'title':'Coding Block','form':form})

def result(request):
    return render(request,'Allin_Test/result.html')
