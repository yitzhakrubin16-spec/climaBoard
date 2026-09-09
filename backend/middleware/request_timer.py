import time
from fastapi import Request

async def request_timer(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    end_time = time.time()

    duration = end_time - start_time

    response.headers["Response-duration"] = str(duration)

    return response