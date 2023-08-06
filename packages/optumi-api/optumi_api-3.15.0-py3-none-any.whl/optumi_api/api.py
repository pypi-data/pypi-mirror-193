##
## Copyright (C) Optumi Inc - All rights reserved.
##
## You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
## To receive a copy of the licensing terms please write to contact@optumi.com or visit us at https://www.optumi.com.
##

from .LoginServer import login as oauth_login
from .HoldoverTime import HoldoverTime
from .Workloads import Workloads
from requests.exceptions import ConnectionError

import phonenumbers

# Generic Operating System Services
import datetime, json, os
from typing import Union

# Optumi imports
import optumi_core as optumi
from optumi_core.exceptions import (
    NotLoggedInException,
    ServiceException,
    OptumiException,
)

DEBUG_LOGIN = False

# We will keep various lists from the controller in place of enums
_machines = None
_providers = None
_graphics_card_types = None


def machines():
    if _machines is None:
        raise NotLoggedInException()
    return _machines


def providers():
    if _providers is None:
        raise NotLoggedInException()
    return _providers


def graphics_card_types():
    if _graphics_card_types is None:
        raise NotLoggedInException()
    return _graphics_card_types


def login(
    connection_token=None,
    dnsName=optumi.login.get_portal(),
    port=optumi.login.get_portal_port(),
    save_token=True,
):
    global _machines, _providers, _graphics_card_types

    # On a dynamic machine we do not need to get an okta token
    if optumi.login.is_dynamic():
        if DEBUG_LOGIN:
            print("Dynamic login")
        if not optumi.login.check_login(dnsName, port, mode="api"):
            if DEBUG_LOGIN:
                print("Not logged in")
            login_status, message = optumi.login.login_rest_server(
                dnsName,
                port,
                "",
                mode="api",
                login_type="dynamic",
                save_token=save_token,
            )
    else:
        if DEBUG_LOGIN:
            print("Normal login")
        if not optumi.login.check_login(dnsName, port, mode="api"):
            if DEBUG_LOGIN:
                print("Not logged in")
            if connection_token == None:
                if DEBUG_LOGIN:
                    print("No connection token")
                if DEBUG_LOGIN:
                    print("Trying login with disk token")
                # Try to log in with the login token from the disk
                login_status, message = optumi.login.login_rest_server(
                    dnsName, port, mode="api", login_type="token", save_token=save_token
                )

                # Fall back on the browser login
                if login_status != 1:
                    if DEBUG_LOGIN:
                        print("Trying browser login")
                    login_status, message = optumi.login.login_rest_server(
                        dnsName,
                        port,
                        oauth_login(),
                        mode="api",
                        login_type="oauth",
                        save_token=save_token,
                    )
                    if login_status != 1:
                        raise NotLoggedInException("Login failed: " + message)
            else:
                if DEBUG_LOGIN:
                    print("Connection token")
                login_status, message = optumi.login.login_rest_server(
                    dnsName,
                    port,
                    connection_token,
                    mode="api",
                    login_type="token",
                    save_token=save_token,
                )
                if login_status != 1:
                    raise NotLoggedInException("Login failed: " + message)

    user_information = json.loads(optumi.core.get_user_information(True).text)

    print("Logged in", user_information["name"])

    _machines = []
    _providers = []
    _graphics_card_types = []

    for machine in user_information["machines"]:
        name = machine["name"]
        provider = name.split(":")[0]
        graphics_card_type = machine["graphicsCardType"]

        if not machine in _machines:
            _machines.append(name)

        if not provider in _providers:
            _providers.append(provider)

        if not graphics_card_type in _graphics_card_types:
            _graphics_card_types.append(graphics_card_type)

    _machines.sort()
    _providers.sort()
    _graphics_card_types.sort()


# Remove token = false
def logout(remove_token=True):
    try:
        optumi.login.logout(mode="api", remove_token=remove_token)
    except NotLoggedInException:
        pass


def get_phone_number():
    return json.loads(optumi.core.get_user_information(False).text)["phoneNumber"]


def get_holdover_time():
    res = optumi.core.get_user_information(False)
    return HoldoverTime(
        int(
            json.loads(optumi.core.get_user_information(False).text)["userHoldoverTime"]
        )
        // 60  # Convert to minutes
    )


def set_holdover_time(holdover_time: Union[int, HoldoverTime]):
    optumi.core.set_user_information(
        "userHoldoverTime",
        str(
            holdover_time.seconds
            if type(holdover_time) is HoldoverTime
            else holdover_time * 60  # Convert to seconds
        ),
    )


def get_connection_token():
    return json.loads(optumi.core.get_connection_token(False).text)


def redeem_signup_code(signupCode):
    optumi.core.redeem_signup_code(signupCode)


def send_notification(message, details=True):
    if get_phone_number():
        optumi.core.send_notification(
            "From " + str(Workloads.current()) + ": " + message
            if details and optumi.login.is_dynamic()
            else message
        )
    else:
        print("Unable to send notification - no phone number specified")


def set_phone_number(phone_number):
    if phone_number == "":
        optumi.core.clear_phone_number()
    else:
        number = phonenumbers.parse(phone_number, "US")
        if not phonenumbers.is_valid_number(number):
            raise OptumiException(
                "The string supplied did not seem to be a valid phone number."
            )

        formatted_number = phonenumbers.format_number(
            number, phonenumbers.PhoneNumberFormat.E164
        )

        optumi.core.send_verification_code(formatted_number)

        while True:
            code = input("Enter code sent to " + formatted_number + ": ")
            text = optumi.core.check_verification_code(formatted_number, code).text

            if text:
                print(text)
                # This is kind of sketchy but wont break if the message changes, it will just continue prompting the user for their code
                if text == "Max check attempts reached":
                    break
            else:
                optumi.set_user_information("notificationsEnabled", True)
                break
