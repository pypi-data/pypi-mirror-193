"""Ocifacts provides an easy means of storing artifacts in OCI registries"""

from enum import Enum
import os
import json
import shutil
import subprocess
import tempfile
from typing import List, Optional, Dict, Union
from os import listdir
from os.path import isfile, join


imgpkg_relpath = os.path.dirname(__file__)
imgpkg_abspath = os.path.abspath(imgpkg_relpath)
BIN_PATHNAME = os.path.join(imgpkg_abspath, "bin/imgpkg")


class ObjEncoderType(Enum):
    """Encoder to use to encode python objects for storage"""

    PICKLE = "pickle"
    JSON_PICKLE = "json_pickle"


def push(
    uri: str,
    filepath: Optional[Union[str, List[str]]] = None,
    labels: Optional[Dict[str, str]] = None,
) -> None:
    """Push data to repository

    Args:
        uri (str): URI of the repository
        filepath (Optional[str | List[str]], optional): Filepath(s) to push. Defaults to None.
        labels (Optional[Dict[str, str]], optional): Labels to add to the artifact. Defaults to None.

    Raises:
        ValueError: If one of file, obj, or obj_map is not provided
    """

    args = [
        BIN_PATHNAME,
        "push",
        "-i",
        uri,
    ]
    fps = []

    temp_dir = ""
    if filepath is not None:
        if isinstance(filepath, str):
            fps = [filepath]
        else:
            fps = filepath

    if len(fps) == 0:
        raise ValueError("Nothing to upload. Must provide one of file, obj, or obj_map")

    for filepath in fps:
        args.append("-f")
        args.append(filepath)

    if labels is not None:
        for k, v in labels.items():
            args.append("-l")
            args.append(f'{k}={v}')

    try:
        subprocess.run(
            args=args,
            capture_output=True,
            check=True,
            text=True,
        )
    except subprocess.CalledProcessError as err:
        print(err.output)
        print(err.stderr)
        print(err.stdout)
        raise err

    if temp_dir != "":
        shutil.rmtree(temp_dir, ignore_errors=True)


def pull(uri: str, out_path: str) -> List[str]:
    """Pull files from registry

    Args:
        uri (str): URI of artifact to pull
        out_path (str): Directory to put files in

    Returns:
        List[str]: List of filepaths of artifacts
    """

    args = [
        BIN_PATHNAME,
        "pull",
        "-i",
        uri,
        "-o",
        out_path,
    ]

    try:
        subprocess.run(
            args=args,
            capture_output=True,
            check=True,
            text=True,
        )
    except subprocess.CalledProcessError as err:
        print(err.output)
        print(err.stderr)
        print(err.stdout)
        raise err

    filepaths = [f for f in listdir(out_path) if isfile(join(out_path, f))]
    return filepaths


def pull_str(uri: str) -> Dict[str, str]:
    """Pull files from registry as strings

    Args:
        uri (str): URI of the artifact

    Returns:
        Dict[str, str]: A map of filename to file text
    """
    with tempfile.TemporaryDirectory() as out_path:
        args = [
            BIN_PATHNAME,
            "pull",
            "-i",
            uri,
            "-o",
            out_path,
        ]

        try:
            subprocess.run(
                args=args,
                capture_output=True,
                check=True,
                text=True,
            )
        except subprocess.CalledProcessError as err:
            print(err.output)
            raise err

        str_files = {}
        for f in listdir(out_path):
            filepath = join(out_path, f)
            if isfile(filepath):
                with open(filepath, "r", encoding="UTF-8") as fr:
                    str_files[f] = fr.read()

        return str_files


def pull_bytes(uri: str) -> Dict[str, bytes]:
    """Pull files from registry as bytes

    Args:
        uri (str): URI of the artifact

    Returns:
        Dict[str, bytes]: A map of filename to file bytes
    """
    with tempfile.TemporaryDirectory() as out_path:
        args = [
            BIN_PATHNAME,
            "pull",
            "-i",
            uri,
            "-o",
            out_path,
        ]

        try:
            subprocess.run(
                args=args,
                capture_output=True,
                check=True,
                text=True,
            )
        except subprocess.CalledProcessError as err:
            print(err.output)
            raise err

        byte_files = {}
        for f in listdir(out_path):
            filepath = join(out_path, f)
            if isfile(filepath):
                with open(filepath, "rb") as fr:
                    byte_files[f] = fr.read()

        return byte_files


# TODO: auto push; detect repo and python project
