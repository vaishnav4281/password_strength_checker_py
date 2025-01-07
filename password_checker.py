def check_password_strength(password):
    score = 0
    
    # Check length
    if len(password) >= 8:
        score += 1
    
    # Check for uppercase
    if any(c.isupper() for c in password):
        score += 1
    
    # Check for lowercase
    if any(c.islower() for c in password):
        score += 1
    
    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1
    
    # Check for special characters
    if any(not c.isalnum() for c in password):
        score += 1
    
    # Return strength based on score
    if score < 2:
        return "Weak"
    elif score < 4:
        return "Medium"
    else:
        return "Strong"

# Get password and check strength
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
