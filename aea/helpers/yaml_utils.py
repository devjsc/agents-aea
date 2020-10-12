# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2020 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------

"""Helper functions related to YAML loading/dumping."""
from collections import OrderedDict
from typing import Any, Dict, List

import yaml


class _AEAYamlLoader(yaml.SafeLoader):
    """
    Custom yaml.SafeLoader for the AEA framework.

    It extends the default SafeLoader in two ways:
    - loads YAML configurations while *remembering the order of the fields*;
    - TODO
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the AEAYamlLoader.

        It adds a YAML Loader constructor to use 'OderedDict' to load the files.
        """
        super().__init__(*args, **kwargs)
        _AEAYamlLoader.add_constructor(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, self._construct_mapping
        )

    @staticmethod
    def _construct_mapping(loader, node):
        """Construct a YAML mapping with OrderedDict."""
        object_pairs_hook = OrderedDict
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))


class _AEAYamlDumper(yaml.SafeDumper):
    """
    Custom yaml.SafeDumper for the AEA framework.

    It extends the default SafeDumper in two ways:
    - dumps YAML configurations while *following the order of the fields*;
    - TODO
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the AEAYamlDumper.

        It adds a YAML Dumper representer to use 'OderedDict' to dump the files.
        """
        super().__init__(*args, **kwargs)
        _AEAYamlDumper.add_representer(OrderedDict, self._dict_representer)

    @staticmethod
    def _dict_representer(dumper, data):
        """Use a custom representer."""
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, data.items()
        )


def yaml_load(*args, **kwargs) -> Dict[str, Any]:
    """
    Load a yaml from a file pointer in an ordered way.

    :return: the yaml
    """
    return yaml.load(*args, **kwargs, Loader=_AEAYamlLoader)  # nosec


def yaml_load_all(*args, **kwargs) -> List[Dict[str, Any]]:
    """
    Load a multi-paged yaml from a file pointer in an ordered way.

    :return: the yaml
    """
    return list(yaml.load_all(*args, **kwargs, Loader=_AEAYamlLoader))  # nosec


def yaml_dump(*args, **kwargs) -> None:
    """
    Dump multi-paged yaml data to a yaml file in an ordered way.

    :return None
    """
    yaml.dump(*args, **kwargs, Dumper=_AEAYamlDumper)  # nosec


def yaml_dump_all(*args, **kwargs) -> None:
    """
    Dump multi-paged yaml data to a yaml file in an ordered way.

    :return None
    """
    yaml.dump_all(*args, **kwargs, Dumper=_AEAYamlDumper)  # nosec
