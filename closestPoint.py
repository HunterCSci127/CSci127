#CSci 127 Teaching Staff
#October 2017
#A template for a program that finds & marks closest point.
#Modified by:  ADD YOUR NAME HERE

import folium
import pandas as pd



def getData():
     """
     Asks the user for the name of the CSV and
     Returns a dataframe of the contents.
     """

     df = None #<-- placeholder, can remove once defined.

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ###################################

     return(df)

def getColumnNames():
     """
     Asks the user for the exact name of the columns that
     contains the latitude and longitude and
     Returns those values as a tuple.
     """

     latName, lonName = "", "" #<-- placeholder, can remove once defined.

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ###################################

     return(latName,lonName)


def getLocale():
     """
     Asks the user for latitude and longitude of the user's current location and
     Returns those floating points numbers.

     """

     lat, lon = 0.0,0.0      #<-- placeholder, can remove once defined.

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ###################################

     return(lat, lon)

def computeDist(x1,y1,x2,y2):
     """
     Computes the squared distance between two points (x1,y1) and (x2,y2) and
     Returns (x1-x2)^2 + (y1-y2)^2
     """
     d = 0.0   #<-- placeholder, can remove once defined.

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ###################################

     return(d)



######################################################################
### DO NOT CHANGE ANYTHING BELOW AND INCLUDING THIS LINE           ###
######################################################################

def dotAllPoints(cMap,df,latCol,lonCol):
     """
     Mark all points in the latCol, lonCol with dots (little circle markers)
     """
     for i, row in df.iterrows():
          folium.CircleMarker(location=[row[latCol],row[lonCol]], radius=4,color='red').add_to(cMap)


def markAndFindClosest(cMap,df,latCol,lonCol,cLat,cLon):
     """
     Goes through the list of points, marking each with a circle marker.
     Finds the closest point using the computeDist() function and
     Returns the lat and lon of closest point.
     """

     #Find closest marker:
     df['Dist'] = df[[latCol,lonCol]].apply(lambda row: computeDist(*row,cLat,cLon), axis=1)
     minRow = df[df['Dist'] == df['Dist'].min()]

     #Make a marker for the closest point:
     folium.Marker(location=[float(minRow[latCol]),float(minRow[lonCol])],
                   popup="Closest").add_to(cMap)
     #Make a marker for the starting point
     folium.Marker(location=[cLat,cLon],
                   popup="You Are Here",
                   icon=folium.Icon(color='red')).add_to(cMap)


def writeMap(cMap):
     """
     Writes the inputted map, cMap, to the file specified by the user.
     """
     outF = input('Enter output file: ')
     cMap.save(outfile=outF)



def main():
     dataF = getData()
     latColName, lonColName = getColumnNames()
     lat, lon = getLocale()
     cityMap = folium.Map(location = [lat,lon], tiles = 'cartodbpositron',zoom_start=11)
     dotAllPoints(cityMap,dataF,latColName,lonColName)
     markAndFindClosest(cityMap,dataF,latColName,lonColName,lat,lon)
     writeMap(cityMap)


if __name__ == "__main__":
     main()
