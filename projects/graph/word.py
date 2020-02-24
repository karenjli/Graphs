from util import Stack, Queue
 
f=open('words.txt','r')
words = f.read().split("\n")
f.close()

word_set=set(words)
print(word_set)


def find_ladders(begin_word, end_word):
    # Using BFS
    # BFS provides the shortest path from one word to another
    
    # Create a queue
    q = Queue()
    # Enqueue path to starting word
    q.enqueue([begin_word])
    # Initialize visited set
    visited=set()
    # While the queue is not empty
    while q is not None:
        # Dequeue path
        path = q.dequeue()
        # Grab last word from path
        w = path[-1]
        # Check if it's been visited. If not...
        if w == end_word:
            return path
        # Check if it's been visited, if not...
        if w not in viisted:
            # Mark as visited
            visited.append(w)
    