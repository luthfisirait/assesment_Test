from django.shortcuts import render
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import jwt
import datetime
from .TheApi import register_user,register_userv1, get_access_token, refresh_access_token, get_user_profile
from .serializers import UserSerializer, ArticleSerializer

JWT_SECRET = 'mysecret'
JWT_ALGORITHM = 'HS256'
JWT_PREFIX = 'TSTMY'

cred = credentials.Certificate("firebase.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://testtechnical-5a735-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
# Create your views here.
@csrf_exempt
@api_view(['POST'])
def register(request):
    email = request.data.get('username')
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    profile_image = request.data.get("profile_image")
    telephone = request.data.get("telephone")
    address = "karya"
    city = "medan"
    province = "sumut"
    country = "indonesia"
    password = request.data.get('password')
    response = register_userv1(email, password,first_name,last_name,profile_image,address,city,province,country,telephone)
    return Response(response)
@csrf_exempt
def send_chat(request):
    sender = request.POST.get('sender')
    recipient = request.POST.get('recipient')
    message = request.POST.get('message')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    chat_ref = db.reference('chats')
    new_chat_ref = chat_ref.push()
    new_chat_ref.set({
        'sender': sender,
        'recipient': recipient,
        'message': message,
        'timestamp': timestamp
    })

    return JsonResponse({'status': 'success'})
@csrf_exempt
def read_chat(request):
    recipient = request.GET.get('recipient')
    chat_ref = db.reference('chats')
    chats = chat_ref.order_by_child('recipient').equal_to(recipient).get()
    
    chat_list = []
    for chat_id, chat_data in chats.items():
        chat_dict = {}
        chat_dict['sender'] = chat_data['sender']
        chat_dict['timestamp'] = chat_data['timestamp']
        chat_dict['message'] = chat_data['message']
        chat_list.append(chat_dict)
    
    sorted_chats = sorted(chat_list, key=lambda k: k['timestamp'])
    
    return JsonResponse(sorted_chats, safe=False)