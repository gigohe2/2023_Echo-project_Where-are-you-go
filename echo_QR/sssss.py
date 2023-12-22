import queue

class NoDuplicatesQueue(queue.Queue):
    def put(self, item, block=True, timeout=None):
        if item not in self.queue:
            super().put(item, block, timeout)

# 사용 예시
q = NoDuplicatesQueue()
q.put((1,2))
q.put((1,2))  # 이미 존재하므로 추가되지 않음
q.put((2,3))

print(q.qsize())
while not q.empty():
    print(q.get())