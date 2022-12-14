from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json
from rest_framework import status

class getCalories(APIView):
    def post(self,request):
        query = request.data.get('fooditem')
        nutriHEADERS = {
        'x-app-id':"8d307319",
        'x-app-key':"2f25f7b3fb74303a68307e8b986d562f",
        'x-remote-user-id':'0'
        }

        nutrientsurl = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
        query = {'query':query}
        nutrires = requests.post(nutrientsurl, headers=nutriHEADERS, json=query)
        nutrires.status_code
        nutrijson = nutrires.json()
        print(nutrijson)
        calories = nutrires['foods'][0]['nf_calories']
        return Response({'calories': calories},status=status.HTTP_200_OK)
