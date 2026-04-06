from django.shortcuts import render
from .models import ClientInfo

# Create your views here.
def home(request):
    client_data=ClientInfo.objects.all()
    context={
        'client_data':client_data,
    }
    return render(request,"index.html",context)

def add_client(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        status=request.POST.get('status')
        client=ClientInfo.objects.create(
            name=name,
            email=email,
            phone=phone,
            status=status,
        )
        client.save()
        return redirect('home')
    return render(request,'index.html')