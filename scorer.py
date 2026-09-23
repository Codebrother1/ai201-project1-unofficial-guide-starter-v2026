"""
Simple scorer for AI201 Unit 2.

A question passes when the generated answer contains the expected
word or phrase from questions.py. Comparison is case-insensitive.
"""


def judge(question, expects, answer, results) -> bool:
    """Return True when the expected phrase appears in the answer."""
    if not expects:
        return False

    return expects.lower() in answer.lower()
