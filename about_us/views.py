from django.shortcuts import render
from accounts.models import User

def about_us(request):
    query = User.objects.all()
    return render(request, 'about_us.html', {'users': query})
