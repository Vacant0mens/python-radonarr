# Python: Sonarr Client

Asynchronous Python client for Sonarr and Radarr API's.

This project was derived from [ctalkington/python-sonarr](https://github.com/ctalkington/python-sonarr) (available via pypi/pip)

Since Sonarr and Radarr were created from the same roots, it's not hard to have them together.

## About

This package allows you to monitor Sonarr and Radarr instances.

## Installation

```bash
pip install sonarr
```

## Usage

```python
import asyncio

from radonarr import Sonarr, Radarr
import calendar
from datetime import datetime


async def main():
    """Show example of connecting to your Sonarr instance."""
    async with Sonarr("192.168.1.100", "API_TOKEN") as sonarr:
        # basic: simple api for monitoring purposes only.
        info = await sonarr.update()
        print(info)

        cal = await sonarr.calendar()
        print(cal)

        commands = await sonarr.commands()
        print(commands)

        queue = await sonarr.queue()
        print(queue)

        series = await sonarr.series()
        print(series)

        wanted = await sonarr.wanted()
        print(wanted)

    async with Radarr("192.168.1.100", "API_KEY", port=7878) as radarr:
        # basic: simple api for monitoring purposes only.
        info = await radarr.update()
        print(f"Update Info:\n{info.info}")
        print("\n--- Calendar ---")
        today = datetime.today()
        cal_range = calendar.monthrange(today.year, today.month)
        cal_start = datetime(today.year, today.month, 1).strftime('%Y-%m-%dT%H:%M:%SZ')
        cal_end = datetime(today.year, 8, cal_range[1]).strftime('%Y-%m-%dT%H:%M:%SZ')
        print(cal_start, cal_end)
        cal = await radarr.calendar(start=cal_start, end=cal_end)
        [print(f"{movie.title} -- Downloaded: {movie.downloaded} \
- InCinemas: {movie.in_cinimas} - ReleaseDate: {movie.physical_release} \
- Wanted: {movie.wanted}") for movie in cal]

        print('\n--- Running Commands ---')
        commands = await radarr.commands()
        print(commands)

        print('\n--- Movies in Queue ---')
        queue_items = await radarr.queue()
        [print(f"{queue.movie.title} ({queue.movie.year}) - Download: {queue.title} - Status: {queue.status} \
- DownloadStatus: {queue.download_status}") for queue in queue_items]

        print('\n--- Wanted Movies ---')
        wanteds = await radarr.wanted()
        [print(f"{wanted.title} -- InCinemas: {wanted.in_cinimas} \
- ReleaseDate: {wanted.physical_release}") for wanted in wanteds.movies]


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```
