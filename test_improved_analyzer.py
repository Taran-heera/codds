import sys
sys.path.insert(0, r'c:\Users\admin\Desktop\echo\backend')

from app.utils.ai_analyzer import OriginallityAnalyzer

# Test 1: WhatsApp (Human conversational)
wa_text = """See da we can't depend on others for doing something, even if you have friends or not just don't feel depressed that you don't have anyone at some point in life we'll all be alone. So just take it as what you're facing is making you strong enough to face the rest"""

# Test 2: Formal AI text
ai_text = """Furthermore, it is worth noting that in conclusion, the aforementioned system provides substantial benefits. Moreover, the subsequent analysis demonstrates that principles are consequential. In essence, this represents an important advancement."""

# Test 3: Mixed normal text
normal_text = """I believe the project went well. We faced some challenges, but we learned from them. The team was amazing and I think our approach was pretty good. Honestly, I'm proud of what we accomplished."""

# Test 4: Clearly AI generated
clear_ai = """The implementation of advanced technological systems has demonstrable efficacy in contemporary organizational paradigms. It should be noted that such initiatives facilitate enhanced operational efficiency. Furthermore, comprehensive analyses indicate substantial improvements in performance metrics across diverse demographic segments."""

print("="*70)
print("IMPROVED ANALYZER - REALISTIC BALANCED SCORING")
print("="*70)

test_cases = [
    ('WhatsApp (Casual/Informal)', wa_text),
    ('Formal AI-like Text', ai_text),
    ('Normal Mixed Text', normal_text),
    ('Clear AI Generated', clear_ai)
]

for name, text in test_cases:
    result = OriginallityAnalyzer.analyze_text(text)
    print(f"\n{name}:")
    print(f"  Originality:  {result['originality_score']:>6}%")
    print(f"  AI Similarity: {result['ai_similarity']:>6}%")
    print(f"  Confidence:   {result['confidence']:>6}%")
    print(f"  Suggestion:   {result['suggestions'][0]}")

print("\n" + "="*70)
print("ANALYSIS:")
print("="*70)
print("✅ WhatsApp should be 75-88% (conversational, informal)")
print("✅ Formal AI-like should be 45-60% (some AI patterns)")
print("✅ Normal mixed should be 65-78% (balanced human)")
print("✅ Clear AI should be 20-40% (heavy AI patterns)")
print("✅ All scores between 5-95 (REALISTIC, not extreme)")
