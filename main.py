from openai import OpenAI

# Set your API key
with open('api_key.txt', 'r') as file:
    api_key = file.readline().strip()

print(api_key)

client = OpenAI(api_key=api_key)

system_prompt = "You're an SEO specialist and know all the ways to promote websites in search engines."

system_role = {"role": "system", "content": system_prompt}

temperature = 0


def get_response(message_log):
    # Create a request to the ChatCompletion endpoint
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
      # Assign the role and content for the message
        messages=message_log)
    return response


def main():
    messages = [{'role': 'system', 'content': system_prompt}]

    print(f"""Description of the bot role:
    {system_prompt}""")
    while True:
        user_massage = input('Enter your message: ')

        if user_massage == 'qqq':
            break

        messages.append({'role': 'user', 'content': user_massage})
        response = get_response(messages)
        assist_message = response.choices[0].message
        messages.append(assist_message)
        print(f"""Botty answer:
        - {response.choices[0].message.content}
        """)



    # response = get_response("You are a chatbot that answers SEO questions.", "Who are you?")

    # print(response)
    # print(response.choices)
    # print(response.choices[0])
    # print(response.choices[0].message)
    # print(response.choices[0].message.content)


if __name__ == '__main__':
    main()
