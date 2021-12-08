from TwitterAPI import TwitterAPI
import os
import requests
import json

consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token_key = os.environ.get("ACCESS_TOKEN_KEY")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
bearer_token = os.environ.get("BEARER_TOKEN")


# Bearer token authentication
def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    return r


# Function 1
# Try to send a search request via Twitter API
def send_request(search_content):
    api = TwitterAPI(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token_key=access_token_key,
        access_token_secret=access_token_secret
    )
    response = api.request('search/tweets', search_content)
    return response.status_code


# Function 2
# The code below helps users to build rules 
# and apply the rules to get filtered stream

# Get rules
def get_rules():
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (status code {}): {}".format(response.status_code, response.text)
        )
    return response.json()


# Build rules
def build_rules():
    pass


# Add rules
def set_rules(rules):
    op = {"add": rules}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=op
    )
    if response.status_code != 201:
        raise Exception(
            "Cannot set rules (status code {}): {}".format(response.status_code, response.text)
        )
    return response.json()


# Delete rules
def delete_rules(rules):
    rule_ids = []
    for rule in rules['data']:
        rule_ids.append(rule['id'])
    op = {"delete": {"ids": rule_ids}}
    response = requests.post(
        "https://api.twitter.com/2/tweets/search/stream/rules",
        auth=bearer_oauth,
        json=op
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get rules (status code {}): {}".format(response.status_code, response.text)
        )
    return response.json()


def get_stream(set):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (status code {}): {}".format(response.status_code, response.text)
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            print(json.dumps(json_response, indent=4, sort_keys=True))


def main():
    # Show current rules
    current_rules = get_rules()
    print(current_rules)
    # Delete current rules
    delete_response = delete_rules(current_rules)
    print(delete_response)
    # Add some new rules
    rules = [
        {"value": "NBA has:images has:media"},
        {"value": "from:codinginflow has:links"},
        {"value": "meme has:images"}
    ]
    new_rules = set_rules(rules)
    print(new_rules)
    # Get stream
    get_stream(new_rules)


if __name__ == '__main__':
    main()
