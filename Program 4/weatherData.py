"""Class that contains information on each piece of weather data"""
class WeatherData:

    def __init__(self, wban, year_month_day, t_max, t_min, t_avg, station, location):
        self.wban = wban
        self.year_month_day = year_month_day
        self.t_max = t_max
        self.t_min = t_min
        self.t_avg = t_avg
        self.station = station
        self.location = location
