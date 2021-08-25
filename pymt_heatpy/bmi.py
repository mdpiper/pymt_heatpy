from __future__ import absolute_import

import pkg_resources
from heat import BmiHeat as HeatModelPy

HeatModelPy.__name__ = "HeatModelPy"
HeatModelPy.METADATA = pkg_resources.resource_filename(__name__, "data/HeatModelPy")

__all__ = [
    "HeatModelPy",
]
