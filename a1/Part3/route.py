#!/usr/local/bin/python3
# route.py : Find routes through maps
#
# Code by: lharwin-aniiyer-a1 (Laya Harwin and Anirudh Iyer)
#
# Based on skeleton code by V. Mathur and D. Crandall, Fall 2022
#


# !/usr/bin/env python3
import sys
from functools import total_ordering
from queue import PriorityQueue
import math

def Cost_Function_Distance(start, end):
    Visited = []
    Fringe_Priority_Queue = PriorityQueue()
    Fringe_Priority_Queue.put((0, start, [], 0))

    Segments = Get_Road_Segments()

    with open('city-gps.txt', "r") as f:
                City_GPS_File=  {line.split()[0]: tuple(line.split()[1:]) for line in f.read().rstrip("\n").split("\n")}
    End_City = City_GPS_File.get(end)

    while not Fringe_Priority_Queue.empty():
        (Cost, Present_City, Path_Travelled, Real_Distance) = Fringe_Priority_Queue.get()
        if Present_City == end:
            return Path_Travelled
        for i in Segments[Present_City]:
            if i in Visited:
                continue
            if i[1] == Present_City:
                i[0], i[1] = i[1], i[0]
            if i[0] == Present_City:
                h = Heuristic_Haversine(City_GPS_File.get(i[1]), End_City)/2
                Fringe_Priority_Queue.put( (Real_Distance + h, i[1], Path_Travelled + [i], Real_Distance + int(i[2])))
                Visited.append(i)
    return []

def Cost_Function_Segments(start, end):
    Visited = []
    Fringe_Priority_Queue = PriorityQueue()
    Fringe_Priority_Queue.put((0, start, []))

    Segments = Get_Road_Segments()
    with open('city-gps.txt', "r") as f:
                City_GPS_File=  {line.split()[0]: tuple(line.split()[1:]) for line in f.read().rstrip("\n").split("\n")}
    End_City = City_GPS_File.get(end)

    while not Fringe_Priority_Queue.empty(): 
        (Total_no_of_Segments , Present_City, Path_Travelled) = Fringe_Priority_Queue.get()
        if Present_City == end:
            return Path_Travelled
        for i in Segments[Present_City]:
            if i in Visited:
                continue
            if i[1] == Present_City:
                i[0], i[1] = i[1], i[0]
            if i[0] == Present_City:
                h = (Heuristic_Haversine(City_GPS_File.get(i[1]), End_City)/932)/2.5 # here 923 is the segment distance of largest segment
                Fringe_Priority_Queue.put( (len(Path_Travelled + [i]) + h, i[1], Path_Travelled + [i]))
                Visited.append(i)
    return []

def Cost_Function_Time(start, end):
    Visited = []
    Fringe_Priority_Queue = PriorityQueue()
    Fringe_Priority_Queue.put((0, start, [], 0))

    Segments = Get_Road_Segments()

    with open('city-gps.txt', "r") as f:
                City_GPS_File=  {line.split()[0]: tuple(line.split()[1:]) for line in f.read().rstrip("\n").split("\n")}
    End_City = City_GPS_File.get(end)

    while not Fringe_Priority_Queue.empty():
        (Time, Present_City, Path_Travelled, Real_Time) = Fringe_Priority_Queue.get()
        if Present_City == end:
            return Path_Travelled
        for i in Segments[Present_City]:
            if i in Visited:
                continue
            if i[1] == Present_City:
                i[0], i[1] = i[1], i[0]
            if i[0] == Present_City:
                h= (Heuristic_Haversine(City_GPS_File.get(i[1]), End_City)/65)/60
                Fringe_Priority_Queue.put( (Real_Time + h, i[1], Path_Travelled + [i], Real_Time + int(i[2])/int(i[3])))
                Visited.append(i)
    return []

def Cost_Function_Delivery(start, end):
    Visited = []
    Fringe_Priority_Queue = PriorityQueue()
    Fringe_Priority_Queue.put((0, start, [], 0))

    Segments = Get_Road_Segments()

    with open('city-gps.txt', "r") as f:
                City_GPS_File=  {line.split()[0]: tuple(line.split()[1:]) for line in f.read().rstrip("\n").split("\n")}
    End_City = City_GPS_File.get(end)

    while not Fringe_Priority_Queue.empty():
        (Delivery, Present_City, Path_Travelled, Real_Delivery_Hours) = Fringe_Priority_Queue.get()
        if Present_City == end:
            return Path_Travelled
        for i in Segments[Present_City]:
            if i in Visited:
                continue
            if i[1] == Present_City:
                i[0], i[1] = i[1], i[0]
            if i[0] == Present_City:
                h=  (Heuristic_Haversine(City_GPS_File.get(i[1]), End_City)/65)/60
                Fringe_Priority_Queue.put( (Real_Delivery_Hours + h, i[1], Path_Travelled + [i], Real_Delivery_Hours + Determine_D_Hours(i, Real_Delivery_Hours)))
                Visited.append(i)
    return []


