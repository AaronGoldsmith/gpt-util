import sys
import os
from dotenv import load_dotenv, find_dotenv
import openai
import tiktoken

# Find and load the .env file from the project root
# load_dotenv('.env')

def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode(string))
    return num_tokens

def generate_summary(code_chunks):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    summaries = []


    for chunk in code_chunks:
        system_intro = "You are a commit message generator used in prepare-commit-msg.\n \
                        1. Review the provided diff\n 2. Identify which category the diff falls into \
                        \n\t [fix][feat][chore][docs][style][refactor][perf][test]   \
                        \n3. respond with [category] <commit message summarizing +/- changes> \
                        Constraint: Respond with the unpunctuated commit message related to the provided code change.\n"
        prompt = f"{chunk}\n<<END_DIFF>>\n\n"
        


        # Count the tokens in the prompt
        tokens = num_tokens_from_string(prompt)

        # Ensure the number of tokens is within the model's limits (4096 tokens for gpt-3.5-turbo)
        if tokens > 4096:
            print(f"Warning: Skipping file '{code_chunks}' due to token limit exceeded ({tokens} tokens).", file=sys.stderr)
            continue

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0,
            messages=[
                {"role": "system", "content": system_intro},
                {"role": "user", "content": prompt}
            ]
        )
        summary = completion.choices[0].message.content
        summaries.append(summary)

    return summaries

if __name__ == "__main__":
    code_chunks = sys.argv[1:]
    summaries = generate_summary(code_chunks)
    print("\n".join(summaries))

