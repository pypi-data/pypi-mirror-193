#!/usr/bin/python
"""
Initializes core file data
"""
__license__ = "BSD-3"
__docformat__ = 'reStructuredText'
__author__ = "Jared Beard"

from importlib.resources import path
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import json 

if __name__ == "__main__":
    CORE_FILE_NAME = "/config/core/core.json"
    CORE_DEFAULT_FILE_NAME = "/config/core/core_default.json"

    with open(parent + CORE_DEFAULT_FILE_NAME, 'rb') as f:
        config = json.load(f)

    config["trial_path"] = parent + "/config/trial/"
    config["expt_path"] = parent + "/config/expt/"
    config["data_path"] = parent + "/results/"
    config["analysis_path"] = parent + "/config/analysis/"
    config["figure_path"] = parent + "/figs/"

    with open(parent + CORE_DEFAULT_FILE_NAME, 'w') as f:
        json.dump(config, f, indent=4)

    with open(parent + CORE_FILE_NAME, 'w') as f:
        json.dump(config, f, indent=4)
        