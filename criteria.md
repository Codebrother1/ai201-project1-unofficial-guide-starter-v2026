# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. _"Retrieval works"_ is an opinion. _"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"_ is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; _"80% seemed reasonable"_ does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that contains the answer.

**Why this target:**

One of my questions asks specifically how the housing lottery works for juniors and seniors. The housing lottery document contains different rules for different class years, so retrieving a housing-related chunk is not enough by itself. The retrieved chunk has to contain the specific rule about juniors and seniors being ordered by accumulated credit hours. I chose 4 out of 5 because I expect retrieval to succeed on most questions while allowing one harder question to miss the exact detail it needs.

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

I want every answer to name at least one source document so I can trace the answer back to the evidence it came from. If the source is named, I can check the document and verify that the system is not inventing information. I chose 5 out of 5 because source attribution should happen every time the system gives an answer.

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate stops it and the system returns "I don't have enough information about that" in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**

The system should not answer questions when the corpus does not contain relevant information. If there is no strong retrieved evidence, the model has no source of truth and could produce a confident but unsupported answer. I chose 4 out of 5 because I want the relevance gate to refuse almost all clearly out-of-scope questions while allowing for one imperfect retrieval decision.

## 4. Chunks keep complete sentences

For at least 4 of my 5 sampled chunks from `campus_life`, no sentence is cut off at the beginning or end of the chunk.

**Why this target:**

In `campus_life`, useful facts are usually short and specific, such as a location, time, rule, or deadline. If the chunker cuts through the sentence containing that fact, the chunk may lose the information needed to answer the question. I chose 4 out of 5 instead of 5 out of 5 because I expect an occasional chunk boundary to be imperfect.

---

## 5. Specific facts are supported by retrieved evidence

For at least 4 of my 5 test answers, every specific factual detail used to answer the question, such as a time, duration, location, fee, or deadline, is directly supported by at least one retrieved chunk.

**Why this target:**

If the system says a dining hall closes at 11 when the retrieved source says 9, I would not trust the system. Practical details like times, locations, costs, and deadlines need to come from the retrieved evidence instead of being invented by the model. I chose 4 out of 5 because I want a high standard while still leaving room for one failure that I can diagnose and improve.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
