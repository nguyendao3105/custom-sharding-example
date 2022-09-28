import psycopg2
from uhashring import HashRing

simple_node_list = [
    {
        "name": "node_1",
        "host": "127.0.0.1",
        "dbname": "postgres_1",
        "user": "postgres_1",
        "password": "postgres_1",
        "port": "5432"
    },
    {
        "name": "node_2",
        "host": "127.0.0.1",
        "dbname": "postgres_2",
        "user": "postgres_2",
        "password": "postgres_2",
        "port": "5433"
    },
    {
        "name": "node_3",
        "host": "127.0.0.1",
        "dbname": "postgres_3",
        "user": "postgres_3",
        "password": "postgres_3",
        "port": "5434"
    }
]

def get_connection(value):
    nodes = list(map(lambda node: node["name"], simple_node_list))
    ring = HashRing(nodes=nodes)
    node_name = ring.get_node(value)
    node = get_node_properties(node_name=node_name, node_list=simple_node_list)
    connection_string = f"host={node['host']} port={node['port']} dbname={node['dbname']} user={node['user']} password={node['password']}"
    print(connection_string)
    return psycopg2.connect(connection_string), node

def get_node_properties(node_name, node_list):
    for node in node_list:
        if node["name"] == node_name:
            return node
    return None
    