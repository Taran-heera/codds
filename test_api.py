import requests
import json

# Register a test user
reg_url = 'http://127.0.0.1:5000/api/auth/register'
reg_data = {
    'username': 'testuser456',
    'email': 'test456@example.com',
    'password': 'test123456'
}

print("1. Testing User Registration...")
try:
    reg_resp = requests.post(reg_url, json=reg_data)
    reg_result = reg_resp.json()
    token = reg_result.get('access_token')
    print(f"   ✓ Registration Success")
    print(f"   Token: {token[:50]}...")
except Exception as e:
    print(f"   ✗ Registration failed: {e}")
    exit(1)

# Test analyze endpoint
print("\n2. Testing Analyze Endpoint...")
analyze_url = 'http://127.0.0.1:5000/api/analyze/text'
analyze_data = {
    'text': 'The quick brown fox jumps over the lazy dog. This is a test sentence with analysis.'
}
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

try:
    analyze_resp = requests.post(analyze_url, json=analyze_data, headers=headers)
    analyze_result = analyze_resp.json()
    
    print(f"   ✓ Analysis Success")
    print(f"   Originality Score: {analyze_result.get('originality_score')}%")
    print(f"   AI Similarity: {analyze_result.get('ai_similarity')}%")
    print(f"   Suggestions: {analyze_result.get('suggestions', [])[:2]}")
    print(f"   Full response keys: {list(analyze_result.keys())}")
except Exception as e:
    print(f"   ✗ Analysis failed: {e}")
    import traceback
    traceback.print_exc()

# Test same text twice
print("\n3. Testing Consistency (same text twice)...")
try:
    analyze_resp1 = requests.post(analyze_url, json=analyze_data, headers=headers)
    score1 = analyze_resp1.json().get('originality_score')
    
    analyze_resp2 = requests.post(analyze_url, json=analyze_data, headers=headers)
    score2 = analyze_resp2.json().get('originality_score')
    
    if score1 == score2:
        print(f"   ✓ CONSISTENT: Both scores = {score1}%")
    else:
        print(f"   ✗ INCONSISTENT: Score 1 = {score1}%, Score 2 = {score2}%")
except Exception as e:
    print(f"   ✗ Consistency test failed: {e}")

print("\nTest complete!")
