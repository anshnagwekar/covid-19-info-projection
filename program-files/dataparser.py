import csv
from state_functions import State_Store
from county_functions import County_Store

cfile_dates = []
cfile_county = []
cfile_state = []
cfile_fips = []
cfile_cases = []
cfile_deaths = []

sfile_dates = []
sfile_state = []
sfile_fips = []
sfile_cases = []
sfile_deaths = []

def returnCountyCaseGivenIndex(index):
    return cfile_cases[index]

def returnStateCaseGivenIndex(index):
    return sfile_cases[index]

def returnCountyDateGivenIndex(index):
    return cfile_dates[index]

def returnStateDateGivenIndex(index):
    return sfile_dates[index]

def returnCountyDeathGivenIndex(index):
    return cfile_deaths[index]

def returnStateDeathGivenIndex(index):
    return sfile_deaths[index]

def parseCountyData():
    global cfile_dates
    global cfile_county
    global cfile_state
    global cfile_fips
    global cfile_cases
    global cfile_deaths

    cfile_dates = []
    cfile_county = []
    cfile_state = []
    cfile_fips = []
    cfile_cases = []
    cfile_deaths = []
    # csv file in same dir
    with open('../../covid-19-data/us-counties.csv', 'r') as csv_file:
        csv_read = csv.reader(csv_file)
        next(csv_read)
        for line in csv_read:
            cfile_dates.append(line[0])
            cfile_county.append(line[1])
            cfile_state.append(line[2])
            cfile_fips.append(line[3])
            cfile_cases.append(int(line[4]))
            cfile_deaths.append(int(line[5]))
'''
    print(len(cfile_dates))
    print(len(cfile_state))
    print(len(cfile_fips))
    print(len(cfile_cases))
    print(len(cfile_deaths))
'''


def parseStateData():
    global sfile_dates
    global sfile_state
    global sfile_fips
    global sfile_cases
    global sfile_deaths

    sfile_dates = []
    sfile_state = []
    sfile_fips = []
    sfile_cases = []
    sfile_deaths = []
    # csv file in the same dir
    with open('../../covid-19-data/us-states.csv', 'r') as csv_file1:
        csv_read1 = csv.reader(csv_file1)
        next(csv_read1)
        for line in csv_read1:
            sfile_dates.append(line[0])
            sfile_state.append(line[1])
            sfile_fips.append(line[2])
            sfile_cases.append(int(line[3]))
            sfile_deaths.append(int(line[4]))
    # write all SCC
'''
    print(len(sfile_dates))
    print(len(sfile_state))
    print(len(sfile_fips))
    print(len(sfile_cases))
    print(len(sfile_deaths))
'''
def returnTotalCasesOnDate(date):
    parseCountyData()
    parseStateData()

    casesTotal = 0
    for i in range(0, len(cfile_dates)):
        if (cfile_dates[i] == date):
            casesTotal = casesTotal + cfile_cases[i]

    casesTotal1 = 0
    counter = 0
    for i in range(0, len(sfile_dates)):
        if (sfile_dates[i] == date):
            counter = counter + 1
            casesTotal1 = casesTotal1 + sfile_cases[i]
            #print(sfile_cases[i])
    return casesTotal

def returnTotalDeathsOnDate(date):
    parseCountyData()
    parseStateData()

    deathTotal = 0
    for i in range(0, len(cfile_dates)):
        if (cfile_dates[i] == date):
            deathTotal = deathTotal + cfile_deaths[i]
    # should return same value:

    deathTotal1 = 0
    for i in range(0, len(sfile_dates)):
        if (sfile_dates[i] == date):
            deathTotal1 = deathTotal1 + sfile_deaths[i]
    return deathTotal

def returnCountyWithMostCasesOnDate(date):
    parseCountyData()
    parseStateData()

    val = 0
    index = 0
    for i in range(0, len(cfile_dates)):
        if (cfile_dates[i] == date):
            if (cfile_cases[i] > val):
                val = cfile_cases[i]
                index = i
    return index

def returnCountyWithMostDeathsOnDate(date):
    parseCountyData()
    parseStateData()

    val = 0
    index = 0
    for i in range(0, len(cfile_dates)):
        if (cfile_dates[i] == date):
            if (cfile_deaths[i] > val):
                val = cfile_deaths[i]
                index = i
    return index


def graphAllCountyCasesOnDate(date, countyList, stateList):
    parseCountyData()
    parseStateData()

    xvals = []
    yvals = []

    for i in range(0, len(cfile_dates)):
        if (cfile_dates[i] == date):
            for j in range(0, len(countyList)):
                if (countyList[j] == cfile_county[i]):
                    if (stateList[j] == cfile_state[i]):
                        print(cfile_county[i], countyList[j])
                        xvals.append(cfile_county[i])
                        yvals.append(cfile_cases[i])

    return {
        'x-axis': xvals,
        'y-axis': yvals,
        'x-label': "Counties",
        'y-label': "Cases"
    }

def createCounty():
    parseCountyData()

    county_name = input("What is the name of your county: ")
    county_state = input("What is the state of your county: ")

    countyObj = County_Store(county_name, county_state)
    for a in range(0,len(cfile_dates)):
        if (cfile_county[a] == countyObj.name):
            if(cfile_state[a] == countyObj.state):
                countyObj.addVal(cfile_dates[a], cfile_cases[a], cfile_deaths[a])
    return countyObj

def createState():
    parseStateData()
    state_name = input("What is the name of your state: ")

    stateObj = State_Store(state_name)
    for a in range(0,len(sfile_dates)):
        if(sfile_state[a] == stateObj.name):
            stateObj.addVal(sfile_dates[a], sfile_cases[a], sfile_deaths[a])
    return stateObj

parseStateData()
