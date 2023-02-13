import openai

# Set up the OpenAI API client
openai.api_key = "*********"

# Set up the model and prompt
model_engine = "text-davinci-003"
# prompt = "Hello, how are you today?"

def initiate_chat():
    # Ask for input
    prompt = input("\nAsk from OpenAI: ")

    # Generate a response
    completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
    )

    # Get response of openAI
    response = completion.choices[0].text

    # Print response
    print(response)


while(1):
    initiate_chat()










