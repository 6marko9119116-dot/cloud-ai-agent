MODELS = {
    "chat": {
        "default": "qwen_chat"
    },
    "coding": {
        "default": "qwen_coder"
    },
    "image": {
        "default": "flux_klein"
    },
    "video": {
        "default": "wan_video"
    }
}


def route_task(task):
    task = task.lower().strip()

    if task in MODELS:
        return {
            "task": task,
            "model": MODELS[task]["default"]
        }

    return {
        "task": "chat",
        "model": MODELS["chat"]["default"]
    }


if __name__ == "__main__":
    print(route_task("coding"))
    print(route_task("image"))
    print(route_task("video"))
    print(route_task("chat"))
