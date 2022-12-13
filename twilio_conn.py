from twilio.rest import Client
import os
 
account_sid = os.environ.get('TWILIO_ACCOUNT_SID') 
auth_token = os.environ.get('TWILIO_ACCOUNT_TOKEN') 
phone_number = os.environ.get('PHONE') 

print(account_sid)
print(auth_token)
print(phone_number)

client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to=phone_number
                          ) 
 
print(message.sid)