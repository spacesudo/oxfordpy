from oxfordpy import oxfordpy

oxford = oxfordpy.Oxford()

word = "hello"

define = oxford.define(word)

pronunciation = oxford.pronunciations(word)

etymology = oxford.etymologies(word)

print(f"word: {word}\nmeaning: {define}\npronunciation: {pronunciation}\netymology: {etymology}")