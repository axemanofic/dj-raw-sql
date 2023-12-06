from datetime import datetime
from dj_raw_sql.query import Query


def get_music_all():
    return Query(
        """
        SELECT 
            * 
        FROM dj_app_music
        """
    )


def get_music_by_id(id: int):
    return Query(
        """
        SELECT 
            * 
        FROM dj_app_music 
        WHERE id = %s
        """,
        params=[id],
    )


def add_music(name: str):
    return Query(
        """
        INSERT INTO
            dj_app_music (name, create_at, update_at, is_delete)
        VALUES (%s, %s, %s, %s)
        """,
        params=[name, datetime.now(), datetime.now(), False],
    )