def get_route(start, end, cost):
    
    """
    Find shortest driving route between start city and end city
    based on a cost function.
    1. Your function should return a dictionary having the following keys:
        -"route-taken" : a list of pairs of the form (next-stop, segment-info), where
           next-stop is a string giving the next stop in the route, and segment-info is a free-form
           string containing information about the segment that will be displayed to the user.
           (segment-info is not inspected by the automatic testing program).
        -"total-segments": an integer indicating number of segments in the route-taken
        -"total-miles": a float indicating total number of miles in the route-taken
        -"total-hours": a float indicating total amount of time in the route-taken
        -"total-delivery-hours": a float indicating the expected (average) time 
                                   it will take a delivery driver who may need to return to get a new package
    2. Do not add any extra parameters to the get_route() function, or it will break our grading and testing code.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """

    # Initializing the varibale that finds the final path based on cost function
    route_taken = []
     
    # Calculating final path based on cost function 
    if cost == 'distance':
        route_taken = Cost_Function_Distance(start, end)
    elif cost == 'segments':
        route_taken = Cost_Function_Segments(start, end)
    elif cost == 'time':
        route_taken = Cost_Function_Time(start, end)
    elif cost == 'delivery':
        route_taken = Cost_Function_Delivery(start, end)
    
    # Initializing variables to calculate the final route taken, total miles travelled, total hours travelled and total delivery hours
    Total_Delivery_Hours = 0.00
    Total_Miles_Travelled = 0.00
    Final_Route_Taken = []
    Total_Hours_Taken = 0.00

    # After finding the final path, calculating the final route taken, total miles travelled, total hours travelled and total delivery hours 
    for i in route_taken:
            Total_Miles_Travelled += float(i[2])
            Total_Hours_Taken += float(i[2])/float(i[3])
            Total_Delivery_Hours += Determine_D_Hours(i, Total_Delivery_Hours)
            Final_Route_Taken.append((i[1], f'{i[4]} for {i[2]} miles'))
    
    return {"total-segments" : len(Final_Route_Taken), 
            "total-miles" : Total_Miles_Travelled, 
            "total-hours" : Total_Hours_Taken, 
            "total-delivery-hours" : Total_Delivery_Hours, 
            "route-taken" : Final_Route_Taken}

def Determine_D_Hours(i, t=0):
    if float(i[3]) < 50:
        return float(i[2])/float(i[3])
    return float(i[2])/float(i[3]) + ( (math.tanh( float(i[2]) /1000 )) * 2 * (float(i[2])/float(i[3]) + t))
                
def Get_Road_Segments():
    Map = {}
    with open('road-segments.txt', "r") as f:
            for i in f.read().rstrip("\n").split("\n"):
                start = i.split()[0]
                end = i.split()[1]
                if start in Map:
                    Map[start].append(i.split())
                else:
                    Map[start] = [i.split()]
                if end in Map:
                    Map[end].append(i.split())
                else:
                    Map[end] = [i.split()]
            return Map

def Heuristic_Haversine(point_1, point_2):
    if point_1 == None or point_2 == None:
        return 0
    Earth_Radius = 6371  # Earth radius
    latitude_1, longitude_1 = (float(x) for x in point_1)
    latitude_2, longitude_2 = (float(x) for x in point_2)
    return Earth_Radius * 2 * math.asin(math.sqrt(math.sin((latitude_2 - latitude_1)/2)**2 + math.cos(latitude_1) * math.cos(latitude_2) * math.sin((longitude_2 - longitude_1 )/2)**2))

# Please don't modify anything below this line
#
if __name__ == "__main__":
    
    if len(sys.argv) != 4:
        raise(Exception("Error: expected 3 arguments"))

    (_, start_city, end_city, cost_function) = sys.argv
    if cost_function not in ("segments", "distance", "time", "delivery"):
        raise(Exception("Error: invalid cost function"))

    result = get_route(start_city, end_city, cost_function)

    # Pretty print the route
    print("Start in %s" % start_city)
    for step in result["route-taken"]:
        print("   Then go to %s via %s" % step)

    print("\n          Total segments: %4d" % result["total-segments"])
    print("             Total miles: %8.3f" % result["total-miles"])
    print("             Total hours: %8.3f" % result["total-hours"])
    print("Total hours for delivery: %8.3f" % result["total-delivery-hours"])
