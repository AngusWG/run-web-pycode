#!/usr/bin/python3
# encoding: utf-8

"""
test_run_web_pycode
----------------------------------

Tests for `run_web_pycode` module.
"""
import pytest

import run_web_pycode


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get("https://github.com/audreyr/cookiecutter-pypackage")


class TestRun_web_pycode:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_something(self, benchmark):
        assert run_web_pycode.__version__
        from run_web_pycode import __main__

        # assert cost time
        benchmark(__main__.version)
        assert benchmark.stats.stats.max < 0.01
