# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

from reporting import *
from monitoring import *
from intelligence import *
import os
import time 


def main_menu():
    """A function that will be executed upon the initialisation of the program, showing the
    main menu of the program allowing the user to navigate through the different options."""

    os.system('cls')
    print("\nHello welcome to the AQUA system User interface\n\nSelect any off the keys ")
    print("You have multiple options here so chose wisely : \n")
    print("• R - Access the PR module\n• I - Access the MI module\n• M - Access the RM module\n• A - Print the About text\n• Q - Quit the application\n")
    print('( if you press the enter key without an input you will refresh the menu )')
    option = input("Menu option chosen : ").upper()
    while option != 'R' and option != 'I' and option != 'M' and option != 'A' and option != 'Q' and option != '':
        option = input("Menu option chosen : ").upper()
    if option == 'R':
        reporting_menu()
    if option == 'I':
        intelligence_menu()
    if option == 'M':
        monitoring_menu()
    if option == 'A':
        about()
    if option == 'Q':
        quit()
    if option == '':
        main_menu()
        
def reporting_menu():
    """A function that will be executed when the user chooses the 'R' option in the
    main menu. It allows the user to choose the necessary options to perform the analyses
    of the reporting file, allowing the user to navigate through the different options and return
    to the main menu."""
    os.system('cls')
    print("\nYou are in the reporting menu\nYou have a lot of options to chose from \n")
    print("In this module you will need to chose a monitoring station and a pollutant \n")
    monitoring_sation = input("Chose from : 'Harlington', 'Marylebone Road' and 'N Kensington'or press q to quit to menu : \n")
    while monitoring_sation != 'Harlington' and monitoring_sation != 'Marylebone Road' and monitoring_sation != 'N Kensington' and monitoring_sation != 'q':
        monitoring_sation = input("Chose from : 'Harlington', 'Marylebone Road' and 'N Kensington'or press q to quit to menu : \n")
    if monitoring_sation == 'q':
        print("\n------------------------")
        main_menu()
    pollutant = input ("Chose from these pollutant : 'no', 'pm10', 'pm25' : \n")
    while pollutant != 'no' and pollutant != 'pm10' and pollutant != 'pm25':
        pollutant = input ("Chose from these pollutant : 'no', 'pm10', 'pm25' : \n")
    print("\n DA - Daily average \n DM - Daily median \n HA - Hourly average \n MA - Monthly average \n PHD - Peak hour date \n CMD - Count missing data\n FMD - Fill missing data\n Q - Quit\n")
    print('( if you press the enter key without an input you will refresh the menu )')
    option = input("Reporting option chosen : \n").upper()
    while option != 'DA' and option != 'DM' and option != 'HA' and option != 'MA' and option != 'PHD' and option != 'CMD' and option != 'FMD' and option != 'Q' and option != '':
        option = input("Reporting option chosen : ").upper()
    if option == 'DA':
        print(daily_average(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],monitoring_sation,pollutant))
        print("\n------------------------")
        out = input('Press any key to exit : ')
        reporting_menu()
    if option == 'DM':
        daily_median(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],monitoring_sation,pollutant)
        print("\n------------------------")
        out = input('Press any key to exit : ')
        reporting_menu()
    if option == 'HA':
        hourly_average(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],monitoring_sation,pollutant)
        print("\n------------------------")
        out = input('Press any key to exit : ')
        reporting_menu()
    if option == 'MA':
        monthly_average(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],monitoring_sation,pollutant)
        print("\n------------------------")
        out = input('Press any key to exit : ')
        reporting_menu()
    if option == 'PHD':
        date = input("Give date under date format ('2021-01-02') : ")
        print(peak_hour_date(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],date,monitoring_sation,pollutant))
        print("\n------------------------")
        out = input('Press any key to exit : ')
        reporting_menu()
    if option == 'CMD':
        print(count_missing_data(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],monitoring_sation,pollutant))
        print("\n------------------------")
        out = input('Press any key to exit : ')
        reporting_menu()
    if option == 'FMD':
        fill = input("With what will you fill the missing data : ")
        fill_missing_data(['Pollution-London Harlington.csv','Pollution-London Marylebone Road.csv','Pollution-London N Kensington.csv'],fill,monitoring_sation,pollutant)
        print("\n------------------------")
        out = input('Press any key to exit : ')
        reporting_menu()
    if option == 'Q':
        main_menu()
        exit()
    if option == '':
        os.system('cls')
        reporting_menu()

