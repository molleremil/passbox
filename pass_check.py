import requests
import hashlib


def request_api_data(query):
    url = "https://api.pwnedpasswords.com/range/" + query
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {response.status_code}, check the api and try again")
    return response


def get_leak_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    sha1password_firstfive, remainder = sha1password[:5], sha1password[5:]
    response = request_api_data(sha1password_firstfive)
    return get_leak_count(response, remainder)
