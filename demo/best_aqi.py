import requests
import json
import get_points
from haversine import haversine


def get_aqi(lat, lon):
    api_url = 'https://api.breezometer.com/air-quality/v2/current-conditions?lat=' + \
        str(lat)+'&lon='+str(lon)+'&key=fa2dfd535bfc41499843cd71dd8752d9'
    call = requests.get(api_url)
    resp = json.loads(call.text)
    dct = {}
    temp = resp['data']['indexes']['baqi']
    info = temp['aqi']
    dct['category'] = temp['category']
    dct['dom_p'] = temp['dominant_pollutant']
    return [info, dct, (lat, lon)]


def helper(coords):
    all_details = []
    for i in coords:
        tmp = get_aqi(i[0][0], i[0][1])
        all_details.append(tmp)
    return all_details


def get_coords(start_lat, start_long, end_lat, end_long):
    api_url = 'https://api.openrouteservice.org/v2/directions/foot-walking?api_key=5b3ce3597851110001cf62481884b0b76b3441aeacb2c2500759b75b&start={},{}&end={},{}'.format(
        str(start_long), str(start_lat), str(end_long), str(end_lat))
    call = requests.get(api_url)
    return json.loads(call.text)


def get_all(start_lat, start_long, distance):
    aqis = helper(get_points.get_points(start_lat, start_long, distance))
    aqis.sort(reverse=True)
    best = aqis[0][2]
    distance = haversine((start_lat, start_long), best)
    print(distance)
    res = get_coords(start_lat, start_long, best[0], best[1])
    points = res['features'][0]['geometry']['coordinates']
    return points, aqis
