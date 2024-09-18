import requests

url = "http://127.0.0.1:5000/books"
data = {
    "author": "New Author",
    "language": "French",
    "title": "New Book"
}

# Send POST request
response = requests.post(url, json=data)

# Check status code and handle possible errors
if response.status_code == 200 or response.status_code == 201:
    try:
        print(response.json())  # Try to print the JSON response
    except requests.exceptions.JSONDecodeError:
        print("Response is not in JSON format")
else:
    print(f"Request failed with status code: {response.status_code}")

