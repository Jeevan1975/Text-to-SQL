from sqlalchemy import inspect
from ..database.connection import engine


def load_schema():
    inspector = inspect(engine)
    schema = {}
    
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema[table_name] = [
            {
                "name": col["name"],
                "type": col["type"],
                "nullable": col["nullable"]
            }
            for col in columns
        ]
    return schema