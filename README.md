# CFG-20 Team 4
## Problem Statement
Non Profit Organisation : Janaagraha

Janaagraha aims to transform the quality of life in India's cities and towns. To achieve the transformation, Janaagraha works with the citizens to catalyse active citizenship in city neighbourhoods and with the government to bring about transformative change to city governance (what it calls “City-Systems”).

Janaagraha currently hosts India's largest civic tech platform, “I Change My City” (www.ichangemycity.com) which enables citizens and governments to interact and produces data on quality of life issues which can enable efficient decision making.
In the current scenario, a user posts a complaint/request in three steps. 
1. Choose a category of complaint. 
2. Pick a picture with description of the issue. 
3. Choose location of the issue occurrence.

With the above information, the complaint is routed to the right officials. The aim is to simplify posting of issue for the citizens where they can a send a text or a social media post.
## Techstack
1. Django
2. HTML, CSS, JS, Bootstrap
3. Machine Learning, Natural Language Processing, Geotagging

## Keyfeatures 
1. WhatsappBot to register citizen complaint using Whatsapp
2. TelegramBot to register citizen complaint using Telegram
3. TwitterBot to register citizen complaint using Twitter
4. Categorizing of data with 93% accuracy
5. Location attraction from description
6. Location Tagging using the metadata from twitter
7. SMS to register citizen complaint
8. PhoneCall to register citizen complaint
9. Database to store real time data
10. Frontend to display all the user complaints. 

## Solution
We propose a diverse system that takes in citizen issues from various platforms and creates a centralised database. The different platfroms that we have aimed to cover in this project are :
1. Whatsapp
2. Twitter
3. Telegram
4. SMS & Phone call

Using the textual data, the three main categories : *'location'*, *'category'* and *'description'*.
### Workflow
1. The citizen posts/messages an issue.
2. The name of the citizen and the location of the issue is extracted from the post/message.
3. The post/message is then classified into one of the many pre-defined categories of issues.
4. The complain is lodged and an id named 'track_id' is generated for the same.
5. A reply is sent back to the user stating the track_id of the issue and the url which can be used to view the issue status.
## Dependecies
1. Twilio : We have used this platform for building the Whatsapp bot, SMS and phone call bots.
## How to successfully run the project
##### Django Project
Execute the following commands :
1. `pip install pipenv`
2. `pipenv shell`
3. `pip install requirements.txt`

Navigate to the 'excalibur' directory and execute the following command :

  `python manage.py runserver`

Great! You have the django server up and running now! 
## Major Files
1. Whatsapp Bot : The code for the bot can be viewed in the file **excalibur/botapi/views.py**. Also, Twilio is used for recieving and sending messages via Whatsapp. There is an env file which has the API details regarding Twilio (not available on this repo).
2. Telegram Bot
3. Twitter Bot
4. Extracting location and name from text : The code for this can be viewed at **excalibur/botapi/name_add_desc_separator.py**. Here regex and NLP is being used to extract the location and name of the person who has complained.
5. Text Classification : The code can be viewed at **excalibur/botapi/textClassification.py**. NLP is used to extract meaning of words, sentences in the message/post. A matrix of vectors is then classified using LogisticClassification.
6. Integration : The integration of the bots with the model and backend can be viewed in **excalibur/botapi/mainExcalibur.py**.
