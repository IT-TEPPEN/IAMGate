import requests
from src.domain.service_action.adapter import IServiceActionAdapter
from src.domain.service_action.entity import ServiceActions, ServiceAction
from .html_parser import IAMServiceActionHTMLParser


class ServiceActionAdapter(IServiceActionAdapter):
    def get_service_actions(self, url):
        """
        Retrieve service actions from the given URL.
        :param url: The URL to retrieve service actions from.
        :return: A list of service actions.
        """
        response = requests.get(url)
        response.raise_for_status()

        content = response.text

        # Extract service action page properties from the content
        service_actions = self.extract_service_actions_from_content(content)
        return service_actions

    def extract_service_actions_from_content(self, content):
        """
        Extract service action page properties from the content.
        :param content: The document site content.
        :return: A list of service action page properties.
        """

        parser = IAMServiceActionHTMLParser()
        parser.feed(content)

        service_name = parser.service_name
        service_prefix = parser.service_prefix
        actions = parser.rows

        return ServiceActions.new(
            service_prefix=service_prefix,
            service_name=service_name,
            service_actions=[
                ServiceAction.new(
                    service_prefix=service_prefix,
                    action_name=action[0]["data"],
                    action_url=action[0]["url"],
                    description=action[1]["data"],
                    access_level=action[2]["data"],
                )
                for action in actions
            ],
        )
