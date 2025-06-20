# emotion_logic_sim.py

def get_system_response(stress_level: float) -> str:
    if stress_level < 0.3:
        return "🟢 Operator baseline normal. Full diagnostic mode enabled."
    elif 0.3 <= stress_level < 0.6:
        return "🟡 Moderate stress detected. UI simplifying to reduce overload."
    elif 0.6 <= stress_level < 0.8:
        return "🟠 High stress! Triggering micro-break protocol and pausing non-critical tests."
    else:
        return "🔴 Critical stress level! Testing paused. Recommend operator disengagement."

def main():
    print("AETHER Emotional Response Simulation")
    try:
        user_input = float(input("Enter stress level (0.0 - 1.0): "))
        if not 0.0 <= user_input <= 1.0:
            print("❗ Error: Please enter a value between 0.0 and 1.0")
            return
        response = get_system_response(user_input)
        print(f"\nSystem Response:\n{response}")
    except ValueError:
        print("❗ Invalid input. Please enter a numeric value between 0.0 and 1.0")

if __name__ == "__main__":
    main()
