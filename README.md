# The Unofficial Guide

TC — Corpus: campus_life

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

This project builds a RAG system over the `campus_life` corpus and defines in advance what a correct, working answer should look like. I chose how the documents should be chunked, tuned retrieval so the system brings back relevant information, and set a relevance cutoff so it can refuse questions that are not supported by the corpus. When the system does answer, it uses retrieved evidence and names the source document so the information can be checked.

## Chunking Strategy

I keep each `campus_life` document as one chunk because the posts are already short. Splitting them further could separate a heading, service name, course name, or location from the sentence containing the useful fact. Keeping each post whole preserves complete sentences and enough context for the chunk to stand on its own.
**Chunk size:**
One whole `campus_life` document per chunk; no fixed character size.

**Overlap:** None.

## Sample Chunks

**Chunk 1** — source: `admin_add_drop_deadline.txt#0` — produced by: `chunker.py::split_documents`

```text
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

**Chunk 2** — source: `course_biol_160.txt#0` — produced by: `chunker.py::split_documents`

```text
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

**Chunk 3** — source: `course_hist_118_workload.txt#0` — produced by: `chunker.py::split_documents`

```text
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

**Chunk 4** — source: `dining_pellew_dining_hall_followup.txt#0` — produced by: `chunker.py::split_documents`

```text
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

**Chunk 5** — source: `housing_innisfree_hall.txt#0` — produced by: `chunker.py::split_documents`

```text
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

**Question:** How are housing lottery numbers determined for juniors and seniors?

**Answer:** Juniors and seniors are ordered by accumulated credit hours first, with a random tie-break used only when necessary.

**Source:** `admin_housing_lottery.txt`

**My relevance cutoff:** `0.6`

My five in-scope questions had best retrieval distances from `0.1467` to `0.3079`. My five out-of-scope questions had best distances from `0.8246` to `0.9340`.

I kept the cutoff at `0.6` because it falls clearly between those two groups. A lower cutoff could reject questions my corpus can actually answer, while a much higher cutoff could let unrelated questions through and give the model a chance to answer without relevant evidence.

| Question                 | In corpus? | Best distance |
| ------------------------ | ---------- | ------------: |
| Housing lottery          | Yes        |        0.1969 |
| Dining dollars           | Yes        |        0.2206 |
| Parking permits          | Yes        |        0.2085 |
| Library holds            | Yes        |        0.1467 |
| CS 210 exams             | Yes        |        0.3079 |
| Capital of Mongolia      | No         |        0.8246 |
| Diesel engine oil change | No         |        0.9340 |
| 1994 World Cup           | No         |        0.8859 |
| Ibuprofen dosage         | No         |        0.8442 |
| Rust for loop            | No         |        0.8960 |

## How I Used AI

**1.** I used AI to help me think through the chunking strategy for the `campus_life` corpus. At first, we considered splitting on paragraph boundaries, but after looking at the documents I decided to keep each short post as one chunk because splitting them could separate a heading, course name, service name, or location from the fact it explains. I used the AI explanation to understand the tradeoff, but the final decision was based on the structure of my corpus.

**2.** I used AI to help me refine my acceptance criteria into specific, testable statements. I explained what I cared about, such as making sure answers are supported by retrieved evidence and that the system refuses questions outside the corpus, and the AI helped turn those ideas into measurable wording. I changed the wording so the criteria reflected my own examples and standards, including checking exact facts against retrieved chunks instead of just accepting answers that sounded reasonable.git status

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

| Criterion                                             | Target | Run 1 | Run 2 | Run 3 | Verdict |
| ----------------------------------------------------- | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer                | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 2. Every answer names a source                        | 5 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 3. Gate stops out-of-corpus questions                 | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 4. Chunks keep complete sentences                     | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |
| 5. Specific facts are supported by retrieved evidence | 4 of 5 | 5/5   | 5/5   | 5/5   | MET     |

The generated-answer and gate evidence below comes from
`results/run_2026-09-23_1618_before.md`, produced by
`run_eval.py::main`.

Retrieval was performed by `store.py::search`, and retrieved chunks were
produced by `chunker.py::split_documents`.

### Real Output — Criterion 1

The criterion asks whether the retrieved chunks contain the answer for at least
4 of the 5 test questions.

Actual retrieval output from run 1:

```text
How are housing lottery numbers determined for juniors and seniors?

Best distance: 0.1969
Sources retrieved: admin_housing_lottery.txt, admin_parking_permits.txt,
advising_registration.txt, course_stat_150_exams.txt, housing_tamsin_court.txt

Do unused dining dollars roll over from spring to the next fall?

