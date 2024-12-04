import random
from colorama import Fore

# Function to simulate an attack
def simulate_attack(team_budget, team_security_features, name):
    attacks = [
        {"name": "Physical Theft", "security_features": ["Physical Access Control"], "impact": 120000},  # Average cost of a data breach due to physical theft
        {"name": "Malware Infection", "security_features": ["Antivirus", "Firewall"], "impact": 450000},  # Average cost of a malware infection (Source: IBM)
        {"name": "Data Breach", "security_features": ["Encryption", "Intrusion Detection System"], "impact": 4240000},  # Average cost of a data breach (Source: Ponemon Institute)
        {"name": "Phishing Attack", "security_features": ["Email Filtering", "User Training"], "impact": 150000}, # Average cost of a phishing attack (Source: Ponemon Institute)
        {"name": "DDoS Attack", "security_features": ["DDoS Protection"], "impact": 200000}, # Average cost of a DDoS attack (Source: Cloudflare)
        {"name": "Insider Threat", "security_features": ["User Monitoring", "Access Control"], "impact": 120000}, # Average cost of an insider threat (Source: Ponemon Institute)
        {"name": "Ransomware Attack", "security_features": ["Backup", "Endpoint Protection"], "impact": 1800000}, # Average cost of a ransomware attack (Source: Cybersecurity Ventures)
        {"name": "Social Engineering", "security_features": ["Security Awareness Training", "Multi-Factor Authentication"], "impact": 150000}, # Average cost of social engineering (Source: Ponemon Institute)
        {"name": "SQL Injection", "security_features": ["Web Application Firewall", "Code Review"], "impact": 160000}, # Average cost of an SQL injection attack (Source: OWASP)
        {"name": "Zero-Day Exploit", "security_features": ["Vulnerability Scanning", "Patch Management"], "impact": 2000000}, # Average cost of a zero-day exploit (Source: Cybersecurity Ventures)
        # Add more/edit attacks as needed
    ]
    name": "Zero-Day Exploit", "security_features": ["Vulnerability Scanning", "Patch Management"], "impact": 2000000
    attack = random.choice(attacks)

    # Check if the team is protected against the attack
    if all(feature in team_security_features for feature in attack['security_features']):
        print(Fore.GREEN + f"{name} is protected against {attack['name']}." + Fore.WHITE)
    else:
        print(Fore.RED + f"{name} is NOT protected against {attack['name']}!")
        print(Fore.RED + f"Impact of {attack['name']}: -£{attack['impact']}")
        team_budget -= attack['impact']
        print(Fore.WHITE + f"Updated Budget for {name}: £{team_budget}")

    return team_budget

# Function to display available security features and let the user choose
  #change costs where needed
def choose_security_features(team_budget, name):
    feature_costs = {
        "Firewall": 1000,  # Example cost for a basic firewall (Source: Sophos)
        "Antivirus": 800,  # Example cost for a basic antivirus (Source: Symantec)
        "Encryption": 1200,  # Example cost for basic data encryption (Source: Cloudflare)
        "Intrusion Detection System": 1500, # Example cost for a basic IDS (Source: IBM)
        "Email Filtering": 700, # Example cost for basic email filtering (Source: Sophos)
        "User Training": 500, # Example cost for basic security awareness training (Source: SANS Institute)
        "DDoS Protection": 2000, # Example cost for basic DDoS protection (Source: Cloudflare)
        "User Monitoring": 1000, # Example cost for basic user monitoring (Source: IBM)
        "Access Control": 1200, # Example cost for basic access control (Source: Microsoft)
        "Backup": 1500, # Example cost for basic backup (Source: Veeam)
        "Endpoint Protection": 1800, # Example cost for basic endpoint protection (Source: Symantec)
        "Security Awareness Training": 600, # Example cost for basic security awareness training (Source: SANS Institute)
        "Multi-Factor Authentication": 1000, # Example cost for basic MFA (Source: Microsoft)
        "Web Application Firewall": 1200, # Example cost for basic WAF (Source: Cloudflare)
        "Code Review": 800, # Example cost for basic code review (Source: OWASP)
        "Vulnerability Scanning": 1500, # Example cost for basic vulnerability scanning (Source: Qualys)
        "Patch Management": 1200 # Example cost for basic patch management (Source: Microsoft)
    }

    print("\nTeam Budget:", team_budget)
    print("Available Security Features:")
    for i, (feature, cost) in enumerate(feature_costs.items(), 1):
        print(f"{i}. {feature} - £{cost}")

    selected_features = []
    while True:
        try:
            choice = int(input("Enter the number of the feature to add (0 to finish): "))
            if 0 <= choice <= len(feature_costs):
                if choice == 0:
                    break
                selected_feature = list(feature_costs.keys())[choice - 1]
                selected_features.append(selected_feature)
                print(f"{selected_feature} added to the team's security features.")

                # Impact the budget when investing in protection
                feature_cost = feature_costs[selected_feature]
                team_budget -= feature_cost
                print(f"Impact of {selected_feature}: -£{feature_cost}")
                print(f"Updated Budget for {name}: £{team_budget}")

            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return selected_features, team_budget

  # Main function
def main():
    team_budget = 500000  # Example budget for a small to medium-sized business
    week = 0
    name = input("Enter team name:")
    team_security_features = []

      # Simulate attacks and allow the user to add security features until the budget runs out
    while team_budget > 0:
        team_budget = simulate_attack(team_budget, team_security_features, name)
        week += 1

        print("\nTeam Security Features:", team_security_features)
        input("Press enter to continue ... ")
        new_features, new_budget = choose_security_features(team_budget, name)
        if new_budget < 0:
          break
        team_budget = new_budget
        team_security_features.extend(new_features)
        r = random.randint(100,1000)
        team_budget = team_budget + r
        print(Fore.BLUE + "\nPay day! Budget increase of £"+str(r)+"\n"+Fore.WHITE)

    print(f"\n{Fore.RED}{name} ran out of budget. Game over! You lasted {week} weeks.")
    print(f"Final Team Security Features: {team_security_features}")

if __name__ == "__main__":
    main()