# Get Started

dj-raw-sql is just a wrapper over the [standard Django query](https://docs.djangoproject.com/en/4.1/topics/db/sql/#executing-custom-sql-directly)

This demo shows how to get the record(s) from the database

Example:

``` py title="queries.py" linenums="1"
def get_music_by_id(id: int):
    return "SELECT * FROM dj_app_music WHERE id = %s", (id,)
```

``` py title="models.py" linenums="1"
from django.db import models

# Our demo model
class Music(models.Model):
    name = models.CharField(max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
```

``` py title="views.py" linenums="1"
from django.http import JsonResponse
from django.views import View

from my_app.queries import get_music_by_id

from dj_raw_sql import QueryExecutor


class MyView(View):
    def get(self, request, *args, **kwargs):
        music: tuple[tuple] = QueryExecutor.fetchone(get_music_by_id, id=1)
        return JsonResponse({"name": music[0][1]})
```
