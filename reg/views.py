from django.core.mail import send_mail
from django.shortcuts import render,redirect
from .models import *
from .forms import RegForm
import random




def index(request):
    img = Image.objects.all()
    return render(request,'index.html',{'img':img})

def gallery(request):
    return render(request,'gallery.html',)

def blog(request):
    return render(request,'blog.html',)

def about(request):
    return render(request,'about.html',)

def contact(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        data = {"name":name,"email":email,"subject":subject,"message":message}
        message = '''
        New message:{}
                                
        From:{}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message,'',['ggpoovarasan321@gmail.com'])
    return render(request,'contact.html',)




def home(request):
    img = Image.objects.all()
    return render(request,'home.html',{'img':img})

def regs(request):
    form = RegForm()
    if request.method=='POST':
        form = RegForm(request.POST,files=request.FILES)
        form.save()
        return redirect('/')
    else:
        form = RegForm()
    return render(request,'register.html',{'form':form} )
        
def code(request):
#     upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     lower = 'abcdefghijklmnopqrstuvwxyz'
#     symbols = '!@#$%^&*?'
    numbers = '0123456789'
    string = numbers
    length = 8
    code = ''.join(random.sample(string,length))
    return render(request,'detail.html',{'code':code})
