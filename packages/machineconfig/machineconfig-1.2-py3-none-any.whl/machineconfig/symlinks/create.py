
"""
This script Takes away all config files from the computer, place them in one directory
`dotfiles`, and create symlinks to those files from thier original locations.
"""

import crocodile.toolbox as tb
from crocodile.environment import DotFiles, system, PathVar, UserName  # ProgramFiles, WindowsApps  # , exe
from machineconfig.utils.utils import symlink
import os


repo_root = tb.P.home().joinpath(f"code/machineconfig/src/machineconfig")
M_CONFIG = tb.P.home().joinpath("code/machineconfig/settings")

mapper = tb.P("~/code/machineconfig/src/machineconfig/symlinks/mapper.toml").readit()
mapper['wsl_windows']['home']["to_this"] = mapper['wsl_windows']['home']["to_this"].replace("username", UserName)
mapper['wsl_linux']['home']["to_this"] = mapper['wsl_linux']['home']["to_this"].replace("username", UserName)

env_path = tb.P("~/code/machineconfig/src/machineconfig/symlinks/env_path.toml").readit()


def link_ssh(overwrite=True):
    """The function can link aribtrary number of files without linking the directory itself (which is not doable in toml config file)"""
    path = tb.P.home().joinpath(".ssh")
    target = DotFiles.joinpath(".ssh")
    for item in target.search("*"):
        if "authorized_keys" in item: continue
        symlink(path.joinpath(item.name), item, prioritize_to_this=overwrite)
    if system == "Linux":  # permissions of ~/dotfiles/.ssh should be adjusted
        os.system("chmod 700 ~/dotfiles/.ssh")  # may require sudo
        os.system("chmod 600 ~/dotfiles/.ssh/*")


def link_aws(overwrite=True):
    path = tb.P.home().joinpath(".aws")
    target = DotFiles.joinpath("aws/.aws")
    for item in target.search("*"): symlink(path.joinpath(item.name), item, prioritize_to_this=overwrite)


def add_to_shell_profile_path(dirs: list):
    addition = PathVar.append_temporarily(dirs=dirs)
    if system == "Windows": tb.Terminal().run("$profile", shell="pwsh").as_path.modify_text(addition, addition, newline=False, notfound_append=True)
    elif system == "Linux": tb.P("~/.bashrc").expanduser().modify_text(addition, addition, notfound_append=True)
    else: raise ValueError


def main():
    overwrite = True
    exclude = ["startup_windows"]
    for key in mapper.keys():
        if key in exclude or f"_{system.lower()}" in key: continue
        symlink(this=mapper[key]['this'], to_this=mapper[key]['to_this'], prioritize_to_this=overwrite)

    link_aws(overwrite=overwrite)
    link_ssh(overwrite=overwrite)
    if system == "Linux": tb.Terminal().run(f'chmod +x {repo_root.joinpath(f"scripts/{system.lower()}")} -R')

    # The following is not a symlink creation, but modification of shell profile by additing dirs to PATH
    # Shell profile is either in dotfiles and is synced (as in Windows), hence no need for update, or is updated on the fly (for Linux)
    # for windows it won't change the profile, if the profile was modified already e.g. due to syncing
    add_to_shell_profile_path(env_path[f'path_{system.lower()}']['extension'])


if __name__ == '__main__':
    pass
