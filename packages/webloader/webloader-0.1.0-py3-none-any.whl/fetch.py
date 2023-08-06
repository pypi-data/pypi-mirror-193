from __future__ import annotations

import os
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple, Union

from webloader import WebLoader

MAX_WORKERS: int = 10


def load_web(
    url: str,
    metadata: bool,
    path: Union[str, os.PathLike],
    archive_assets: bool,
):
    try:
        webloader = WebLoader(url)
        webloader.save_webpage(path=path)
        if metadata:
            print(" === Metadata === ")
            print(webloader.metadata)
        if archive_assets:
            webloader.archive_assets(path)
    except Exception as err:
        print("Error fetching webpage:", url, err)


def execute(
    urls: List[str],
    metadata: bool,
    path: Union[str, os.PathLike],
    archive_assets: bool,
):
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        args: Tuple[Tuple[str, bool, str]] = (
            (url, metadata, path, archive_assets) for url in urls
        )
        [_ for _ in executor.map(lambda arg: load_web(*arg), args)]


def run():
    arg_parser = ArgumentParser(description="Python Module to Save/Load Webpage")
    arg_parser.add_argument(
        "urls",
        type=str,
        nargs="+",
        help="Enter Web URLs separated by space",
    )
    arg_parser.add_argument("--metadata", action="store_true")
    arg_parser.add_argument("--archive_assets", action="store_true")
    arg_parser.add_argument("-p", "--path", type=str, default=".")
    args = arg_parser.parse_args()
    execute(args.urls, args.metadata, args.path, args.archive_assets)


if __name__ == "__main__":
    run()
