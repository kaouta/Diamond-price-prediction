import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={
    
        
        "carat":"0.72",
         "cut":"5",
         "color":"6",
         "clarity":"7",
         "depth":"56.0",
         "table":"58.0",
         "x":"5.0",
         "y":"4.76",
         "z":"3.5"
})

print(r.json())