import os.path
import json
from weatherData import WeatherData
from datetime import datetime

if __name__ == '__main__':

    weatherInfo = []
    running = True
    while running:

        n = input('Please enter the name of the weather file to be processed: ')
        if not(os.path.exists(n)):
            print('\nSorry, but that file does not exist.\n')

        elif('tempData2015' not in n) and ('tempData2017' not in n):
            print('\nPlease enter a valid weather data file.\n')

        else:
            with open(n, 'r') as f:
                data = f.readlines()
            f.closed

            for i, item in enumerate(data):
                items = item.split()
                locationRep = items[6].replace('_', ' ')
                weatherInfo.append(WeatherData(int(items[0]), int(items[1]), int(items[2]), int(items[3]), int(items[4]), items[5], locationRep))

            number_of_stations = len(weatherInfo) / 31

            year = 2015 if n == 'tempData2015.txt' else 2017
            loc = ''
            date = 0
            stat = ''

            # Find the maximum temperature
            print("1. What is the maximum temperature reported by any of the WBAN's during August %d?" % year)
            maximum = 0

            for i, item in enumerate(weatherInfo):
                if item.t_max > maximum:
                    maximum = item.t_max
                    loc = item.location
                    date = item.year_month_day
                    convertDate = str(date)
                    dateFormat = datetime(year=int(convertDate[0:4]), month=int(convertDate[4:6]), day=int(convertDate[6:8]))
                    ymdDate = dateFormat.strftime("%B %d, %Y")
                    stat = item.station

            print(f'The max temperature recorded in August {year} was {maximum} on {ymdDate} at {stat} in {loc}. \n')

            # Find the minimum temperature
            print("2. What is the minimum temperature reported by any of the WBAN's during August %d?" % year)
            minimum = 100000000

            for i, item in enumerate(weatherInfo):
                if item.t_min < minimum:
                    minimum = item.t_min
                    loc = item.location
                    date = item.year_month_day
                    convertDate = str(date)
                    dateFormat = datetime(year=int(convertDate[0:4]), month=int(convertDate[4:6]), day=int(convertDate[6:8]))
                    ymdDate = dateFormat.strftime("%B %d, %Y")
                    stat = item.station

            print(f'The min temperature recorded in August {year} was {minimum} on {ymdDate} at {stat} in {loc}. \n')

            # Find the average temperature
            print("3. What is the average average temperature for all 25 reporting stations in August?")
            average = 0
            count = 0
            total_t_avg = 0

            for i, item in enumerate(weatherInfo):
                count += 1
                total_t_avg += item.t_avg

            average = total_t_avg / count
            convertedAv = int(average)

            print(f'The average temperature recorded in August {year} was {convertedAv}. \n')

            # Find the hottest day
            print("4. What was the hottest day in Pennsylvania in August %d?" % year)
            current_max_station = 1
            total_t_max = 0
            t_max_average = 0
            t_max_date = 0
            t_max_station = ""
            t_max_location = ""

            for i, item in enumerate(weatherInfo):
                total_t_max += item.t_max
                if current_max_station == int(number_of_stations):
                    if int(total_t_max / int(number_of_stations)) > t_max_average:
                        t_max_average = total_t_max / int(number_of_stations)
                        t_max_date = item.year_month_day
                        convertDate = str(t_max_date)
                        dateFormat = datetime(year=int(convertDate[0:4]), month=int(convertDate[4:6]), day=int(convertDate[6:8]))
                        ymdDate = dateFormat.strftime("%B %d, %Y")
                        t_max_station = item.station
                        t_max_location = item.location

                current_max_station += 1
            convertedTMaxAv = int(t_max_average)

            print(f'The hottest day in August {year} was {convertedTMaxAv} on {ymdDate} at {t_max_station} in {t_max_location}. \n')

            # Find the coldest day
            print("5. What was the coldest day in Pennyslvania in August %d?" % year)
            current_min_station = 1
            total_t_min = 0
            t_min_average = 100000000
            t_min_date = 0
            t_min_station = ""
            t_min_location = ""

            for i, item in enumerate(weatherInfo):
                total_t_min += item.t_min
                if current_min_station == int(number_of_stations):
                    if int(total_t_min / int(number_of_stations)) < t_min_average:
                        t_min_average = total_t_min / int(number_of_stations)
                        t_min_date = item.year_month_day
                        convertDate = str(t_min_date)
                        dateFormat = datetime(year=int(convertDate[0:4]), month=int(convertDate[4:6]), day=int(convertDate[6:8]))
                        ymdDate = dateFormat.strftime("%B %d, %Y")
                        t_min_station = item.station
                        t_min_location = item.location

                current_min_station += 1
            convertedTMinAv = int(t_min_average)

            print(f'The coldest day in August {year} was {convertedTMinAv} on {ymdDate} at {t_min_station} in {t_min_location}. \n')

            running = False