Best distance: 0.2206
Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt,
admin_parking_permits.txt, dining_halden_hall.txt, dining_north_kitchen.txt

How quickly do west lot student parking permits sell out?

Best distance: 0.2085
Sources retrieved: admin_library_holds.txt, admin_parking_permits.txt,
advising_registration.txt, dining_halden_hall.txt, transit_shuttle.txt

How long does a hold on a checked-out library book usually take to arrive?

Best distance: 0.1467
Sources retrieved: admin_library_holds.txt,
dining_halden_hall_followup.txt,
dining_verrill_street_grill_followup.txt,
money_textbooks.txt,
study_group_rooms.txt

What material are the CS 210 exams drawn from?

Best distance: 0.3079
Sources retrieved: course_cs_210.txt, course_cs_210_exams.txt,
course_cs_340_exams.txt, course_engl_205.txt,
course_engl_205_exams.txt
```

For all 5 questions, the retrieved results included the document containing the
answer. The same retrieval results were produced in all three runs.

### Real Output — Criterion 2

The criterion asks whether every produced answer names at least one real source
document.

Actual answers from run 1:

```text
Housing:

For juniors and seniors, housing lottery numbers are ordered by accumulated
credit hours first, with a random tie-break used only when necessary
(admin_housing_lottery.txt).

Dining:

No, unused dining dollars do not roll over from spring to the following
autumn; whatever is left in May disappears
(from admin_dining_dollars.txt).

Parking:

Student permits for the west lots sell out in about three days
(admin_parking_permits.txt).

Library:

A hold on a checked-out book usually arrives in two to three days.
(Source: admin_library_holds.txt)

CS 210:

The CS 210 exams are drawn from lecture material rather than the textbook.

Sources: course_cs_210_exams.txt and course_cs_210.txt
```

All 5 of 5 answers named at least one real source document in each of the three
runs.

### Real Output — Criterion 3

This criterion is measured by `run_eval.py::check_out_of_scope` using the
relevance cutoff of `0.6`.

Actual output:

```text
refused  (best distance 0.825)  What is the capital of Mongolia?
refused  (best distance 0.934)  How do I change the oil in a diesel engine?
refused  (best distance 0.886)  Who won the 1994 World Cup?
refused  (best distance 0.844)  What is the recommended dosage of ibuprofen for a headache?
refused  (best distance 0.896)  How do I write a for loop in Rust?
-> gate refused 5 of 5
```

The target was at least 4 of 5 refusals. The system refused all 5 of 5.

Retrieval and the relevance gate are deterministic, so the same 5/5 result is
recorded in all three run columns.

### Real Output — Criterion 4

This criterion was checked with `app.py::cmd_chunks` using chunks produced by
`chunker.py::split_documents`.

The same deterministic sample was checked three times.

Actual sampled chunks:

```text
Chunk 1 | source: admin_add_drop_deadline.txt#0
produced by: chunker.py::split_documents

On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer
window — through the end of week six — but a drop after week two shows as a W
on your transcript. Nothing anywhere on the registrar's site says this plainly,
and students find out from each other.

Chunk 2 | source: course_biol_160.txt#0
produced by: chunker.py::split_documents

BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a
weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks;
falling behind once is very hard to recover from.

Chunk 3 | source: course_hist_118_workload.txt#0
produced by: chunker.py::split_documents

Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem
sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because
you're learning the format.

Chunk 4 | source: dining_pellew_dining_hall_followup.txt#0
produced by: chunker.py::split_documents

Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of
12 to 18 minutes at peak matches what I've seen. If you're trying to eat
between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics
centre. Nobody tells you this at orientation.

Chunk 5 | source: housing_innisfree_hall.txt#0
produced by: chunker.py::split_documents

Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991,
renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom
between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best
compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of
September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the
building is L-shaped and the short wing is much quieter.
```

All 5 of 5 sampled chunks began and ended on complete sentence/document
boundaries in each check.

### Real Output — Criterion 5

The criterion asks whether every specific factual detail used in the answer is
directly supported by retrieved evidence.

Actual run-1 answers:

```text
Housing:
For juniors and seniors, housing lottery numbers are ordered by accumulated
credit hours first, with a random tie-break used only when necessary
(admin_housing_lottery.txt).

Dining:
No, unused dining dollars do not roll over from spring to the following
autumn; whatever is left in May disappears
(from admin_dining_dollars.txt).

Parking:
Student permits for the west lots sell out in about three days
(admin_parking_permits.txt).

Library:
A hold on a checked-out book usually arrives in two to three days.
(Source: admin_library_holds.txt)

