import json
import io

import requests

from . import exceptions

__all__ = ['APIClient']


class APIClient:
    """
    A client for the CareHome.co.uk API.
    """

    def __init__(self, api_key, timeout=None):
        self._api_key = api_key
        self._timeout = timeout

    def __call__(self, path, params=None):
        """Call the API"""

        # Build headers
        headers = {'Accept': 'application/json'}

        # Build the params
        params = params or {}
        params['api_key'] = self._api_key

        # Make the request
        r = requests.get(
            f'https://api.carehome.co.uk/index.cfm/{path}/',
            headers=headers,
            params=params,
            timeout=self._timeout
        )

        # Handle a successful response
        if r.status_code == 200:
            return r.json()

        # Raise an error related to the response
        try:
            error_message = r.json().get('error')[0]

        except ValueError:
            error_message = 'Unknown error'

        raise exceptions.APIException(error_message)
