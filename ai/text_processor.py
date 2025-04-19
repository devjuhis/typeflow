from groq import Groq
from functions.read_config import read_config

def process_voice_prompt(raw_text):

    groq_api_key = read_config()
    client = Groq(api_key=groq_api_key)

    prompt = f'"{raw_text}"'

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a speech-to-text post-processing assistant. "
                        "Your task is to clean up spoken input by removing disfluencies such as 'um', 'uh', false starts, repeated words, filler phrases, and stutters. "
                        "Do not change the intended meaning, tone, or language of the original speech. "

                        "Preserve the structure of the speech, including:\n"
                        "- Lists (e.g. 'first', 'second', 'third') formatted with line breaks and bullets if appropriate\n"
                        "- Line breaks where there are clear pauses or topic shifts\n"
                        "- Emphasized or stressed words using **bold** Markdown formatting, if the emphasis is clearly spoken.\n"

                        "Maintain proper grammar, punctuation, and natural sentence flow. "

                        "Return only the cleaned-up version of the speech as a single string, with no additional explanation or formatting outside of the rules above."
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
