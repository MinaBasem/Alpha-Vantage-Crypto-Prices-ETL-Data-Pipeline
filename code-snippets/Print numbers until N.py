import time

if __name__ == '__main__':
    n = int(input())
    number = 1
    print(number, end="", flush=True)
    while number < n:
        number = number + 1
        print(number, end="|", flush=True)
        n + 1
    
time.sleep(1000)
