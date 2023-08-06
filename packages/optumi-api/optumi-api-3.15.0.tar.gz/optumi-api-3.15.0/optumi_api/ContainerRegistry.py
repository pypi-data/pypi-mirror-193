##
## Copyright (C) Optumi Inc - All rights reserved.
##
## You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
## To receive a copy of the licensing terms please write to contact@optumi.com or visit us at https://www.optumi.com.
##

import optumi_core as optumi
from optumi_core.exceptions import (
    NotLoggedInException,
    ServiceException,
    OptumiException,
)


import json


class ContainerRegistry:
    def __init__(
        self,
        name: str = "",
        url: str = None,
        username: str = None,
        password: str = None,
    ):
        got_url = url != None and len(username) > 0
        got_username = username != None and len(username) > 0
        got_password = password != None and len(username) > 0
        if got_url != got_username or got_url != got_password:
            raise OptumiException(
                "Need url, username, and password to specify registry"
            )

        self._name = name

        if url is None:
            # Retrieve the container registry
            # This is not the best way to do this...
            integrations = json.loads(optumi.core.get_integrations().text)[
                "integrations"
            ]
            for integration in integrations:
                if integration["name"] == name:
                    self._name = integration["name"]
                    self._url = integration["url"]
                    return
            raise OptumiException(
                "Unable to find container registry named '" + name + "'"
            )
        else:
            # Store the container registry
            info = {
                "integrationType": "container registry",
                "name": name,
                "registryService": "generic container registry",
                "url": url,
                "username": username,
                "password": password,
            }
            res = optumi.core.add_integration(name, json.dumps(info), False).text
            try:
                integration = json.loads(res)
                self._name = integration["name"]
                self._url = integration["url"]
            except json.decoder.JSONDecodeError:
                raise OptumiException(res)

    def rename(self, newName):
        optumi.core.rename_integration(self._name, newName)
        self._name = newName

    def remove(self):
        ContainerRegistry.purge(self._name)

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @classmethod
    def purge(cls, name: str):
        optumi.core.remove_integration(name)

    def __str__(self):
        return str(self._url)
