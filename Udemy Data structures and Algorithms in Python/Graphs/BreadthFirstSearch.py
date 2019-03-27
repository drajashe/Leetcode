#visit dictionary will have the pointer indicating whether a node is visited or no
#queue will maintain the the node which is visited for checking its neighbours
import queue
#https://www.youtube.com/channel/UCliJsnOQEU9ZkWEE7Vtryng/videos
# From class queue, Queue is
# created as an object Now L
# is Queue of a maximum
# capacity of 20
L = queue.Queue(maxsize=20)

# Data is inserted into Queue
# using put() Data is inserted
# at the end
L.put(5)
L.put(9)
L.put(1)
L.put(7)
def bfs(i,n):
    visited={}
    #initialisation
    for j in range(1,n):
        visited[j]=0

    return (visited)
print(bfs(1,5))
