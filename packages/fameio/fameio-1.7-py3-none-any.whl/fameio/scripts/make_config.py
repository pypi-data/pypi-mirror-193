#!/usr/bin/env python
import logging as log
from pathlib import Path
from typing import Union

from fameio.source.cli import Options, arg_handling_make_config, get_config_or_default
from fameio.source.loader import load_yaml, check_for_yaml_file_type
from fameio.source.logs import set_up_logger
from fameio.source.scenario import Scenario
from fameio.source.validator import SchemaValidator
from fameio.source.writer import ProtoWriter

DEFAULT_CONFIG = {
    Options.LOG_LEVEL: "info",
    Options.LOG_FILE: None,
    Options.OUTPUT: Path("config.pb"),
}


def run(file: Union[str, Path], config: dict = None) -> None:
    """Executes the main workflow for the building of a FAME configuration file"""
    config = get_config_or_default(config, DEFAULT_CONFIG)
    set_up_logger(level_name=config[Options.LOG_LEVEL], file_name=config[Options.LOG_FILE])

    check_for_yaml_file_type(Path(file))
    scenario = Scenario.from_dict(load_yaml(Path(file)))
    SchemaValidator.ensure_is_valid_scenario(scenario)
    writer = ProtoWriter(config[Options.OUTPUT])
    writer.write_validated_scenario(scenario)

    log.info("Configuration completed.")


if __name__ == "__main__":
    input_file, run_config = arg_handling_make_config(DEFAULT_CONFIG)
    run(input_file, run_config)
