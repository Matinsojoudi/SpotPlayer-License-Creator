from confings import *
import requests
import json

def create_license(test, course, name, offline, payload, data, watermark_texts):
    headers = {
        "Content-Type": "application/json",
        "$API": API_KEY,
        "$LEVEL": str(LEVEL)
    }

    request_data = {
        "test": test,
        "course": course,
        "name": name,
        "offline": offline,
        "payload": payload,
        "data": data,
        "watermark": {
            "texts": [{"text": text} for text in watermark_texts]  
        },
        "device": {
            "p0": 1,  # همه دستگاه‌ها
            "p1": 0,  # Windows غیرفعال
            "p2": 0,  # MacOS غیرفعال
            "p3": 0,  # Ubuntu غیرفعال
            "p4": 1,  # Android Active
            "p5": 0,  # iOS غیرفعال
            "p6": 0   # WebApp غیرفعال
        }
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(request_data))

    if response.status_code == 200:
        print("License created successfully!")
        print("Response:", response.json())
    else:
        print("Failed to create license")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

test_license = True  # لایسنس تستی
courses = ["6701f593595f23d5f6c30e7e"] 
name = "Matin"  
watermark_texts = ["09140000000"]  
offline = 30  
payload = "" 

data = {
    "confs": 0,
    "limit": {
        "6701f593595f23d5f6c30e7e": "0-" 
    }
}

create_license(test_license, courses, name, offline, payload, data, watermark_texts)
