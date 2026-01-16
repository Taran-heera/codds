#!/usr/bin/env python
"""Test the enhanced AI analyzer"""

import sys
sys.path.insert(0, r'c:\Users\admin\Desktop\echo\backend')

from app.utils.ai_analyzer import OriginallityAnalyzer

# Test 1: Pure AI text (no contractions, no personal pronouns, formal)
ai_text = """Furthermore, it is evident that the implementation of advanced technologies has become increasingly important in contemporary society. Nevertheless, it should be noted that such innovations can present significant challenges. In conclusion, it is clear that proper consideration and planning are essential. As previously mentioned, the framework requires careful analysis. Ultimately, the results demonstrate conclusively that systematic approaches yield better outcomes. Moreover, the data suggests that ongoing refinement is necessary. Indeed, the evidence indicates that continued investment in research remains paramount."""

print("=" * 70)
print("TEST 1: PURE AI TEXT (Expected: < 30% originality)")
print("=" * 70)
result1 = OriginallityAnalyzer.analyze_text(ai_text)
print(f"Originality Score: {result1['originality_score']}%")
print(f"AI Similarity: {result1['ai_similarity']}%")
print(f"Style Drift: {result1['style_drift']:.1f}")
print(f"Confidence: {result1['confidence']:.1f}")
print(f"AI Phrase Count: {result1['drift_details']['ai_phrase_count']}")

# Test 2: Human text (with contractions, personal pronouns, casual)
human_text = """I think it's really important to understand that technology isn't just about fancy gadgets. You know, I've spent years looking at this stuff, and honestly? It's not that complicated. What I mean is, don't get me wrong - there's definitely some complex stuff happening. But here's the thing: you don't really need to understand all of it to benefit from it. I mean, I can't tell you how many times I've seen people overthinking this! Look, the bottom line is that if you're willing to try new things, you'll figure it out. Really, that's it."""

print("\n" + "=" * 70)
print("TEST 2: HUMAN TEXT (Expected: > 70% originality)")
print("=" * 70)
result2 = OriginallityAnalyzer.analyze_text(human_text)
print(f"Originality Score: {result2['originality_score']}%")
print(f"AI Similarity: {result2['ai_similarity']}%")
print(f"Style Drift: {result2['style_drift']:.1f}")
print(f"Confidence: {result2['confidence']:.1f}")

# Test 3: Mixed text
mixed_text = """I've been thinking about this for a while now. It's important to understand that modern systems have become increasingly complex. You know? But furthermore, it's evident that proper implementation requires careful planning. As I mentioned earlier, I think innovation is crucial. However, one must consider the ramifications carefully. In conclusion, I believe we should continue exploring these opportunities. The data suggests, moreover, that our approach is sound."""

print("\n" + "=" * 70)
print("TEST 3: MIXED TEXT (Expected: 40-60% originality)")
print("=" * 70)
result3 = OriginallityAnalyzer.analyze_text(mixed_text)
print(f"Originality Score: {result3['originality_score']}%")
print(f"AI Similarity: {result3['ai_similarity']}%")
print(f"Style Drift: {result3['style_drift']:.1f}")
print(f"Confidence: {result3['confidence']:.1f}")

print("\n" + "=" * 70)
print("ANALYSIS COMPLETE")
print("=" * 70)
print(f"Test 1 (AI): {result1['originality_score']:.1f}% - {'PASS ✓' if result1['originality_score'] < 40 else 'FAIL ✗'}")
print(f"Test 2 (Human): {result2['originality_score']:.1f}% - {'PASS ✓' if result2['originality_score'] > 60 else 'FAIL ✗'}")
print(f"Test 3 (Mixed): {result3['originality_score']:.1f}% - {'PASS ✓' if 40 <= result3['originality_score'] <= 70 else 'FAIL ✗'}")
