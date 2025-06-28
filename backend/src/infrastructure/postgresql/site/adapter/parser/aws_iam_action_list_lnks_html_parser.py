from html.parser import HTMLParser
from typing import Set

from src.domain.document_site.entity import DocumentSiteProperty, EDocumentType


class AwsIamActionListLinksHTMLParser(HTMLParser):
    """
    HTML parser for extracting links from AWS IAM action list pages.
    This parser is used to extract links from the HTML content of AWS IAM action list pages.
    """

    split_str: str = "#####"
    href: str | None = None
    links: Set[str] = set()

    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr in attrs:
                if attr[0] == "href" and attr[1].startswith("./list_"):
                    self.href = attr[1]

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        if self.href:
            self.links.add(f"{data}{self.split_str}{self.href}")
            self.href = None

    def get_actions_site_properties(self) -> list[DocumentSiteProperty]:
        """
        Get the AWS IAM action list URLs from the parsed HTML content.

        :param top_page_property: The top page property.
        :return: A list of AWS IAM action list URLs.
        """
        if not self.links:
            return []

        return list(
            map(
                lambda link: self.__convert_to_document_site_property(link),
                self.links,
            )
        )

    def __convert_to_document_site_property(self, link: str) -> DocumentSiteProperty:
        """
        Convert a link to a DocumentSiteProperty.

        :param link: The link to convert.
        :return: The DocumentSiteProperty.
        """
        service_name, url = link.split(self.split_str)

        if url.startswith("./"):
            url = url[2:]

        return DocumentSiteProperty.new(
            document_type=EDocumentType.アクション一覧ページ,
            description=service_name,
            url=f"https://docs.aws.amazon.com/service-authorization/latest/reference/{url}",
        )
