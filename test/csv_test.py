import csv
'''
def csv_data_function(datafile):
    with open('data\\'+str(datafile)) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')


#csv_data_function('Pollution-London Harlington.csv')
'''

'''
#first verison
def daily_average(data, monitoring_station:str, pollutant:str):
    """
    Questions: 
    to what coresponds the data argument ?
    shoud i include the case where a wrong data is inputed ?
    is the CSv file reding format good ?
    can i use replace ?
    are my values ok ?
    can my data be with list?
    in the utils can i use isinstance?

    """

    line_count = 0
    stocking_value = 0.0
    value_list =[]
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
                    continue
                stocking_value += float(row[2])
                line_count += 1
                if line_count %24 == 0:
                    value_list.append(stocking_value/24)
                    stocking_value = 0 
            if pollutant == 'pm10':
                if row[3] == "No data":
                    continue
                stocking_value += float(row[3])
                line_count += 1
                if line_count %24 == 0:
                    value_list.append(stocking_value/24)
                    stocking_value = 0 
            elif pollutant == 'pm25':
                if row[4] == "No data":
                    continue
                stocking_value += float(row[4])
                line_count += 1
                if line_count %24 == 0:
                    value_list.append(stocking_value/24)
                    stocking_value = 0
            
        print(value_list)
        print(len(value_list))
        print(f'Processed {line_count} lines.')
'''



def csv_readerf(data,monitoring_station):
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
        
def testing_csv(data = 'Pollution-London testfile.csv'):
    stocking = []
    with open('test\\'+str(data)) as csv_file:
        csv_read = csv.reader(csv_file, delimiter=',')
        next(csv_read)
        for row in csv_read:
            stocking.append(row)
        return stocking




def daily_average(data, monitoring_station :str, pollutant: str) ->list[float]:
    """

    """

    line_count = 0
    stocking_value = 0.0
    value_list =[]
    nodata_lines = 0
    csv_reader = csv_readerf(data,monitoring_station)
    for row in csv_reader:
        line_count += 1
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
   


def daily_median(data, monitoring_station, pollutant):
    line_count = 0
    stocking_value = 0.0
    daily_data_list = []
    value_list =[]
    nodata_lines = 0
    csv_reader = csv_readerf(data,monitoring_station)
    for row in csv_reader:
        line_count += 1
        if pollutant == 'no':
            if row[2] == "No data":
                nodata_lines += 1
                row[2] = -1
            daily_data_list.append(float(row[2])) 
            if line_count %24 == 0:
                daily_data_list.sort()
                for i in range(len(daily_data_list)):
                        if daily_data_list[0] == -1:
                            #print(i)
                            daily_data_list.remove(daily_data_list[0])
                #print(daily_data_list)
                middle = float(len(daily_data_list))/2
                #print(middle)
                if middle == 0.0:
                    value_list.append(0)
                if middle % 2 == 0:
                    stocking_value = (daily_data_list[int(middle)] +daily_data_list[int(middle-1)])/2
                    value_list.append(stocking_value)
                    stocking_value = 0
                    daily_data_list = []
                else:
                    stocking_value = (daily_data_list[int(middle-0.5)])
                    value_list.append(stocking_value)
                    stocking_value = 0
                    daily_data_list = []


        if pollutant == 'pm10':
            if row[3] == "No data":
                nodata_lines += 1
                row[3] = -1
            daily_data_list.append(float(row[3])) 
            if line_count %24 == 0:
                daily_data_list.sort()
                for i in range(len(daily_data_list)):
                        if daily_data_list[0] == -1:
                            #print(i)
                            daily_data_list.remove(daily_data_list[0])
                #print(daily_data_list)
                middle = float(len(daily_data_list))/2
                #print(middle)
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




        if pollutant == 'pm25':
            if row[4] == "No data":
                nodata_lines += 1
                row[4] = -1
            daily_data_list.append(float(row[4])) 
            if line_count %24 == 0:
                daily_data_list.sort()
                for i in range(len(daily_data_list)):
                        if daily_data_list[0] == -1:
                            #print(i)
                            daily_data_list.remove(daily_data_list[0])
                #print(daily_data_list)
                middle = float(len(daily_data_list))/2
                #print(middle)
                if middle == 0.0:
                    value_list.append(0)
                if middle % 2 == 0:
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
    print(len(value_list))
    print(line_count)
     
#daily_median(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],'Marylebone Road','pm10')

'''
def hourly_average(data, monitoring_station, pollutant):
    stocking_value = 0
    value_list = []
    intermidiate_list = []
    nodata_lines = 0
    csv_reader = testing_csv()
    for hours in range(24):
        pass
    for row in csv_reader:
        if pollutant == 'no':
            if row[2] == "No data":
                nodata_lines += 1
                row[2] = 0  
                if row[1][0] == str(0):
                    hours = str(0)+str(hours)
                if row[1] == str(hours)+':00:00':

                    stocking_value +=float(row[2])
                    

                if nodata_lines == 24:
                    value_list.append(0)
                    nodata_lines = 0
                    stocking_value = 0
                else:
                    value_list.append((stocking_value)/(24-nodata_lines))
                    nodata_lines = 0
                    stocking_value = 0
    
    print(value_list)
    print(len(value_list))
'''


