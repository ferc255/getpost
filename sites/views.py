# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
from sites.models import SiteRequest
import json
import urllib
import urllib.request


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
    soup = BeautifulSoup(html, 'html.parser')

    sitehost = urllib.parse.urlparse(url).hostname
    for link in soup.findAll('a'):
        href = link.get('href')
        host = urllib.parse.urlparse(href).hostname
        path = urllib.parse.urlparse(href).path
        
        if href and href != '#':
            if len(href) >= 4 and href[:4] == 'http' and host == sitehost:
                href = path
                
            if len(href) < 4 or href[:4] != 'http':
                result['internal'].append(href)
            else:
                result['external'].append(href)

    result['internal'] = list(set(result['internal']))
    result['external'] = list(set(result['external']))
    
    return result


@csrf_exempt
def main_view(request, id):
    if request.method == 'GET':
        if id:
            try:
                cur_item = SiteRequest.objects.get(id=id)
            except SiteRequest.DoesNotExist: 
                answer = {}
            else:
                answer = {
                    'url': cur_item.url,
                    'id': id,
                    'status': cur_item.status,
                    'internal_links': json.loads(cur_item.internal),
                    'external_links': json.loads(cur_item.external)
                }
        else:
            answer = {'sites': []}
            for site in SiteRequest.objects.all():
                item = {
                    'url': site.url,
                    'id': site.id,
                    'status': site.status
                }
                answer['sites'].append(item)
    elif request.method == 'POST':
        target_url = json.loads(request.body.decode())['url']
        attrs = scrape_site(target_url)
        
        new_req = SiteRequest.objects.create(
            url=target_url,
            status=attrs['status'],
            internal=json.dumps(attrs['internal']),
            external=json.dumps(attrs['external'])
        )
        new_req.save()

        answer = {'id': new_req.id}
        
    return JsonResponse(answer)
