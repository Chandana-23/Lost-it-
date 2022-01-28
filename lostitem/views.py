from django.shortcuts import redirect, render
from django.core.mail import send_mail
from lostitem.models import LostItem

# Create your views here.
def home(request):
    items = LostItem.objects.all()
    return render(request,"base.html",{'items':items})
def add(request):
    if request.method=='POST':
        name = request.POST['item_name']
        img = request.FILES['image']
        desc = request.POST['item_desc']
        place = request.POST['found']
        d = LostItem(item_name=name,item_img=img,item_desc=desc,place=place)
        d.save()
    return redirect("/")

def claim(request,pk):
    if request.method=='POST':
        pk = int(pk)
        d = LostItem.objects.get(pk=pk)
        d.claim = True
        d.save()
        subject = 'Lost it!'
        message = 'Kindly contact AEC for your lost item. Your Item id is '+str(pk)
        from_email = 'chandanasamineni23@gmail.com'
        recipient_list = ['chandanasamineni23@gmail.com']
        send_mail(subject,message,from_email,recipient_list)
    return redirect('/')

