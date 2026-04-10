# Travel Budget Calculator (Per Person Model)
import heapq

#identifies heading and gives an underline
def heading(title):
    print("\n" + title)
    print("-" * len(title))

#a dictionary with each state and UN as key, has all travel cost data
data = {
    "Andhra Pradesh": {"hotel": 1400, "food": 600, "transport": 1800},
    "Arunachal Pradesh": {"hotel": 2200, "food": 700, "transport": 4000},
    "Assam": {"hotel": 1500, "food": 650, "transport": 2600},
    "Bihar": {"hotel": 1000, "food": 500, "transport": 1500},
    "Chhattisgarh": {"hotel": 1100, "food": 550, "transport": 1600},
    "Goa": {"hotel": 2500, "food": 900, "transport": 2800},
    "Gujarat": {"hotel": 1600, "food": 700, "transport": 2000},
    "Haryana": {"hotel": 1500, "food": 650, "transport": 1800},
    "Himachal Pradesh": {"hotel": 2000, "food": 750, "transport": 3000},
    "Jharkhand": {"hotel": 1100, "food": 550, "transport": 1700},
    "Karnataka": {"hotel": 1800, "food": 800, "transport": 2200},
    "Kerala": {"hotel": 2200, "food": 850, "transport": 3200},
    "Madhya Pradesh": {"hotel": 1300, "food": 600, "transport": 1800},
    "Maharashtra": {"hotel": 2600, "food": 900, "transport": 2800},
    "Manipur": {"hotel": 1800, "food": 700, "transport": 3500},
    "Meghalaya": {"hotel": 2000, "food": 750, "transport": 3200},
    "Mizoram": {"hotel": 1900, "food": 700, "transport": 3600},
    "Nagaland": {"hotel": 1900, "food": 700, "transport": 3500},
    "Odisha": {"hotel": 1400, "food": 600, "transport": 2000},
    "Punjab": {"hotel": 1600, "food": 700, "transport": 2000},
    "Rajasthan": {"hotel": 1700, "food": 650, "transport": 2300},
    "Sikkim": {"hotel": 2200, "food": 750, "transport": 3500},
    "Tamil Nadu": {"hotel": 1700, "food": 700, "transport": 2100},
    "Telangana": {"hotel": 1600, "food": 700, "transport": 2000},
    "Tripura": {"hotel": 1400, "food": 600, "transport": 3000},
    "Uttar Pradesh": {"hotel": 1400, "food": 600, "transport": 1800},
    "Uttarakhand": {"hotel": 2000, "food": 750, "transport": 2800},
    "West Bengal": {"hotel": 1600, "food": 650, "transport": 2000},
    "Delhi": {"hotel": 2200, "food": 800, "transport": 2200},
    "Jammu and Kashmir": {"hotel": 2100, "food": 750, "transport": 3200},
    "Ladakh": {"hotel": 3000, "food": 900, "transport": 4500},
    "Chandigarh": {"hotel": 1800, "food": 750, "transport": 1800},
    "Puducherry": {"hotel": 1700, "food": 700, "transport": 2300},
    "Andaman and Nicobar": {"hotel": 3500, "food": 1000, "transport": 6000},
    "Dadra and Nagar Haveli": {"hotel": 1400, "food": 650, "transport": 1800},
    "Daman and Diu": {"hotel": 1600, "food": 700, "transport": 2000},
    "Lakshadweep": {"hotel": 3800, "food": 1000, "transport": 6500}
}

# Build a simple graph using transport costs as weights
graph = {place: {} for place in data}

# For simplicity, assume direct travel possible between all states
for src in data:
    for dest in data:
        if src != dest:
            graph[src][dest] = data[dest]["transport"]

def dijkstra(start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        visited.add(node)
        if node == end:
            return (cost, path)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
    return (float("inf"), [])



#calling heading function, main title
heading("TripWise Budget Planner")

#converts all names into a list, to access with a number
places = list(data.keys())

#choosing a number
heading("Select a Destination")

for i in range(len(places)):
    print(f"{i+1}. {places[i]}")

#takes user input
choice = int(input("\nEnter destination number: "))

#checks if input is valid
if choice < 1 or choice > len(places):
    print("Invalid choice")
    exit()

#converts number to name of destination
destination = places[choice - 1]

origin = input("Enter your origin state/UT: ")

if origin not in data:
    print("Invalid origin")
    exit()

best_cost, best_path = dijkstra(origin, destination)

heading("Minimum Path Cost Search")

if best_path:
    print("Travel route:")
    for i, node in enumerate(best_path):
        if i < len(best_path) - 1:
            print(f"{node} -> ", end="")
        else:
            print(node)
    print(f"\nMinimum transport cost to reach {destination} from {origin}: {best_cost}")
else:
    print("No path found")

heading("Visual Path Output")

# Inputs
days = int(input("Enter number of days: "))
people = int(input("Enter number of people: "))
travel_type = input("Enter travel type (budget/standard/luxury): ").lower() #ensures input is correct
budget_per_person = int(input("Enter your budget per person: "))

#ensures values are positive
if days <= 0 or people <= 0:
    print("Invalid input")
    exit()

#puts cost values from dataset
hotel = data[destination]["hotel"]
food = data[destination]["food"]


#calculates per person cost
hotel_cost_pp = hotel * days
food_cost_pp = food * days
transport_cost_pp = best_cost

#total cost per person
total_per_person = hotel_cost_pp + food_cost_pp + transport_cost_pp

#adjusts cost according to selected budget type
if travel_type == "luxury":
    rate1=int(input("Enter its level from scale of [1-7]:"))
    total_per_person *= rate1
elif travel_type == "standard":
    rate2=int(input("Enter its level from scale of [1-3]:"))
    total_per_person *= rate2

# Predictive model
predicted_cost_pp = 300 * days + 700 * people + 1000
final_per_person = (total_per_person + predicted_cost_pp) / 2

#total group cost
total_group_cost = final_per_person * people

# Output
heading("Selected Destination")
print(destination)

heading("Cost Breakdown (Per Person)")
print("Hotel:", hotel_cost_pp)
print("Food:", food_cost_pp)
print("Transport:", transport_cost_pp)

print("\nFinal cost per person:", int(final_per_person))
print("Total cost for group:", int(total_group_cost))

#analysing the budget

heading("Budget Analysis")

if final_per_person > budget_per_person:
    print("Trip exceeds your budget per person")
else:
    print("Trip is within your budget per person")

# Comparing all destinations
heading("Cheapest Destination")

costs = {}

for place in data:
    h = data[place]["hotel"]
    f = data[place]["food"]
    t = data[place]["transport"]

    cost_pp = (h * days) + (f * days) + t

    if travel_type == "luxury":
        cost_pp *= 2
    elif travel_type == "standard":
        cost_pp *= 1.5

    costs[place] = cost_pp

cheapest = min(costs, key=costs.get)

print(cheapest)
print("Cost per person:", int(costs[cheapest]))

# Suggestions
heading("Suggestions")

if final_per_person > budget_per_person:
    print("Reduce days or choose budget travel")

if people >= 4:
    print("Group travel can reduce cost")

if days >= 5:
    print("Look for long stay discounts")

if travel_type == "luxury":
    print("Standard travel can save money")

print("Book early to reduce costs")
