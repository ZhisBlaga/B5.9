import time

class Time_this:
    def __init__(self,num_runs=1):
        self.num_runs = num_runs
    #Декоратор
    def __call__(self, fn):
        avg_time = 0
        for _ in range(self.num_runs):
            t0 = time.time()
            #Вызов функции
            fn()

            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.num_runs
        print("Выполнение заняло %.5f секунд" % avg_time)

#количество запусков можно менять.
num_runs=100
@Time_this(num_runs)
def f():
    for j in range(1000000):
        pass
