import requests
import json

class GetRequester:
    '''
    A class for making HTTP GET requests to APIs and processing JSON responses.

    This class provides a simple interface to:
    - Make GET requests to a specified URL
    - Retrieve the raw response body
    - Parse JSON responses into Python data structures
    '''

    def __init__(self, url):
        '''
        Initialize a GetRequester instance with a target URL.

        Args:
            url (str): The URL to send GET requests to
        '''
        self.url = url

    def get_response_body(self):
        '''
        Send a GET request to the URL and return the raw response body.

        Returns:
            str: The raw response body as bytes
        '''
        # Make a GET request to the specified URL
        response = requests.get(self.url)

        # Return the raw content (as bytes)
        return response.content

    def load_json(self):
        '''
        Get the response from the URL and parse it as JSON.

        Returns:
            dict/list: The parsed JSON response data as Python objects
        '''
        # Get the raw response content
        response_body = self.get_response_body()

        # Parse the JSON content into Python objects
        return json.loads(response_body)