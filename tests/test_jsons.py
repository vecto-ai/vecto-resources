"""Tests for corpus module."""

import unittest
import json
import os


def get_entries():
    rootDir = './resources'
    for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
        for fname in fileList:
            yield(os.path.join(dirName, fname))


def load_json(path):
    f = open(path)
    s_data = f.read()
    data = json.loads(s_data)
    f.close()
    return data


class Tests(unittest.TestCase):

    def test_jsons(self):
        for f in get_entries():
            data = load_json(f)
        unittest.assertIsInstance(data, dict, msg=None)