def hourly_average_calculation(hours, data, monitoring_station, pollutant):
    csv_reader = csv_readerf(data,monitoring_station)
    stocking_value = 0
    nodata = 0
    if pollutant == 'no':
        for row in csv_reader:
            if int(row[1].replace(':00:00','')) == hours:
                if row[2] == "No data":
                    row[2] = 0
                    nodata += 1
                stocking_value += float(row[2])
        return stocking_value/(365-nodata)
    if pollutant == 'pm10':
        for row in csv_reader:
            if int(row[1].replace(':00:00','')) == hours:
                if row[3] == "No data":
                    row[3] = 0
                    nodata += 1
                stocking_value += float(row[3])
        return stocking_value/(365-nodata)
    if pollutant == 'pm25':
        for row in csv_reader:
            if int(row[1].replace(':00:00','')) == hours:
                if row[4] == "No data":
                    row[4] = 0
                    nodata += 1
                stocking_value += float(row[4])
        return stocking_value/(365-nodata)
    


#print(hourly_average_calculation(4,['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],'Marylebone Road','pm10'))

def hourly_average(data, monitoring_station, pollutant):
    value_list = []
    for i in range(1,25):
        value_list.append(hourly_average_calculation(i,data,monitoring_station,pollutant))

    print(value_list)
    print(len(value_list))
#hourly_average(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],'Marylebone Road','no')



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

#print(monthsdict)

# total valuer /(nb jour dans mois * 24) =  monthly avrage 
def monthly_average_calculation(month, data, monitoring_station, pollutant):
    csv_reader = csv_readerf(data,monitoring_station)
    stocking_value = 0
    nodata = 0
    if pollutant == 'no':
        for row in csv_reader:
            if int(row[0][5:7]) == month:
                if row[2] == "No data":
                    row[2] = 0
                    nodata += 1
                stocking_value += float(row[2])
            nbjm = int(monthsdict[str(month)])
        return stocking_value /((nbjm * 24)-nodata)

    if pollutant == 'pm10':
        for row in csv_reader:
            if int(row[0][5:7]) == month:
                if row[3] == "No data":
                    row[3] = 0
                    nodata += 1
                stocking_value += float(row[3])
            nbjm = int(monthsdict[str(month)])
        return stocking_value /((nbjm * 24)-nodata) 

    if pollutant == 'pm25':
        for row in csv_reader:
            if int(row[0][5:7]) == month:
                if row[4] == "No data":
                    row[4] = 0
                    nodata += 1
                stocking_value += float(row[4])
            nbjm = int(monthsdict[str(month)])
        return stocking_value /((nbjm * 24)-nodata)                   
    
#print(monthly_average_calculation(1,['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],'Marylebone Road','no'))


def monthly_average(data, monitoring_station, pollutant):
    value_list = []
    for i in range(1,13):
        value_list.append(monthly_average_calculation(i,data,monitoring_station,pollutant))

    print(value_list)
#monthly_average(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],'Marylebone Road','no')



def peak_hour_date(data, date, monitoring_station,pollutant):
    """Your documentation goes here"""

    csv_reader = csv_readerf(data,monitoring_station)
    nodata = 0
    value_dict = {}
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

#connected_component = set([333])
#print(connected_component)

b_file =[[1,2,3],
        [4,5,6],
        [7,8,9]]

#print(b_file[-1][-1])

import numpy as np
b_file =np.array([[1,2,3],[4,5,6]])
k = np.array([[0,1,2],[5,6,7]])
#print(k[0])
print(np.concatenate([k,b_file]))

'''
from collections import deque

def detect_connected_components(image):
    """
    Detects connected components in a binary image and returns a list
    of connected component coordinates in the form [(x1, y1), (x2, y2), ...].
    """
    
    # Define the directions in which to search for neighboring pixels
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1),(-1, -1),(1, 1)]

    # Create a list to store the connected component coordinates
    connected_components = []

    # Create a visited matrix to keep track of which pixels have been visited
    visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]

    # Iterate over all the pixels in the image
    for i in range(len(image)):
        for j in range(len(image[0])):
            # Check if the pixel is not visited and is set to 1 (i.e. it is part of the component)
            if not visited[i][j] and image[i][j] == 1:
                # Create a queue to store the pixels in the connected component
                q = deque()

                # Add the current pixel to the queue and mark it as visited
                q.append((i, j))
                visited[i][j] = True

                # Create a list to store the coordinates of the connected component
                component = []

                # Continue searching while there are still pixels in the queue
                while len(q) > 0:
                    # Pop the first pixel from the queue
                    pixel = q.popleft()

                    # Add the pixel to the connected component
                    component.append(pixel)

                    # Search the neighboring pixels
                    for direction in directions:
                        x = pixel[0] + direction[0]
                        y = pixel[1] + direction[1]

                        # Check if the neighboring pixel is within the bounds of the image,
                        # is not visited, and is set to 1
                        if (x >= 0 and x < len(image) and y >= 0 and y < len(image[0])
                            and not visited[x][y] and image[x][j] == 1):
                            # Add the neighboring pixel to the queue and mark it as visited
                            q.append((x, y))
                            visited[x][y] = True

                # Add the connected component to the list of connected components
                connected_components.append(component)

    return connected_components
'''



'''
def connected_components(image):
  # Create a list to store the connected components
  components = []

  # Create a 2D list to keep track of which pixels have been visited
  visited = [[False for _ in range(image.width)] for _ in range(image.height)]

  # Iterate over each pixel in the image
  for y in range(image.height):
    for x in range(image.width):
      # If the pixel has not been visited and has a value of 1 (i.e. it is part of the foreground)
      if not visited[y][x] and image.get_pixel(x, y) == 255:
        # Create a new list to store the connected component
        component = []

        # Perform a depth-first search to find all the pixels in the connected component
        stack = [(x, y)]
        while stack:
          x, y = stack.pop()
          if not visited[y][x] and image.get_pixel(x, y) == 255:
            visited[y][x] = True
            component.append((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
              stack.append((x + dx, y + dy))

        # Add the connected component to the list of components
        components.append(component)

  # Return the list of connected components
  return components


'''