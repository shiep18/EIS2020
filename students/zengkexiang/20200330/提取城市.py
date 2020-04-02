from geotext import GeoText

places = GeoText("London and Shanghai is a great city 上海")
places.cities
# "London"
print(places.cities)
# filter by country code
result = GeoText('I loved Rio de Janeiro and Havana', 'BR').cities
# 'Rio de Janeiro'

GeoText('New York, Texas, and also China').country_mentions
# OrderedDict([(u'US', 2), (u'CN', 1)])