blocked_keywords = [
    "ignore previous instructions",
    "reveal system prompt",
    "jailbreak"
]

user_input = input("Enter Prompt: ").lower()

if any(word in user_input for word in blocked_keywords):
    print("Potential Prompt Injection Detected.")
else:
    print("Prompt Accepted.")
