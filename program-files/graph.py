from dataparser import graphAllCountyCasesOnDate
import matplotlib.pyplot as plt
bbox = {'fc': '0.8', 'pad': 0}
props = {'ha': 'left', 'va': 'bottom', 'bbox': bbox}

def graphDemoDeaths(countyToGraph):
    date1 = input("First date (write start for first instance): ")
    date2 = input("Second date (write end for last instance): ")
    if date1 == "start":
        date1 = countyToGraph.returnFirstDeath()
    if date2 == 'end':
        date2 = countyToGraph.returnLatestDeath()


    data = countyToGraph.graphDeathsFromTwoDates(date1, date2)
    plt.plot(data['x'], data['y'], linestyle='--', marker='o', color='r')
    plt.xlabel(data['x-label'])
    plt.ylabel(data['y-label'])
    plt.yscale('linear')
    # You can specify a rotation for the tick labels in degrees or with keywords.
    plt.xticks(rotation='vertical')
    # Pad margins so that markers don't get clipped by the axes
    plt.margins(0.05)
    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom=0.15)
    plt.grid(True)

    counter = 0
    for i_x, i_y in zip(data['x'], data['y']):
        counter = counter + 1
        if ((counter % 3) == 0):
            st = "(" + str(i_y) + ")"
            plt.text(i_x, i_y, st, props, rotation=0)
            # fontsize=12, rotation='90', rotation_mode='anchor'

    plt.show()

def graphDemoCases(countyToGraph):
    date1 = input("First date (write start for first instance): ")
    date2 = input("Second date (write end for last instance): ")
    if date1 == "start":
        date1 = countyToGraph.returnFirstCase()
    if date2 == 'end':
        date2 = countyToGraph.returnLatestCase()


    data = countyToGraph.graphCasesFromTwoDates(date1, date2)
    plt.plot(data['x'], data['y'], linestyle='--', marker='o', color='r')
    plt.xlabel(data['x-label'])
    plt.ylabel(data['y-label'])
    plt.yscale('linear')
    # You can specify a rotation for the tick labels in degrees or with keywords.
    plt.xticks(rotation='vertical')
    # Pad margins so that markers don't get clipped by the axes
    plt.margins(0.05)
    # Tweak spacing to prevent clipping of tick-labels
    plt.subplots_adjust(bottom=0.15)
    plt.grid(True)
    
    counter = 0
    for i_x, i_y in zip(data['x'], data['y']):
        counter = counter + 1
        if ((counter % 3) == 0):
            st = "(" + str(i_y) + ")"
            plt.text(i_x, i_y, st, props, rotation=0)
            # fontsize=12, rotation='90', rotation_mode='anchor'

    plt.show()



'''
data = graphAllCountyCasesOnDate("2020-04-02", ["Santa Clara", "Los Angeles", "Bibb", "Teton"], ["California", "California", "Alabama", "Wyoming"])
plt.bar(data['x-axis'], data['y-axis'])
plt.xlabel(data['x-label'])
plt.ylabel(data['y-label'])
plt.show()
'''
