from django.shortcuts import render
from .models import First
from pprint import pprint

# Create your views here.

def add(request):
    # pprint(request.method)
    if request.method == 'POST':
        if request.POST.get("firstname") and request.POST.get("lastname") and request.POST.get("in_no"):
        #     data = request.POST['lastname']
        #     print(data)
        #     first = First(lastname=data,)
        # first.save()
            firstData = First()
            firstData.firstname = request.POST.get("firstname",'')
            firstData.lastname = request.POST.get("lastname",'')
            firstData.in_no = request.POST.get('in_no')
            # pprint(firstData)
            firstData.save()
    #     # pprint('a')
    #     # firstname = request.POST.get('firstname','')
    #     # # pprint(firstname)
    #     # lastname = request.POST.get('lastname','')
    #     # in_no = request.POST.get('in_no','')

       
        
        return render(request, 'myapp/add.html')
        
    else:
        # first = First(firstname=firstname,lastname=lastname,in_no=123)
        # first.save()
        return render(request, 'myapp/add.html')

    
