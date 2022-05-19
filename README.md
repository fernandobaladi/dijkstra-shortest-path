# Dijkstra's Shortest Path by Fernando Baladi

This algorithm calculates the shortest path for traveling between some airports in a mock graph, taking into consideration if the user have visa and if they want the shortest path or the cheapest path.

## Graph

The graph is a dictionary of dictionaries, where every airport code have a dictionary with the flights to other airports and their cost.

## How to use it

The algorithm starts asking the user four questions:

* Do you have visa?: Because some cities needs visa to enter.
* Do you care about the cost of the travel?: If the user enter yes, it will calculate the cheapest path. If the user enter no, it will calculate the shortest path.
* Indicate your departure place: Where the user want to start the "travel". A three letters airport code
* Indicate your arrival place: Where the user want to end the "travel". A three letters airport code


## Airports

These are the airports and their codes. You are free to download and add other airport and find other routes.

| Codes      | Airports |
| ----------- | ----------- |
| CCS   | Caracas       |
| AUA   | Aruba        |
| BON   | Bonaire        |
| CUR   | Curaçao        |
| SXM	| Saint Martin        |
| SDQ	| Santo Domingo        |
| SBH	| Saint Barthélemy        |
| POS	| Port of Spain (Trinidad and Tobago)        |
| BGI	| Barbados        |	
| FDF	| Fort-de-France (Martinica)        |	
| PTP	| Point-a-Pitre (Guadalupe)        |
## Requirements

* Python3 (any version)