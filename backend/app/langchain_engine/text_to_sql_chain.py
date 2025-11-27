from .llm import get_llm
from .prompts import chat_prompt, fixer_prompt


def generate_sql_from_nl(schema: str, nl: str, max_rows: int = 100):
    formatted_prompt = chat_prompt.format_prompt(schema=schema, user_question=nl, max_rows=max_rows)
    messages = formatted_prompt.to_messages()
    
    model = get_llm()
    
    response = model.invoke(messages)
    
    return response.content



# Fixing the generated sql if error occurs
def fix_sql(schema: str, bad_sql: str, error: str, max_rows: int = 100):
    formatted_prompt = fixer_prompt.format_prompt(
        schema=schema, 
        bad_sql=bad_sql, 
        error_message=error, 
        max_rows=max_rows
    )
    messages = formatted_prompt.to_messages()
    model = get_llm()
    response = model.invoke(messages)
    
    return response.content