from django.shortcuts import render
from django.http import HttpResponse
from contactme.models import contactmemodel
from contactme.models import projectsmodel
from contactme.models import reviewmodel

def mainhome(request):
    param={
        'title':"Spandy's Portfolio", 
        'projects':projectsmodel.objects.all(),
        'clients':reviewmodel.objects.all()
        }
    return render(request,'index1.html',param)