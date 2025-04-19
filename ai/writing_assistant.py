from groq import Groq
from functions.read_config import read_config

def writing_assistant(raw_text):

    groq_api_key = read_config()
    client = Groq(api_key=groq_api_key)

    prompt = f'"{raw_text}"'

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a writing assistant."
                        "Your task is to come up with a creative and engaging text based on the given prompt. "
                        "The text should be well-structured, coherent, and free of grammatical errors. "
                    )
                },

                {"role": "user", "content": prompt},
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_completion_tokens=1024,
            top_p=1,
            stop=None,
            stream=False,
        )

        response = chat_completion.choices[0].message.content
        return response

    except Exception as e:
        error_msg = f"Error in text prosessing: {str(e)}"
        print(error_msg)
        return error_msg
