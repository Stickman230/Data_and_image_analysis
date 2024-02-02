# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help

import requests
import datetime
from utils import maxvalue

Site_code = ['MY1','KC1','HRL']
Species_code = ['NO','PM10','PM25']
original_addr = 'https://api.erg.ic.ac.uk/AirQuality'
Start_date = datetime.date.today()
End_date = Start_date + datetime.timedelta(days=1)

def get_live_data_from_api(site_code='MY1',species_code='PM10',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = Start_date,
        end_date = End_date
    )
        
    res = requests.get(url)
    return res.json()


def daily_mean_pollutant():
    """Function with no arguments that return the  value of all 3 pollutant for the last day for a single site """

    no_datalines = 0
    stocking_value = 0
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
    station = input("Which station shoud we get the data from ? 'MY1' or 'KC1' or 'HRL' : \n").upper()
    while station not in Site_code:
        station = input("Which station shoud we get the data from ? 'MY1' or 'KC1' or 'HRL' : \n").upper()
    print('\n')
    #itarate over the stations 
    if station in Site_code:
        #itarate over the pollutants
        for nbOfSpecies in range(len(Species_code)):
            url = endpoint.format(
                site_code = station,
                species_code = Species_code[nbOfSpecies],
                start_date = Start_date,
                end_date = End_date)
            req = requests.get(url)
            response = req.json() 
            pollutant_value = response['RawAQData']['Data']
            #get all the data values needed for calculations
            for date in range(len(pollutant_value)):
                #check if there is data for the date
                if pollutant_value[date]['@Value'] == '':
                    pollutant_value[date]['@Value'] = 0
                    no_datalines += 1
                stocking_value += float(pollutant_value[date]['@Value'])
            nb_data = len(pollutant_value)-no_datalines
            if nb_data == 0:
                print("This is the mean value of the " + str(Species_code[nbOfSpecies])+" pollutant : " + str(0.0))
            else:
                print("This is the mean value of the " + str(Species_code[nbOfSpecies])+" pollutant : " + str(abs(stocking_value/nb_data)))
            stocking_value = 0
        print("\nALL THE POLLUTANT ARE FOR THE "+ station+ " STATION")
        print("ALL VALUES ARE FROM "+ str(Start_date) + " to " + str(End_date)+"\n")

#daily_mean_pollutant()


def over_threshold():
    """a function with no arguments that returns the values that are over a threshold
     for a or all chosen polutant and for a given period of time """

    no_datalines = 0
    stocking_list = []
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
    #get all needed info from the user 
    station = str(input("Which station shoud we get the data from ? 'MY1' or 'KC1' or 'HRL' : \n").upper())
    while station not in Site_code:
        station = str(input("Which station shoud we get the data from ? 'MY1' or 'KC1' or 'HRL' : \n").upper())
    pollutant = str(input("Do you want a particular pollutant ('' = all 3 else enter species code) : \n").upper())
    while pollutant not in Species_code and pollutant != '':
        pollutant = str(input("Do you want a particular pollutant ('' = all 3 else enter species code) : \n").upper())
    threshold = input("Decide a lower threshold value : ")
    period_start = input("What is the start period of your data, enter 'd' for daily analysis ( format = " +str(Start_date)+ " ) : \n")
    if period_start == 'd':
        period_start = Start_date
        period_end = End_date
        end_line  = "\nALL VALUES ARE FROM "+ str(Start_date) + " to " + str(End_date)+"\n" 
    else:
        period_end = input("What is the end period of your data , enter 't' key for today date ( normal format = " +str(Start_date)+ " ) : \n")
        end_line = "\nALL VALUES ARE FROM "+ str(period_start) + " to " + str(period_end)+"\n"  
    print('\n')
    if period_end == 't':
        period_end = End_date
        end_line = "\nALL VALUES ARE FROM "+ str(period_start) + " to " + str(End_date)+"\n"
    #if all stations chosen
    #iterate over stations
    if station in Site_code:
        if pollutant == '':
            #iterate over pollutant
            for nbOfSpecies in range(len(Species_code)):
                url = endpoint.format(
                    site_code = station,
                    species_code = Species_code[nbOfSpecies],
                    start_date = period_start,
                    end_date = period_end)
                req = requests.get(url)
                response = req.json() 
                #get all the data values needed for calculations
                pollutant_value = response['RawAQData']['Data']
                for date in range(len(pollutant_value)):
                    #check if there is data for the date
                    if pollutant_value[date]['@Value'] == '':
                        pollutant_value[date]['@Value'] = 0
                        no_datalines += 1
                    #check if values are over threshold
                    if float(pollutant_value[date]['@Value']) > int(threshold):
                        stocking_list.append(pollutant_value[date]['@Value'])
                print("Here are all the values for this "+str(Species_code[nbOfSpecies])+" pollutant with "+str(threshold) +" as a lower threshold\n")
                print(str(stocking_list)+'\n')
                stocking_list = []    
        else:
            #if a single pollutant chosen
            url = endpoint.format(
                    site_code = station,
                    species_code = pollutant,
                    start_date = period_start,
                    end_date = period_end)
            req = requests.get(url)
            response = req.json() 
            #get all the data values needed for calculations
            pollutant_value = response['RawAQData']['Data']
            for date in range(len(pollutant_value)):
                #check if there is data for the date
                if pollutant_value[date]['@Value'] == '':
                    pollutant_value[date]['@Value'] = 0
                    no_datalines += 1
                #check if values over threshold
                if float(pollutant_value[date]['@Value']) > int(threshold):
                    stocking_list.append(pollutant_value[date]['@Value'])
            print("Here are all the values for this "+str(pollutant)+" pollutant with "+str(threshold) +" as a lower threshold\n")
            print(str(stocking_list)+'\n')
    #return the period chosen
    print(end_line)  
           
