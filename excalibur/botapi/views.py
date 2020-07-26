from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from .env import ACCOUNT_SID, AUTH_TOKEN
from .mainExcalibur import mainExcalibur
from datetime import datetime


greetings = [
    'hi', 'hello', 'hey', 'heya', 'good morning'
]
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
    
    def sendReply(self, message, to, from_):
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        msg = client.messages.create(
            body=message,
            # body=str(msg_str),
            # body = result,
            from_=from_,
            to=to
        )

        return msg

    def get(self, request, format=None):
        """
            GET method not allowed
        """
        return Response({'detail' : 'get method not allwoed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):
        """
            POST method for recieving the query
            return type: Http response
        """
        # print(request.data['Body'])
        
        # Reading user query
        description = request.data['Body']
        user_phone_number = request.data['From'].split(':')[1]

        # print(user_phone_number)

        response = MessagingResponse()
        msg = response.message("Hello world!")
        
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        # A basic logic for the reply to user
        if request.data['Body'].lower() in greetings and len(description) <= 10:
            message = client.messages.create(
                body='Hello there! Hope you are having a good day.\nPlease post your complain here or logon to https://www.ichangemycity.com/.',
                from_=request.data['To'],
                to=request.data['From']
            )

            return HttpResponse(str(msg))
        
        else:
            result = mainExcalibur(
                para=description,
                source="WH",
                phone_number=user_phone_number,
                timestamp=datetime.now()
            )
            print(result)
            msg_str = "Thank you for posting the complain. Your complaint id is {}. Your complaint id is For more details visit {}.".format(str(result["id"]), str(result["url"]))
            print(msg_str, type(msg_str))
            temp = "Hello! Hello1"
            print(type(temp))
            # message = client.messages.create(
            #     body="Thank you for posting your complain! We will get back to you shortly!",
            #     # body=str(msg_str),
            #     # body = result,
            #     from_=request.data['To'],
            #     to=request.data['From']
            # )
            # print(message)
            message = self.sendReply("Thank you for posting your complain! We will get back to you shortly!", request.data['From'], request.data['To'])
            # msg = response.message(str(msg_str))
            return HttpResponse(str(msg))


        # print(message)
        return HttpResponse(str(msg)) 


