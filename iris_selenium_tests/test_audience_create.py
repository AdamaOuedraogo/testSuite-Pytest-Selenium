# -*- coding: utf-8 -*-
import pytest
import time

from fixtures import login, get_driver, audience_create


def test_create_an_audience(get_driver, login, audience_create):
    audience_name = audience_create()