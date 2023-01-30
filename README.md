# dj-raw-sql

This is a Django wrapper to make it easier to write raw SQL queries.

## Get Started

This demo shows how to get the record(s) from the database

``` py title="queries.py" linenums="1"
# queries.py
from dj_raw_sql import execute_sql

@execute_sql()
def get_music_by_id(id: int):
    return "SELECT * FROM dj_app_music WHERE id = %s", (id,)
```

``` py title="models.py" linenums="1"
# models.py
from django.db import models

# Our demo model
class Music(models.Model):
    name = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
```

``` py title="views.py" linenums="1"
# views.py
from django.http import JsonResponse
from django.views import View

from my_app.queries import get_music_by_id


class MyView(View):
    def get(self, request, *args, **kwargs):
        music: tuple[tuple] = get_music_by_id(id=1)
        return JsonResponse({"name": music[0][1]})
```

## Benchmarks

**Q**: How were performance tests conducted?

**A**: tests/test_collection/ performance tests are located here. A dataset of 5000 elements was generated and loaded into the database. Then the query "SELECT * FROM dj_app_music LIMIT %s" was called, where the value of LIMIT changed from 10 to 5000 in each test.

---
Test results

| Number of items |    fetchall   | to_ordereddict=True |
|-----------------|:-------------:|:-------------------:|
| 10              | 0.00006       | 0.00011             |
| 100             | 0.00017       | 0.00025             |
| 1000            | 0.00138       | 0.00207             |
| 5000            | 0.00658       | 0.01052             |

## Improve project

If you want to improve the project then create "Issues" . If you want to help with writing tests or typing, create a "pull request".