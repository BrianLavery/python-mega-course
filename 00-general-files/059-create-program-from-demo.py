ans = ""

while True:
    user_input = input("Say something: ").lower()
    if user_input == "\end": break
    elif "how" in user_input or "why" in user_input or "what" in user_input:
        ans += user_input.capitalize() + "? "
    else:
        ans += user_input.capitalize() + ". "

print(ans)