import requests                                                                                                                                                                                                                                                        
import json

url = "https://www.fast2sms.com/dev/bulk"
my_data = { 'sender_id': 'FSTSMS',  
                 'message': "***************",    # type the message here  
                 'language': 'english', 
                 'route': 'p', 
                 'numbers': **********} # type the number to whom u want to send sms

headers = { 'authorization': '*********************************************************',  # type the authorization key    
                'Content-Type': "application/x-www-form-urlencoded", 
                'Cache-Control': "no-cache"}

response = requests.request("POST", url, data = my_data, headers = headers) 
returned_msg = json.loads(response.text) 
print(returned_msg['message'])
