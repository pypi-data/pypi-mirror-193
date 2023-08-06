#COOLMAP ROUTE PATH ESTIMATION


Instructions

from cool_mapMapboxRoute.route_mapbox import CoolmapRoutePath


obj = CoolmapRoutePath("34.01076,-117.44858","33.94559,-118.18381")

#to get the path of route
obj.get_mapbox_response()

#return estimated time of route
obj.estimated_time_in_minute()

#return estimated distance of route
obj.estimated_distance_in_mile























