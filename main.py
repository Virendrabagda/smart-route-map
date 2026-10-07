from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import connection
from graph import g, city_index, cities

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/cities")
def get_cities():
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM cities")

    cities = cursor.fetchall()

    cursor.close()

    return cities

@app.get("/routes")
def get_routes():
    cursor = connection.cursor()
    query = """
    SELECT 
        routes.id,
        source.name,
        destination.name,
        routes.distance
    FROM routes
    JOIN cities AS source ON routes.source_id = source.id
    JOIN cities AS destination ON routes.destination_id = destination.id"""

    cursor.execute(query)


    routes = cursor.fetchall()

    cursor.close()

    return routes
@app.get("/shortest-route")
def shortest_route(source: str, destination: str):

    source = source.lower()
    destination = destination.lower()

    source_index = city_index[source]
    destination_index = city_index[destination]

    distance, parent = g.dijkstra(source_index)
    path = []
    node = destination_index

    while node != -1:
        path.append(node)
        node = parent[node]

    path.reverse()

    route = []

    for node in path:
        route.append(cities[node])

    return {
        "source": source,
        "destination": destination,
        "route": route,
        "distance": distance[destination_index]
    }