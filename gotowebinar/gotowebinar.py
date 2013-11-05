import json
import requests

CITRIX_API_KEY = ""

class GoToWebinarAPI(object):

    host = "api.citrixonline.com"
    base_path = "/G2W/rest"
    protocol = "https"
    authorize_url = "https://api.citrixonline.com/oauth/access_token"

    def __init__(self):
        self.access_token = ""
        self.organizer_key = ""

    def authorize(self, username, password):
        params = {"grant_type":"password","user_id":username,"password":password,"client_id":CITRIX_API_KEY}
        json_data = self.send_data(url=self.authorize_url, params=params) 
        
        if not json_data.get('error', None):
            self.access_token = json_data.get('access_token')
            self.organizer_key = json_data.get('organizer_key')
            return {'access_token':self.access_token, 'organizer_key':self.organizer_key}

        return json_data

    # WEBINARS
    def get_historical_webinars(self):
        path = "/organizers/%s/historicalWebinars" % (self.organizer_key)
        json_data = self.send_data(path=path)
        return json_data

    def get_upcoming_webinars(self):
        path = "/organizers/%s/upcomingWebinars" % (self.organizer_key)
        json_data = self.send_data(path=path)
        return json_data

    def get_webinar(self, webinar_key):
        path = "/organizers/%s/webinars/%s" % (self.organizer_key, webinar_key)
        json_data = self.send_data(path=path)
        print json_data

    def get_webinar_times(self, webinar_key):
        path = "/organizers/%s/webinars/%s/meetingtimes" % (self.organizer_key, webinar_key)
        json_data = self.send_data(path=path)
        print json_data

    # REGISTRANT
    def create_registrant(self, webinar_key, registrant_data):
        path = "/organizers/%s/webinars/%s/registrants" % (self.organizer_key, webinar_key)
        json_data = self.send_data(method="POST", params=registrant_data, path=path)
        return json_data

    def send_data(self, method="GET", url="", path="", params="", headers={}):

        if not url:
            url = "%s//%s%s%s" % (self.protocol, self.host, self.base_path, path)

        headers = {"Content-type":"application/json", "Accept":"application/vnd.citrix.g2wapi-v1.1+json"}
        if self.access_token:
            headers["Authorization"] = "OAuth oauth_token=%s" % self.access_token

        if method == "POST":
            r = requests.post(url, data=json.dumps(params), headers=headers)
        else:
            r = requests.get(url, params=params, headers=headers)

        if r.status_code == 500:
            raise Exception

        return json.loads(r.text)        
