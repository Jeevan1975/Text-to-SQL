import re


class SQLValidator:
    """
    Allows only SELECT statements.
    Blocks: DROP, TRUNCATE, UPDATE, DELETE, ALTER, INSERT, CREATE, REPLACE
    """
    
    forbidden_keywords = [
        r"\bDELETE\b",
        r"\bUPDATE\b",
        r"\bINSERT\b",
        r"\bDROP\b",
        r"\bALTER\b",
        r"\bTRUNCATE\b",
        r"\bCREATE\b",
        r"\bREPLACE\b",
    ]
    
    
    @staticmethod
    def is_safe(sql: str) -> bool:
        sql_upper = sql.upper()
        
        if not sql_upper.strip().startswith("SELECT"):
            return False
        
        for pattern in SQLValidator.forbidden_keywords:
            if re.search(pattern, sql_upper):
                return False
        
        return True