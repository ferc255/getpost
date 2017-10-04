# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import urllib
import urllib.request
from bs4 import BeautifulSoup


def scrape_site(url):
    result = {'internal': [], 'external': []}
    
    user_agent = 'Mozilla/5.0 (Windows)'
    request = urllib.request.Request(url, headers={'User-Agent': user_agent})
    try:
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as err:
        result['status'] = err.code
        return result
    except urllib.error.URLError as err:
        result['status'] = err.args[0].errno
        return result

    result['status'] = response.getcode()
    html = response.read()

    links = set()
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.findAll('a'):
        href = link.get('href')
        if href and href != '#':
            links.add(href)

    for link in links:
        if link[0] == '/':
            result['internal'].append(link)
        else:
            result['external'].append(link)

    return result


def b_pr(d):
    for key in d:
        print(key, ':', d[key])
        


@csrf_exempt
def main_view(request, id):
    answer = {}
    if request.method == 'GET':
        if id:
            answer = {'type': 'GET', 'id': 'available',}
        else:
            answer = {'type': 'GET', 'id': 'absent'}
    elif request.method == 'POST':
        target_url = json.loads(request.body.decode())['url']
        attrs = scrape_site(target_url)
        #b_pr(attrs)
        temp = json.dumps(attrs)
        tt = json.loads(temp)
        print(len(temp))
        answer = attrs
        
        
    return JsonResponse(answer)
