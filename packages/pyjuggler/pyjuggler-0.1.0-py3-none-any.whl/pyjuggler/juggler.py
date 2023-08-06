from concurrent.futures import ProcessPoolExecutor

from typing import List, Any


def run_process(func, args, workers: int = 8) -> List[Any]:
    final_result: List[Any] = []
    with ProcessPoolExecutor(max_workers=workers) as executor:
        results = executor.map(func, *zip(*args))
        for result in results:
            final_result.append(result)
    return final_result
