#!/usr/bin/env python
# encoding: utf-8
# Created by zza on 2021/6/21 14:33
# Copyright 2021 LinkSense Technology CO,. Ltd
import requests


def run_remote_script(url: str) -> None:
    req = requests.get(url)
    code = req.text

    exec(code)  # noqa:S102
