from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

# Create your views here.
def index(request):
    return Response({'index' : 'works'}, status=status.HTTP_200_OK)

#
# Whatsapp Chat Bot API class
# POST request API view.
#   
class WhatsappBot(APIView):
    """
        Captures user message and replies with a response.
    """
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        print(request.data['Body'])
        
        response = MessagingResponse()
        msg = response.message("Hello world!")
        
        return HttpResponse("Hello world") 