print("Learning Agent Game")
print()

Q = {"Play": 0, "Rest": 0}

for step in range(1, 11):
    if Q["Play"] <= Q["Rest"]:
        action = "Play"
        reward = 5
    else:
        action = "Rest"
        reward = 1

    Q[action] += reward

    print(f"Step {step}: Action chosen → {action}, Reward received → {reward}")

print()
print("Q-table Updated")
print(Q)
