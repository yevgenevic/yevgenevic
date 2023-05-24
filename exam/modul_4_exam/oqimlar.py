import threading

import httpx


def oqim1():
    url = "https://www.olx.uz/"
    response = httpx.get(url)
    print(f"Oqim1 natija:{url}", response.status_code)


def oqim2():
    url = "https://olcha.uz/ru"
    response = httpx.get(url)
    print(f"Oqim2 natija:{url}", response.status_code)


def oqim3():
    url = "https://uzum.uz/uz"
    response = httpx.get(url)
    print(f"Oqim3 natija:{url}", response.status_code)


def oqim4():
    url = "https://korzinka.uz/uz"
    response = httpx.get(url)
    print(f"Oqim4 natija:{url}", response.status_code)


def oqim5():
    url = "https://uz.wildberries.ru/"
    response = httpx.get(url)
    print(f"Oqim5 natija:{url}", response.status_code)


thread1 = threading.Thread(target=oqim1)
thread2 = threading.Thread(target=oqim2)
thread3 = threading.Thread(target=oqim3)
thread4 = threading.Thread(target=oqim4)
thread5 = threading.Thread(target=oqim5)

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()

print("Barcha oqimlar bajarildi")
