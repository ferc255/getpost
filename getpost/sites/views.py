# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def main_view(request, id):
    if request.method == 'GET':
        if id:
            return JsonResponse({'type': 'GET', 'id': 'available',})
        else:
            return JsonResponse({'type': 'GET', 'id': 'absent'})
    elif request.method == 'POST' and not id:
        target_url = json.loads(request.body)['url']
        print(target_url)


        response = 'goodmorning'
        return JsonResponse({'type': 'POST', 'id': 'absent', 'response': response})
