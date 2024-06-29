from django.shortcuts import render, HttpResponse, redirect
import requests

# Create your views here.

def homePage(request):
    params = request.GET
    return render(request, 'home/Homepage.html', dict(username=params['username']))


def startChat(request):
    if request.method == 'POST':
        username = request.POST['username']
        data = dict(username=username)
        r = requests.post('http://localhost:8080/chat/startChat', json=data)
        if r.status_code == 200:
            r = r.json()
            token = r['token']
            channelID = r['channelId']
            return redirect(f'http://localhost:3000/?channel_id={channelID}&user_token={token}&user={username}')
        return HttpResponse(f'ERROR {r.status_code}')

def getHistory(request):
    if request.method == 'POST':
        username = request.POST['username']
        data = dict(username=username)
        r = requests.post('http://localhost:8080/chat/chatHistory', json=data)
        if r.status_code == 200:
            a = r.json()['chatInfoList']
            res = '\n'.join([str(ele) for ele in a])
            return HttpResponse(res, content_type="text/plain")
        return HttpResponse(f'ERROR {r.status_code}')
