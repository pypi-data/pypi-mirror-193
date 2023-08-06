#!/usr/bin/env python
# encoding: utf-8
__author__ = 'l9h8'
__time__ = '2020/9/3 5:02 PM'

import os

import yaml

from CommonzZ.singleton import Singleton


class Config(Singleton):
    def __init__(self):
        self.config_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.ini")

    def get(self, key=None):
        with open(self.config_file, "r") as f:
            config = yaml.safe_load(f.read())
        if key:
            config = config[key]

        return config


__all__ = ["Config"]
