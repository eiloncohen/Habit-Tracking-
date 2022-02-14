import requests
from datetime import datetime
from decouple import config
import os


USERNAME = config('USER')
TOKEN = config('TOKEN')
graph_id = config('graph_id')


#  create user in pixela
# TODO 1 - create user in pixela
pixela_endpoint = "https://pixe.la/v1/users"
users_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)


# TODO 2 - create a pixela graph with API
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}
graph_params = {"id": graph_id,
                "name": "my-swimming-cycling-graph",
                "unit": "Km",
                "type": "float",
                "color": "sora"}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

post_to_graph_endpoint = f"{graph_endpoint}/{graph_id}"


# TODO 3 - Add value to the graph
def add_training_to_graph(distance):
    date_time = datetime.now().strftime("%Y%m%d")

    post_to_graph_params = {
        "date": date_time,
        "quantity": distance,

    }
    post_to_graph_res = requests.post(url=post_to_graph_endpoint, headers=headers, json=post_to_graph_params)
    print(post_to_graph_res.text)


# TODO 4 - delete value in the graph

def delete_training_from_graph(date):
    delete_pixel_from_graph_endpoint = f"{post_to_graph_endpoint}/{date}"
    delete_pixel_from_graph_res = requests.delete(url=delete_pixel_from_graph_endpoint, headers=headers)
    print(delete_pixel_from_graph_res.text)


def get_date():
    day = input("Please enter day (1-31): ")
    month = input("Please enter month (1-12): ")
    year = input("Please enter year: ")
    date = datetime(int(year), int(month), int(day))
    date_format = date.strftime("%Y%m%d")
    return date_format


def edit_traning_from_graph(distance, date):
    delete_pixel_from_graph_endpoint = f"{post_to_graph_endpoint}/{date}"
    body_params = {
        "quantity": distance
    }
    edit_pixel_from_graph_res = requests.put(url=delete_pixel_from_graph_endpoint, headers=headers, json=body_params)
    print(edit_pixel_from_graph_res.text)


mode = input("Welcome to Swim pixela tracking! please enter mode: \n 0 - add \n 1- edit \n 2 -delete\n")
if mode == "2":
    date = get_date()
    delete_training_from_graph(date)
elif mode == "1":
    date = get_date()
    distance = input("please enter the distance you swam that day: ")
    edit_traning_from_graph(distance, date)
else:
    distance = input("please enter the distance you swam today: ")
    add_training_to_graph(distance)
