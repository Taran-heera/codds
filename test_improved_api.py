import requests

# Register test user
reg_url = 'http://127.0.0.1:5000/api/auth/register'
reg_data = {
    'username': 'testuser999',
    'email': 'test999@example.com',
    'password': 'test123456'
}

print("Registering...")
reg_resp = requests.post(reg_url, json=reg_data)
token = reg_resp.json().get('access_token')

# Test cases
test_cases = {
    'WhatsApp (Casual)': "See da we can't depend on others for doing something, even if you have friends or not just don't feel depressed that you don't have anyone at some point in life we'll all be alone. So just take it as what you're facing is making you strong enough to face the rest",
    
    'Formal AI-like': "Furthermore, it is worth noting that in conclusion, the aforementioned system provides substantial benefits. Moreover, the subsequent analysis demonstrates that principles are indeed consequential.",
    
    'Normal Text': "I believe the project went well. We faced some challenges, but we learned from them. The team was amazing and I think our approach was pretty good.",
    
    'Heavy AI': "The implementation of advanced technological systems has demonstrable efficacy in contemporary organizational paradigms. It should be noted that such initiatives facilitate enhanced operational efficiency."
}

analyze_url = 'http://127.0.0.1:5000/api/analyze/text'
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

print("\n" + "="*70)
print("IMPROVED ANALYZER - REALISTIC BALANCED SCORING")
print("="*70)

for name, text in test_cases.items():
    resp = requests.post(analyze_url, json={'text': text}, headers=headers)
    result = resp.json()
    
    print(f"\n{name}:")
    print(f"  Originality:   {result['originality_score']:>6.1f}%")
    print(f"  AI Similarity:  {result['ai_similarity']:>6.1f}%")
    print(f"  Suggestion: {result['suggestions'][0][:50]}")

print("\n" + "="*70)
print("EXPECTED RANGES:")
print("  WhatsApp: 75-88% (conversational, informal)")
print("  Formal: 45-60% (some AI patterns)")
print("  Normal: 65-78% (balanced)")
print("  Heavy AI: 20-40% (lots of AI patterns)")
print("="*70)
