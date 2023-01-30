import json, pathlib, time
from typing import Callable

from dj_app.models import Music


def make_music():
    path = pathlib.Path() / "tests" / "test_collections" / "data" / "db.json"
    f = open(path.absolute())
    data = json.load(f)
    for i in data:
        Music.objects.create(name=i["name"])


def measure_execution_time(func, number_elements):
    t_start = time.monotonic()
    func(number_elements)
    t_end = time.monotonic()
    t_run = t_end - t_start
    print(f"Time execution: {t_run:.5f} for {number_elements} elements")
