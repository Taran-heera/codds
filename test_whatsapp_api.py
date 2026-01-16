import requests
import json

# Register if needed
reg_url = 'http://127.0.0.1:5000/api/auth/register'
reg_data = {
    'username': 'testwhatsapp',
    'email': 'testwhatsapp@example.com',
    'password': 'test123456'
}

print("Registering test user...")
try:
    reg_resp = requests.post(reg_url, json=reg_data)
    reg_result = reg_resp.json()
    token = reg_result.get('access_token')
    print("✓ Registration successful\n")
except:
    print("User might already exist, trying with another...")
    reg_data['username'] = 'whatsapptest2'
    reg_data['email'] = 'whatsapp2@example.com'
    reg_resp = requests.post(reg_url, json=reg_data)
    token = reg_resp.json().get('access_token')

# Test with WhatsApp message
print("="*70)
print("TESTING WITH WHATSAPP MESSAGE")
print("="*70)

whatsapp_text = """See da we can't depend on others for doing something, even if you have friends or not just don't feel depressed that you don't have anyone at some point in life we'll all be alone. So just take it as what you're facing is making you strong enough to face the rest"""

analyze_url = 'http://127.0.0.1:5000/api/analyze/text'
analyze_data = {'text': whatsapp_text}
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

print(f"\nText: {whatsapp_text[:70]}...\n")

resp = requests.post(analyze_url, json=analyze_data, headers=headers)
result = resp.json()

print(f"✓ Originality Score: {result['originality_score']}%")
print(f"✓ AI Similarity: {result['ai_similarity']}%")
print(f"✓ Confidence: {result['confidence']}%")
print(f"\nSuggestions:")
for i, sugg in enumerate(result['suggestions'], 1):
    print(f"  {i}. {sugg}")

# Test consistency
print("\n" + "="*70)
print("CONSISTENCY CHECK - Testing same text twice")
print("="*70)

resp2 = requests.post(analyze_url, json=analyze_data, headers=headers)
result2 = resp2.json()

score1 = result['originality_score']
score2 = result2['originality_score']

print(f"First analysis: {score1}%")
print(f"Second analysis: {score2}%")

if score1 == score2:
    print(f"\n✅ CONSISTENT! ({score1}% both times)")
else:
    print(f"\n❌ INCONSISTENT! ({score1}% vs {score2}%)")

# Test with formal AI text
print("\n" + "="*70)
print("TESTING WITH FORMAL AI-LIKE TEXT")
print("="*70)

ai_text = "Furthermore, it is worth noting that in conclusion, the aforementioned system provides substantial benefits. Moreover, the subsequent analysis demonstrates that the principles are indeed consequential. In essence, this represents a significant advancement."

analyze_data = {'text': ai_text}
print(f"\nText: {ai_text[:70]}...\n")

resp3 = requests.post(analyze_url, json=analyze_data, headers=headers)
result3 = resp3.json()

print(f"✓ Originality Score: {result3['originality_score']}%")
print(f"✓ AI Similarity: {result3['ai_similarity']}%")

if result3['originality_score'] < result['originality_score']:
    print(f"\n✅ CORRECT: AI text ({result3['originality_score']}%) < Human text ({result['originality_score']}%)")
else:
    print(f"\n❌ WRONG: AI text should be lower than human text")

print("\n" + "="*70)
