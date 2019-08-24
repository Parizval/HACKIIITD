from haversine import haversine
from random import randint


def get_points(start_lat, start_long, distance):
    distance = (distance/2)
    tolerance = 0.1
    tp = (start_lat, start_long)
    coords = []
    reference_points = 8
    while True:
        if len(coords) >= reference_points:
            break
        else:
            diff = distance * (randint(1, 100))/(10**4)
            one = ((start_lat - diff), (start_long - diff))
            two = ((start_lat - diff), (start_long + diff))
            three = ((start_lat + diff), (start_long - diff))
            four = ((start_lat + diff), (start_long + diff))
            five = ((start_lat), (start_long + diff))
            six = ((start_lat), (start_long - diff))
            seven = ((start_lat + diff), (start_long))
            eight = ((start_lat - diff), (start_long))
            if distance*(1-tolerance) < haversine(tp, one) < distance*(1+tolerance):
                coords.append([one, haversine(tp, one)])

            if distance*(1-tolerance) < haversine(tp, two) < distance*(1+tolerance):
                coords.append([two, haversine(tp, two)])

            if distance*(1-tolerance) < haversine(tp, three) < distance*(1+tolerance):
                coords.append([three, haversine(tp, three)])

            if distance*(1-tolerance) < haversine(tp, four) < distance*(1+tolerance):
                coords.append([four, haversine(tp, four)])
            if distance*(1-tolerance) < haversine(tp, five) < distance*(1+tolerance):
                coords.append([five, haversine(tp, five)])

            if distance*(1-tolerance) < haversine(tp, six) < distance*(1+tolerance):
                coords.append([six, haversine(tp, six)])

            if distance*(1-tolerance) < haversine(tp, seven) < distance*(1+tolerance):
                coords.append([seven, haversine(tp, seven)])

            if distance*(1-tolerance) < haversine(tp, eight) < distance*(1+tolerance):
                coords.append([eight, haversine(tp, eight)])
    distance /= 2
    while True:
        if len(coords) >= 2 * reference_points:
            break
        else:
            diff = distance * (randint(1, 100))/(10**4)
            one = ((start_lat - diff), (start_long - diff))
            two = ((start_lat - diff), (start_long + diff))
            three = ((start_lat + diff), (start_long - diff))
            four = ((start_lat + diff), (start_long + diff))
            five = ((start_lat), (start_long + diff))
            six = ((start_lat), (start_long - diff))
            seven = ((start_lat + diff), (start_long))
            eight = ((start_lat - diff), (start_long))
            if distance*(1-tolerance) < haversine(tp, one) < distance*(1+tolerance):
                coords.append([one, haversine(tp, one)])

            if distance*(1-tolerance) < haversine(tp, two) < distance*(1+tolerance):
                coords.append([two, haversine(tp, two)])

            if distance*(1-tolerance) < haversine(tp, three) < distance*(1+tolerance):
                coords.append([three, haversine(tp, three)])

            if distance*(1-tolerance) < haversine(tp, four) < distance*(1+tolerance):
                coords.append([four, haversine(tp, four)])

            if distance*(1-tolerance) < haversine(tp, five) < distance*(1+tolerance):
                coords.append([five, haversine(tp, five)])

            if distance*(1-tolerance) < haversine(tp, six) < distance*(1+tolerance):
                coords.append([six, haversine(tp, six)])

            if distance*(1-tolerance) < haversine(tp, seven) < distance*(1+tolerance):
                coords.append([seven, haversine(tp, seven)])
    
            if distance*(1-tolerance) < haversine(tp, eight) < distance*(1+tolerance):
                coords.append([eight, haversine(tp, eight)])
    return coords
