from memory import load_memory, save_memory
from planner import suggest_next_topic

def prompt_user(prompt_text):
    return input(f"{prompt_text}\n> ").strip().lower()

def main():
    memory = load_memory()

    if not memory["goal"]:
        memory["goal"] = prompt_user("What is your study goal? (e.g., 'learn ML in 14 days')")
    
    if not memory["level"]:
        memory["level"] = prompt_user("What's your current level? (beginner/intermediate/advanced)")

    print("\n🤖 Planning your next learning step...\n")
    topic = suggest_next_topic(memory)

    print(f"\n📘 Suggested Topic: {topic['title']}")
    print(f"📎 Resource: {topic['link']} [{topic['type']}]")
    print(f"🧠 Reason: {topic.get('reason', 'No reason provided.')}\n")

    status = prompt_user("Did you complete it? (yes / no / skip)")
    if status == "yes":
        memory["completed"].append(topic["title"])
    elif status == "skip":
        memory["skipped"].append(topic["title"])
    else:
        print("No worries — we'll revisit this topic later.")

    save_memory(memory)
    print("\n✅ Progress saved. See you next session!")

if __name__ == "__main__":
    main()

