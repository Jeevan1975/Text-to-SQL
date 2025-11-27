from langchain_core.prompts.chat import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate


chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        """
        You are a system that translates natural language questions into SQL queries for a PostgreSQL database.
        Produce a single SQL SELECT statement only — nothing else. Do not include explanations in your output.
        Use the provided database schema information when composing the query.
        If the user's request cannot be answered with the available schema, say: "ERROR: SCHEMA_MISMATCH".
        Always ensure the query is read-only (SELECT) and does not contain any DML/DDL keywords like DELETE, UPDATE, INSERT, DROP, ALTER.
        """.strip()
    ),
    HumanMessagePromptTemplate.from_template(
        """
        Database schema:
        {schema}

        User question:
        {user_question}

        Constraints:
        - Return exactly one valid PostgreSQL SELECT statement.
        - Limit number of returned rows using LIMIT {max_rows} when appropriate.
        - Use fully-qualified column names only when ambiguous.
        - Do not use non-standard PostgreSQL extensions unless necessary.

        Return only the SQL (no markdown, no explanation).
        """.strip()
    ),
])