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

from alertify.opsgenie import Client

api_key = "xxxxxxxxxxxxxxxxxxxxx"
message = "SaaS monitoring detected an incident"
description = "The SaaS service is currently down."
priority = "P1"
tags = ["monitoring", "incident"]
details = {
    "service_name": "Cloud",
    "incident_time": "2023-02-19T12:00:00Z"
}

c = Client()

# Trigger Incident
o1 = c.trigger_incident(
	api_key,
	message,
	description,
	priority,
	tags,
	details
)

# Fetch Alert ID with Request ID
r1 = c.fetch_request(
	api_key,
	o1['requestId']
)

# Resolve Incident
o2 = c.resolve_incident(
	api_key,
	r1['data']['alertId']
)

# Fetch Request Status
r2 = c.fetch_request(
	api_key,
	o2['requestId']
)
