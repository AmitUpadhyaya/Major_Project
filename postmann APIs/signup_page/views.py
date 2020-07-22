
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignupApiSerializer
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from api.models import UserAPI
from django.shortcuts import render
import requests

import json

# Create your views here.

def signup(request):
    return render(request, "Boot_app/signup.html")


def signupUser(request):
    email = request.GET['usrname']
    password = request.GET['psw']
    name = request.GET['name']
    print(email,password,name, "this is me")

    url = "http://127.0.0.1:8000/login1/"

    payload = {"email":email, "password":password, "name": name}
    payload= json.dumps(payload)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data= response.text
    return render(request, "Boot_app/temp.html", {'data':data})


class SignupApiView(APIView):
    def get(self, request):
        print(request.data.get('email'))
        queryset = UserAPI.objects.filter(email=request.data.get('email'))
        if queryset:
            if queryset.values('password').first()['password']== request.data.get('password'):
                return Response("you are succesfully logged in")
            else:
                return Response("Password is incorrect")
        else:
            return Response("User is not registered")

    def post(self, request):
        queryset=request.data
        serializers= SignupApiSerializer(data=queryset)
        if serializers.is_valid(raise_exception=True):
            save_data= serializers.save()

        # return Response("user saved")
        return Response({"Success":"User '{}' created successfully".format(save_data.name)})


    def put(self, request, pk):
        queryset=get_object_or_404(UserAPI.objects.all(),pk=pk)
        parsed_data= request.data
        serializers= SignupApiSerializer(instance=queryset, data= parsed_data, partial=True)
        if serializers.is_valid(raise_exception=True):
            save_data= serializers.save()

        # return Response("user saved")
        return Response({"Success":"User '{}' created successfully".format(save_data.name)})


    def delete(self, request, pk):
        queryset = get_object_or_404(UserAPI.objects.all(), pk=pk)
        queryset.delete()

        return Response({"Success": "User '{}' deleted successfully".format(pk)})

