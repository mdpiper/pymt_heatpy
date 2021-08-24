#! /usr/bin/env python
import pkg_resources

__version__ = pkg_resources.get_distribution("pymt_heatpy").version


from .bmi import HeatModelPy

__all__ = [
    "HeatModelPy",
]
