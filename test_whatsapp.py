import sys
sys.path.insert(0, r'c:\Users\admin\Desktop\echo\backend')

from app.utils.ai_analyzer import OriginallityAnalyzer

# Test with the WhatsApp message
whatsapp_text = """See da we can't depend on others for doing something, even if you have friends or not just don't feel depressed that you don't have anyone at some point in life we'll all be alone. So just take it as what you're facing is making you strong enough to face the rest"""

print("="*60)
print("TESTING FIXED ANALYZER")
print("="*60)
print(f"Text: {whatsapp_text[:60]}...\n")

result = OriginallityAnalyzer.analyze_text(whatsapp_text)

print(f"Originality Score: {result['originality_score']}%")
print(f"AI Similarity: {result['ai_similarity']}%")
print(f"\nSuggestions:")
for i, sugg in enumerate(result['suggestions'], 1):
    print(f"  {i}. {sugg}")

print(f"\nStyle Analysis:")
fp = result['style_fingerprint']
print(f"  - Word count: {fp['word_count']}")
print(f"  - AI phrases found: {fp['ai_phrase_count']}")
print(f"  - Vocabulary diversity: {fp['vocabulary_diversity']}%")

print("\n" + "="*60)
print("CONSISTENCY TEST")
print("="*60)
result2 = OriginallityAnalyzer.analyze_text(whatsapp_text)
if result['originality_score'] == result2['originality_score']:
    print(f"✅ CONSISTENT: {result['originality_score']}% both times")
else:
    print(f"❌ INCONSISTENT: {result['originality_score']}% vs {result2['originality_score']}%")
