"""NLP preprocessing and FAQ matching."""

from __future__ import annotations

import re
from dataclasses import dataclass

import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def _ensure_nltk_resource(path: str, resource: str) -> None:
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(resource, quiet=True)


_ensure_nltk_resource("tokenizers/punkt_tab", "punkt_tab")
_ensure_nltk_resource("tokenizers/punkt", "punkt")
_ensure_nltk_resource("corpora/stopwords", "stopwords")

from nltk.tokenize import word_tokenize

# Keep cricket terms like "over", "out", "wide" — NLTK stopwords remove too many of these.
MINIMAL_STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "what", "who", "how", "why", "when", "where", "which", "whom", "whose",
    "do", "does", "did", "doing", "done",
    "in", "on", "at", "to", "for", "of", "and", "or", "but", "if", "then",
    "me", "my", "your", "you", "i", "we", "they", "he", "she", "it", "them",
    "tell", "explain", "describe", "define", "please", "can", "could", "would",
    "about", "also", "just", "like", "get", "give",
}


@dataclass
class FAQMatch:
    question: str
    answer: str
    score: float


def preprocess(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in MINIMAL_STOP_WORDS and len(token) > 1]
    return " ".join(tokens)


def _faq_search_text(item: dict[str, str]) -> str:
    aliases = item.get("aliases", [])
    parts = [item["question"], *aliases]
    return " ".join(parts)


class FAQMatcher:
    def __init__(self, faqs: list[dict[str, str]], threshold: float = 0.12) -> None:
        self.faqs = faqs
        self.threshold = threshold
        self.questions = [item["question"] for item in faqs]
        self.answers = [item["answer"] for item in faqs]
        self.search_texts = [_faq_search_text(item) for item in faqs]
        self.processed_search_texts = [preprocess(text) for text in self.search_texts]
        self.processed_questions = [preprocess(q) for q in self.questions]

        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1)
        self.search_matrix = self.vectorizer.fit_transform(self.processed_search_texts)

    def _exact_match_bonus(self, processed_query: str, faq_index: int) -> float:
        processed_question = self.processed_questions[faq_index]
        if processed_query == processed_question:
            return 0.35
        return 0.0

    def _relevance_bonus(self, query_tokens: set[str], faq_index: int) -> float:
        question_tokens = set(self.processed_questions[faq_index].split())
        if not query_tokens or not question_tokens:
            return 0.0

        matched = query_tokens & question_tokens
        extra_tokens = question_tokens - query_tokens

        if len(query_tokens) <= 2:
            coverage = len(matched) / len(question_tokens)
            extra_penalty = 0.12 * len(extra_tokens)
            return max(0.0, 0.42 * coverage - extra_penalty)

        overlap_ratio = len(matched) / len(query_tokens)
        return 0.2 * overlap_ratio

    def find_best_match(self, user_query: str) -> FAQMatch | None:
        processed_query = preprocess(user_query)
        if not processed_query.strip():
            return None

        query_tokens = set(processed_query.split())
        query_vector = self.vectorizer.transform([processed_query])
        cosine_scores = cosine_similarity(query_vector, self.search_matrix)[0]

        ranked_indices = cosine_scores.argsort()[::-1][:8]
        best_index = int(ranked_indices[0])
        best_score = float(cosine_scores[best_index])

        for index in ranked_indices:
            idx = int(index)
            combined = (
                float(cosine_scores[idx])
                + self._relevance_bonus(query_tokens, idx)
                + self._exact_match_bonus(processed_query, idx)
            )
            current_best = (
                float(cosine_scores[best_index])
                + self._relevance_bonus(query_tokens, best_index)
                + self._exact_match_bonus(processed_query, best_index)
            )
            if combined > current_best:
                best_index = idx
                best_score = float(cosine_scores[best_index])

        best_score = (
            float(cosine_scores[best_index])
            + self._relevance_bonus(query_tokens, best_index)
            + self._exact_match_bonus(processed_query, best_index)
        )

        if best_score < self.threshold:
            return None

        return FAQMatch(
            question=self.questions[best_index],
            answer=self.answers[best_index],
            score=min(best_score, 1.0),
        )
