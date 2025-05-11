import requests

from .parser import AwsIamActionListLinksHTMLParser

from src.domain.document_site.adapter import IDocumentSiteAdapter
from src.domain.document_site.entity import DocumentSiteContent


class DocumentSiteAdapter(IDocumentSiteAdapter):
    """
    Implementation of the document site adapter.
    """

    def __init__(self):
        self.aws_iam_actions_list_links_parser = AwsIamActionListLinksHTMLParser()

    def get_document(self, property) -> DocumentSiteContent:
        """
        Retrieve the document from the given property.

        :param property: The document site property.
        :return: The content of the document.
        """
        response = requests.get(property.url)
        response.raise_for_status()

        return DocumentSiteContent.new(
            id=property.id,
            content=response.text,
            acquired_at=property.updated_at,
        )

    def get_aws_iam_actions_page_properties(self, top_page_property):
        """
        Retrieve a list of AWS IAM action list URLs.

        :param top_page_property: The top page property.
        :return: A list of AWS IAM action list URLs.
        """
        response = requests.get(top_page_property.url)
        response.raise_for_status()

        self.aws_iam_actions_list_links_parser.feed(response.text)
        return self.aws_iam_actions_list_links_parser.get_actions_site_properties()
