#!/usr/bin/env python
"""Test login and analyzer with new AI detection"""
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

# Test 1: Login
print("=" * 60)
print("TEST 1: LOGIN WITH ADMIN")
print("=" * 60)
login_data = {
    "username": "admin",
    "password": "AdminPassword123"
}
response = requests.post(f"{BASE_URL}/api/auth/login", json=login_data)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

if response.status_code == 200:
    token = response.json()['access_token']
    print(f"✅ LOGIN SUCCESSFUL!")
    print(f"Token: {token[:50]}...")
    
    # Test 2: Analyze AI-generated text
    print("\n" + "=" * 60)
    print("TEST 2: ANALYZE AI-GENERATED TEXT")
    print("=" * 60)
    ai_text = """
    Furthermore, it is worth noting that in light of contemporary technological advancement, 
    artificial intelligence has become increasingly prevalent in modern society. Consequently, 
    the implications of this technological evolution are manifold and multifaceted. Moreover, 
    as previously mentioned, it should be noted that the aforementioned developments warrant 
    careful consideration. In conclusion, therefore, it is evident that the subsequent era 
    shall present novel challenges and opportunities. Nevertheless, it is important to highlight 
    that the cumulative effects of these technological innovations remain uncertain.
    """
    
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(
        f"{BASE_URL}/api/analyze/text",
        json={"text": ai_text},
        headers=headers
    )
    if response.status_code == 201:
        result = response.json()
        print(f"✅ AI Text Analysis:")
        print(f"   Originality Score: {result['originality_score']}% (should be LOW 10-30%)")
        print(f"   AI Similarity: {result['ai_similarity']}% (should be HIGH 70-90%)")
        print(f"   Confidence: {result['confidence']}%")
        print(f"   Suggestions: {result['suggestions'][0] if result['suggestions'] else 'None'}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.json())
    
    # Test 3: Analyze human text
    print("\n" + "=" * 60)
    print("TEST 3: ANALYZE HUMAN-GENERATED TEXT")
    print("=" * 60)
    human_text = """
    So like, I was thinking about how technology has changed everything, right? 
    I mean, honestly, when I was younger, we didn't have smartphones and stuff. 
    Now I literally can't imagine living without my phone! It's crazy how fast things change. 
    Don't you think? Anyway, I really believe that AI is going to be important in the future, 
    but I'm not sure if it'll be all good, you know? I think we need to be careful with it.
    """
    
    response = requests.post(
        f"{BASE_URL}/api/analyze/text",
        json={"text": human_text},
        headers=headers
    )
    if response.status_code == 201:
        result = response.json()
        print(f"✅ Human Text Analysis:")
        print(f"   Originality Score: {result['originality_score']}% (should be HIGH 70-90%)")
        print(f"   AI Similarity: {result['ai_similarity']}% (should be LOW 10-30%)")
        print(f"   Confidence: {result['confidence']}%")
        print(f"   Suggestions: {result['suggestions'][0] if result['suggestions'] else 'None'}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.json())
    
    # Test 4: Analyze mixed text
    print("\n" + "=" * 60)
    print("TEST 4: ANALYZE MIXED TEXT (FORMAL BUT HUMAN)")
    print("=" * 60)
    mixed_text = """
    I've been reading a lot about machine learning lately, and I think it's really interesting. 
    From what I can understand, it's basically just computers learning patterns from data. 
    However, I'm still trying to wrap my head around how it all works, to be honest. 
    The way I see it, we're only at the beginning of what AI can do. What do you think? 
    Would you want to learn more about this?
    """
    
    response = requests.post(
        f"{BASE_URL}/api/analyze/text",
        json={"text": mixed_text},
        headers=headers
    )
    if response.status_code == 201:
        result = response.json()
        print(f"✅ Mixed Text Analysis:")
        print(f"   Originality Score: {result['originality_score']}% (should be MEDIUM 50-70%)")
        print(f"   AI Similarity: {result['ai_similarity']}%")
        print(f"   Confidence: {result['confidence']}%")
        print(f"   Suggestions: {result['suggestions'][0] if result['suggestions'] else 'None'}")
    else:
        print(f"❌ Error: {response.status_code}")
        print(response.json())
    
else:
    print(f"❌ LOGIN FAILED: {response.json()}")
