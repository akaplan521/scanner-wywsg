#ok basically this is all null and void because X API free tier is terrible and
#next time i should check which endpoints are allowed on the free tier.



import requests
import os
import json


bearer_token = os.environ.get("X_BEARER_TOKEN")
USERNAME = "celtics"

def create_url(): #create url using id passed from get_id
    return "https://api.twitter.com/2/users/{}/following".format(get_id(USERNAME))

def get_id(user=USERNAME):   #get user id by username
    url = "https://api.twitter.com/2/users/by/username/{}".format(user)
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "User-Agent": "v2UserLookupPython"
    }

    response = requests.get(url, headers=headers)
    return response.json()["data"]["id"]

def get_params():
    return {"user.fields": "created_at"}


def bearer_oauth(r):

    #Method required by bearer token authentication.
    
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FollowingLookupPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def main():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()