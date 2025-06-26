import requests
response = requests.get("http://peoplepulse.diu.edu.bd:8189/result?grecaptcha=&semesterId=251&studentId=0242310005341263")
print(response.status_code)
print(response.json())