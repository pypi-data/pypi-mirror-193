import requests
import json
from pprint import pprint

EI_API_URL = "https://studio.edgeimpulse.com/v1/api/"
EI_API_LOGIN_URL = "https://studio.edgeimpulse.com/v1/api-login"


def get_headers(org_key):
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "x-api-key": org_key
    }


def get_jwt_headers(jwt_token, portal_token=""):
    if portal_token == "":
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-jwt-token": jwt_token
        }
    else:
        return {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "x-jwt-token": jwt_token,
            "x-token": portal_token
        }


def get_org_url(org_id):
    return EI_API_URL + "organizations/" + str(org_id)


def check_response(res, type="json", debug=False):
    payload = json.loads(res.text)
    if debug:
        print("check_response: ", end="")
        pprint(payload)
    if res.ok:
        if payload["success"]:
            return payload
    raise RuntimeError("Invalid response %s" % payload)


def do_org_get(org_id, org_key, endpoint, debug=False):
    url = (get_org_url(org_id) + endpoint)
    if debug:
        print("do_org_get: %s" % url)
    res = requests.get(url, headers=get_headers(org_key))
    return check_response(res, debug=debug)


def do_jwt_get(token, endpoint, portal_token="", debug=False):
    url = EI_API_URL + endpoint
    if debug:
        print("do_jwt_get: %s" % url)
    res = requests.get(url, headers=get_jwt_headers(token, portal_token))
    return check_response(res, debug=debug)


def do_jwt_post(token, endpoint, payload, portal_token="", debug=False):
    url = EI_API_URL + endpoint
    if debug:
        print("do_jwt_post: %s" % url)
    res = requests.post(url,
                        headers=get_jwt_headers(token, portal_token),
                        json=payload)
    return check_response(res, debug=debug)


def do_org_delete(org_id, org_key, endpoint, debug=False):
    url = (get_org_url(org_id) + endpoint)
    if debug:
        print("do_org_delete: %s" % url)
    res = requests.delete(url, headers=get_headers(org_key))
    return check_response(res, debug=debug)


def do_org_post(org_id, org_key, endpoint, payload, debug=False):
    url = (get_org_url(org_id) + endpoint)
    if debug:
        print("do_org_post: %s" % url)
    res = requests.post(url, headers=get_headers(org_key), json=payload)
    return check_response(res, debug=debug)


def get_jwt(username, password, debug=False):
    url = EI_API_LOGIN_URL
    payload = {"username": username, "password": password}
    if debug:
        print("get_jwt: %s" % url)
    res = requests.post(url,
                        headers={"Content-Type": "application/json"},
                        json=payload)
    return check_response(res, debug=debug)
