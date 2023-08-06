# MIT License
#
# Copyright (c) 2022 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests
import logging
import json
from alertify.exception import ApiError


class Client:
    """Opsgenie Client Class"""

    def __init__(self):
        self._logging = logging.getLogger(__name__)

    def trigger_incident(
        self, api_key, message, description, priority, tags=[], details={}
    ):
        """Trigger Incident"""
        data = {
            "message": message,
            "description": description,
            "priority": priority,
            "tags": tags,
            "details": details,
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": "GenieKey " + api_key,
        }

        try:
            response = requests.post(
                "https://api.eu.opsgenie.com/v2/alerts", headers=headers, json=data
            )
        except Exception as e:
            raise ApiError("Failed to create opsgenie incident: {}".format(str(e)))

        if response.status_code // 100 != 2:
            raise ApiError(
                "Opsgenie respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return json.loads(response.content.decode("utf-8"))

    def fetch_request(self, api_key, request_id):
        """Fetch Alert With Request ID"""
        headers = {
            "Content-Type": "application/json",
            "Authorization": "GenieKey " + api_key,
        }

        try:
            response = requests.get(
                "https://api.opsgenie.com/v2/alerts/requests/{}".format(request_id),
                headers=headers,
            )
        except Exception as e:
            raise ApiError("Failed to fetch opsgenie request: {}".format(str(e)))

        if response.status_code // 100 != 2:
            raise ApiError(
                "Opsgenie respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return json.loads(response.content.decode("utf-8"))

    def resolve_incident(
        self,
        api_key,
        incident_id,
        source="Uptimedog",
        note="Action executed via Alert API",
    ):
        """Resolve Incident"""
        data = {"source": source, "note": note}

        headers = {
            "Content-Type": "application/json",
            "Authorization": "GenieKey " + api_key,
        }

        try:
            response = requests.post(
                "https://api.opsgenie.com/v2/alerts/{}/close?identifierType=id".format(
                    incident_id
                ),
                data=json.dumps(data),
                headers=headers,
            )
        except Exception as e:
            raise ApiError("Failed to close opsgenie incident: {}".format(str(e)))

        if response.status_code // 100 != 2:
            raise ApiError(
                "Opsgenie respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return json.loads(response.content.decode("utf-8"))
