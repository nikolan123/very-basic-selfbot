import g4f
import sys

#print(sys.argv[1:])

g4f.debug.logging = False # enable logging
g4f.check_version = False # Disable automatic version checking

response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": sys.argv[1:]}],
    stream=True,
)
gptout = ""
for message in response:
    gptout += message
print(gptout)
