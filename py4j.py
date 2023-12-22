from py2neo import Graph, Node, Relationship
graph = Graph(password='P@k!sTan2008')

# node1 = Node("Animal", name="Cat")
# graph.create(node1)
# node2 = Node("Object", name="Fur")
# graph.create(node2)
# node3 = Node("Person", name="Ali Raza")
# graph.create(node3)

# relationship = Relationship(node1, "HAS", node2)
# graph.create(relationship)
# relationship = Relationship(node3, "LIKES", node1)
# graph.create(relationship)
# relationship = Relationship(node3, "LIKES", node2)
# graph.create(relationship)


# Create relationships
graph.run(f"MATCH (p:person {{name: 'Bob'}}), (a:animal {{name: 'tommy'}}) CREATE (p)-[:HAS_PET]->(a)").evaluate()
graph.run(f"MATCH (p:person {{name: 'Alice'}}), (a:animal {{name: 'jerry'}}) CREATE (p)-[:HAS_PET]->(a)").evaluate()