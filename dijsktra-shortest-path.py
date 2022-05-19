# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 14:39:34 2021

@author: Fernando Baladi
"""

#A graph with data of the flights between airports and its price per person

mock_graph = {
    'CCS': {'AUA': 40, 'BON': 60, 'CUR': 35, 'SDQ': 180, 'POS': 150, 'BGI': 180},
    'AUA': {'CCS': 40, 'BON': 15, 'CUR': 15, 'SXM': 85},
    'BON': {'CCS': 60, 'AUA': 15, 'CUR': 15},
    'CUR': {'CCS': 35, 'AUA': 15, 'BON': 15, 'SXM': 80},
    'SXM': {'AUA': 85, 'CUR': 80, 'SDQ': 50, 'SBH': 45, 'POS': 90, 'BGI': 70, 'PTP': 100},
    'SDQ': {'CCS': 180, 'SXM': 50},
    'SBH': {'SXM': 45, 'PTP': 80},
    'POS': {'CCS': 150, 'SXM': 90, 'BGI': 35, 'FDF': 75, 'PTP': 80},
    'BGI': {'CCS': 180, 'SXM': 70, 'POS': 35},
    'FDF': {'POS': 75},
    'PTP': {'SXM': 100, 'SBH': 80, 'POS': 80}
}

#A dictionary with the airports and if they need a visa
visa_required = {'CCS':0, 'AUA':1, 'BON':1, 'CUR':1, 'SXM':1, 'SDQ':1, 'SBH':0, 'POS':0, 'BGI':0, 'FDF':0, 'PTP':0}

airports_code = ['Caracas\nCodigo: CCS', 'Aruba:\nCodigo: AUA', 'Bonaire\nCodigo: BON', 'Curaçao\nCodigo: CUR', 'Saint Martin\nCodigo: SXM', 
'Santo Domingo\nCodigo: SDQ', 'Saint Barthélemy\nCodigo: SBH', 'Port of Spain\nCodigo: POS', 'Barbados\nCodigo: BGI', 'Fort de France\nCodigo: FDF', 'Point a Pitre: PTP']


def dijkstra(mock_graph, departure, arrive, have_visa, care_about_cost):
    shortest_distance = {}
    predecessor = {}
    unseen_nodes = mock_graph
    path = []

    #This set all distances to infinity excepting the start node
    #'shortest_distance' dictionary have all the nodes and their distance

    for node in unseen_nodes:
        shortest_distance[node] = float('inf')
    shortest_distance[departure] = 0

    #Dijkstra algorithm

    while unseen_nodes: 
        
        min_node = None #Departure node

        for node in unseen_nodes:
            if min_node is None:
                min_node = node #This if set el first node as the min_node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node #It changes from a node to another if it has a minor distance
        
        
        #This section will get the child_node of our min_node (where we are) and their weight

        if care_about_cost==1:
            for child_node, weight in mock_graph[min_node].items(): #
                if visa_required[child_node] <= have_visa:
                    if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                        shortest_distance[child_node] = weight + shortest_distance[min_node]
                        predecessor[child_node] = min_node
        else:
            for child_node, weight in mock_graph[min_node].items(): 
                if visa_required[child_node] <= have_visa:
                    if 1 + shortest_distance[min_node] < shortest_distance[child_node]:
                        shortest_distance[child_node] = 1 + shortest_distance[min_node]
                        predecessor[child_node] = min_node
        
        unseen_nodes.pop(min_node) #We remove the min node (node ​​we visited) from our unvisited list


    # Draw the path that we'll "travel"
    current_node = arrive
    while current_node != departure:
        try:
            path.insert(0,current_node) #Insert the first node or current node because we are going back to front
            current_node = predecessor[current_node]
        
        except KeyError:
            print("Invalid path")
            break
    path.insert(0, departure)

    #Print cost
    if shortest_distance[arrive] != float('inf'):
        print('Shortest path cost ' + str(shortest_distance[arrive]))
        print('The path is ' + str(path))


#Asks if the user have visa

valid_visa_option = True
while valid_visa_option:
    try:
        have_visa = int(input("Do you have visa? Yes:1 , No:0\n"))
        print("="*50)
        while have_visa!=1 and have_visa!=0:
            print("="*50)   
            have_visa = int(input("Invalid input, please enter 1 or 0.\n Do you have visa? Yes:1 , No:0\n"))
        valid_visa_option = False
    except:
        valid_visa_option= True
        print("="*50)
        print("Letters or characters are not accepted, please enter 1 or 0")
        print("="*50)

#Asks if the user care about the cost (money)
#If the user doesn't care about the cost, 
#it means that he want the minimum amount of flights

valid_care_about_cost = True
while valid_care_about_cost:
    try:
        care_about_cost = int(input("Do you care about the cost of the travel? Yes:1 , No:0\n"))
        while care_about_cost !=0 and care_about_cost!=1:
            print("="*50)
            care_about_cost = int(input("Invalid input, please enter 1 or 0.\n Do you care about the cost of the travel? Yes:1 , No:0\n"))
        valid_care_about_cost = False
    except:
        valid_care_about_cost= True
        print("="*50)
        print("Letters or characters are not accepted, please enter 1 or 0")
        print("="*50)

    

# have_visa = 1 
# #No = 0; Yes = 1

print("="*50)
print("Below are the tourist places you can visit")
print("="*50)
for i in airports_code:
    print(i)
    print("="*50)



valid_departure=True
while valid_departure:
    try:
        departure = str(input("Indicate your departure place\n")).upper()
        print("="*50)
        while departure not in mock_graph.keys():
            print("="*50)
            departure = str(input("Invalid departure! Indicate your departure place\n"))
        valid_departure = False
    except:
        valid_departure=True
        print("="*50)
        print("Salida invalida")
        print("="*50)


valid_arrive=True
while valid_arrive:
    try:
        arrive = str(input("Indicate your arrival place\n")).upper()
        print("="*50)
        while arrive not in mock_graph.keys():
            print("="*50)
            arrive = str(input("Invalid arrival! Indicate your arrival place\n"))
        valid_arrive = False
    except:
        valid_arrive=True
        print("="*50)
        print("Salida invalida")
        print("="*50)
    

#check if the final airport requires a visa

if have_visa == 0:
    if visa_required[arrive] == 1:
        print("You can't go to that place because you don't have a visa")
    else:
        dijkstra(mock_graph, departure, arrive, have_visa, care_about_cost)
else:
    dijkstra(mock_graph, departure, arrive, have_visa, care_about_cost)