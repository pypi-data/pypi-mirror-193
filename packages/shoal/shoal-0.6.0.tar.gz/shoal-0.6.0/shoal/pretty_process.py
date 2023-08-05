"""Track delegated processes with rich progress meters.

Based on: https://www.deanmontgomery.com/2022/03/24/rich-progress-and-multiprocessing

"""

import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from time import sleep
from beartype.typing import Any, Callable, Dict, List
from rich.progress import Progress, BarColumn, TimeRemainingColumn, TimeElapsedColumn
import math
from beartype import beartype


@beartype
def _chunked(data: List[Any], count: int) -> List[List[Any]]:
    # TODO: See below link for other options for chunking
    #   https://realpython.com/how-to-split-a-python-list-into-chunks/
    size = len(data)
    chunk_size, chunk_rem = size // count, size % count
    chunk_size += int(math.ceil(chunk_rem / size))
    return [
        data[ix:ix + chunk_size] for ix in range(0, size, chunk_size)
    ]


@beartype
def pretty_process(delegated_task: Callable[[int, Dict, List], List], *, data: List[Any], num_workers: int = 3) -> List[Any]:
    futures = []  # keep track of the jobs
    with Progress(
        "[progress.description]{task.description}",
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
        TimeElapsedColumn(),
        refresh_per_second=1,
    ) as progress:
        # Share state between process and workers
        with multiprocessing.Manager() as manager:
            shared_progress = manager.dict()
            totals = {}
            task_id_all = progress.add_task("[green]All jobs progress:")

            with ProcessPoolExecutor(max_workers=num_workers) as executor:
                for ix, chunk in enumerate(_chunked(data, count=num_cpus)):
                    task_id = progress.add_task(f"task {ix}")
                    shared_progress[task_id] = 0
                    totals[task_id] = len(chunk)
                    futures.append(executor.submit(
                        delegated_task, task_id=task_id, shared_progress=shared_progress, data=chunk,
                    ))

                # Update progress bar from shared state
                remaining = len(futures)
                while remaining:
                    n_done = 0
                    for task_id, latest in shared_progress.items():
                        n_done += latest
                        progress.update(task_id, completed=latest, total=totals[task_id])
                    progress.update(task_id_all, completed=n_done, total=len(data))
                    remaining = len(futures) - sum([future.done() for future in futures])

                # Collect results and catch and errors
                return [future.result() for future in futures]


# Note: can't use beartype here
def _long_task(task_id: int, shared_progress: Dict, data: List[Any]) -> None:
    for val in data:
        sleep(1)
        shared_progress[task_id] += 1
    return val


if __name__ == "__main__":
    # Resolve number of cores or specified maximum
    num_cpus = 4
    try:
        import psutil
        num_cpus = psutil.cpu_count(logical=False)
    except Exception as exc:
        print(exc)

    result = pretty_process(_long_task, data=[*range(50)], num_workers=num_cpus)
    print(result)