def intelligence_menu():
    """A function that will be executed when the user chooses the 'I' option in the
    main menu. It allows the user to choose the necessary options to perform the analyses
    of the intelligence file, allowing the user to navigate through the different options and return
    to the main menu"""
    map_filename = 'map.png'
    binary_image = 'map-red-pixels.jpg'
    os.system('cls')
    print("\nYou are in the intelligence menu\nWhat option do you chose : \n")
    print("\n FRP - Find red pixels \n FCP - Find cyan pixels \n DCC - Detect conected components \n DCCS - Detect conected components sorted ( no return from this function ) \n Q - Quit\n")
    print('( if you press the enter key without an input you will refresh the menu )')
    option = input("Intelligence module option chosen : ").upper()
    while option != 'FRP' and option != 'FCP' and option != 'DCC' and option != 'DCCS' and option != 'Q' and option != '':
        option = input("Intelligence module option chosen : ").upper()
    if option == 'FRP':
        find_red_pixels(map_filename, upper_threshold=100, lower_threshold=50)
        print("\n------------------------")
        out = input('Press any key to exit : ')
        intelligence_menu()
    if option == 'FCP':
        find_cyan_pixels(map_filename, upper_threshold=100, lower_threshold=50)
        print("\n------------------------")
        out = input('Press any key to exit : ')
        intelligence_menu()
    if option == 'DCC':
        print(detect_connected_components(binary_image))
        print("\n------------------------")
        out = input('Press any key to exit : ')
    if option == 'DCCS':
        detect_connected_components_sorted(detect_connected_components(binary_image))
        print('\nfunction has been executed')
        print("\n------------------------")
        out = input('Press any key to exit : ')
        intelligence_menu()
    if option == 'Q':
        main_menu()
        exit()
    if option == '':
        os.system('cls')
        intelligence_menu()


def monitoring_menu():
    """A function that will be executed when the user chooses the 'M' option in the
    main menu. It allows the user to choose the necessary options to perform the analyses
    of the monitoring file, allowing the user to navigate through the different options and return
    to the main menu"""
    os.system('cls')
    print("\nYou are in the monitoring menu\nWhat option do you chose : \n")
    print("In this module you will need to chose a monitoring station and a pollutant for certain functions \n")
    print("\n DMP - Daily mean pollutant \n OT - Over threshold \n AMPS - Average most polluted station daily \n DNN - Daily number of nodata \n Q - Quit\n")
    print('( if you press the enter key without an input you will refresh the menu )')
    option = input("Monitoring option chosen : ").upper()
    while option != 'DMP' and option != 'OT' and option != 'AMPS' and option != 'DNN' and option != 'Q' and option != '':
        option = input("Monitoring option chosen : ").upper()
    if option == 'DMP':
        daily_mean_pollutant()
        print("\n------------------------")
        out = input('Press any key to exit : ')
        monitoring_menu()
    if option == 'OT':
        over_threshold()
        print("\n------------------------")
        out = input('Press any key to exit : ')
        monitoring_menu()
    if option == 'AMPS':
        average_most_polluted_station_daily()
        print("\n------------------------")
        out = input('Press any key to exit : ')
        monitoring_menu()
    if option == 'DNN':
        daily_nb_Nodata()
        print("\n------------------------")
        out = input('Press any key to exit : ')
        monitoring_menu()
    if option == 'Q':
        main_menu()
    if option == '':
        monitoring_menu()

def about():
    """ A function that will be executed when the user chooses the 'A' option in the main menu. It
    prints a string containing the module code (ECM1400) and a string with the 6-digits
    candidate number returning to the main menu afterwards."""
    print("\n------------------------")
    print('\nECM1400', 234495)
    print("\n------------------------")
    out = input('Press any key to exit : ')
    main_menu()

def quit():
    """A function that will be executed when the user chooses the 'Q' option in the main menu.
    It terminates the program."""
    print("\n------------------------")
    print("\nProgam end")
    print("\n------------------------")
    time.sleep(1.5)
    os.system('cls')
    exit()



if __name__ == '__main__':
    main_menu()