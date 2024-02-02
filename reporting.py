# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
import csv

def csv_readerf(data,monitoring_station):
    """Function that reads the data set based on the monitoring station specified"""
    stocking = []
    if monitoring_station == 'Harlington':
        data = data[0]
    elif monitoring_station == 'Marylebone Road':
        data = data[1]
    else:
        data = data[2]
    with open('data\\'+str(data)) as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        next(csv_read)
        for row in csv_read:
            stocking.append(row)
        return stocking



def daily_average(data, monitoring_station :str, pollutant: str) ->list[float]:
    """
    A function that returns a list/array with
    the daily averages (i.e., 365 values) for a particular pollutant and monitoring station.

    arguments : 
        ----data : list of filenames with data
        ----monitoring_station : monitoring station from witch we take the polution result
        ----pollutant : a particulat pollutant 
    """

    line_count = 0
    stocking_value = 0.0
    value_list =[]
    nodata_lines = 0
    csv_reader = csv_readerf(data,monitoring_station)
    for row in csv_reader:
        line_count += 1

        #section for no pollutant 
        if pollutant == 'no':
            if row[2] == "No data":
                nodata_lines += 1
                row[2] = 0
            stocking_value += float(row[2])
            if line_count %24 == 0:
                if nodata_lines != 24:
                    value_list.append((stocking_value)/(24-nodata_lines))
                    stocking_value = 0 
                    nodata_lines = 0
                else:
                    value_list.append(0)
                    stocking_value = 0 
                    nodata_lines = 0

        #section for pm10 pollutant 
        if pollutant == 'pm10':
            if row[3] == "No data":
                nodata_lines += 1
                row[3] = 0
            stocking_value += float(row[3])
            if line_count %24 == 0:
                if nodata_lines != 24:
                    value_list.append((stocking_value)/(24-nodata_lines))
                    stocking_value = 0 
                    nodata_lines = 0
                else:
                    value_list.append(0)
                    stocking_value = 0 
                    nodata_lines = 0

        #section for pm25 pollutant 
        elif pollutant == 'pm25':
            if row[4] == "No data":
                nodata_lines += 1
                row[4] = 0
            stocking_value += float(row[4])
            if line_count %24 == 0:
                if nodata_lines != 24:
                    value_list.append((stocking_value)/(24-nodata_lines))
                    stocking_value = 0 
                    nodata_lines = 0
                else:
                    value_list.append(0)
                    stocking_value = 0 
                    nodata_lines = 0
                
    return value_list
#print(daily_average(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],'Marylebone Road','no'))
   


def daily_median(data, monitoring_station :str, pollutant:str)-> list[float]:
    """
    returns a list/array with
    the daily median values (i.e., 365 values) for a particular pollutant and monitoring station.

    arguments : 
        ----data : list of filenames with data
        ----monitoring_station : monitoring station from witch we take the polution result
        ----pollutant : a particulat pollutant 
    """
    line_count = 0
    stocking_value = 0.0
    daily_data_list = []
    value_list =[]
    csv_reader = csv_readerf(data,monitoring_station)
    for row in csv_reader:
        line_count += 1

        #section for no pollutant 
        if pollutant == 'no':
            if row[2] == "No data":
                row[2] = -1
            daily_data_list.append(float(row[2])) 
            if line_count %24 == 0:
                daily_data_list.sort()
                for _ in range(len(daily_data_list)):
                        if daily_data_list[0] == -1:
                            daily_data_list.remove(daily_data_list[0])
                middle = float(len(daily_data_list))/2
                if middle == 0.0:
                    value_list.append(0)
                elif middle % 2 == 0:
                    stocking_value = (daily_data_list[int(middle)] +daily_data_list[int(middle-1)])/2
                    value_list.append(stocking_value)
                    stocking_value = 0
                    daily_data_list = []
                else:
                    stocking_value = (daily_data_list[int(middle-0.5)])
                    value_list.append(stocking_value)
                    stocking_value = 0
                    daily_data_list = []

        #section for pm10 pollutant 
        if pollutant == 'pm10':
            if row[3] == "No data":
                row[3] = -1
            daily_data_list.append(float(row[3])) 
            if line_count %24 == 0:
                daily_data_list.sort()
                for _ in range(len(daily_data_list)):
                        if daily_data_list[0] == -1:
                            daily_data_list.remove(daily_data_list[0])
                middle = float(len(daily_data_list))/2
                if middle == 0.0 :
                    value_list.append(0)
                elif middle % 2 == 0:
                    stocking_value = (daily_data_list[int(middle)] +daily_data_list[int(middle-1)])/2
                    value_list.append(stocking_value)
                    stocking_value = 0
                    daily_data_list = []
                else:
                    stocking_value = (daily_data_list[int(middle-0.5)])
                    value_list.append(stocking_value)
                    stocking_value = 0
                    daily_data_list = []

        #section for pm25 pollutant 
        if pollutant == 'pm25':
            if row[4] == "No data":
                row[4] = -1
            daily_data_list.append(float(row[4])) 
            if line_count %24 == 0:
                daily_data_list.sort()
                for _ in range(len(daily_data_list)):
                        if daily_data_list[0] == -1:
                            daily_data_list.remove(daily_data_list[0])
                middle = float(len(daily_data_list))/2
                if middle == 0.0:
                    value_list.append(0)
                elif middle % 2 == 0:
                    stocking_value = (daily_data_list[int(middle)] +daily_data_list[int(middle-1)])/2
                    value_list.append(stocking_value)
                    stocking_value = 0
                    daily_data_list = []
                else:
                    stocking_value = (daily_data_list[int(middle-0.5)])
                    value_list.append(stocking_value)
                    stocking_value = 0
                    daily_data_list = []
    print(value_list)    
