from openai import OpenAI

# Set your API key
with open('api_key.txt', 'r') as file:
    api_key = file.readline().strip()

client = OpenAI(api_key=api_key)

# Create a request to obtain embeddings
response = client.embeddings.create(
    model='text-embedding-ada-002',
    input='Hello! My name is Pavel. I am from Ukraine and I am living in Lviv city.'
)

# Convert the response into a dictionary
response_dict = response.model_dump()

print(response_dict)
