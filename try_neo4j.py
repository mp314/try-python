# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "bolt://<HOST>:<BOLTPORT>", 
  auth=basic_auth("<USERNAME>", "<PASSWORD>"))

cypher_query = '''
MATCH (p:Product)-[:PART_OF]->(:Category)-[:PARENT*0..]->
(:Category {categoryName:$category})
RETURN p.productName as product
'''