#daily_median(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],'Marylebone Road','no')
    


def hourly_average_calculation(hours, data, monitoring_station, pollutant):
    ''' Function that makes the hourly avrage calculation for a single hour '''
    csv_reader = csv_readerf(data,monitoring_station)
    stocking_value = 0
    nodata = 0
    #section for no pollutant 
    if pollutant == 'no':
        for row in csv_reader:
            if int(row[1].replace(':00:00','')) == hours:
                if row[2] == "No data":
                    row[2] = 0
                    nodata += 1
                stocking_value += float(row[2])
        return stocking_value/(365-nodata)

    #section for pm10 pollutant 
    if pollutant == 'pm10':
        for row in csv_reader:
            if int(row[1].replace(':00:00','')) == hours:
                if row[3] == "No data":
                    row[3] = 0
                    nodata += 1
                stocking_value += float(row[3])
        return stocking_value/(365-nodata)

    #section for pm25 pollutant 
    if pollutant == 'pm25':
        for row in csv_reader:
            if int(row[1].replace(':00:00','')) == hours:
                if row[4] == "No data":
                    row[4] = 0
                    nodata += 1
                stocking_value += float(row[4])
        return stocking_value/(365-nodata)

def hourly_average(data, monitoring_station :str, pollutant : str) -> list[float]:
    """
    returns a list/array with
    the hourly averages (i.e., 24 values) for a particular pollutant and monitoring station
    using the hourly_average_claculation fonction for 24 values to get data for the hours of a whole day 

    arguments : 
        ----data : list of filenames with data
        ----monitoring_station : monitoring station from witch we take the polution result
        ----pollutant : a particulat pollutant 
    """

    value_list = []
    for i in range(1,25):
        value_list.append(hourly_average_calculation(i,data,monitoring_station,pollutant))
    print(value_list)

#hourly_average(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],'Marylebone Road','no')


''' dictionary of the numbers of days in every month'''
monthsdict = {
        '1' : 31,
        '2' : 28,
        '3' : 31,
        '4' : 30,
        '5' : 31,
        '6' : 30,
        '7' : 31,
        '8' : 31,
        '9' : 30,
        '10' : 31,
        '11' : 30,
        '12' : 31}

def monthly_average_calculation(month, data, monitoring_station, pollutant):
    ''' Function that makes the monthly avrage calculation for a single month '''
    csv_reader = csv_readerf(data,monitoring_station)
    stocking_value = 0
    nodata = 0
    #section for no pollutant 
    if pollutant == 'no':
        for row in csv_reader:
            if int(row[0][5:7]) == month:
                if row[2] == "No data":
                    row[2] = 0
                    nodata += 1
                stocking_value += float(row[2])
            nbjm = int(monthsdict[str(month)])
        return stocking_value /((nbjm * 24)-nodata)
    
    #section for pm10 pollutant 
    if pollutant == 'pm10':
        for row in csv_reader:
            if int(row[0][5:7]) == month:
                if row[3] == "No data":
                    row[3] = 0
                    nodata += 1
                stocking_value += float(row[3])
            nbjm = int(monthsdict[str(month)])
        return stocking_value /((nbjm * 24)-nodata) 

    #section for pm25 pollutant 
    if pollutant == 'pm25':
        for row in csv_reader:
            if int(row[0][5:7]) == month:
                if row[4] == "No data":
                    row[4] = 0
                    nodata += 1
                stocking_value += float(row[4])
            nbjm = int(monthsdict[str(month)])
        return stocking_value /((nbjm * 24)-nodata)                   
    
