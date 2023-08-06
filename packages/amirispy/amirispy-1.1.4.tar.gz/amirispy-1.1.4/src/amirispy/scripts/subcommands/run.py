# SPDX-FileCopyrightText: 2022 German Aerospace Center <amiris@dlr.de>
#
# SPDX-License-Identifier: Apache-2.0

import logging as log
import os
import subprocess
from pathlib import Path

from fameio.scripts import make_config, convert_results
from fameio.source.cli import Options, ResolveOptions

from amirispy.source.cli import GeneralOptions, RunOptions
from amirispy.source.files import ensure_folder_exists, check_if_write_access
from amirispy.source.logs import log_error_and_raise
from amirispy.source.util import check_java_installation

_ERR_NOT_A_FILE = "Specified Path '{}' does not point to an existing file."


def run_amiris(options: dict) -> None:
    """
    Compile scenario to protobuf using fameio.scripts.make_config,
    execute AMIRIS,
    and extract results using fameio.scripts.convert_results

    Args:
        options:
            RunOptions.JAR: Path to amiris-core_<version>-jar-with-dependencies.jar
            RunOptions.SCENARIO: Path to scenario.yaml
            RunOptions.OUTPUT: Directory to write output to
            GeneralOptions.LOG: Logging level gathered by CLI
            GeneralOptions.LOGFILE: Path to log_file gathered by CLI

    Returns:
        None
    """
    check_java_installation(raise_exception=True)
    origin_wd = Path.cwd()

    fameio_input_config = {
        Options.LOG_LEVEL: options[GeneralOptions.LOG],
        Options.LOG_FILE: options[GeneralOptions.LOGFILE],
        Options.OUTPUT: f"{origin_wd}/input.pb",
    }

    path_to_scenario: Path = options[RunOptions.SCENARIO]
    if not path_to_scenario.is_file():
        log_error_and_raise(ValueError(_ERR_NOT_A_FILE.format(path_to_scenario)))
    scenario_wd = path_to_scenario.parents[0]

    check_if_write_access(origin_wd)
    os.chdir(scenario_wd)
    log.info("Converting binary protobuf file")
    make_config(path_to_scenario.name, fameio_input_config)
    os.chdir(origin_wd)

    path_to_jar = options[RunOptions.JAR]
    jar_wd = path_to_jar.parents[0]
    fame_setup_path = Path(jar_wd, "fameSetup.yaml")

    input_pb = fameio_input_config[Options.OUTPUT]

    call = 'java -jar "{}" -f "{}" -s "{}"'.format(path_to_jar, input_pb, fame_setup_path)
    log.info("Starting AMIRIS")
    subprocess.run(call, shell=True, check=True)

    output_folder = options[RunOptions.OUTPUT]
    fameio_output_config = {
        Options.LOG_LEVEL: options[GeneralOptions.LOG],
        Options.LOG_FILE: options[GeneralOptions.LOGFILE],
        Options.AGENT_LIST: None,
        Options.OUTPUT: output_folder,
        Options.SINGLE_AGENT_EXPORT: False,
        Options.MEMORY_SAVING: False,
        Options.RESOLVE_COMPLEX_FIELD: ResolveOptions.SPLIT,
    }

    path_to_amiris_pb_result = "output.pb"
    ensure_folder_exists(output_folder)
    check_if_write_access(output_folder)
    log.info("Converting protobuf to csv files")
    convert_results(path_to_amiris_pb_result, fameio_output_config)
