from openai import OpenAI

# Set your API key
with open('api_key.txt', 'r') as file:
    api_key = file.readline().strip()

print(api_key)

client = OpenAI(api_key=api_key)


def get_response(system_prompt, user_prompt):
    # Create a request to the ChatCompletion endpoint
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      # Assign the role and content for the message
      messages=[{"role": "system", "content": system_prompt},
                {"role": 'user', "content": user_prompt}], temperature=0)
    return response


def main():
    response = get_response("You are a chatbot that answers SEO questions.", "Who are you?")
    print(response)
    print(response.choices)
    print(response.choices[0])
    print(response.choices[0].message)
    print(response.choices[0].message.content)


if __name__ == '__main__':
    main()
