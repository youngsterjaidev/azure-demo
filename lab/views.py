from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect

# adding the list
tempData = []

# Create your views here.
@csrf_exempt
def Register(request):
    if request.method == "POST":
        my_name = request.POST.get("name")
        my_email = request.POST.get("email")
        my_phone = request.POST.get("phone")
        
        print("The Data will be", my_name, my_email, my_phone)
        tempData.append({
            "name": my_name,
            "email": my_email,
            "phone": my_phone
        })

        return JsonResponse({ "message": "Data stored successfully !" }, safe=False)
    
    return JsonResponse({ "message": "All set !" }, safe=False)

@csrf_exempt
def index(request):
    return JsonResponse(tempData, safe=False)
