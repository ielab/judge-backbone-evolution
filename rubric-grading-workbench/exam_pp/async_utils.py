import asyncio
from typing import Iterator, TypeVar, Awaitable, Callable, Tuple

A = TypeVar('A')
B = TypeVar('B')


class RateLimit:
    def __init__(self, rate: float):
        self.rate = rate
        self._sem = asyncio.Semaphore(1)

    async def limit(self):
        async def trigger():
            await asyncio.sleep(1. / self.rate)
            self._sem.release()

        await self._sem.acquire()
        asyncio.create_task(trigger())


class RateLimit2:
    def __init__(self, rate: float, dt: float=1):
        """
        rate given in events per second.
        dt is the integration period given in seconds.
        """
        self.rate = rate
        self.dt = dt
        self._count = 0
        self._lock = asyncio.Lock()
        self._cond = asyncio.Condition(self._lock)
        self._worker_task = asyncio.get_event_loop().create_task(self._worker())

    async def _worker(self):
        while True:
            async with self._lock:
                self._count = self.rate
                self._cond.notify_all()

            await asyncio.sleep(self.dt)

    async def limit(self, n: int=1):
        async with self._lock:
            await self._cond.wait_for(lambda: self._count >= n)
            self._count -= n


async def apply_concurrently(func: Callable[[A], Awaitable[None]], xs: Iterator[A], n_workers: int):
    queue: asyncio.Queue = asyncio.Queue(maxsize=4*n_workers)

    async def worker():
        while True:
            x = await queue.get()
            if x is None:
                queue.task_done()
                break
            try:
                try:
                    await func(x)
                except Exception as e:
                    import traceback
                    print(f"Worker caught exception: {e}")
                    traceback.print_exc()
            finally:
                queue.task_done()

    workers = [asyncio.create_task(worker(), name=f'worker {n}') for n in range(n_workers)]

    for x in xs:
        await queue.put(x)
        
    for _ in range(n_workers):
        await queue.put(None)

    await asyncio.gather(*workers)
