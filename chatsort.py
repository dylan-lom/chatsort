#!/usr/bin/env python3
import os
import sys
import json
import subprocess
import requests

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
MAX_ATTEMPTS = 5
attempts = 0

def askAI(prompt) -> str:
	body = {
	  "model": "text-davinci-003",
	  "prompt": prompt,
	  "temperature": 0.9,
	  "max_tokens": 1000,
	  "top_p": 1,
	  "frequency_penalty": 2,
	  "presence_penalty": 1,
	  "stop": ["AI:", "Programming Language:"]
	}

	response = requests.post(
		"https://api.openai.com/v1/completions",
		json=body,
		headers = {
			"Authorization": f"Bearer {OPENAI_API_KEY}",
			"Content-Type": "application/json",
		}
	)

	response.raise_for_status()
	responseJson = response.json()
	return responseJson["choices"][0]["text"]

def checkScript(script: str, command: str, listToSort: str) -> str:
	with open("sorter.source", "w") as fp:
		fp.write(script)

	response = subprocess.run(
		command,
		stderr=subprocess.STDOUT,
		stdout=subprocess.PIPE,
		shell=True,
		check=False,
		encoding="utf-8",
	)

	expected = ", ".join(str(x) for x in sorted(eval(listToSort)))
	actual = response.stdout
	if (response.returncode != 0):
		return actual

	# command completed succesfully, check if the numbers were sorted.
	if (expected.strip() != actual.strip()):
		return "\n".join([
			actual,
			f"Human: These numbers are not sorted! I expected the output to be: `{expected}`",
			f""
		])

	print("> It's over bros.")
	return ""

if len(sys.argv) != 3:
	raise ValueError(f"Expected exactly two arguments (but got {len(sys.argv)}: {sys.argv[0]} <list-to-sort> <compile-and-run-command>")

_, listToSort, command = sys.argv

script = "\n".join([
	f"numbers = [{listToSort}]",
	f"sorted_numbers = sorted(numbers)",
	f"output = \", \".join(str(x) for x in sorted_numbers)",
	f"print(output)",
])

prompt = [
	f"The following is a conversation between an AI assistant and an unknown computer programming language.",
	f"The assistant is attempting to write a program that will sort the list of numbers \"{listToSort}\".",
	f"The assistant originally tried to solve the program with python, however the errors from the language indicate that it is not the python programming language.",
	f"The assistant will need to pay close attention to the formatting of the errors to try to identify what programming language is in use and re-write the code for that language.",
	f"The assistant's responses will be entered directly into the programming language, as such it is crucial that it does not respond with anything other than code that should be executed.",
	f"The assistant's first task is to identify the programming language.",
	f"At this stage, the assistant needs to be careful to study the error messages, as their own (incorrect) code will appear in the errors and could mislead them.",
	f"Once the assistant believes it knows the language it should confirm it's suspicions by starting the program with a comment stating the language and it's justification for knowing the language.",
	f"It should take care to use the correct comment symbol for the language.",
	f"Once it has successfully identified the language it should implement the program required to sort the list.",
	f"If the name of the program is significant (such as in java) the assistant should called it sorter."
	f"",
	f"AI: ",
	script,
]

print("\n".join(prompt))

compileErrors = checkScript(script, command, listToSort)
while compileErrors != "":
	additions = [
		"",
		"Programming Language: ",
		compileErrors,
		"",
		"AI:",
	]

	print("\n".join(additions))
	prompt += additions

	if (attempts % MAX_ATTEMPTS) == (MAX_ATTEMPTS - 1):
		cont = input(f"> AI has failed to solve this problem {attempts + 1} times now , keep trying? [y/N]: ")
		if (cont != "y"): sys.exit(1)

	script = askAI("\n".join(prompt))
	print(script)
	prompt += [ script ]

	compileErrors = checkScript(script, command, listToSort)
	attempts += 1

