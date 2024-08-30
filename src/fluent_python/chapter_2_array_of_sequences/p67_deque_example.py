"""
>>> from collections import deque
>>> dq = deque(range(10), maxlen=10)
>>> dq
deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)
>>> dq.rotate(4)
>>> dq
deque([6, 7, 8, 9, 0, 1, 2, 3, 4, 5], maxlen=10)
>>> dq.rotate(-2)
>>> dq
deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7], maxlen=10)
>>> dq.append(128)
>>> dq
deque([9, 0, 1, 2, 3, 4, 5, 6, 7, 128], maxlen=10)
>>> dq.appendleft(-64)
>>> dq
deque([-64, 9, 0, 1, 2, 3, 4, 5, 6, 7], maxlen=10)
>>> dq.extend([20, 30, 40, 50])
>>> dq
deque([2, 3, 4, 5, 6, 7, 20, 30, 40, 50], maxlen=10)
>>> dq.extendleft([100, 200, 300])
>>> dq
deque([300, 200, 100, 2, 3, 4, 5, 6, 7, 20], maxlen=10)
"""