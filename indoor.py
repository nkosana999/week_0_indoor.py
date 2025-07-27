def calm_voice(tone):
    return tone.lower()

def main():
    tone = input("Say something: ")
    print(calm_voice(tone))

main()