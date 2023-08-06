"""
Collector plugin for pypi images
"""
from __future__ import annotations

import importlib.util
import re
import sys

from subprocess import CalledProcessError
from urllib.parse import ParseResult, urljoin, urlparse

from hoppr_cyclonedx_models.cyclonedx_1_4 import Component
from packageurl import PackageURL

from hoppr import __version__
from hoppr.base_plugins.collector import SerialCollectorPlugin
from hoppr.base_plugins.hoppr import hoppr_rerunner
from hoppr.context import Context
from hoppr.hoppr_types.cred_object import CredObject
from hoppr.result import Result


class CollectPypiPlugin(SerialCollectorPlugin):
    """
    Collector plugin for pypi images
    """

    supported_purl_types = ["pypi"]
    required_commands = [sys.executable]
    products: list[str] = ["pypi/*"]
    system_repositories = ["https://pypi.org/simple"]

    def get_version(self) -> str:  # pylint: disable=duplicate-code
        return __version__

    def __init__(self, context: Context, config: dict | None = None) -> None:
        super().__init__(context=context, config=config)

        self.manifest_repos: list[str] = []
        self.password_list: list[str] = []
        self.base_command = [self.required_commands[0], "-m", "pip"]

    def _run_cmd_wrapper(  # pylint: disable=too-many-arguments
        self, command, password_list, param: str, pkg_format: str, log_if_error: str
    ) -> bool:
        """
        Run command utility for discrete function calls - required for DO-178C Level-A branch isolation coverage
        """
        run_result = self.run_command([*command, param], password_list)
        try:
            run_result.check_returncode()
            return True
        except CalledProcessError:
            self.get_logger().debug(msg=f"{log_if_error} {pkg_format} package", indent_level=2)
        return False

    def collect_binary_only(self, command, password_list, log_if_error: str) -> bool:
        """
        Only collect the PyPI binary (WHL)
        """
        return self._run_cmd_wrapper(command, password_list, "--only-binary=:all:", "binary", log_if_error)

    def collect_source(self, command, password_list, log_if_error: str) -> bool:
        """
        Only collect the PyPI source package
        """
        return self._run_cmd_wrapper(command, password_list, "--no-binary=:all:", "source", log_if_error)

    @hoppr_rerunner
    def collect(self, comp: Component, repo_url: str, creds: CredObject | None = None) -> Result:
        """
        Copy a component to the local collection directory structure
        """
        if importlib.util.find_spec(name="pip") is None:
            return Result.fail(message="The pip package was not found. Please install and try again.")

        purl = PackageURL.from_string(comp.purl)
        result = self.check_purl_specified_url(purl, repo_url)  # type: ignore
        if not result.is_success():
            return result

        source_url = repo_url
        if not re.match(pattern="^.*simple/?$", string=source_url):
            source_url = urljoin(base=source_url, url="simple")

        password_list = []

        if creds is not None:
            parsed_url = urlparse(url=source_url)._asdict()
            parsed_url["netloc"] = f"{creds.username}:{creds.password}@{parsed_url['netloc']}"
            source_url = ParseResult(**parsed_url).geturl()
            password_list = [creds.password]

        target_dir = self.directory_for(purl.type, repo_url, subdir=f"{purl.name}_{purl.version}")

        self.get_logger().info(msg=f"Target directory: {target_dir}", indent_level=2)

        command = [
            *self.base_command,
            "download",
            "--no-deps",
            "--no-cache",
            "--timeout",
            "60",
            "--index-url",
            source_url,
            "--dest",
            f"{target_dir}",
            f"{purl.name}=={purl.version}",
        ]

        base_error_msg = f"Failed to download {purl.name} version {purl.version}"

        if self.collect_binary_only(command, password_list, base_error_msg):  # pylint: disable=no-else-return
            return Result.success()
        elif self.collect_source(command, password_list, base_error_msg):  # pylint: disable=no-else-return
            return Result.success()
        else:
            return Result.retry(f"{base_error_msg} as either binary or source.")
