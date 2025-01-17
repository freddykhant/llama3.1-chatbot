from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
You are an expert data analyst. Given the following CSV data, generate a short summary or key insights in 50 words or less (but don't mention word limit in your answer). Highlight any trends, anomalies, or interesting patterns in the data. Be clear, concise, and specific. Use plain language suitable for a general audience.

Here is the data in csv format: {file}

Summary:
"""

model = OllamaLLM(model="llama3.1")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def summarise():
    print("\nWelcome to Llama 3.1 for Data Analysis\n")
    file_path = input("Please enter the file path of the data that you would like for me to analyse! (or type 'exit' to quit):\n")
   
    if file_path.lower() == "exit" or file_path == None:
        exit

    with open(file_path, "r") as f:
        content = f.read()
        result = chain.invoke({"file": content})
        print(result)

if __name__ == "__main__":
    summarise()