import json

states_capitals = {
    "Andhra Pradesh": "Hyderabad",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Maharashtra": "Mumbai",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Uttar Pradesh": "Lucknow"
}

with open('indian_states.json', 'w') as f:
    json.dump(states_capitals, f)
