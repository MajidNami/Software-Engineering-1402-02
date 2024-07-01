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
            chat_info_list = r.json()['chatInfoList']
            # Filter out the chat partner's information
            filtered_chat_info_list = []
            for item in chat_info_list:
                if item['firstUsername'] == username:
                    chat_partner = {
                        'username': item['secondUsername'],
                        'userId': item['secondUserId']
                    }
                else:
                    chat_partner = {
                        'username': item['firstUsername'],
                        'userId': item['firstUserId']
                    }
                filtered_chat_info_list.append(chat_partner)
            context = {'history_data': filtered_chat_info_list}
            return render(request, 'chat_history/Chathistory.html', context)
        return HttpResponse(f'ERROR {r.status_code}')
    else:
        return HttpResponse('Method not allowed', status=405)
