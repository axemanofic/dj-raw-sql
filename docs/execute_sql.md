# Execute sql

This decorator allows you to execute raw sql query and also apply different parameters to it

=== "Using a decorator"

    ``` py linenums="1"
    from dj_raw_sql import execute_sql

    @execute_sql()
    def get_music_by_id(id: int):
        return "SELECT * FROM dj_app_music WHERE id = %s", (id,)
    ```

=== "Without using a decorator"

    ``` py linenums="1"
    from django.db import connection

    def my_custom_sql(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM dj_app_music WHERE id = %s", (id, ))
            row = cursor.fetchall()

        return row
    ```

And this is how you get the value

``` py title="views.py" linenums="1"
from django.http import JsonResponse
from django.views import View

from my_app.queries import get_music_by_id

class MyView(View):
    def get(self, request, *args, **kwargs):
        music: tuple[tuple] = get_music_by_id(id=1)
        return JsonResponse({"name": music[0][0]})
```

## Option `#!python to_ordereddict=True`

If you want to return not a "tuple with tuples" then you can use this option to return a list of ordered dictionaries.

!!! danger "Attention"
    If performance and fractions of a second for a response are VERY VERY important to you, then do not use this parameter. Although, according to my calculations, the performance is only visible on 5000 elements in the array.

=== "Using a decorator"

    ``` py linenums="1"
    from dj_raw_sql import execute_sql

    @execute_sql(to_ordereddict=True)
    def get_music_by_id(id: int):
        return "SELECT * FROM dj_app_music WHERE id = %s", (id,)
    ```

=== "Without using a decorator"

    ``` py linenums="1"
    from django.db import connection

    def my_custom_sql(id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM dj_app_music WHERE id = %s", (id, ))
            description = cursor.description
            data = cursor.fetchall()
            if description:
                columns: list[str] = [element[0] for element in description]
                result = [OrderedDict(zip(columns, row)) for row in data]
            else:
                result = None
        return result
    ```
And this is how you get the value

``` py title="views.py" linenums="1"
from django.http import JsonResponse
from django.views import View

from my_app.queries import get_music_by_id

class MyView(View):
    def get(self, request, *args, **kwargs):
        music: tuple[tuple] = get_music_by_id(id=1)
        return JsonResponse({"name": music[0]["name"]})
```
