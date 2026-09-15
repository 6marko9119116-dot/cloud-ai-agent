def route_message(message):
    message = message.lower()

    if any(word in message for word in ["كود", "برمجة", "python", "code"]):
        return "CODING"

    if any(word in message for word in ["صورة", "صمم", "image", "picture"]):
        return "IMAGE"

    if any(word in message for word in ["فيديو", "video"]):
        return "VIDEO"

    return "CHAT"


if __name__ == "__main__":
    while True:
        message = input("You: ")

        if message.lower() == "exit":
            break

        task = route_message(message)
        print(f"Agent → {task}")
