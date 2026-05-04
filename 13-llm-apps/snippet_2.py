import time
from typing import Callable, TypeVar

T = TypeVar('T')

def retry_with_backoff(
    func: Callable[[], T],
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0
) -> T:
    """
    Retry a function with exponential backoff.

    Returns None if all retries fail, allowing graceful degradation.
    """
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            if attempt == max_retries - 1:
                return None
            delay = min(base_delay * (2 ** attempt), max_delay)
            time.sleep(delay)