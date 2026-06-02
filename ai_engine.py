import ollama

def get_atk_justification(task_name, proposed_lever):
    prompt = (
        f"You are an enterprise automation expert. Write a punchy, 2-sentence executive justification "
        f"explaining why the automation lever '{proposed_lever}' is perfect for optimizing the task '{task_name}'. "
        f"Focus on efficiency and cost reduction. Do not introduce yourself."
    )

    try:
        response = ollama.generate(model='mistral', prompt=prompt)
        return response['response'].strip()
    except Exception:
        return f"Optimization via {proposed_lever} mitigates manual touchpoints within '{task_name}'. Implementing this logic scales throughput, standardizes operational workflows, and safely decreases human error margins."