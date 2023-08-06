from __future__ import annotations

import os
import shlex
import sys
from dataclasses import dataclass
from pathlib import Path
from shutil import which
from typing import Any

import myke
import yapx
from packaging import version

from .__version__ import __version__

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


@dataclass
class CliCheckReport:
    name: str
    expected: str
    found: str | None = None
    path: str | None = None
    satisfied: bool = False
    ref: str | None = None


def _check_cli_version(
    cmd: str | list[str],
    version_idx: int,
    expected: str,
    name: str | None = None,
    ref: str | None = None,
) -> CliCheckReport:
    if isinstance(cmd, str):
        cmd = cmd.split()

    report: CliCheckReport = CliCheckReport(
        name=name if name else cmd[0],
        expected=expected,
        ref=ref,
    )

    expected_ver: version.Version = version.parse(expected)

    report.path = which(cmd[0])

    if not report.path:
        report.found = "None"
    else:
        try:
            ver: str = [
                x for x in myke.sh_stdout_lines(" ".join(cmd), check=False) if x.strip()
            ][0].split()[version_idx]
            parsed_ver: version.Version = version.parse(ver.lower().lstrip("v"))
        except (IndexError, version.InvalidVersion):
            report.found = "Error"
        else:
            report.found = str(parsed_ver)
            report.satisfied = expected_ver.major == parsed_ver.major

    return report


def _check_tools() -> None:
    myke.echo.table(
        [
            vars(
                _check_cli_version(
                    ["vim", "--version"],
                    version_idx=4,
                    expected="8.2",
                    ref="apt install --upgrade vim",
                ),
            ),
            vars(
                _check_cli_version(
                    ["nvim", "--version"],
                    name="neovim",
                    version_idx=1,
                    expected="0.8.3",
                    ref="https://github.com/neovim/neovim/releases",
                ),
            ),
            vars(
                _check_cli_version(
                    ["broot", "--version"],
                    version_idx=1,
                    expected="1.20.0",
                    ref="https://github.com/Canop/broot/releases",
                ),
            ),
            vars(
                _check_cli_version(
                    "llama --version 2>&1",
                    version_idx=3,
                    expected="1.4.0",
                    ref="https://github.com/antonmedv/llama/releases",
                ),
            ),
            vars(
                _check_cli_version(
                    ["fzf", "--version"],
                    version_idx=0,
                    expected="0.38.0",
                    ref="https://github.com/antonmedv/llama/releases",
                ),
            ),
            vars(
                _check_cli_version(
                    ["fdfind", "--version"],
                    version_idx=1,
                    expected="8.3.1",
                    ref="https://github.com/sharkdp/fd/releases",
                ),
            ),
            vars(
                _check_cli_version(
                    ["rg", "--version"],
                    name="ripgrep",
                    version_idx=1,
                    expected="13.0.0",
                    ref="https://github.com/BurntSushi/ripgrep/releases",
                ),
            ),
            vars(
                _check_cli_version(
                    ["glow", "--version"],
                    version_idx=2,
                    expected="1.5.0",
                    ref="https://github.com/charmbracelet/glow/releases",
                ),
            ),
            vars(
                _check_cli_version(
                    ["code-minimap", "--version"],
                    version_idx=1,
                    expected="0.6.4",
                    ref="https://github.com/wfxr/code-minimap/releases",
                ),
            ),
        ],
    )


