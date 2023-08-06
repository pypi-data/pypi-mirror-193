""" WebLoader """
from __future__ import annotations

import os
from datetime import datetime
from pathlib import Path
from typing import Any, List, Optional, Set, Union
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from requests.models import Response

from .constants import ALLOW_VERIFICATION, BS4_HTML_PARSER
from .models import Url


class WebLoader:
    """Load a Webpage into Local Directory"""

    def __init__(self, url: str, parser_type: Optional[str] = BS4_HTML_PARSER) -> None:
        """Initialzes required attributes for WebLoader
        Args:
            url (str): Web Url to be loaded
            parser_type (Optional[str]): Defaults to BS4_HTML_PARSER.
        """
        self.url: Url = Url(link=url)
        self.webpage: str = self.load_webpage()
        self.soup = BeautifulSoup(self.webpage, parser_type)
        self.fetch_time = datetime.utcnow()

    def __str__(self) -> str:
        """String representation of Webloder"""
        return f"<WebLoader: {self.url.link}>"

    @property
    def images(self) -> List[Tag]:
        """Gets Tags related to images
        Returns:
            List[Tag]: List of Tags
        """
        return self.soup.findAll("img")

    @property
    def links(self) -> List[Tag]:
        """Finds Tags related to links
        Returns:
            List[Tag]: List of Tags
        """
        return self.soup.findAll("a")

    @property
    def scripts(self) -> List[Tag]:
        """Finds Tags related to scripts
        Returns:
            List[Tag]: List of Tags
        """
        return self.soup.findAll("script")

    @property
    def metadata(self) -> str:
        """
        Makes metadata for the loaded webpage
        Returns:
            str: metadata
        """
        return (
            f"site: {self.url.site}\n"
            + f"num_links: {len(self.links)}\n"
            + f"images: {len(self.images)}\n"
            + f"last_fetch: {self.fetch_time.strftime('%a %B %d %Y %H:%M UTC')}\n"
        )

    def load_webpage(self) -> str:
        """
        Load webpage
        Returns:
            str: String representation for response
        """
        response: Response = requests.get(self.url.link, verify=ALLOW_VERIFICATION)
        response.raise_for_status()
        return response.content

    def save_webpage(
        self,
        content: Optional[bytes] = None,
        filename: Optional[str] = None,
        path: Union[str, os.PathLike] = ".",
        extend_dir: Optional[bool] = False,
    ) -> str:
        """
        Save webpage to local disk
        Args:
            content (Optional[bytes], optional): Content to written to a file. Defaults to None.
            filename (Optional[str], optional): Name of file. Defaults to None.
            path (Union[str, os.PathLike], optional): Path where file will be written. Defaults to ".".
            extend_dir (Optional[bool], optional): True if we want to create a addition directory for saving assets. Defaults to False.
        Returns:
            str: Filepath
        """
        directory: str = path if not extend_dir else os.path.join(path, self.url.site)
        _ = Path(directory).mkdir(parents=True, exist_ok=True)

        file_content = content if content else self.webpage
        filepath: str = (
            os.path.join(directory, filename)
            if filename
            else os.path.join(directory, self.url.site + ".html")
        )
        with open(filepath, "wb") as f:
            f.write(file_content)
            f.close()
        return filepath

    @staticmethod
    def get_assets_from_tag(tag: Tag) -> str:
        """Fetches asset url from Tag"""
        if src := tag.get("src"):
            return src
        elif (
            tag.name == "link"
            and tag.has_attr("href")
            and tag["rel"][0].lower() == "stylesheet"
        ):
            return tag["href"]

    def archive_assets(self, path: Union[str, os.PathLike] = ".") -> None:
        """
        Archive assets to local disk
        Args:
            path (Union[str, os.PathLike], optional): Path to store asset. Defaults to ".".
        """
        assets: Set[Any] = set()
        for tag in self.images + self.scripts + self.links:
            if asset := WebLoader.get_assets_from_tag(tag):
                assets.add(asset)

        for asset_url in assets:
            try:
                if not asset_url.startswith("http") and not asset_url.startswith("//"):
                    asset_url = urljoin(self.url.link, asset_url)
                response: Response = requests.get(asset_url)
                response.raise_for_status()
                self.save_webpage(
                    content=response.content,
                    filename=os.path.basename(urlparse(asset_url).path),
                    path=path,
                    extend_dir=True,
                )
            except:
                continue
