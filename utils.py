#! /usr/bin/env python3

import json
import os
import sys


def process(entries):
    """ Recursively create a hierarchical file tree from a dictionary of nested entries.
        The structure of the tree can include both directories, files and symlinks.

        Args:
          - entries: a dictionary representing the tree hierarchy, which is loaded from a json file
            whose content was written by a `tree -J -a --noreport > autogen-tree.json` shell command
        Usage:
            if __name__ == "__main__":
                with open(sys.argv[1]) as f:
                    entries = json.load(f)
                    process(entries)
    """
    for entry in entries:
        if entry["type"] == "directory":
            os.makedirs(entry["name"], exist_ok=True)
            os.chdir(entry["name"])
            process(entry.get("contents", []))
            os.chdir('..')
        elif entry["type"] == "file":
            with open(entry["name"], "w"): pass
        elif entry["type"] == "link":
            os.symlink(entry["name"], entry["target"])


if __name__ == "__main__":
    pass
