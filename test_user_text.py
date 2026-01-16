#!/usr/bin/env python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from app.utils.ai_analyzer import OriginallityAnalyzer

text = """Technology has become an inseparable part of modern life. From smartphones that connect us instantly across the globe to artificial intelligence systems that help doctors diagnose diseases faster, innovation continues to reshape the way we live and work. While these advancements bring convenience and efficiency, they also raise important questions about privacy, ethics, and the role of humans in a rapidly changing world. Understanding both the benefits and challenges of technology is essential for preparing future generations to thrive in this digital age."""

result = OriginallityAnalyzer.analyze_text(text)
print(f"Your Text Analysis: {result['originality_score']}%")
print(f"AI Similarity: {result['ai_similarity']}%")
print(f"\n⚠️  Problem: Should be <50% but showing {result['originality_score']}%")
print(f"Reason: This is clearly AI-generated (formal, structured, no personal voice)")
