tmp = queue.dequeue()
    queue = recursive_reverse(queue)
    queue.enqueue(tmp)
    return queue