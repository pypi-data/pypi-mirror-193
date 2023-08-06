##
## Copyright (C) Optumi Inc - All rights reserved.
##
## You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
## To receive a copy of the licensing terms please write to contact@optumi.com or visit us at https://www.optumi.com.
##

from .api import providers, machines

from optumi_core.exceptions import (
    OptumiException,
)


# Support embedding the provider in the machine string, have no default provider argument
class Server:
    def __init__(self, size: str = "Standard_NC4as_T4_v3", provider: str = "Azure"):
        if ":" in size:
            s = size.split(":")
            self._provider = s[0].lower()
            self._size = s[1].lower()
        else:
            self._provider = provider.lower()
            self._size = size.lower()

        if not self._provider in [x.lower() for x in providers()]:
            raise OptumiException(
                "Unexpected provider '"
                + self._provider
                + "', expected on of "
                + str(providers())
            )

        if not self._provider + ":" + self._size in [x.lower() for x in machines()]:
            raise OptumiException(
                "Unexpected machine size '"
                + self._provider
                + ":"
                + self._size
                + "', expected on of "
                + str(machines())
            )

    @property
    def provider(self):
        return self._provider

    @property
    def size(self):
        return self._size

    def __str__(self):
        return str(self.provider) + ":" + str(self.size)
