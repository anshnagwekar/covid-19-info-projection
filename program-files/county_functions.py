class County_Store:
    dates = []
    fips = []
    cases = []
    deaths = []
    name = ''
    state = ''

    def __init__(self, name, state):
        self.name = name
        self.state = state


    def addVal (self, date, case, death):
        self.dates.append(date)
        self.cases.append(case)
        self.deaths.append(death)

    def returnFirstCase (self):
        for i in range(0, len(self.dates)):
            if (int(self.cases[i]) != 0):
                return self.dates[i]
        return "no cases in this county"

    def returnFirstDeath (self):
        for i in range(0, len(self.dates)):
            if (int(self.deaths[i]) != 0):
                return self.dates[i]
        return "no deaths in this county"

    def returnLatestCase (self):
        return self.dates[len(self.dates)-1]

    def returnLatestDeath (self):
        return self.dates[len(self.deaths)-1]

    def returnDeathCount (self):
        return self.deaths[len(self.deaths)-1]

    def returnCaseCount (self):
        return self.cases[len(self.cases)-1]
    
    def casesOnDate(self, referDate):
        flag = True
        for i in range(0,len(self.dates)):
            if (self.dates[i] == referDate):
                flag = True
                index = i
                break
            else:
                flag = False
        
        if (flag):
            if (index == 0):
                return self.cases[index]
            else: 
                return self.cases[index] - self.cases[index-1]
        else:
            return 0
    
    def deathsOnDate(self, referDate):
        flag = True
        
        for i in range(0,len(self.dates)):
            if (self.dates[i] == referDate):
                flag = True
                index = i
                break
            else:
                flag = False
        
        if (flag):
            if (index == 0):
                return self.deaths[index]
            else: 
                return self.deaths[index] - self.deaths[index-1]
        else:
            return 0
    
    def maxCases(self):
        maxNum = self.cases[0]
        maxDate = self.dates[0]

        for i in range(0, len(self.dates)):
            if(self.casesOnDate(self.dates[i]) >= maxNum):
                maxNum = self.casesOnDate(self.dates[i])
                maxDate = self.dates[i]

        return str(maxNum) + " on " + str(maxDate)
    
    def maxDeaths(self):
        maxNum = self.deaths[0]
        maxDate = self.dates[0]

        for i in range(0, len(self.dates)):
            if(int(self.deathsOnDate(self.dates[i])) >= maxNum):
                maxNum = self.deathsOnDate(self.dates[i])
                maxDate = self.dates[i]

        return str(maxNum) + " on " + str(maxDate)
    
    #precondition: date1 is before date2
    def graphCasesFromTwoDates(self, date1, date2):
        xvals = []
        yvals = []
        index1 = 0
        index2 = 0
        for i in range(0, len(self.dates)):
            if (self.dates[i] == date1):
               index1 = i
            if (self.dates[i] == date2):
                index2 = i
        
        for i in range(index1, index2+1):
            xvals.append(self.dates[i][-5:])
            yvals.append(self.cases[i])


        ylabeled = "Cases in " + self.name + ", " + self.state
        return {
            'x': xvals,
            'y': yvals,
            'x-label': "Dates",
            'y-label': ylabeled
        }

    def graphDeathsFromTwoDates(self, date1, date2):
        xvals = []
        yvals = []
        index1 = 0
        index2 = 0
        for i in range(0, len(self.dates)):
            if (self.dates[i] == date1):
               index1 = i
            if (self.dates[i] == date2):
                index2 = i
        
        for i in range(index1, index2+1):
            xvals.append(self.dates[i][-5:])
            yvals.append(self.deaths[i])

        ylabeled = "Deaths in " + self.name + ", " + self.state
        return {
            'x': xvals,
            'y': yvals,
            'x-label': "Dates",
            'y-label': ylabeled
        }