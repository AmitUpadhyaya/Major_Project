# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserApiSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
import requests

import json

# Create your views here.

def index(request):
    return HttpResponse("Hello world")
def index1(request):
    return render(request, "login/FIRST_webpage.html")
def index2(request):
    return render(request, "Boot_app/home.html")
def index3(request):
    return render(request, "Boot_app/Assignment_page2.html")
def index4(request):
    return render(request, "Boot_app/aassignment3.html")



def submitUser(request):
    email = request.GET['email']
    password = request.GET['password']
    name = request.GET['name']
    print(email,password,name, "this is me")

    url = "http://127.0.0.1:8000/api/login/"

    payload = {"email":email, "password":password, "name": name}
    payload= json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)
    data= response.is_redirect
    print(data)
    return render(request, "Boot_app/temp.html", {'data': data})


    # if data=="correct":
    # return render(request, "Boot_app/Assignment_page2.html")
    # else:
    #     return render(request, "Boot_app/temp.html", {'data': data})





# Create your views here.
from .models import UserAPI

class UserApiView(APIView):
    def get(self, request):
        print(request.data.get('email'))
        queryset = UserAPI.objects.filter(email=request.data.get('email'))
        if queryset:
            if queryset.values('password').first()['password']== request.data.get('password'):
                return Response("Successfully logged in")
                # return render(request, "Boot_app/Assignment_page2.html")

            else:
                return Response("Password is incorrect")
        else:
            return Response("User is not registered")

    def post(self, request):
        queryset=request.data
        serializers= UserApiSerializer(data=queryset)
        if serializers.is_valid(raise_exception=True):
            save_data= serializers.save()

        # return Response("user saved")
        return Response({"Success":"User '{}' created successfully".format(save_data.name)})


    def put(self, request, pk):
        queryset=get_object_or_404(UserAPI.objects.all(),pk=pk)
        parsed_data= request.data
        serializers= UserApiSerializer(instance=queryset, data= parsed_data, partial=True)
        if serializers.is_valid(raise_exception=True):
            save_data= serializers.save()

        # return Response("user saved")
        return Response({"Success":"User '{}' created successfully".format(save_data.name)})


    def delete(self, request, pk):
        queryset = get_object_or_404(UserAPI.objects.all(), pk=pk)
        queryset.delete()

        return Response({"Success": "User '{}' deleted successfully".format(pk)})

