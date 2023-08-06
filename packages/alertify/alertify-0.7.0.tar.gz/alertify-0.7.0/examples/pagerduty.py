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

from alertify.pagerduty import Client


c = Client()

routing_key = 'xxxxxxxxxxxxxxxxxxxxx'
summary = 'An issue has been detected'
source = 'Uptimedog'
severity = 'critical'
component = 'API'
group = 'Production'
class_type = 'deploy'
details = {
	'details': 'More details about the issue'
}

# Trigger Incident
r = c.trigger_incident(
	routing_key,
	summary,
	source,
	severity,
	component,
	group,
	class_type,
	details
)

# Resolve Incident
r = c.resolve_incident(
	routing_key,
	r['dedup_key'],
	summary,
	source,
	severity,
	component,
	group,
	class_type,
	details
)
