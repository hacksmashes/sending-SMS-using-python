import requests                                                                                                                                                                                                                                                        
import json

url = "https://www.fast2sms.com/dev/bulk"
my_data = { 'sender_id': 'FSTSMS',  
                 'message': "your child didn't attend the class today, so kindly meet & speak with his class teacher tomorrow",                  
                 'language': 'english', 
                 'route': 'p', 
                 'numbers': 9080964552} 

headers = { 'authorization': 'NZ6vWLcC790uoTAhatBkgMYFesmVribHS8qI52R3dEnx1fQjlX3TAJSerIM82opHkN90biVnqOUK16gE',   
                'Content-Type': "application/x-www-form-urlencoded", 
                'Cache-Control': "no-cache"}

response = requests.request("POST", url, data = my_data, headers = headers) 
returned_msg = json.loads(response.text) 
print(returned_msg['message'])