#over_threshold()


def average_most_polluted_station_daily():
    """a function that compares 3 pollutant for 3 stations and finds the most polluted station for every pollutant by using the men value.
     Every thing is based on daily data"""
    no_datalines = 0
    stocking_list = []
    site_dict = {0 : 'MY1',
                    1 : 'KC1',
                    2 : 'HRL'}
    stocking_value = 0
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
    print("\n")
    #iterate over stations
    for nbOfStations in range(len(Site_code)):
        #iterate over pollutant
        for nbOfSpecies in range(len(Species_code)):
            url = endpoint.format(
                site_code = Site_code[nbOfStations],
                species_code = Species_code[nbOfSpecies],
                start_date = Start_date,
                end_date = End_date)
            req = requests.get(url)
            response = req.json()
            #get all the data values needed for calculations
            pollutant_value = response['RawAQData']['Data']
            for date in range(len(pollutant_value)):
                #check if there is data for the date
                if pollutant_value[date]['@Value'] == '':
                    pollutant_value[date]['@Value'] = 0
                    no_datalines += 1
                stocking_value += float(pollutant_value[date]['@Value'])
            nb_data = len(pollutant_value)-no_datalines
            if nb_data == 0:
                #if no data for pollutant
                print("This is the mean value of the " + str(Species_code[nbOfSpecies])+" pollutant : " + str(0.0))
                stocking_list.append(0.0)
            else:
                #calculate average
                print("This is the mean value of the " + str(Species_code[nbOfSpecies])+" pollutant : " + str(abs(stocking_value/nb_data)))
                stocking_list.append(abs(stocking_value/nb_data))
            stocking_value = 0
        print("ALL THE POLLUTANT ARE FOR THE "+ str(Site_code[nbOfStations])+ " STATION\n")

    #highest average for every pollutant and where it is from if there is value 
    no_list = [stocking_list[0],stocking_list[3],stocking_list[6]]
    if int(no_list[maxvalue(no_list)]) == 0:
        print("For the NO pollutant he highest mean value is " + str(no_list[maxvalue(no_list)]))
    else:
        print("For the NO pollutant he highest mean value is " + str(no_list[maxvalue(no_list)])+ " from the "+str(site_dict[maxvalue(no_list)]) + " station")
    pm10_list = [stocking_list[1],stocking_list[4],stocking_list[7]]
    if int(pm10_list[maxvalue(pm10_list)]) == 0:
        print("For the PM10 pollutant he highest mean value is " + str(pm10_list[maxvalue(pm10_list)]))
    else:
        print("For the PM10 pollutant he highest mean value is " + str(pm10_list[maxvalue(pm10_list)])+ " from the "+ str(site_dict[maxvalue(pm10_list)]) + " station")
    pm25_list = [stocking_list[2],stocking_list[5],stocking_list[8]]
    if int(pm25_list[maxvalue(pm25_list)]) == 0:
        print("For the PM25 pollutant he highest mean value is " + str(pm25_list[maxvalue(pm25_list)]))
    else:
        print("For the PM25 pollutant he highest mean value is " + str(pm25_list[maxvalue(pm25_list)])+ " from the "+ str(site_dict[maxvalue(pm25_list)]) + " station")
    print("\nALL VALUES ARE FROM "+ str(Start_date) + " to " + str(End_date))

#average_most_polluted_station_daily()


def daily_nb_Nodata():
    """ a function with no arguments that return the number of 'No data' value per polluant and station 
    during the last day """
    no_datalines = 0
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
    print("\n")
    #iterate over stations
    for nbOfStations in range(len(Site_code)):
        #iterate over pollutant
        for nbOfSpecies in range(len(Species_code)):
            url = endpoint.format(
                site_code = Site_code[nbOfStations],
                species_code = Species_code[nbOfSpecies],
                start_date = Start_date,
                end_date = End_date)
            req = requests.get(url)
            response = req.json()
            #get all the data values needed for calculations
            pollutant_value = response['RawAQData']['Data']
            for date in range(len(pollutant_value)):
                #check if there is data for the date
                if pollutant_value[date]['@Value'] == '':
                    no_datalines += 1
            #return the number of emplty values per pollutant per station
            print("There is "+str(no_datalines)+" empty data in the values out of "+ str(len(pollutant_value)) +" from the "+ str(Species_code[nbOfSpecies]) +" polllutant." )
            no_datalines = 0
        print("ALL THE POLLUTANT ARE FOR THE "+ str(Site_code[nbOfStations])+ " STATION\n") 
    print("\nALL VALUES ARE FROM "+ str(Start_date) + " to " + str(End_date))

#daily_nb_Nodata()