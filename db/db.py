import psycopg2
from uhashring import HashRing

simple_node_list = [
    {
        "name": "node_1",
        "host": "localhost",
        "dbname": "postgres_1",
        "user": "postgres_1",
        "password": "postgres_1"
    },
    {
        "name": "node_2",
        "host": "localhost",
        "dbname": "postgres_2",
        "user": "postgres_2",
        "password": "postgres_2"
    },
    {
        "name": "node_3",
        "host": "localhost",
        "dbname": "postgres_3",
        "user": "postgres_3",
        "password": "postgres_3"
    }
]

def get_connection(value):
    nodes = list(map(lambda node: node["name"], simple_node_list))
    ring = HashRing(nodes=nodes)
    return ring.get_node(value)