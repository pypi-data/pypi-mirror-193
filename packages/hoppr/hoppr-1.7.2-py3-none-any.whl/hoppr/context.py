"""
Define context in which a plug-in runs
"""
from __future__ import annotations

import logging
import threading

from dataclasses import dataclass
from typing import TYPE_CHECKING

# Only import these classes during type-checking
#
# If we import at all times, on execution we get an error like
#    "ImportError: cannot import name 'Credentials' from partially initialized module
#         'hoppr.configs.credentials' (most likely due to a circular import)"
#
# If we don't import for type checking, mypy fails.

if TYPE_CHECKING:  # pragma: no cover
    from hoppr_cyclonedx_models.cyclonedx_1_4 import CyclonedxSoftwareBillOfMaterialsStandard as Bom  # type: ignore

    from hoppr.configs.manifest import Manifest


@dataclass
class Context:  # pylint: disable="too-many-instance-attributes"
    """
    Define context in which a plug-in runs
    """

    manifest: Manifest
    collect_root_dir: str
    consolidated_sbom: Bom
    delivered_sbom: Bom
    max_processes: int
    logfile_lock: threading.RLock
    max_attempts: int = 3
    retry_wait_seconds: float = 5
    logfile_location: str = "hoppr.log"
    log_level: int = logging.INFO
    strict_repos: bool = True
