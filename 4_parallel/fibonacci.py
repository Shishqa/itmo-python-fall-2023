import sys
import logging
import threading
import multiprocessing as mp

from common import timing

logging.basicConfig(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

log = logging.getLogger(__file__)
log.addHandler(stream_handler)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def worker(tag):
    num = 38
    log.info(f"worker_{tag} | started calculation of fib({num})")
    res = fibonacci(num)
    log.info(f"worker_{tag} | stopped calculation, fib({num}) = {res}")


@timing
def fib_synchronous(num_repetitions):
    for i in range(num_repetitions):
        worker(i)


@timing
def fib_threads(num_repetitions):
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(num_repetitions)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


@timing
def fib_processes(num_repetitions):
    processes = [mp.Process(target=worker, args=(i,)) for i in range(num_repetitions)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()


if __name__ == "__main__":
    num_repetitions = 10
    fib_synchronous(num_repetitions)
    fib_threads(num_repetitions)
    fib_processes(num_repetitions)
