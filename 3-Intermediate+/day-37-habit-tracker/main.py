import requests
import os
import datetime


USERNAME = "ihsan666"
TOKEN = os.environ.get("PIXELA_TOKEN")
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": "ihsan666",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }

# headers = {
#     "X-USER-TOKEN": TOKEN
# }

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

def post_pixel(graph_id, quantity: float, data = None):
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    today = datetime.datetime.today()
    today = today.strftime("%Y%m%d")
    post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
    post_pixel_config = {
        "date": today,
        "quantity": str(quantity),
        "optional_data": data
    }
    response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
    print(response.text)

post_pixel("graph1", 5,5)