def monthly_average(data, monitoring_station : str, pollutant :str) -> list[float]:
    """
    returns a list/array with
    the monthly averages (i.e., 12 values) for a particular pollutant and monitoring station.
    using the monthly_average_claculation fonction for 12 values to get the data for the whole year 

    arguments : 
        ----data : list of filenames with data
        ----monitoring_station : monitoring station from witch we take the polution result
        ----pollutant : a particulat pollutant 
    """
    value_list = []
    for i in range(1,13):
        value_list.append(monthly_average_calculation(i,data,monitoring_station,pollutant))
    print(value_list)

#monthly_average(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],'Marylebone Road','no')



def peak_hour_date(data, date : str, monitoring_station : str, pollutant : str) -> tuple:
    """
    For a given date (e.g., 2021-01-01) returns the hour of the day with the highest pollution level 
    and its corresponding value (e.g., (12:00, 14.8))

    arguments : 
        ----data : list of filenames with data
        ----date : a given date under the date format
        ----monitoring_station : monitoring station from witch we take the polution result
        ----pollutant : a particulat pollutant
    """

    csv_reader = csv_readerf(data,monitoring_station)
    nodata = 0
    value_dict = {}
    #section for no pollutant 
    if pollutant == 'no':
        for row in csv_reader:
            if row[0] == date:
                if row[2] == "No data":
                    row[2] = 0
                    nodata += 1
                value_dict[row[1]] = float(row[2])
        v =max(value_dict.values())
        for time, value in value_dict.items():
            if value == v:
                t = time

    #section for pm10 pollutant 
    if pollutant == 'pm10':
        for row in csv_reader:
            if row[0] == date:
                if row[3] == "No data":
                    row[3] = 0
                    nodata += 1
                value_dict[row[1]] = float(row[3])
        v =max(value_dict.values())
        for time, value in value_dict.items():
            if value == v:
                t = time

    #section for pm25 pollutant 
    if pollutant == 'pm25':
        for row in csv_reader:
            if row[0] == date:
                if row[4] == "No data":
                    row[4] = 0
                    nodata += 1
                value_dict[row[1]] = float(row[4])
        v =max(value_dict.values())
        for time, value in value_dict.items():
            if value == v:
                t = time
                
    return t[:5],v
#print(peak_hour_date(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],'2021-01-02','Marylebone Road','pm10'))

def count_missing_data(data,  monitoring_station : str, pollutant : str):
    """
    For a given monitoring station and pollutant, 
    returns the number of 'No data' entries are there in the data.

    arguments : 
        ----data : list of filenames with data
        ----monitoring_station : monitoring station from witch we take the polution result
        ----pollutant : a particulat pollutant
    """

    counter = 0
    if monitoring_station == 'Harlington':
        data = data[0]
    elif monitoring_station == 'Marylebone Road':
        data = data[1]
    else:
        data = data[2]
    with open('data\\'+str(data)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if pollutant == 'no':
                if row[2] == "No data":
                    counter += 1
            if pollutant == 'pm10':
                if row[3] == "No data":
                    counter += 1
            if pollutant == 'pm25':
                if row[4] == "No data":
                    counter += 1
        return counter

#print(count_missing_data(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],'Marylebone Road','pm25'))


def fill_missing_data(data, new_value,  monitoring_station :str,pollutant :str):
    """
    For a given monitoring station and pollutant, returns a copy of the data with the missing
    values 'No data' replaced by the value in the parameter new value.

    arguments : 
        ----data : list of filenames with data
        ----new_value : a new value to change the 'No data' to 
        ----monitoring_station : monitoring station from witch we take the polution result
        ----pollutant : a particulat pollutant

    """
    
    if monitoring_station == 'Harlington':
        data = data[0]
    elif monitoring_station == 'Marylebone Road':
        data = data[1]
    else:
        data = data[2]
    with open('data\\'+str(data)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        for row in csv_reader:
            if pollutant == 'no':
                new = row[2].replace('No data',str(new_value))
                print(new)
            if pollutant == 'pm10':
                new = row[3].replace('No data',str(new_value))
                print(new)
            elif pollutant == 'pm25':
                new = row[4].replace('No data',str(new_value))
                print(new)
            else:
                raise ValueError("wrong pollutant inputed")

#fill_missing_data(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],0.0000001,'Marylebone Road','pm25')