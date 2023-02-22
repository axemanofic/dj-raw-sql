# OrderedDictQueryExecutor

This class inherits from QueryExecutor and modifies methods for outputting data.

Changed Methods:

1. fetchall - returns list[OrderedDict], i.e. suitable for queries like 'SELECT * FROM table'
2. fetchone - returns one entry as a OrderedDict

Example:

``` py title="queries.py" linenums="1"
def get_all_music():
    return "SELECT * FROM dj_app_music"

def get_music_by_id(id: int):
    return "SELECT * FROM dj_app_music", (id,)
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

from dj_raw_sql import OrderedDictQueryExecutor


class AllMusicView(View):
    def get(self, request, *args, **kwargs):
        musics: tuple[tuple] = OrderedDictQueryExecutor.fetchall(get_all_music)
        result = []

        for music in musics:
            result.append({"id": music["id"], "name": music["name"]})

        return JsonResponse({"result":result})


class MusicView(View):
    def get(self, request, *args, **kwargs):

        music: tuple[tuple] = OrderedDictQueryExecutor.fetchone(get_music_by_id, id=1)

        return JsonResponse({"result": music["name"]})
```
