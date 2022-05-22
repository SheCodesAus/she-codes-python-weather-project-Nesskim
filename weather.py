import csv
from datetime import datetime
from encodings import utf_8
import statistics


DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"

def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    convert_date = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z") 
    convert_date =  datetime.strftime(convert_date, "%A %d %B %Y") 
    return convert_date   


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_c = round(((float(temp_in_farenheit) - 32) * 5 / 9),1) 
    return temp_c


def calculate_mean(weather_data):
    weather_list = []
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    for weather in weather_data:
        weather = float(weather)
        weather_list.append(weather) 
        calculate_mean = statistics.mean(weather_list)
    return calculate_mean

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """   

    weather_data = []

    with open(csv_file, encoding="utf-8") as csv_file: 
        file_reader = csv.reader(csv_file, delimiter = ",")
        next(file_reader)
        for line in file_reader: 
            if line:
                weather_data.append([line[0],float(line[1]),float((line[2]))])      
    return weather_data


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if weather_data == []: #if list is empty
        return() #skip
    else: #if list has content
        min_val = float(weather_data[0]) 
        for i in range(0,len(weather_data),1): 
            if min_val >= float(weather_data[i]): 
                min_val = min(min_val, float(weather_data[i])) 
                min_index = i 
    return min_val, min_index
    

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []: 
        return() 
    else: 
        max_val = float(weather_data[0]) 
        for i in range(0,len(weather_data),1): 
            if max_val <= float(weather_data[i]): 
                max_val = max(max_val, float(weather_data[i])) 
                max_index = i 
    return max_val, max_index


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    # weather_data = load_data_from_csv("tests/data/example_two.csv")
    days = len(weather_data)
    lowest_record = [min[1] for min in weather_data] 
    highest_record = [max[2] for max in weather_data]
    dates = [date[0] for date in weather_data]

    lowest_temp =  format_temperature(convert_f_to_c(find_min(lowest_record)[0])) 
    highest_temp = format_temperature(convert_f_to_c(find_max(highest_record)[0]))
    lowest_date = convert_date(dates[find_min(lowest_record)[1]])
    highest_date = convert_date(dates[find_max(highest_record)[1]])

    avg_low = format_temperature(convert_f_to_c(calculate_mean(lowest_record)))
    avg_high = format_temperature(convert_f_to_c(calculate_mean(highest_record)))

   
   
    # print(f" highest_temp: {highest_temp}")
    # print(f" lowest_temp: {lowest_temp}")
    # print(f" avg high: {avg_high}")
    # print(f" avg low: {avg_low}")


    return f"{days} Day Overview\n  The lowest temperature will be {lowest_temp}, and will occur on {lowest_date}.\n  The highest temperature will be {highest_temp}, and will occur on {highest_date}.\n  The average low this week is {avg_low}.\n  The average high this week is {avg_high}.\n"

# print(generate_summary(weather_data))


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    weather_data = load_data_from_csv("tests/data/example_one.csv")
    daily_list = []


    for data in weather_data:
        day = convert_date(data[0])
        min_temp = format_temperature(convert_f_to_c(data[1]))
        max_temp = format_temperature(convert_f_to_c(data[2]))
        daily_forecast = f"---- {day} ----\n  Minimum Temperature: {min_temp}\n  Maximum Temperature: {max_temp}\n\n"
        daily_list.append(daily_forecast)
    return "".join(daily_list) 

