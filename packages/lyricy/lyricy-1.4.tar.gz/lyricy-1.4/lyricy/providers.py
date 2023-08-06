"""lyrics providers"""

from typing import List
from urllib.parse import quote_plus

import requests
from bs4 import BeautifulSoup

from .classes import BaseLyrics


class Megalobiz:
    """Search and scrape lyrics for Megalobiz site"""

    @staticmethod
    def search_lyrics(song_name: str) -> List[BaseLyrics]:
        """Search for lyrics"""

        results = []
        search_link = "https://www.megalobiz.com/search/all?qry="
        markup = requests.get(search_link + quote_plus(song_name)).text
        soup = BeautifulSoup(markup, "html.parser")
        required_tags = soup.find_all("a", {"class": "entity_name"})

        outer_tags = soup.findAll("div", {"class": "details"})

        inner_tags = [
            outer_tags[i].find_all("span")[-1] for i in range(0, len(outer_tags), 2)
        ]

        sample_lyrics_list = [i.text for i in inner_tags]

        for index, tag in enumerate(required_tags):
            results.append(
                BaseLyrics(
                    title=tag.get("title"),
                    link="https://www.megalobiz.com" + tag.get("href"),
                    sample_lyrics=sample_lyrics_list[index],
                    index=str(index + 1),
                )
            )

        if len(results) == 0:
            return [
                BaseLyrics(
                    title=" No result found", link="", sample_lyrics="", index="1"
                )
            ]

        return results

    @staticmethod
    def get_lyrics(link: str) -> str:
        """Scrape the lyrics for given track link"""

        markup = requests.get(link).text
        soup = BeautifulSoup(markup, "html.parser")
        return (
            soup.find("div", {"class": "lyrics_details entity_more_info"})
            .find("span")
            .text
        )


class RcLyricsBand:
    """Search and scrape lyrics for RcLyricsBand site"""

    @staticmethod
    def search_lyrics(song_name: str):
        """Search for lyrics"""

        search_link = "https://rclyricsband.com/?s="
        markup = requests.get(search_link + quote_plus(song_name)).text
        soup = BeautifulSoup(markup, "html.parser")
        outer_tags = soup.find_all("p", {"class": "elementor-post__title"})
        results = []
        for index, outer_tag in enumerate(outer_tags):
            inner_tag = outer_tag.find("a")
            results.append(
                BaseLyrics(
                    title=outer_tag.text.strip(),
                    link=inner_tag.get("href"),
                    sample_lyrics="",
                    index=str(index + 1),
                )
            )
        if len(results) == 0:
            return [
                BaseLyrics(
                    title=" No result found", link="", sample_lyrics="", index="1"
                )
            ]
        return results

    @staticmethod
    def get_lyrics(link: str):
        """Scrape the lyrics for given track link"""

        markup = requests.get(link).text
        soup = BeautifulSoup(markup, "html.parser")
        return soup.find("div", {"class": "su-box su-box-style-default"}).text
