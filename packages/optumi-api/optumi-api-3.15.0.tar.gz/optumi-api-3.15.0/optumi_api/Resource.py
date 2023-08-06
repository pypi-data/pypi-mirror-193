##
## Copyright (C) Optumi Inc - All rights reserved.
##
## You may only use this code under license with Optumi Inc and any distribution or modification is strictly prohibited.
## To receive a copy of the licensing terms please write to contact@optumi.com or visit us at https://www.optumi.com.
##

from .api import graphics_card_types
from typing import Union

from optumi_core.exceptions import (
    OptumiException,
)


class Resource:
    def __init__(self, gpu: Union[bool, str] = True, memory_per_card=0):
        if type(gpu) is str and not gpu.lower() in [x.lower() for x in graphics_card_types()]:
            raise OptumiException(
                "Unexpected GPU type '"
                + gpu
                + "', expected on of "
                + str(graphics_card_types())
            )
        self._gpu = gpu
        self._memory_per_card = memory_per_card

    @property
    def gpu(self):
        return self._gpu

    @property
    def memory_per_card(self):
        return self._memory_per_card

    def __str__(self):
        return "gpu=" + str(self.gpu)
