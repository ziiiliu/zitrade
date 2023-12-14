import asyncio
import time

class PeriodicWorker:
    def __init__(self, function, interval):
        self.function = function
        self.interval = interval
        self.is_running = False

    async def start(self):
        if self.is_running:
            print("Worker started.")
            return
        self.is_running = True
        await self._run()

    async def stop(self):
        if not self.is_running:
            print("Worker shut down.")
            return
        self.is_running = False

    async def _run(self):
        while self.is_running:
            self.function()
            await asyncio.sleep(self.interval)

# TODO
class Worker:
    def __init__(self, function):
        self.function = function
        self.is_running = False

    def start(self):
        if self.is_running:
            print("Worker Started")
            return
        self.is_running = True
        self._run()

    def stop(self):
        if not self.is_running:
            print("Worker shut down.")
            return
        self.is_running = False

    def _run(self):
        self.function()