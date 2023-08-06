##
## Copyright (C) Optumi Inc - All rights reserved.
##
## You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
## To receive a copy of the licensing terms please write to contact@optumi.com or visit us at https://www.optumi.com.
##

import optumi_core as optumi
from optumi_core.exceptions import (
    OptumiException,
)

from .Workload import Workload

import json, os


class Workloads:
    @classmethod
    def list(cls, status: str = None):
        if status != None and not status in Workload.status_values:
            raise OptumiException(
                "Unexpected workload status '"
                + status
                + "', expected on of "
                + str(Workload.status_values)
            )

        workloads = []

        user_information = json.loads(optumi.core.get_user_information(True).text)

        # Add apps from user information if they don't already exist
        if "jobs" in user_information:
            for app_map in user_information["jobs"]:
                workload = Workload.reconstruct(app_map)
                if (status is None) or (workload.status == status):
                    workloads.append(workload)
        return workloads

    @classmethod
    def current(cls):
        if not os.environ["OPTUMI_MOD"]:
            raise OptumiException(
                "Workloads.current() only supported on Optumi dynamic machines."
            )

        user_information = json.loads(optumi.core.get_user_information(True).text)

        workloads = []

        # Add apps from user information if they don't already exist
        if "jobs" in user_information:
            for app_map in user_information["jobs"]:
                for module in app_map["modules"]:
                    if module["uuid"] == os.environ["OPTUMI_MOD"]:
                        return Workload(*Workload.reconstruct(app_map))
