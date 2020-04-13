import requests
import simplejson as json
import os

url = "https://api.rebrandly.com/v1/links"
headers = {"Content-Type": "application/json"}
api="09c2bbbd470249e3940e6b6546987a59"
shorted1 = input("Link Yang Ingin Di Short: http://www." )
payload = {"destination" : "http://"+shorted1,"apikey" : api}
r = requests.post(url,json=payload,headers=headers)
data = json.loads(r.text)
shorted = "https://rebrand.ly/"+data["slashtag"]
print("Linkmu Adalah : ", shorted)
shorted = "SHORTED LINK FOR "+ shorted1 + " IS >>>> "+ shorted +" <<<<< Thankyou \n"
if os.path.isfile('./link.txt'):
    print("File exist.")
    f = open("./link.txt","a+")
    f.write(shorted)
else:
    f = open("./link.txt","w+")
    f.write(shorted)