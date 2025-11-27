from app.langchain_engine.llm import get_llm
from app.langchain_engine.prompts import chat_prompt


async def run_langchain_pipeline(schema: str, nl: str, max_rows: int = 100):
    formatted_prompt = chat_prompt.format_prompt(schema=schema, user_question=nl, max_rows=max_rows)
    messages = formatted_prompt.to_messages()
    
    model = get_llm()
    
    response = await model.ainvoke(messages)
    
    return response.content




if __name__ == "main":
    run_langchain_pipeline()