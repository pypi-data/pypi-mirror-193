"""
Collector plugin for git repositories
"""

import os
import pathlib
import re

from typing import Any, Dict, List, Optional

from packageurl import PackageURL  # type: ignore

from hoppr import __version__
from hoppr.base_plugins.collector import SerialCollectorPlugin
from hoppr.base_plugins.hoppr import hoppr_rerunner
from hoppr.context import Context
from hoppr.hoppr_types.cred_object import CredObject
from hoppr.result import Result


class CollectGitPlugin(SerialCollectorPlugin):
    """
    Class to copy git repositories
    """

    supported_purl_types = ["git", "gitlab", "github"]
    required_commands = ["git"]
    products: List[str] = ["git/*", "gitlab/*", "github/*"]

    def get_version(self) -> str:  # pylint: disable=duplicate-code
        return __version__

    def __init__(self, context: Context, config: Optional[Dict] = None) -> None:
        super().__init__(context=context, config=config)
        if self.config is not None:
            if "git_command" in self.config:
                self.required_commands = [self.config["git_command"]]

    @hoppr_rerunner
    def collect(self, comp: Any, repo_url: str, creds: CredObject = None):
        """
        Collect git repository
        """
        purl = PackageURL.from_string(comp.purl)
        git_result = self.check_purl_specified_url(purl, repo_url)
        if not git_result.is_success():
            return git_result

        source_url = os.path.join(repo_url, purl.namespace, purl.name)

        self.get_logger().info(
            msg=f"Cloning {source_url}",
            indent_level=2,
        )

        target_dir = self.directory_for(purl.type, repo_url, subdir=os.path.join(purl.namespace, purl.name))

        git_result = self.git_clone(target_dir, source_url, creds)
        if not git_result.is_success():
            return git_result

        git_result = self.git_update(target_dir, purl.name)
        if not git_result.is_success():
            return git_result

        return Result.success()

    def git_clone(self, tmp_dir, source_url, source_creds):
        """Git clone"""

        git_src = source_url
        password_list = []
        if re.match("^https?://", git_src) and source_creds is not None:
            git_src = git_src.replace("://", f"://{source_creds.username}@", 1)
            if source_creds.password:
                git_src = git_src.replace("@", f":{source_creds.password}@")
                password_list = [source_creds.password]

        if git_src.startswith("ssh://") and source_creds is not None:
            git_src = git_src.replace("ssh://", f"ssh://{source_creds.username}@")

        if not git_src.endswith(".git"):
            git_src += ".git"

        result = self.run_command(
            [self.required_commands[0], "clone", "--mirror", git_src],
            password_list,
            cwd=tmp_dir,
        )
        if result.returncode != 0:
            msg = f"Failed to clone {source_url}"
            self.get_logger().debug(msg=msg, indent_level=2)
            return Result.retry(message=msg)

        return Result.success()

    def git_update(self, tmp_dir, name_git):
        """Git update-server-info"""

        if not name_git.endswith(".git"):
            name_git += ".git"

        repo_dir = os.path.join(pathlib.Path(tmp_dir), name_git)

        # Make the clone usable as a remote
        result = self.run_command(
            [self.required_commands[0], "update-server-info"],
            cwd=repo_dir,
        )
        if result.returncode != 0:
            msg = "Failed to make the clone usable as a remote"
            self.get_logger().debug(msg=msg, indent_level=2)
            return Result.retry(message=msg)

        return Result.success()
