from .text_to_sql_chain import generate_sql_from_nl, fix_sql
from .executor import SQLExecutor
from ..database.schema_loader import load_schema



def nl_to_results(nl_query: str, max_rows: int = 100):
    """
    Full pipeline:
    1. Load schema of database tables
    2. Generate SQL from NL using LLM
    3. Validate SQL
    4. Execute
    5. If error, call fix_sql and re-run once
    """
    
    schema = load_schema()
    
    # Generate SQL from NL
    sql_gen = generate_sql_from_nl(schema=schema, nl=nl_query, max_rows=max_rows)
    
    # Validate and execute
    exec_res = SQLExecutor.execute(sql=sql_gen, max_rows=max_rows)
    if exec_res.get("error"):
        fixed_sql = fix_sql(schema=schema, bad_sql=sql_gen, error=exec_res["error"], max_rows=max_rows)

        exec_res2 = SQLExecutor.execute(sql=fixed_sql, max_rows=max_rows)
        if exec_res2.get("error"):
            return {
                "sql": fixed_sql,
                "error": exec_res2["error"]
            }

        # Success after fix
        return {
            "sql": fixed_sql,
            "results": exec_res2.get("rows"),
            "row_count": exec_res2.get("row_count")
        }
    # Success in first try
    return {
        "sql": sql_gen,
        "results": exec_res.get("rows"),
        "row_count": exec_res.get("row_count")
    }
        
    
        
        
    