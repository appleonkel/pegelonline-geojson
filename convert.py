import geojson


def to_feature(station):
    if 'latitude' in station and 'longitude' in station:
        my_point = geojson.Point(
                (station.pop('latitude'), station.pop('longitude'))
        )
        my_feature = geojson.Feature(geometry=my_point)
        my_feature['properties'] = station
        return my_feature


def to_collection(stations):
    features = []
    for i in stations:
        features.append(to_feature(i))
    return geojson.FeatureCollection(features)
