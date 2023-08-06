"""@Author: Rayane AMROUCHE

The source code is composed of three main components:

- A DataManager component

- A Controller component

- A Model component

The View component can also be used if needed.
"""

import logging

from dsmanager.controller import Config

from dsmanager.datamanager import DataManager

try:
    from dsmanager.model import ModelManager
except ModuleNotFoundError as m_error:
    logging.getLogger(None).debug(
        "'ModelManager' is not available because '%s' is missing.", m_error.name
    )

try:
    from dsmanager.model import Model
except ModuleNotFoundError as m_error:
    logging.getLogger(None).debug(
        "'Model' is not available because '%s' is missing.", m_error.name
    )
