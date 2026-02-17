print("==========================================")
print("🎓 Welcome to Student Study Planner Bot")
print("Type 'exit' to end the conversation.")
print("==========================================\n")

while True:

    user_input = input("You: ").lower().strip()
    words = user_input.split()

    # Exit
    if user_input == "exit":
        print("Bot: All the best for your studies! 📚✨")
        break

    # Greeting
    elif "hello" in words or "hi" in words:
        print("Bot: Hello! Ready to plan your study schedule today? 📖")

    # Study plan
    elif "study" in words and "plan" in words:
        print("Bot: A good study plan includes:")
        print("1. Set daily goals")
        print("2. Study in 45-minute sessions")
        print("3. Take 10-minute breaks")
        print("4. Revise before sleeping")

    # Time management
    elif "time" in words or "manage" in words:
        print("Bot: Try the Pomodoro Technique (25 min focus + 5 min break).")

    # Exam preparation
    elif "exam" in words:
        print("Bot: For exams:")
        print("- Start early")
        print("- Revise regularly")
        print("- Solve previous year questions")

    # Motivation
    elif "motivate" in words or "motivation" in words:
        print("Bot: Success comes from consistency, not intensity. Keep going! 🔥")

    # Concentration
    elif "concentration" in words or "focus" in words:
        print("Bot: Remove distractions, keep phone away, and study in a quiet place.")

    # Subjects help
    elif "math" in words:
        print("Bot: Practice daily problems and understand concepts clearly.")

    elif "programming" in words or "coding" in words:
        print("Bot: Practice coding daily and work on small projects to improve.")

    elif "ai" in words or "data" in words:
        print("Bot: Focus on Python, statistics, and machine learning basics.")

    # Revision
    elif "revision" in words:
        print("Bot: Revise important topics every weekend to retain concepts.")

    # Stress
    elif "stress" in words:
        print("Bot: Take short breaks, exercise, and get enough sleep.")

    # Default
    else:
        print("Bot: I can help with study plan, exam prep, focus, motivation, time management, and revision.")
