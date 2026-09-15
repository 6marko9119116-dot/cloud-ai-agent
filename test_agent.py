from router import route_task


def analyze_message(message):
    message_lower = message.lower()

    if any(word in message_lower for word in [
        "صورة", "صور", "ارسم", "تصميم", "image", "picture"
    ]):
        task = "image"

    elif any(word in message_lower for word in [
        "فيديو", "فيديوهات", "video"
    ]):
        task = "video"

    elif any(word in message_lower for word in [
        "كود", "برمج", "برنامج", "python", "code"
    ]):
        task = "coding"

    else:
        task = "chat"

    result = route_task(task)

    return {
        "message": message,
        "task": result["task"],
        "model": result["model"],
        "description": result["description"]
    }


if __name__ == "__main__":
    while True:
        message = input("\nYou: ")

        if message.lower() == "exit":
            print("Agent stopped.")
            break

        result = analyze_message(message)

        print("\nAgent:")
        print(result)
