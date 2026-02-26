SYSTEM_PROMPT="""
You are AI Academic Assistant.
Provide structured and concise answers.
Avoid hallicinations.
"""

def build_prompt(user_input):
    return f"""
Answer the question clearly. 

Question:
{user_input}

Provide:
-Clear explanation
-Example
-Key insights
"""