# core/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from mongo import db

@csrf_exempt
def add_ngo(request):
    if request.method == "POST":
        data = json.loads(request.body)
        ngo = {
            "name": data.get("name"),
            "email": data.get("email"),
            "address": data.get("address"),
            "contact": data.get("contact"),
            "site_link": data.get("site_link"),
        }
        result = db.ngos.insert_one(ngo)
        return JsonResponse({"message": "NGO added", "id": str(result.inserted_id)})
    return JsonResponse({"error": "Only POST allowed"}, status=405)


def list_ngos(request):
    ngos = list(db.ngos.find({}, {"_id": 0}))  # exclude _id for frontend
    return JsonResponse(ngos, safe=False)
