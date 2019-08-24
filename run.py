from gmplot import gmplot
import best_aqi
# st_lat = 28.4499693
# st_long = 77.5821314
st_lat = 28.5456282
st_long = 77.2731505
distance = 20


def make_map(st_lat, st_long, distance):
    distance = int(distance)
    st_long = float(st_long)
    st_lat = float(st_lat)
    res = best_aqi.get_aqi(st_lat, st_long)

    gmap = gmplot.GoogleMapPlotter(st_lat, st_long, 13)

    points, rest = best_aqi.get_all(st_lat, st_long, distance)

    best = rest[0]
    if res[0] < best[0]:
        var = 0
    elif res[0] > best[0]:
        var = 1
    else:
        var = 2
    size = len(points)//3
    if var == 0:
        lons, lats = zip(*points[:size])
        gmap.plot(lats, lons, 'yellow', edge_width=8)
        lons, lats = zip(*points[size:(size*2)+2])
        gmap.plot(lats, lons, 'orange', edge_width=8)
        lons, lats = zip(*points[size*2:])
        gmap.plot(lats, lons, 'cornflowerblue', edge_width=8)
    st = set()
    new_rest = []
    for i in rest:
        if i[0] not in st:
            new_rest.append(i)
            st.add(i[0])
    for i in new_rest:
        gmap.marker(i[2][0], i[2][1],
                    title='AQI: {}, Pollutant: {}'.format(str(i[0]), i[1]['dom_p'].upper()))
    gmap.marker(res[2][0], res[2][1], color='green',
                title='AQI: {}, Pollutant: {}'.format(str(res[0]), res[1]['dom_p'].upper()))
    # print(rest)
    gmap.draw(
        "D:\\projects\\webdevlopment\\hackiiittest\\hackiiittest\\templates\\map.html")


make_map(st_lat, st_long, distance)
