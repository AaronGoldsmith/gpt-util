#!/bin/sh

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

contains_use_gpt() {
    while IFS= read -r line; do
        if [[ $line == *"<USE_GPT>"* ]]; then
            return 0
        fi
    done < "$1"
    return 1
}

if contains_use_gpt "$COMMIT_MSG_FILE"; then
    #    # Get the added code chunks
    ADDED_CODE=$(git diff --cached --patch)
    # echo "Added code chunks:"
    # echo "$ADDED_CODE"

    # Split the added code into chunks (separated by diff headers)
    IFS=$'\n' read -ra CHUNKS <<< "$(echo "$ADDED_CODE" | awk '/^diff/{if (p) {print s}; s=""; p=1} {s=s $0 RS} END{if (p) print s}')"
    # echo "Chunks array:"
    # printf '%s\n' "${CHUNKS[@]}"

    # Generate commit message summaries using the OpenAI completions endpoint
    SUMMARIES=$(python ".git/hooks/gpt_commit_msg.py" "${CHUNKS[@]}")

    # Remove the original commit message prompt and add the generated summaries
    /usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"
    echo -n "" > "$COMMIT_MSG_FILE"
    echo -e "$SUMMARIES\n" >> "$COMMIT_MSG_FILE"

    # exit 1  # Uncomment this line to prevent commits while debugging
fi


