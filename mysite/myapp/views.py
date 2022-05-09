from django.shortcuts import render
from .models import First
from pprint import pprint

# Create your views here.

def add(request):
    # pprint(request.POST.get('lastname'))
    if request.method == 'POST':
    #     # pprint('a')
    #     # firstname = request.POST.get('firstname','')
    #     # # pprint(firstname)
    #     # lastname = request.POST.get('lastname','')
    #     # in_no = request.POST.get('in_no','')

        # first = First()
        # first.firstname = request.POST.get('firstname')
        # first.lastname = request.POST.get('lastname')
        # first.in_no = 123
        # first.save()
        
        
        first = First(firstname=request.POST.get('firstname'),lastname=request.POST.get('lastname'),in_no=123)
        first.save()
    return render(request, 'myapp/add.html')
