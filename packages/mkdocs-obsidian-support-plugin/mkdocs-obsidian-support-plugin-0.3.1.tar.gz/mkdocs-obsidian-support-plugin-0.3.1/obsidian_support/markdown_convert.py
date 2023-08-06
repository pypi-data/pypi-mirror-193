import re

from obsidian_support.abstract_conversion import AbstractConversion
from obsidian_support.markdown_code_extract import EXCLUDE_RANGES

"""
A template method that applies conversion for every regex matches 
"""


def markdown_convert(markdown: str, conversion: AbstractConversion,
                     exclude_indices_pairs: EXCLUDE_RANGES) -> str:
    converted_markdown = ""
    index = 0
    for obsidian_syntax in re.finditer(conversion.obsidian_regex, markdown):
        ## found range of markdown where the obsidian_regex matches
        start = obsidian_syntax.start()
        end = obsidian_syntax.end()

        ## continue if match is in excluded range
        if __is_excluded(start, end, exclude_indices_pairs):
            continue

        syntax_groups = list(map(lambda group: obsidian_syntax.group(group), conversion.obsidian_regex_groups))

        mkdocs_syntax = conversion.convert(syntax_groups) + "\n"
        converted_markdown += markdown[index:start]
        converted_markdown += mkdocs_syntax
        index = end + 1

    converted_markdown += markdown[index:len(markdown)]
    return converted_markdown


def __is_excluded(start: int, end: int, exclude_indices_pairs: EXCLUDE_RANGES) -> bool:
    for exclude_indices_pair in exclude_indices_pairs:
        if exclude_indices_pair[0] < start and end < exclude_indices_pair[1]:
            return True
    return False
