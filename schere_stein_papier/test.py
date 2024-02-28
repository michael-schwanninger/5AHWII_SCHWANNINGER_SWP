import requests

query = {"Rock": 13, "Paper": 18, "Scissors": 20, "Lizard": 12, "Spock": 11}
res = requests.post("http://localhost:5000/upload_statistics", json=query)
print(res.json())