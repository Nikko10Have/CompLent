from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

stations = build_station_list()
incon = inconsistent_typical_range_stations(stations)

incon_Names = []
for stat in incon:
    incon_Names.append(stat.name)

incon_Names.sort()

print(incon_Names)
