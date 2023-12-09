#!/usr/bin/env python3
# coding: utf8

"""
Silly chatbot that can answer questions
by using OpenAI's GPT-3.5 API
In order to run you have to set the OPENAI_API_KEY
environment variable to your OpenAI API key.
"""

import sys
import openai
import os


class DenisBot:
    """CLI Chatbot using OpenAI's API"""

    def __init__(self):
        """constructor for DenisBot"""
        self.start_our_bot(sys.argv[1:])

    def start_our_bot(self, argv):
        """driver method to start our bot"""

        if len(argv) == 0:

            error = self.get_response(
                "Start the sentence with "
                + "'Exiting because no arguments were passed you silly'"
                + "followed by a funny pet name in quotes"
                )
            error = error.replace("\n", "")
            print(error)
            sys.exit(1)
        else:
            print(
                self.get_response(
                    " ".join(argv)
                    + ", format the answer you give me in markup format"
                    + " with a title, but do not use Title:"
                    + " and add a space after # in the title"
                    + " and line break after the title"
                    + ", if you output code put it in markup backticks"
                )
            )

    def get_response(self, user_question):
        """demonstrates a completion request with the openAI API"""

        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_question,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].text + "\n"


if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    DenisBot()
