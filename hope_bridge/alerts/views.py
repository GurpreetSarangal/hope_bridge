# core/views.py
import logging
logger = logging.getLogger(__name__)

from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import json
import os
import csv
from django.shortcuts import render
from django.http import HttpResponse
from .models import User, NGO



def _add_cors_headers(response):
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, OPTIONS, GET"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    return response








@csrf_exempt
def add_user(request):
    if request.method == "OPTIONS":
        response = JsonResponse({"message": "OK"})
        return _add_cors_headers(response)

    if request.method == "POST":
        try:
            data = json.loads(request.body)

            # Accept both "fullName" and "full_Name"
            full_name = data.get("fullName") or data.get("full_Name")
            email = data.get("email")
            password = data.get("password")
            blood_group = data.get("blood_group")
            phone_number = data.get("phone_number")
            medical_condition = data.get("medical_condition", "")
            location = data.get("location")

            # Validate required fields
            if not all([full_name, email, password, blood_group, phone_number, location]):
                return _add_cors_headers(JsonResponse({"error": "Missing required fields"}, status=400))

            # Create user
            user = User.objects.create_user(
                email=email,
                full_name=full_name,
                password=password,
                blood_group=blood_group,
                phone_number=phone_number,
                medical_condition=medical_condition,eturn _add_cors_headers(response)

        except Exception as e:
            return _add_cors_headers(JsonResponse({"error": str(e)}, status=500))

    return _add_cors_headers(JsonResponse({"error": "Only POST allowed"}, status=405))




                location=location
            )

            response = JsonResponse({
                "message": "User added successfully",
                "user_id": user.id
            })
            r
# alerts/views.py
from django.http import JsonResponse
from .models import NGO   # make sure you have NGO model in models.py

def list_ngos(request):
    if request.method == "GET":
        ngos = list(NGO.objects.values())  # fetch all NGOs
        return JsonResponse({"ngos": ngos}, safe=False)

    return JsonResponse({"error": "Only GET allowed"}, status=405)

from django.http import JsonResponse
from django.db import connection

def debug_db(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")  # simple DB test
            row = cursor.fetchone()
        return JsonResponse({"db_status": "OK", "result": row[0]})
    except Exception as e:
        return JsonResponse({"db_status": "ERROR", "error": str(e)}, status=500)



def list_users(request):
    if request.method == "GET":
        users = list(User.objects.values())  # Use Django ORM instead of MongoDB
        response = JsonResponse({"users": users}, safe=False)
        return _add_cors_headers(response)
    return _add_cors_headers(JsonResponse({"error": "Only GET allowed"}, status=405))



    ngos = list(_db.ngos.find({}, {"_id": 0}))  # exclude _id for frontend
    response = JsonResponse(ngos, safe=False)
    return _add_cors_headers(response)





def pickle_load():
    import pickle
    with open('rf_hotspot.pkl', 'rb') as f:
        model = pickle.load(f)
    return model


def home(request):
    return HttpResponse("Hello Hackathon!")