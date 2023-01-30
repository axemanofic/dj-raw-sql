# Get Started

This demo shows how to get the record(s) from the database

``` py title="queries.py" linenums="1"
from dj_raw_sql import execute_sql

@execute_sql()
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


class MyView(View):
    def get(self, request, *args, **kwargs):
        music: tuple[tuple] = get_music_by_id(id=1)
        return JsonResponse({"name": music[0][1]})
```