CS 210:
The CS 210 exams are drawn from lecture material rather than the textbook.

Sources: course_cs_210_exams.txt and course_cs_210.txt
```

The retrieved source documents directly support those details:

```text
admin_housing_lottery.txt:
juniors and seniors are ordered by accumulated credit hours first,
and only tie-break randomly.

admin_dining_dollars.txt:
Whatever is left in May disappears.

admin_parking_permits.txt:
Student permits for the west lots go on sale in August and sell out
in about three days.

admin_library_holds.txt:
You can place a hold on a checked-out book and it usually arrives
in two to three days.

course_cs_210_exams.txt:
Two midterms and a final, all drawn from lecture material rather than
the textbook.
```

All 5 of 5 answers had their specific factual details directly supported by
retrieved evidence in all three runs.

## Verdicts

| # | Criterion| Verdict | How I decided|| --- | -------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | Retrieved chunk contains the answer | MET | The frozen target was at least 4 of 5 questions retrieving a chunk that contained the answer. All three runs achieved 5 of 5, so the criterion held consistently. |
| 2 | Every answer names a source | MET | The target was 5 of 5 produced answers naming at least one real source document. All 5 answers named a real source in all three runs. |
| 3 | Gate stops out-of-corpus questions | MET | The target was for the relevance gate to refuse at least 4 of 5 clearly out-of-corpus questions. It refused all 5 of 5. |
| 4 | Chunks keep complete sentences | MET | The target was for at least 4 of 5 sampled `campus_life` chunks to begin and end with complete sentence boundaries. All 5 sampled chunks had complete boundaries in all three checks. |
| 5 | Specific facts are supported by retrieved evidence | MET | The frozen target was for at least 4 of 5 test answers to have every specific factual detail directly supported by retrieved evidence. All 5 of 5 answers were supported in all three runs. |

## Diagnoses

No criteria were missed.

However, Criterion 4 was set too low. The original target required at least
4 of 5 sampled chunks to have complete sentence boundaries, but the
whole-document chunking strategy produced 5 of 5 complete chunks in every
check.

If I wrote this criterion again, I would tighten the target to 5 of 5 because
my whole-document chunking strategy is specifically designed to preserve each
short document intact.

I also noticed a retrieval-stage weakness even though it did not cause a
criterion failure. With `TOP_K = 5`, the system often retrieved the correct
answer-bearing document along with several unrelated distractor chunks. For
example, the housing question retrieved `admin_housing_lottery.txt`, but also
retrieved parking, advising, statistics, and another housing document. This
means the generation stage receives more irrelevant context than it needs.

## The Improvement

**What I changed:**

I will reduce retrieval `TOP_K` from `5` to `3` in `config.py`.
**Why I picked it:**

The baseline showed that the answer-bearing document was already ranked highly
for all five test questions, but the five-result retrieval set also contained
unrelated distractor chunks. Reducing `TOP_K` from 5 to 3 should give the model
less irrelevant context while still preserving the evidence needed to answer
the questions. I will measure the full test again to see whether that actually
helps or hurts.

### Run Log — After

| Criterion                                             | Target | Run 1 | Run 2 | Run 3 | Verdict |
| ----------------------------------------------------- | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer                | 4 of 5 |       |       |       |         |
| 2. Every answer names a source                        | 5 of 5 |       |       |       |         |
| 3. Gate stops out-of-corpus questions                 | 4 of 5 |       |       |       |         |
| 4. Chunks keep complete sentences                     | 4 of 5 |       |       |       |         |
| 5. Specific facts are supported by retrieved evidence | 4 of 5 |       |       |       |         |

**Did it help?**

To be completed after running:

`python run_eval.py --label after`

I will compare this run log directly with the Before run log and report whether
reducing `TOP_K` from 5 to 3 improved, preserved, or hurt the measured results.

## What's Still Broken

To be completed after the After evaluation.

If any criterion is missed after the improvement, I will state which pipeline
stage caused the remaining problem, what I would change next, and why I stopped
after this one measured improvement.

If all five criteria are still met, I will still report any remaining weakness
I observed rather than claiming the system is perfect.

## What I'd Do Differently

Knowing what I know now, I would write Criterion 4 more strictly.

The original criterion required at least 4 of 5 sampled `campus_life` chunks
to contain complete sentence boundaries. Because my chunking strategy keeps
each short document intact and produced 5 of 5 complete chunks every time I
checked it, I would set the target to 5 of 5 in a future version.

I would not change the original Unit 1 criterion now because it was measurable
as written and existed before I saw the results. The stricter 5-of-5 target is
what I learned from testing it.
