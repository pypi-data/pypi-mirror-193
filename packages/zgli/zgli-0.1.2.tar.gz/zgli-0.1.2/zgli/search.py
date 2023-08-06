################# IMPORTS #################
import numpy as np

################# SEARCH ALGORITHMS #################
def bfs_dfs_search(args):
    
    graf = args[0]
    start = args[1]
    end = args[2]
    option = args[3]
    
    # Initialize queue. Queue starts by only having the 'start node'.
    queue = [(start,[start])]
    cicle = 1
    
    while queue:
        head = queue[0]  #(start,[start])
        rest = queue[1:] #[(ex1,[ex1]),(ex2,[ex2]),(ex3,[ex3]), ...]
        
        # If end reached, stop search
        if head[0] == end:
            break
            
        else:
            # Get ajacent noeds. They come in a tupule.
            expand = graf[head[0]] #('A',['A']) #( 'C' , 'B' )
            
            # Turn the tupule into an array so we can eddit it.
            expand = list(expand)
            
            # Expand format is as follows: (Adjacent,[pathToThisAdjacentNode])
            addToQueue = []
            for i, point in enumerate(expand):
                if point not in head[1]:
                    # Here we use o 'path + node' and not the .append().
                    # Check out the difference here: https://stackoverflow.com/questions/10748158/why-does-not-the-operator-change-a-list-while-append-does
                    addToQueue.append((expand[i],head[1] + [point]))
            
            # DFS: Depth first search   
            if option == 0: 
                queue = sorted(addToQueue) + rest
            
            # Breath first seach
            else: 
                queue = rest + sorted(addToQueue)
        
        # Cicle count if the user wants to see how many iterations it took
        cicle = cicle + 1
        
    return head[1][1:-1]

def cluster_path_search(args):
    
    '''
    Search for the path between 2 clusters. If the paths beeing uncovered are of lenght > 2, stop search early.

        Parameters
        ----------
        cluster_one : array_like
            Mother node of cluster one.
            
        cluster_two : array_like
            Mother node of cluster two.
            
        tree_graph : dict
            A graph describing the tree stucture.

        Returns
        -------
        path : array_like
            A list of max length 2, with the nodes corresponding to the path of the given clusters.

        Notes
        --------
        Function returns error if leafs are less than 6.
    '''
    
    graf = args[0]
    start = args[1]
    end = args[2]
    id_start = args[3]
    id_end = args[4]
    
    # print(f'Searching from {start} to {end}')
    
    # Initialize queue. Queue starts by only having the 'start node'.   
    queue = [(start,[start])]
    cicle = 1
    
    while queue:
        head = queue[0]  #(start,[start])
        rest = queue[1:] #[(ex1,[ex1]),(ex2,[ex2]),(ex3,[ex3]), ...]
        
        # If end reached, stop search
        if head[0] == end:
            return (id_start,id_end), tuple(head[1][1:-1])
            # return 'len(path) > 2'
            
        if len(head[1]) > 3:
            return 
            
        else:
            # Get ajacent noeds. They come in a tupule.
            expand = graf[head[0]] #('A',['A']) #( 'C' , 'B' )
            
            # Turn the tupule into an array so we can eddit it.
            expand = list(expand)
            
            # Expand format is as follows: (Adjacent,[pathToThisAdjacentNode])
            addToQueue = []
            for i, point in enumerate(expand):
                if point not in head[1]:
                    # Here we use o 'path + node' and not the .append().
                    # Check out the difference here: https://stackoverflow.com/questions/10748158/why-does-not-the-operator-change-a-list-while-append-does
                    addToQueue.append((expand[i],head[1] + [point]))
            
            # Breath first seach 
            queue = rest + sorted(addToQueue)
        
        # Cicle count if the user wants to see how many iterations it took
        cicle = cicle + 1
