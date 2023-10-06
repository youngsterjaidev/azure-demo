from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def Register(request):
    if request.method == "POST":
        my_name = request.POST.get("name")
        my_email = request.POST.get("email")
        my_phone = request.POST.get("phone")
        
        print("The Data will be", my_name, my_email, my_phone)
    
    return JsonResponse({ "message": "All set !" }, safe=False)
