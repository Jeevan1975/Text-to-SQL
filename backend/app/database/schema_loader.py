from sqlalchemy import inspect
from .connection import engine


def load_schema():
    inspector = inspect(engine)
    schema = {}
    
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        schema[table_name] = [
            {
                "name": col["name"],
                "type": str(col["type"]),
                "nullable": col["nullable"]
            }
            for col in columns
        ]
    return schema




if __name__=="__main__":
    print(load_schema())