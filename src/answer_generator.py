def generate_answer(paths):
    if not paths:
        return "No reasoning path found."

    best_path = max(paths, key=len)

    reasoning = " → ".join(best_path)
    answer = f"The system infers: {reasoning}"

    return answer, best_path
