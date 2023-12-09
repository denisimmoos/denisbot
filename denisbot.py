#!/usr/bin/env python3
# coding: utf8

"""
Silly chatbot that can answer questions
by using OpenAI's GPT-3.5 API
In order to run you have to set the OPENAI_API_KEY
environment variable to your OpenAI API key.
"""

import os
import random
from openai import OpenAI

# get the API key from the environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# some farewell words
byebyes = ["quit", "exit", "bye", "adios"]

# make it colorful
colors = ["Red", "Green", "Blue", "Yellow", "Purple"]


class DenisBot:
    """CLI Chatbot using OpenAI's API"""

    def __init__(self):
        """constructor for DenisBot"""
        self.start_our_bot()

    def start_our_bot(self):
        """driver method to start our bot"""

        random_color = self.random_element(colors)
        silly_text = ">"
        colored_text = [
            self.color_text(
                silly_text.format(random_color),
                random.randint(0, 84)
            ),
            self.color_text(
                silly_text.format(random_color),
                random.randint(85, 169)
            ),
            self.color_text(
                silly_text.format(random_color),
                random.randint(170, 255)
            ),
        ]

        first_prompt = input(
            "Hi, ask me anything at the prompt or type 'quit'.\n"
            + f"{colored_text[0]}{colored_text[1]}{colored_text[2]} "
        )

        if first_prompt in byebyes:
            self.exit_with_grace()
        else:
            self.chat_loop(first_prompt)

    def random_element(self, array):
        """Wow that's random"""

        return random.choice(array)

    def color_text(self, text, color_code):
        """Wow tastes like skiddles"""
        return "\033[38;5;{}m{}\033[0m".format(color_code, text)

    def ensure_quotes(self, s):
        """ensures that the string s starts and ends with a quote"""

        if not s.startswith('"'):
            s = '"' + s
        if not s.endswith('"'):
            s = s + '"'
        return s

    def exit_with_grace(self):
        """exits the bot with a nice message"""

        pet_name = self.get_response(
            "tell me a cute pet name"
            + " use an adjective followed by one word"
            + "and make sure it is only one word"
        )
        pet_name = pet_name.replace("\n", "")
        pet_name = self.ensure_quotes(pet_name)

        random_color = self.random_element(colors)
        colored_text = self.color_text(
            pet_name.format(random_color), random.randint(0, 255)
        )

        print(f"Bye, bye talk to you later my { colored_text } ...")

        exit(0)

    def chat_loop(self, loop_prompt):
        """main chat loop"""

        if loop_prompt:
            print(self.get_response(loop_prompt))

        while True:
            random_color = self.random_element(colors)
            silly_text = ">"
            colored_text = [
                self.color_text(
                    silly_text.format(random_color),
                    random.randint(0, 84)
                ),
                self.color_text(
                    silly_text.format(random_color),
                    random.randint(85, 169)
                ),
                self.color_text(
                    silly_text.format(random_color), random.randint(170, 255)
                ),
            ]

            # get user input
            user_input = input(
                f"{colored_text[0]}"
                + f"{colored_text[1]}"
                + f"{colored_text[2]} "
                )

            # get response from OpenAI
            print(self.get_response(user_input))

    def get_response(self, user_question):
        """demonstrates a completion request with the openAI API"""

        # if user_question is a byebye word, exit gracefully
        if user_question in byebyes:
            self.exit_with_grace()

        # ask OpenAI for a response
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=user_question,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # return the first response
        return response.choices[0].text + "\n"


if __name__ == "__main__":

    # get the OPENAI_API_KEY environment variable

    try:
        # start our bot
        DenisBot()

    # CTRL-C is caught
    except KeyboardInterrupt:
        print("\nBye, my endless love!")
