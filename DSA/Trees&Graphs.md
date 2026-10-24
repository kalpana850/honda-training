# Trees and Graphs: Visual Understanding

1. What are Nodes and Edges?
- Node (Vertex): Represents an item or object.
- Edge: Represents a connection between two nodes.
Example: In a social network, people are nodes and friendships are edges.

2. What is a Tree?
A tree is a hierarchical data structure made up of nodes connected by edges. It has a root node and no cycles.

               A
              / \
             B   C
            / \
           D   E   

A is the root; B and C are its children; D and E are children of B

Important terms:
- Root: Topmost node (A).
- Parent: A node that has children (B is the parent of D).
- Child: A node connected below a parent.
- Leaf: A node with no children (C, D, E).
- Subtree: A smaller tree inside a larger tree.

Practical use: File and folder organization, company hierarchies, and website DOM structures.

3. What is a Graph?
A graph consists of nodes and edges that represent relationships. Unlike a tree, a graph can contain cycles and multiple paths between nodes.

       A -------- B
       |\        /| \
       | \      / |  \
       |  \    /  |   C
       |   \  /   |  /
       E -------- D


Each letter is a node; each line is an edge. Multiple routes connect the nodes.

Types of graphs:
- Undirected: Connections work both ways, like friendships.
- Directed: Connections have a direction, like Instagram follows.
- Weighted: Edges have values, like distances between cities.
Practical use: GPS navigation, social networks, and computer networks.

4. Tree vs. Graph

Feature	Tree	Graph
Structure	Hierarchical	General network
Root	Usually has one	Not required
Cycles	No cycles	May have cycles
Connections	Exactly one path between any two nodes	May have multiple paths
Example	Folder structure	Road network

5. What is Traversal?
Traversal means visiting nodes in a particular order.

Two important methods are:

# A. BFS — Breadth-First Search
Visits nodes level by level, using a queue.

For the tree above, starting at A:

A → B → C → D → E

Python example:

from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": [],
    "D": [],
    "E": []
}

queue = deque(["A"])

while queue:
    node = queue.popleft()
    print(node, end=" ")
    queue.extend(graph[node])

Output: A B C D E

# B. DFS — Depth-First Search

Explores one branch as far as possible before returning. It can be implemented using recursion or a stack.

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node in visited:
        return

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        dfs(graph, neighbor, visited)

dfs(graph, "A")

Output: A B D E C

Note: Traversal order depends on the order in which neighbors are stored.