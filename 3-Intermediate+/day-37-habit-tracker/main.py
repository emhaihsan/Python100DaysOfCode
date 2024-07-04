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

today = datetime.datetime.today()
today = today.strftime("%Y%m%d")

def create_graph(graph_id, graph_name, graph_unit, graph_type, graph_color):
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_config = {
        "id": graph_id,
        "name": graph_name,
        "unit": graph_unit,
        "type": graph_type,
        "color": graph_color
    }
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

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

def update_pixel(graph_id, date, quantity):
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{date}"
    update_pixel_config = {
        "quantity": str(quantity)
    }
    response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
    print(response.text)

def delete_pixel(graph_id, date):
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{date}"
    response = requests.delete(url=delete_pixel_endpoint, headers=headers)
    print(response.text)


create_graph("graph1", "Cycling", "Km", "float", "sora")
post_pixel("graph1", 5,5)
update_pixel("graph1", today, 10)
delete_pixel("graph1", today)
