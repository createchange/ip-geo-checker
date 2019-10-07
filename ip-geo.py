import requests
from pprint import pprint

ip = input("What is the IP?\n> ")

r = requests.get("http://ip-api.com/json/" + str(ip))
data = r.json()

print("\nOrganization: " + data["org"])
print("Location: " + data["city"] + ", " + data["regionName"] + ", " + data["country"])
print("ISP: " + data["isp"])

