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
    """Pagerduty Client Class"""

    def __init__(self):
        self._logging = logging.getLogger(__name__)

    def trigger_incident(
        self,
        routing_key,
        summary,
        source,
        severity,
        component,
        group,
        class_type,
        details={},
    ):
        """Trigger Incident"""
        data = {
            "routing_key": routing_key,
            "event_action": "trigger",
            "payload": {
                "summary": summary,
                "source": source,
                "severity": severity,
                "component": component,
                "group": group,
                "class": class_type,
                "custom_details": details,
            },
        }

        try:
            response = requests.post(
                "https://events.pagerduty.com/v2/enqueue", json=data
            )
        except Exception as e:
            raise ApiError("Failed to create PagerDuty incident: {}".format(str(e)))

        if response.status_code // 100 != 2:
            raise ApiError(
                "PagerDuty respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return json.loads(response.content.decode("utf-8"))

    def resolve_incident(
        self,
        routing_key,
        dedup_key,
        summary,
        source,
        severity,
        component,
        group,
        class_type,
        details={},
    ):
        """Resolve Incident"""
        data = {
            "routing_key": routing_key,
            "event_action": "resolve",
            "dedup_key": dedup_key,
            "payload": {
                "summary": summary,
                "source": source,
                "severity": severity,
                "component": component,
                "group": group,
                "class": class_type,
                "custom_details": details,
            },
        }

        try:
            response = requests.post(
                "https://events.pagerduty.com/v2/enqueue", json=data
            )
        except Exception as e:
            raise ApiError("Failed to create PagerDuty incident: {}".format(str(e)))

        if response.status_code // 100 != 2:
            raise ApiError(
                "PagerDuty respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return json.loads(response.content.decode("utf-8"))
