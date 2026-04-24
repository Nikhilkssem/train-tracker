from django.http import JsonResponse

def live_status(request):
    return JsonResponse({
        "status": "Running",
        "location": "Near Mysore",
        "delay": "10 mins"
    })
from django.shortcuts import render

def search_train(request):
    if request.method == "POST":
        train_no = request.POST.get("train_no")

        # Dummy data
        data = {
            "name": "Demo Train",
            "number": train_no,
            "status": "Running",
            "location": "Bangalore",
            "delay": "5 mins"
        }

        return render(request, "result.html", {"data": data})

    return render(request, "search.html")
import random
from django.http import JsonResponse

def live_status(request):
    lat = 12.97 + random.uniform(-0.05, 0.05)
    lng = 77.59 + random.uniform(-0.05, 0.05)

    return JsonResponse({
        "status": "Running",
        "location": "Near Bangalore",
        "delay": "5 mins",
        "lat": lat,
        "lng": lng
    })