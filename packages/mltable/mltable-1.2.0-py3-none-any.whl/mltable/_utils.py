# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
from jsonschema import validate
import os
import re

from azureml.dataprep.api.mltable._mltable_helper import _parse_path_format, _PathType
from azureml.dataprep.api._loggerfactory import _LoggerFactory


_logger = _LoggerFactory.get_logger('MLTableUtils')
_long_form_aml_uri = re.compile(
    r'^azureml://subscriptions/([^\/]+)/resourcegroups/([^\/]+)/'
    r'(?:providers/Microsoft.MachineLearningServices/)?workspaces/([^\/]+)/(.*)',
    re.IGNORECASE)


def _is_local_path(path):
    return _parse_path_format(path)[0] == _PathType.local


def _make_all_paths_absolute(mltable_yaml_dict, base_path, is_local=False):
    if base_path and 'paths' in mltable_yaml_dict:
        for path_dict in mltable_yaml_dict['paths']:
            for path_prop, path in path_dict.items():
                # get absolute path from base_path + relative path
                if _is_local_path(path) and not path.startswith('file://'):
                    # assume that local relative paths are co-located in directory of MLTable file
                    path = os.path.normpath(path)

                    if not os.path.isabs(path):
                        # when path == '.' it represents the current dir, which is base_path ex) folder: .
                        path = base_path if _path_is_current_directory_variant(path) else os.path.join(base_path, path)

                    if _is_local_path(base_path):
                        path = os.path.normpath(path)

                    if is_local:
                        path = "file://" + os.path.abspath(path)

                    path_dict[path_prop] = path

    return mltable_yaml_dict


def _path_is_current_directory_variant(path):
    return path in ['.', './', '.\\']


def _validate(mltable_yaml_dict):
    cwd = os.path.dirname(os.path.abspath(__file__))
    schema_path = "{}/schema/MLTable.json".format(cwd.rstrip("/"))
    with open(schema_path, "r") as stream:
        try:
            schema = json.load(stream)
        except json.decoder.JSONDecodeError:
            raise RuntimeError("MLTable json schema is not a valid json file.")
    try:
        validate(mltable_yaml_dict, schema)
    except Exception as e:
        _logger.warning("MLTable validation failed with error: {}".format(e.args))
        raise ValueError("Given MLTable does not adhere to the AzureML MLTable schema: {}".format(e.args))


# will switch to the api from dataprep package once new dataprep version is released
def _parse_workspace_context_from_longform_uri(uri):
    long_form_uri_match = _long_form_aml_uri.match(uri)

    if long_form_uri_match:
        return {
            'subscription': long_form_uri_match.group(1),
            'resource_group': long_form_uri_match.group(2),
            'workspace_name': long_form_uri_match.group(3)
        }

    return None
