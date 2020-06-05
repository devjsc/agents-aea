# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2019 Fetch.AI Limited
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

"""This module contains utilities for loading components."""
import logging
import re
from typing import Dict, Type

from aea.components.base import Component
from aea.configurations.base import (
    ComponentConfiguration,
    ComponentType,
)
from aea.connections.base import Connection
from aea.contracts.base import Contract
from aea.exceptions import AEAPackageLoadingError
from aea.protocols.base import Protocol
from aea.skills.base import Skill


logger = logging.getLogger(__name__)


def component_type_to_class(component_type: ComponentType) -> Type[Component]:
    type_to_class: Dict[ComponentType, Type[Component]] = {
        ComponentType.PROTOCOL: Protocol,
        ComponentType.CONTRACT: Contract,
        ComponentType.CONNECTION: Connection,
        ComponentType.SKILL: Skill,
    }
    return type_to_class[component_type]


def load_component_from_config(  # type: ignore
    component_type: ComponentType,
    configuration: ComponentConfiguration,
    *args,
    **kwargs
) -> Component:
    """
    Load a component from a directory.

    :param component_type: the component type.
    :param configuration: the component configuration.
    :return: the component instance.
    """
    component_class = component_type_to_class(component_type)
    try:
        return component_class.from_config(*args, configuration=configuration, **kwargs)  # type: ignore
    except ModuleNotFoundError as e:
        _handle_error_while_loading_component_module_not_found(configuration, e)
    except Exception as e:
        _handle_error_while_loading_component_generic_error(configuration, e)


def _handle_error_while_loading_component_module_not_found(
    configuration: ComponentConfiguration, e: ModuleNotFoundError
):
    """
    Handle ModuleNotFoundError for AEA packages.

    It will rewrite the error message only if the import path starts with 'packages'.
    To do that, it will extract the wrong import path from the error message.

    Depending on the import path, the possible error messages can be:

    - "No AEA package found with author name '{}', type '{}', name '{}'"
    - "'{}' is not a valid type name, choose one of ['protocols', 'connections', 'skills', 'contracts']"
    - "The package '{}/{}' of type '{}' exists, but cannot find module '{}'"

    :raises ModuleNotFoundError: if it is not
    :raises AEAPackageLoadingError: the same exception, but prepending an informative message.
    """
    error_message = str(e)
    extract_import_path_regex = re.compile(r"No module named '([\w.]+)'")
    match = extract_import_path_regex.match(error_message)
    if match is None:
        # if for some reason we cannot extract the import path, just re-raise the error
        raise e from e

    import_path = match.group(1)
    parts = import_path.split(".")
    nb_parts = len(parts)
    if parts[0] != "packages" and nb_parts < 2:
        # if the first part of the import path is not 'packages',
        # the error is due for other reasons - just re-raise the error
        raise e from e

    def get_new_error_message_no_package_found() -> str:
        """Create a new error message in case the package is not found."""
        assert nb_parts <= 4, "More than 4 parts!"
        author = parts[1]
        new_message = "No AEA package found with author name '{}'".format(author)

        if nb_parts >= 3:
            pkg_type = parts[2]
            try:
                ComponentType(pkg_type[:-1])
            except ValueError:
                return "'{}' is not a valid type name, choose one of {}".format(
                    pkg_type, list(map(lambda x: x.to_plural(), ComponentType))
                )
            new_message += ", type '{}'".format(pkg_type)
        if nb_parts == 4:
            pkg_name = parts[3]
            new_message += ", name '{}'".format(pkg_name)
        return new_message

    def get_new_error_message_with_package_found() -> str:
        """Create a new error message in case the package is found."""
        assert nb_parts >= 5, "Less than 5 parts!"
        author, pkg_name, pkg_type = parts[:3]
        the_rest = ".".join(parts[4:])
        return "The package '{}/{}' of type '{}' exists, but cannot find module '{}'".format(
            author, pkg_name, pkg_type, the_rest
        )

    if nb_parts < 5:
        new_message = get_new_error_message_no_package_found()
    else:
        new_message = get_new_error_message_with_package_found()

    raise AEAPackageLoadingError(
        "An error occurred while loading {} {}: No module named {}; {}".format(
            str(configuration.component_type),
            configuration.public_id,
            import_path,
            new_message,
        )
    ) from e


def _handle_error_while_loading_component_generic_error(
    configuration: ComponentConfiguration, e: Exception
):
    """
    Handle Exception for AEA packages.

    :raises Exception: the same exception, but prepending an informative message.
    """
    raise Exception(
        "An error occurred while loading {} {}: {}".format(
            str(configuration.component_type), configuration.public_id, str(e)
        )
    ) from e