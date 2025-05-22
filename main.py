import requests

api_key = "om8VQc4xWjkMsGBdr69ALk8YGwVwX3T5NWSfzk9H"
url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-01-01&end_date=2024-01-07&api_key={api_key}"
print(url)
response = requests.get(url)
data = response.json()
print(data)
