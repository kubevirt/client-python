#!/usr/bin/env python3
import json
import re
from pathlib import Path


CONFIG_PATH = Path("swagger-codegen-config.json")
SETUP_PATH = Path("setup.py")


def pep440_version(version):
    match = re.match(
        r"^v?(?P<release>\d+(?:\.\d+)*)"
        r"(?:-(?P<pre>alpha|beta|rc)\.(?P<pre_number>\d+))?"
        r"(?:-(?P<distance>\d+)-g(?P<sha>[0-9a-fA-F]+))?$",
        version,
    )
    if not match:
        return version

    prerelease = {
        "alpha": "a",
        "beta": "b",
        "rc": "rc",
    }

    normalized = match.group("release")
    pre = match.group("pre")
    if pre:
        normalized += prerelease[pre] + match.group("pre_number")

    distance = match.group("distance")
    if distance:
        normalized += ".post%s+g%s" % (distance, match.group("sha").lower())

    return normalized


def main():
    with CONFIG_PATH.open() as config_file:
        generated_version = json.load(config_file)["packageVersion"]

    normalized_version = pep440_version(generated_version)
    setup_contents = SETUP_PATH.read_text()
    setup_contents, replacements = re.subn(
        r'^VERSION = ".*"$',
        'VERSION = "%s"' % normalized_version,
        setup_contents,
        count=1,
        flags=re.MULTILINE,
    )

    if replacements != 1:
        raise RuntimeError("Could not find VERSION assignment in setup.py")

    SETUP_PATH.write_text(setup_contents)
    print("Normalized setup.py version: %s -> %s" % (generated_version, normalized_version))


if __name__ == "__main__":
    main()
