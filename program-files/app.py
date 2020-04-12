from dataparser import parseStateData, parseCountyData, returnTotalCasesOnDate, returnTotalDeathsOnDate, returnCountyWithMostCasesOnDate, returnCountyWithMostDeathsOnDate, createCounty, createState
from county_functions import County_Store
from state_functions import State_Store
from graph import graphDemoCases, graphDemoDeaths

# add a while loop or try 
# catch to detect wrong input type
def test1():
    countyParse = createState()
    givenDate = input("What date are you asking about: ")

    print("First case in", countyParse.name, "recorded on:", countyParse.returnFirstCase())
    print("First death in", countyParse.name, "recorded on:", countyParse.returnFirstDeath())
    print("Total deaths in", countyParse.name, "is", countyParse.returnDeathCount())
    print("Total cases in", countyParse.name, "is", countyParse.returnCaseCount())
    print("Latest Case Date in", countyParse.name, ":", countyParse.returnLatestCase())
    print("Number of Cases on", givenDate, "in", countyParse.name, "was", countyParse.casesOnDate(givenDate))
    print("Number of Deaths on", givenDate, "in", countyParse.name, "was", countyParse.deathsOnDate(givenDate))
    print("Most number of cases in", countyParse.name, "was", countyParse.maxCases())
    print("Most number of deaths in", countyParse.name, "was", countyParse.maxDeaths())
    print("National Total Cases on", givenDate, "was", returnTotalCasesOnDate(givenDate))
    print("National Total Deaths on", givenDate, "was", returnTotalDeathsOnDate(givenDate))

    '''
    if (cfile_cases[returnCountyWithMostCasesOnDate(givenDate)] != 0):
        print("County with most cases on", givenDate, "was", cfile_county[returnCountyWithMostCasesOnDate(givenDate)], "in", cfile_state[returnCountyWithMostCasesOnDate(givenDate)], "with", cfile_cases[returnCountyWithMostCasesOnDate(givenDate)])
    else:
        print("No cases recorded on given date in any counties")
    if (cfile_deaths[returnCountyWithMostDeathsOnDate(givenDate)] != 0):
        print("County with most deaths on", givenDate, "was", cfile_county[returnCountyWithMostDeathsOnDate(givenDate)], "in", cfile_state[returnCountyWithMostDeathsOnDate(givenDate)], "with", cfile_deaths[returnCountyWithMostDeathsOnDate(givenDate)])
    else:
        print("No deaths recorded on given date in any counties")

    '''

def executable():
    res = input("Would you like to see 1 (state/county statistics) or 2 (general statistics): ")
    if res == '1':
        res = input("1 (State) or 2 (County)?: ")
        if res == '1':
            given = createState()
        else:
            given = createCounty()
        
        res = input("Would you like to see 1 (graph) or 2 (statistics)?: ")
        if res == '1':
            res = input("1 (Cases) or 2 (Deaths)?: ")
            if res == '1':
                graphDemoCases(given)
            else:
                graphDemoDeaths(given)
        #else:
            #stats program/part for county/state
    #else:
        #stats program for all of US


        
    
executable()