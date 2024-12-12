from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.1")

result = model.invoke(input="Hello World!")
print(result)