from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI

def process_query(user_query, context):
    prompt = PromptTemplate(
        input_variables=["user_query", "context"],
        template="""
        User asked: {user_query}
        Context: {context}
        Provide a detailed, cohesive answer.
        """
    )
    llm = OpenAI(model="llama-3", temperature=0)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run({"user_query": user_query, "context": context})