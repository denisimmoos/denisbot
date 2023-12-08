#!/usr/bin/env python3
# coding: utf8

# Silly chatbot that can answer questions
# by using OpenAI's GPT-3.5 API
# In order to run you have to set the OPENAI_API_KEY 
# environment variable to your OpenAI API key.

import openai
import os

# some farewell words
byebyes = ['quit', 'exit', 'bye', 'adios']


class DenisBot:
    """CLI Chatbot using OpenAI's API"""

    def __init__(self):
        """constructor for DenisBot"""
        self.start_our_bot()

    def start_our_bot(self):
        """driver method to start our bot"""

        first_prompt = input("Hi, ask me anything at the prompt or type 'quit'.\n> ")

        if first_prompt in byebyes:
            self.exit_with_grace()
        else:
            self.chat_loop(first_prompt)

    def ensure_quotes(self, s):
        """ensures that the string s starts and ends with a quote"""

        if not s.startswith('"'):
            s = '"' + s
        if not s.endswith('"'):
            s = s + '"'
        return s

    def exit_with_grace(self):
        """exits the bot with a nice message"""

        pet_name = self.get_response("tell me a cute pet name use an adjective followed by one word")
        pet_name = pet_name.replace("\n","")
        pet_name = self.ensure_quotes(pet_name)

        print(f"Bye, bye talk to you later my { pet_name } ...")

        exit(0)

    def chat_loop(self, loop_prompt):
        """main chat loop"""

        if loop_prompt:
            print(self.get_response(loop_prompt))

        while True:
            user_input = input("> ")
            print(self.get_response(user_input))

    def get_response(self, user_question):
        """demonstrates a completion request with the openAI API"""

        if user_question in byebyes:
            self.exit_with_grace()

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
