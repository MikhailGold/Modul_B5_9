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
            for i in range(1,iters+1):
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


class benchmark_class(object):
    def start(self):
        self.start = time.time()
        return self
    def end(self, *args, **kwargs):
        self.end = time.time()
        print('[*] Время выполнения: {:.3f} секунд.'.format(self.end-self.start))

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
a = benchmark_class()
a.start()
time.sleep(5)
a.end()
