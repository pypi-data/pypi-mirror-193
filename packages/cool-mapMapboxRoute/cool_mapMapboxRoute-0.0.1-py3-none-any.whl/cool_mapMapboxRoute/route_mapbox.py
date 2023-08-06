import requests,json

class CoolmapRoutePath():

    POOL_RECYCLE=1
    MAPBOX_API_PUBLIC_KEY="pk.eyJ1IjoiYWdnZGlyZWN0IiwiYSI6ImNqcW9lamRoMjAweGkzeHFlcGcwdHdlcmQifQ.Lxh5XIOkWFRqIE9hgR0RaA"
    MAX_OVERFLOW=-1
    headers = {'Content-Type': 'application/json', 'Authorization': ''}
    def __init__(self, from_lat_log,to_lat_log ):
        self.from_lat_log = from_lat_log
        self.to_lat_log = to_lat_log

    @classmethod
    def estimated_time_in_minute(cls, resp):
        return f"{str(round((resp['trip']['summary']['time'] * 0.0166667), 2))} Minutes"

    @classmethod
    def estimated_distance_in_mile(cls, resp):
        return f"{str(round(resp['trip']['summary']['length'] * 0.621371, 2))} Miles"

    def get_mapbox_response(self):
        from_lat_log=self.from_lat_log.split(",")
        to_lat_log=self.to_lat_log.split(",")
        from_lat = from_lat_log[0]
        from_lon = from_lat_log[1]
        to_lat = to_lat_log[0]
        to_lon = to_lat_log[1]
        param = {
                "locations":[
                            {
                                "lat": float(from_lat),
                                "lon": float(from_lon)
                            }, 
                            {
                                "lat": to_lat,
                                "lon": to_lon,
                            }
                            ],
                "costing": "truck",
                "costing_options": {
                                    "truck": {
                                                "height": 3.66,
                                                "width": "2.6",
                                                "length": "21.64",
                                                "axle_load": "18.07",
                                                "hazmat": False
                                            }
                                    }
                }

        return requests.get('https://api.mapbox.com/valhalla/v1/route?json={0}&access_token={1}'.format(json.dumps(param), self.MAPBOX_API_PUBLIC_KEY), headers=self.headers).json()