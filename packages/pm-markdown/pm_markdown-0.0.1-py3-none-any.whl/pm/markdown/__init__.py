from collections import UserList
from dataclasses import dataclass
try:
    from functools import cached_property
except ImportError:
    from cached_property import cached_property
import re


BLOCK_LINE_RE = re.compile(r"""
    (?P<code> ```(?P<style> \S* )(?P<flags> .*)?\n )
    |
    (?P<comment> <!--- \s* (?P<comment_text> .*? ) \s* -->\n )
    |
    (?P<text> .*\n )
""", flags=re.VERBOSE)


@dataclass
class Link:
    text: str = ""
    anchor: str = ""
    url: str = ""
    hover: str = ""

    open1_re = re.compile(r"""
        \[ (?P<text> .+? ) \]
        \[ (?P<anchor> [\w\s!.-]+? ) \]
    """, flags=re.VERBOSE)
    open2_re = re.compile(r"""
        \[ (?P<text> (?P<anchor> .[^]\n]+? ) ) \]
        \[\]
    """, flags=re.VERBOSE)
    close_re = re.compile(r"""
        ^
        \[ (?P<anchor> .+? ) \]:
        \s+
        (?P<url> https?://.+ )
        $
    """, flags=re.MULTILINE | re.VERBOSE)
    link_re = re.compile(r"""
        \[ (?P<text> .* ) \]
        \(
        (?P<url> https?://[^\s]+[^)] )
        (?: \s+ " (?P<hover> .* ) " )?
        \)
    """, flags=re.MULTILINE | re.VERBOSE)

    def __post_init__(self):
        self.anchor = self.anchor.casefold()


class MarkdownBlocks(UserList):

    @cached_property
    def text_blocks(self):
        return MarkdownBlocks(
            block
            for block in self
            if isinstance(block, Text)
        )

    @cached_property
    def code_blocks(self):
        return MarkdownBlocks(
            block
            for block in self
            if isinstance(block, Code)
        )

    @cached_property
    def start_anchors(self):
        return [
            link
            for block in self.text_blocks
            for link in block.start_anchors
        ]

    @cached_property
    def end_anchors(self):
        return [
            link
            for block in self.text_blocks
            for link in block.end_anchors
        ]

    @cached_property
    def inline_links(self):
        return [
            link
            for block in self.text_blocks
            for link in block.inline_links
        ]

    @cached_property
    def links(self):
        links = self.inline_links
        starts = self.start_anchors
        anchors = {
            link.anchor: link
            for link in self.end_anchors
        }
        for link in starts:
            if link.anchor in anchors:
                link.url = anchors[link.anchor].url
                links.append(link)
        return links


@dataclass
class Text:
    text: str
    line: int

    @cached_property
    def parts(self):
        if self.text.count("`") % 2 == 1:
            raise ValueError(f"[Line {self.line}] Unclosed backtick in block")
        parts = [""]
        in_code = False
        in_link = False
        escaped = False
        for char in self.text:
            if escaped:
                parts[-1] += char
            elif not in_link and char == "`":
                if in_code:
                    parts[-1] += char
                    in_code = False
                    parts.append("")
                else:
                    parts.append(char)
                    in_code = True
            elif not in_code and char == "[":
                if in_link:
                    parts[-1] += char
                else:
                    parts.append(char)
                    in_link = True
            elif char == "]":
                parts[-1] += char
                if in_link and parts[-1].count("]") == 2:
                    in_link = False
                    parts.append("")
            elif char == ":" and in_link and parts[-1].endswith("]"):
                parts[-1] += char
                in_link = False
            elif char == ")":
                parts[-1] += char
                if (in_link
                        and parts[-1].count("[") - parts[-1].count("]") == 0
                        and parts[-1].count("(") - parts[-1].count(")") == 0):
                    in_link = False
                    parts.append("")
            elif not in_code and char == "\\":
                parts[-1] += char
                escaped = True
            elif char == "\n" and not in_code and not in_link:
                parts[-1] += char
                parts.append("")
            else:
                parts[-1] += char
        if parts[-1] == "":
            parts.pop()
        return parts

    @cached_property
    def start_anchors(self):
        links = []
        for part in self.parts:
            match = Link.open1_re.fullmatch(part)
            if match:
                links.append(Link(**match.groupdict()))
            else:
                match = Link.open2_re.fullmatch(part)
                if match:
                    links.append(Link(**match.groupdict()))
        return links

    @cached_property
    def end_anchors(self):
        links = []
        for match in Link.close_re.finditer(self.text):
            links.append(Link(**match.groupdict()))
        return links

    @cached_property
    def inline_links(self):
        links = []
        for part in self.parts:
            match = Link.link_re.fullmatch(part)
            if match:
                links.append(Link(**match.groupdict()))
        return links


@dataclass
class Comment:
    text: str
    line: int


@dataclass
class Code:
    style: str
    flags: str
    text: str
    line: int


def parse(markdown):
    """Return information about each atomic block of code."""
    lines = [0] + [
        m.start() + 1
        for m in re.finditer(r"\n", markdown)
    ]
    def find_line(index):
        for n, line_start in enumerate(lines, start=1):
            if index < line_start:
                return n-1
    raw_blocks = BLOCK_LINE_RE.finditer(markdown)
    blocks = MarkdownBlocks()
    in_code_block = False
    code_block_text = ""
    for n, match in enumerate(raw_blocks):
        kind = match.lastgroup
        line_number = find_line(match.start())
        if in_code_block:
            if kind == "code":
                style = match.group("style")
                flags = match.group("flags")
                if style or flags:
                    raise ValueError(
                        f"[Line {line_number}] End code block "
                        f"with extras: {style} {flags}"
                    )
                blocks[-1].text = code_block_text
                in_code_block = False
            else:
                code_block_text += match.group()
        elif kind == "code":
            code_block_text = ""
            blocks.append(Code(
                match.group("style"),
                match.group("flags"),
                "",
                line=line_number,
            ))
            in_code_block = True
        elif kind == "comment":
            blocks.append(
                Comment(match.group("comment_text"), line=line_number)
            )
        else:
            if blocks and isinstance(blocks[-1], Text):
                blocks[-1].text += match.group("text")
            else:
                blocks.append(Text(match.group("text"), line=line_number))
    return blocks
