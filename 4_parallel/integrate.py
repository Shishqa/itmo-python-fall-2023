import math
import sys
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing as mp
import logging

from common import timing


logging.basicConfig(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

log = logging.getLogger(__file__)
log.addHandler(stream_handler)


def split_by_count(lst, n_chunks):
    chunk_size = len(lst) // n_chunks

    start = 0
    while start < len(lst):
        end = min(start + chunk_size, len(lst))
        yield lst[start:end]
        start = end


def integrate_part(f, x_array, step):
    acc = 0
    log.info(f"started calculation of integral of {f.__name__} from {x_array[0]} to {x_array[-1]} with step {step}")
    for x in x_array:
        acc += f(x) * step
    log.info(f"integral of {f.__name__} on [{x_array[0]}, {x_array[-1]}] = {acc}")
    return acc


@timing
def integrate(f, a, b, *, pool_class = ThreadPoolExecutor, n_jobs=1, n_iter=100000000):
    acc = 0
    step = (b - a) / n_iter
    x_array = [a + i * step for i in range(n_iter)]

    with pool_class(max_workers=n_jobs) as pool:
        for res in pool.map(integrate_part, [f] * n_jobs, split_by_count(x_array, n_jobs), [step] * n_jobs):
            acc += res

    return acc


def run_with_executor(pool_class):
    log.info(f"running with executor {pool_class.__name__}")
    eps = 0.05
    results = []
    for n_jobs in range(1, mp.cpu_count() * 2 + 1):
        timing, res = integrate(math.cos, 0, math.pi / 2, n_jobs=n_jobs, pool_class=pool_class)
        assert 1 - eps < res < 1 + eps
        results.append((n_jobs, timing))

    with open(f"artifacts/{pool_class.__name__}.csv", "w") as fp:
        fp.write("n_jobs,time\n")
        for n_jobs, timing in results:
            fp.write(f"{n_jobs},{timing}\n")



if __name__ == "__main__":
    run_with_executor(ProcessPoolExecutor)
    run_with_executor(ThreadPoolExecutor)
