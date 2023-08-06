from pathlib import Path

import yaml

CONFIG = yaml.safe_load(open(Path(__file__).parent / "workflow.yaml"))

MOUNTS = CONFIG["mounts"]

TEST_CONFIG = yaml.safe_load(open(Path(__file__).parent / "test_workflow.yaml"))

TEST_MOUNTS = TEST_CONFIG["mounts"]
