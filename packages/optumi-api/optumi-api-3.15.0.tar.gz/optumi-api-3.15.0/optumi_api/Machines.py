##
## Copyright (C) Optumi Inc - All rights reserved.
##
## You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
## To receive a copy of the licensing terms please write to contact@optumi.com or visit us at https://www.optumi.com.
##

import optumi_core as optumi

import json

from .Machine import Machine

from optumi_core.exceptions import (
    OptumiException,
)


class Machines:
    @classmethod
    def list(cls, status: str = None):
        if status != None and not status in Machine.status_values:
            raise OptumiException(
                "Unexpected machine status '"
                + status
                + "', expected on of "
                + str(Machine.status_values)
            )

        machines = []

        response = json.loads(optumi.core.get_machines().text)

        for machine in response["machines"]:
            machine = Machine(*Machine.reconstruct(machine))
            if (status is None and machine.is_visible()) or (machine.status == status):
                machines.append(machine)

        return machines
