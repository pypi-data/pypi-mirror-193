# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.
"""Module for utility."""
import re

import inflection


def _get_function_name(mutation_name: str) -> str:
    """
    Returns the corresponding function name
    for the given mutation name.
    """
    name = re.sub("^core__", "", mutation_name)
    return inflection.underscore(name)
