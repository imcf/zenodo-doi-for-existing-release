#!/usr/bin/env python3
"""Simple script to force-push existing GitHub releases to Zenodo."""

import argparse
import pprint
import sys

import requests
import yaml


parser = argparse.ArgumentParser()
parser.add_argument(
    "settings",
    type=argparse.FileType("r", encoding="UTF-8"),
    help="path to a YAML settings file",
)

parsed_settings = yaml.safe_load(parser.parse_args().settings)
repo = parsed_settings["repo"]
token = parsed_settings["token"]

headers = {"Accept": "application/vnd.github.v3+json"}

repo_response = requests.get(f"https://api.github.com/repos/{repo}", headers=headers)
release_response = requests.get(
    f"https://api.github.com/repos/{repo}/releases", headers=headers
)


if len(release_response.json()) > 1:
    print("more than one release found, processing from oldest to newest...\n")

for release in reversed(release_response.json()):
    name = release["name"]
    tag_name = release["tag_name"]
    published = release["published_at"]
    print(f"{name} (tag: '{tag_name}', published {published}")

    payload = {
        "action": "published",
        "release": release,
        "repository": repo_response.json(),
    }

    submit_response = requests.post(
        f"https://zenodo.org/api/hooks/receivers/github/events/?access_token={token}",
        json=payload,
    )
    print(submit_response)
    print("\n--------\n")
