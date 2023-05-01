from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .function import get_response
import json
import os
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def request_fun(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        request_value = get_response(json_data["myData"])
        contents = {json_data["myData"]: request_value}
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                contents = json.load(f)
                print(contents)
                if contents:
                    contents[json_data["myData"]] = request_value
                    print(contents)
        with open("data.json", "w") as f:
            json.dump(contents, f)
        return JsonResponse({'data': request_value})

@csrf_exempt
def load_fun(request):
    if request.method == "POST":
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                data = json.load(f)
            print(data)
            return JsonResponse({"data": data})
        return JsonResponse({"data": False})


@csrf_exempt
def delete_fun(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                data = json.load(f)
            if json_data["myData"] in data:
                del data[json_data["myData"]]
                if os.path.exists("data.json"):
                    with open("data.json", "w") as f:
                        json.dump(data, f)
            if json_data["myData"] in data.values():
                key = list(data.keys())[list(data.values()).index(json_data["myData"])]
                del data[key]
                if os.path.exists("data.json"):
                    with open("data.json", "w") as f:
                        json.dump(data, f)
            if not data:
                os.remove("data.json")
            return JsonResponse({"data": True})
        return JsonResponse({"data": False})