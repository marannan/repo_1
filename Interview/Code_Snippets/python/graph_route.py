#find route between two nodes

state = ["unvisited", "visiting", "visited"]

def is_route_exists(graph, start, end):
    if graph == None or start == None or end == None:
        return False
    
    if start == end:
        return True
    
    #queue
    node_queue = []
    
    #set all nodes as unvisited
    for node in graph:
        node.state = state[0]
     
     #add start to the queue   
    start.state = state[1]  
    node_queue.append(start)
    
    #take first element from queue and check all its neighbours #this is bfs but dfs can also be used
    while len(node_queue) != 0:
        node = node_queue.pop(0) 
        if node != None:
            for adj_node in graph.get_adajacent(node):
                if adj_node.state == state[0]:
                    if adj_node == end:
                        return True
                    else:
                        adj_node.state = state[1]
                        node_queue.append(adj_node)
            node.state = state[2]
            
    return False
                
            
    
    
    