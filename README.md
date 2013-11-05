# python-citrix
A Python client for the Citrix ( GoToMeeting, GoToWebinar, etc. ) APIs.

## Requires
- requests

## Authentication
The Citrix API uses the Direct Login method for authentication. See the docs for more information: https://developer.citrixonline.com/page/authentication-and-authorization

## Usage
```python

import gotowebinar

# Authorize
webinar = GoToWebinarAPI()
webinar.authorize("username","p@$$w0rD")

# Get Webinars
webinar.get_upcoming_webinars()

# Register User
registrant = {"firstName":"Zach", "lastName":"Holmquist", "email":"zholmquist@gmail.com", "organization":"Ender Labs"}
webinar.create_registrant("webinar_key", registrant)

```