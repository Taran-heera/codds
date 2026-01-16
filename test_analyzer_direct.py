#!/usr/bin/env python
"""Direct analyzer test without Flask"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app.utils.ai_analyzer import OriginallityAnalyzer

print("=" * 70)
print("AI ANALYZER TEST - NEW FIXED VERSION")
print("=" * 70)

# Test 1: Heavy AI text
print("\n🤖 TEST 1: HEAVY AI TEXT (should be LOW 10-30%)")
print("-" * 70)
ai_text = """
Furthermore, it is worth noting that in light of contemporary technological advancement, 
artificial intelligence has become increasingly prevalent in modern society. Consequently, 
the implications of this technological evolution are manifold and multifaceted. Moreover, 
as previously mentioned, it should be noted that the aforementioned developments warrant 
careful consideration. In conclusion, therefore, it is evident that the subsequent era 
shall present novel challenges and opportunities. Nevertheless, it is important to highlight 
that the cumulative effects of these technological innovations remain uncertain.
"""
result = OriginallityAnalyzer.analyze_text(ai_text.strip())
print(f"Originality Score: {result['originality_score']}%")
print(f"AI Similarity: {result['ai_similarity']}%")
print(f"Suggestions: {result['suggestions'][0]}")
if result['originality_score'] < 40:
    print("✅ CORRECT - Low originality detected (AI text)")
else:
    print(f"❌ WRONG - Should be <40%, got {result['originality_score']}%")

# Test 2: Human conversational text
print("\n👤 TEST 2: HUMAN CONVERSATIONAL TEXT (should be HIGH 70-90%)")
print("-" * 70)
human_text = """
So like, I was thinking about how technology has changed everything, right? 
I mean, honestly, when I was younger, we didn't have smartphones and stuff. 
Now I literally can't imagine living without my phone! It's crazy how fast things change. 
Don't you think? Anyway, I really believe that AI is going to be important in the future.
"""
result = OriginallityAnalyzer.analyze_text(human_text.strip())
print(f"Originality Score: {result['originality_score']}%")
print(f"AI Similarity: {result['ai_similarity']}%")
print(f"Suggestions: {result['suggestions'][0]}")
if result['originality_score'] > 65:
    print("✅ CORRECT - High originality detected (Human text)")
else:
    print(f"❌ WRONG - Should be >65%, got {result['originality_score']}%")

# Test 3: Mixed formal but human
print("\n📝 TEST 3: MIXED FORMAL BUT HUMAN (should be MEDIUM 50-70%)")
print("-" * 70)
mixed_text = """
I've been reading a lot about machine learning lately, and I think it's really interesting. 
From what I can understand, it's basically just computers learning patterns from data. 
However, I'm still trying to wrap my head around how it all works, to be honest. 
The way I see it, we're only at the beginning of what AI can do. What do you think?
"""
result = OriginallityAnalyzer.analyze_text(mixed_text.strip())
print(f"Originality Score: {result['originality_score']}%")
print(f"AI Similarity: {result['ai_similarity']}%")
print(f"Suggestions: {result['suggestions'][0]}")
if 45 < result['originality_score'] < 75:
    print("✅ CORRECT - Mixed originality detected")
else:
    print(f"⚠️ BORDERLINE - Expected 45-75%, got {result['originality_score']}%")

print("\n" + "=" * 70)
print("ANALYZER TESTS COMPLETE")
print("=" * 70)
