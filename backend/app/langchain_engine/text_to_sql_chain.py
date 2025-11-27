import asyncio
from .llm import get_llm
from .prompts import chat_prompt
from ..database.schema_loader import load_schema


async def run_langchain_pipeline(schema: str, nl: str, max_rows: int = 100):
    formatted_prompt = chat_prompt.format_prompt(schema=schema, user_question=nl, max_rows=max_rows)
    messages = formatted_prompt.to_messages()
    
    model = get_llm()
    
    response = await model.ainvoke(messages)
    
    return response.content
