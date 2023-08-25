from timeit import timeit

n=int(input())
b=int(input())


def kodeFibv1():
    for n in range(n):
        n+1

def kodeFibv2():
    for b in range(b):
        b+1


normal_tid:  float = timeit(stmt=kodeFibv1)
optimal_tid: float = timeit(stmt=kodeFibv2)

print(f"Normal tid:  {round(normal_tid, 4)} sekund.")
print(f"Optimal tid: {round(optimal_tid, 4)} sekund.") # denne er rask!