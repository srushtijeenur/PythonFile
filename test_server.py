def verify_intermediate(intermediate, encrypted_keyword, trapdoor):
    expected = encrypted_keyword[:16] + trapdoor[-16:]
    return intermediate == expected

# Use the actual values you got
intermediate = "04431690e428aee7068895c07f3e0c5a"
encrypted_keyword = "04431690e428aee731cd57f49da0c058f3dbb685d1f9f03b1b13ee4a6bb8a2c7"
trapdoor = "a12dd3a7fd3203a452eb34d91a9be20569d5e337a3384347068895c07f3e0c5a"

if verify_intermediate(intermediate, encrypted_keyword, trapdoor):
    print("Match confirmed — Intermediate Ciphertext is correct.")
else:
    print("Mismatch — Intermediate Ciphertext is incorrect.")