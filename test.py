from collections import deque

MAX_LEN = 5

elements = "Al"

lifo = deque(['Nick', 'Bob', 5, 6, 7], maxlen = MAX_LEN)
# print(lifo)
# print(type(lifo))
print(lifo)
def push(element):
    lifo.appendleft(element)
    #print(lifo)
    return lifo

lifo = push(elements)

def pop():
    result = lifo.popleft()
    #print(result)
    return result


print(lifo)
print(pop())
print(lifo)


# d = deque()
# d.append('last')
# d.appendleft('first')
# d.insert(0, 'middle')
# print(d)  # deque(['first', 'middle', 'last'])

# print(d.pop())  # 'last'
# print(d.popleft())  # 'first'
# print(d)  # deque(['middle'])