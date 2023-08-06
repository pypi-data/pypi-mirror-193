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
from alertify.exception import ApiError


class Client:
    """Client Class"""

    def __init__(self):
        self._logging = logging.getLogger(__name__)

    def send_sms(self, sendgrid_api_key, from_phone, to_phone, message):
        payload = {
            "api_user": sendgrid_api_key,
            "api_key": sendgrid_api_key,
            "from": from_phone,
            "to": to_phone,
            "text": message,
        }

        try:
            response = requests.post("https://api.sendgrid.com/v1/sms/send", data=data)
        except Exception as e:
            raise ApiError("Failed to send SMS: {}".format(str(e)))

        if response.status_code // 100 != 2:
            raise ApiError(
                "Sendgrid respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return True

    def send_text_email(self, sendgrid_api_key, from_email, to_email, subject, body):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + sendgrid_api_key,
        }

        payload = {
            "personalizations": [{"to": [{"email": to_email}], "subject": subject}],
            "from": {"email": from_email},
            "content": [{"type": "text/plain", "value": body}],
        }

        try:
            response = requests.post(
                "https://api.sendgrid.com/v3/mail/send", headers=headers, json=payload
            )
        except Exception as e:
            raise ApiError("Failed to send Email: {}".format(str(e)))

        if response.status_code // 100 != 2:
            raise ApiError(
                "Sendgrid respond with invalid status code {}".format(
                    response.status_code
                )
            )

        return True
