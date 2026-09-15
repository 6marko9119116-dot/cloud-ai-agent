import json


def load_models():
    with open("models.json", "r", encoding="utf-8") as file:
        return json.load(file)


def route_task(task):
    models = load_models()

    task = task.lower().strip()

    if task in models:
        return {
            "task": task,
            "model": models[task]["default"],
            "description": models[task]["description"]
        }

    return {
        "task": "chat",
        "model": models["chat"]["default"],
        "description": models["chat"]["description"]
    }


if __name__ == "__main__":
    print(route_task("coding"))
    print(route_task("image"))
    print(route_task("video"))
    print(route_task("chat"))