def setup(
    path_or_args: str | None = yapx.arg(None, pos=True),
    paths: list[str] = yapx.arg(lambda: [], pos=True),
    editor: Literal["vim", "nvim", "vym", "nvym", "lvym", "lnvym"] = yapx.arg(
        "vim",
        flags=["-e", "--editor"],
        env="EDITOR",
    ),
    editor_profile: str
    | None = yapx.arg(None, flags=["-u", "--editor-profile"], env="VYM_PROFILE"),
    no_editor_chdir: bool = yapx.arg(False, flags=["--no-editor-chdir"]),
    launcher: str = yapx.arg("broot", flags=["--launcher"]),
    launcher_config: str | None = yapx.arg(None, flags=["--launcher-config"]),
    new_window: bool = yapx.arg(False),
    debug: bool = yapx.arg(False, env="VYM_DEBUG"),
    print_version: bool = yapx.arg(False, flags=["--version"], exclusive=True),
    which_profile: bool = yapx.arg(False, exclusive=True),
    check_tools: bool = yapx.arg(False, exclusive=True),
    install_plugins: bool = yapx.arg(False, exclusive=True),
) -> None:
    if print_version:
        print(__version__)
        sys.exit(0)

    if check_tools:
        _check_tools()
        sys.exit(0)

    if debug:
        print("*** vym cwd:", Path.cwd())
        print("path_or_args:", path_or_args)
        print("paths:", paths)

    os.environ["EDITOR"] = editor

    if " " in editor:
        editor, _ = editor.split(maxsplit=1)

    if editor in ("lvym", "lnvym"):
        launcher = "llama"
        editor = editor.lstrip("l")

    if not path_or_args:
        paths = [str(Path.cwd())]
    elif (
        path_or_args == "-"
        or (
            " " not in path_or_args
            and not path_or_args.startswith(("+", "-"))
            and not paths
        )
        or os.access(path_or_args, os.R_OK)
        or os.access(os.path.dirname(path_or_args), os.R_OK)
    ):
        paths.insert(0, path_or_args)
        path_or_args = None

    if debug:
        print("parsed path_or_args:", path_or_args)
        print("parsed paths:", paths)

    is_stdin: bool = "-" in paths

    if paths and len(paths) == 1 and not is_stdin and not Path(paths[0]).exists():
        if ":" in paths[0]:
            path_parts = [x for x in paths[0].split(":") if x]
            paths[0] = path_parts[0]
            i_row: int = int(path_parts[1])
            i_col: int = 0 if len(path_parts) < 3 else int(path_parts[2])
            jump_to_pos = f'"+call cursor({i_row}, {i_col})"'
            if path_or_args:
                path_or_args += " " + jump_to_pos
            else:
                path_or_args = jump_to_pos
        elif "*" in paths[0] or Path(paths[0]).suffix:
            found_files = myke.sh_stdout_lines(
                (
                    "fdfind --type f --max-depth 8 --hidden --ignore --case-sensitive"
                    f' --exclude ".git" --glob "{paths[0]}"'
                ),
            )
            if found_files:
                paths = found_files
            elif "*" in paths[0] or not Path(paths[0]).suffix:
                raise FileNotFoundError(paths[0])
        else:
            found_dirs: list[str] = myke.sh_stdout_lines(f"zoxide query '{paths[0]}'")

            if not found_dirs:
                raise FileNotFoundError(paths[0])

            if len(found_dirs) > 1:
                found_dirs = myke.sh_stdout_lines(
                    f"zoxide query --interactive '{paths[0]}'",
                )

            assert len(found_dirs) == 1
            paths[0] = str(Path(found_dirs[0]))

    work_dir: Path = (
        Path.cwd()
        if no_editor_chdir or is_stdin or not paths
        else Path(paths[0])
        if Path(paths[0]).is_dir()
        else Path(paths[0]).parent
    )

    configs_root: Path = Path(__file__).parent / "configs"

    init_cmd: list[str] = ["x-terminal-emulator", "-e"] if new_window else []
    init_kwargs: dict[str, Any] = {"stdin": sys.stdin} if is_stdin else {}

    _editor_args: list[str] = shlex.split(path_or_args) if path_or_args else []

    if (
        which_profile
        or install_plugins
        or is_stdin
        or _editor_args
        or not Path(paths[0]).is_dir()
    ):
        if not editor_profile:
            editor_profile = str(configs_root / "vym" / "vymrc")

        if which_profile:
            print(editor_profile)
            sys.exit(0)

        os.environ["VYM_PROFILE"] = editor_profile

        _editor_args += ["-u", editor_profile]

        if install_plugins:
            _editor_args.extend(["-c", "PlugUpgrade|PlugClean!|PlugUpdate"])

        init_cmd.extend([editor.replace("vym", "vim"), *_editor_args])

        if is_stdin:
            init_cmd.extend(*paths)
        else:
            init_cmd.extend(str(Path(p).relative_to(work_dir)) for p in paths)

    else:
        init_cmd.append(launcher)

        if launcher == "broot":
            if not launcher_config:
                launcher_config = str(configs_root / "broot" / "conf.hjson")

            init_cmd.extend(
                ["--sort-by-type-dirs-last", "--conf", launcher_config],
            )

    env_update: dict[str, str | None] = {
        "EDITOR": editor,
        "PYENV_VERSION": None,
    }

    home_dir: Path = Path.home()
    for k, v in {
        "XDG_CACHE_HOME": home_dir / ".cache",
        "XDG_CONFIG_HOME": home_dir / ".config",
        "XDG_DATA_HOME": home_dir / ".local" / "share",
        "XDG_STATE_HOME": home_dir / ".local" / "state",
    }.items():
        (v / "vym").mkdir(parents=True, exist_ok=True)
        env_update[k] = os.getenv(k, str(v))

    path_parent: Path = work_dir
    next_path_parent: Path = work_dir.parent
    set_pypath: bool = False
    set_pyenv: bool = False
    i = 0
    i_max = 8
    while i == 0 or (
        i < i_max and not (set_pypath and set_pyenv) and path_parent != next_path_parent
    ):
        i += 1

        if not set_pypath:
            py_src: Path = path_parent / "src"
            set_pypath = py_src.is_dir()
            if set_pypath:
                env_update["PYTHONPATH"] = str(py_src)

        if not set_pyenv:
            py_env_file: Path = path_parent / ".python-version"
            set_pyenv = py_env_file.is_file()
            if set_pyenv:
                env_update["PYENV_VERSION"] = py_env_file.read_text(
                    encoding="utf-8",
                ).strip()

        path_parent = next_path_parent
        next_path_parent = path_parent.parent

    if not set_pyenv:
        env_update["PYENV_VERSION"] = None

    kwargs: dict[str, Any] = {
        "args": " ".join(init_cmd) + " &" if new_window else init_cmd,
        "env_update": env_update,
        "cwd": str(work_dir),
        **init_kwargs,
    }

    if debug:
        print("invoking:", kwargs)

    myke.run(**kwargs, shell=new_window)


def main(extra_args: list[str] | None = None) -> None:
    args = sys.argv[1:]
    if extra_args:
        args.extend(extra_args)
    yapx.run(setup, _args=args)


def main_nvym() -> None:
    main(extra_args=["--editor", "nvim"])


def main_lvym() -> None:
    main(extra_args=["--launcher", "llama"])


if __name__ == "__main__":
    main()
