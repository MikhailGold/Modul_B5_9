import time


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {:.3f} секунд.'.format(end-start))
        return return_value
    return wrapper


def benchmark_par(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(1, iters+1):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print("Количество попыток: ", iters)
            print('[*] Среднее время выполнения: {} секунд.'.format(total/iters))
            return return_value
        return wrapper
    return actual_decorator


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


@benchmark_par(3)
def fetch_webpage_1(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


class benchmark_class:
    def __init__(self, iters=10):
        self.iters = iters
        self.avg_time = 0
        self.t0 = 0
        self.t1 = 0

    def __call__(self, func):
        def wrap(*args, **kwargs):
            avg_t = 0
            for i in range(self.iters):
                t0 = time.time()
                func(*args, **kwargs)
                t1 = time.time()
                avg_t += (t1 - t0)

            self.avg_time = avg_t/self.iters
            print("[*]Среднее время выполнения 1 запуска из",
                  self.iters, "заняло %.5f секунд" % self.avg_time)
        return wrap

    def __enter__(self):
        self.t0 = time.time()
        return self

    def __exit__(self, type, value, traceback):
        self.t1 = time.time()
        print("[*]Время выполнения 1 запуска заняло %.5f секунд" %
              (self.t1 - self.t0))
        return self

print("Время до www.psu.by")
webpage=fetch_webpage("https://www.psu.by")
print("Время до www.nur.kz")
webpage=fetch_webpage("https://www.nur.kz")

print("Расчет среднего времени выполнения(Используем декоратор с параметром)")

print("Время до www.psu.by")
webpage = fetch_webpage_1("https://www.psu.by")
print("Время до www.nur.kz")
webpage = fetch_webpage_1("https://www.nur.kz")


print("Декоратор класс - секундомер")
@benchmark_class(iters=3)
def pause():
    import time
    time.sleep(1)

pause()


def pause_2():
    import time
    time.sleep(2)


with benchmark_class() as tf:
    pause_2()
