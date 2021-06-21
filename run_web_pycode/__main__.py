#!/usr/bin/python3
# encoding: utf-8
""" run_web_pycode 's entry_points"""
import fire


def entry_point() -> None:  # pragma: no cover
    """
    默认函数 触发fire包
    https://github.com/google/python-fire
    """
    fire.core.Display = lambda lines, out: print(*lines, file=out)
    fire.Fire(command="version")


def ipython() -> None:  # pragma: no cover
    """打开ipython命令"""
    from IPython import embed

    embed()


def version() -> str:
    """显示当前版本"""
    import run_web_pycode

    return run_web_pycode.__version__


def run(url: str) -> None:
    from run_web_pycode.core import run_remote_script

    return run_remote_script(url)


if __name__ == "__main__":
    entry_point()
