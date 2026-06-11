from __future__ import annotations

import re

from ..models import FAQ


COMMON_WORDS = {
    "what", "when", "where", "how", "your", "you", "the", "is", "are", "do", "does", "can", "i", "we", "a", "an", "to", "for", "of", "in", "on", "and", "or", "please",
}


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9\s]", " ", (text or "").lower()).strip()


def tokens(text: str) -> set[str]:
    return {t for t in normalize(text).split() if t not in COMMON_WORDS and len(t) > 2}


def match_faq(text: str) -> FAQ | None:
    query_tokens = tokens(text)
    if not query_tokens:
        return None
    best_score = 0
    best_faq = None
    for faq in FAQ.query.filter_by(is_active=True).all():
        faq_tokens = tokens(" ".join([faq.question, faq.answer, faq.category, faq.keywords]))
        score = len(query_tokens & faq_tokens)
        if normalize(faq.question) in normalize(text):
            score += 10
        for keyword in [k.strip().lower() for k in faq.keywords.split(",") if k.strip()]:
            if keyword and keyword in normalize(text):
                score += 3
        if score > best_score:
            best_score = score
            best_faq = faq
    return best_faq if best_score >= 2 else None


def faq_categories_summary() -> str:
    categories = sorted({faq.category for faq in FAQ.query.filter_by(is_active=True).all()})
    if not categories:
        return "No FAQs are configured yet."
    return "You can ask me about: " + ", ".join(categories) + "."
