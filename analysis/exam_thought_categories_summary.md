# EXAM Thought Analysis Category Mapping

This document summarizes the error categories generated for the EXAM prompt regressions, and their mapping to the standard UMBRELA categories.

## Overall Category Distribution

| Category | Count | Is UMBRELA Category? |
|---|---|---|
| Overly Strict Relevance Threshold | 2284 | Yes |
| Over-crediting tangential relevance | 973 | Yes |
| Score-Reasoning Inconsistency | 761 | No (New) |
| Overly Strict Interpretation | 563 | Yes |
| Hallucinated Requirement | 453 | Yes |
| Missing Reasoning | 357 | Yes |
| Superficial Keyword Matching | 204 | Yes |
| Ignored Nuance | 147 | Yes |
| Score-Reasoning Discrepancy | 98 | No (New) |
| Hallucinated Query | 88 | No (New) |
| Score-Reasoning Mismatch | 82 | No (New) |
| Over-weighted specific aspect | 72 | Yes |
| Over-weighted keyword match | 49 | Yes |
| Score Inconsistency | 42 | No (New) |
| Reasoning-Output Inconsistency | 24 | No (New) |
| Flawed Meta-Reasoning | 23 | No (New) |
| Internal Contradiction | 19 | No (New) |
| Internal Inconsistency | 18 | No (New) |
| Reasoning-Output Disconnect | 16 | No (New) |
| Task Misinterpretation | 16 | No (New) |
| Reasoning-Score Inconsistency | 16 | No (New) |
| Over-weighted topical overlap | 15 | Yes |
| Scoring Scale Confusion | 15 | No (New) |
| Score Mismatch | 14 | No (New) |
| Scale Calibration Error | 12 | No (New) |
| Reasoning-Output Discrepancy | 11 | No (New) |
| Failure to Recognize Identifier Query | 11 | No (New) |
| Meta-Reasoning Fallacy | 9 | No (New) |
| Score/Reasoning Inconsistency | 9 | No (New) |
| Reasoning-Output Mismatch | 8 | No (New) |
| Score Mapping Inconsistency | 8 | No (New) |
| Failed Identifier Resolution | 8 | No (New) |
| Failure to Recognize Identifier | 8 | No (New) |
| Rubric Miscalibration | 7 | No (New) |
| Literal Interpretation of Query ID | 7 | No (New) |
| Identifier Mapping Failure | 7 | No (New) |
| Scale Misalignment | 6 | No (New) |
| Score Discrepancy | 6 | No (New) |
| Reasoning-Output Contradiction | 6 | No (New) |
| Failure to Resolve Query ID | 6 | No (New) |
| Score Calibration | 5 | No (New) |
| Reasoning-Score Discrepancy | 5 | No (New) |
| Score Miscalibration | 5 | No (New) |
| Failed Identifier Recognition | 5 | No (New) |
| Failure to Resolve Query Identifier | 5 | No (New) |
| Rubric Misinterpretation | 4 | No (New) |
| Reasoning-Score Contradiction | 4 | No (New) |
| Scoring Inconsistency | 4 | No (New) |
| Conclusion-Score Mismatch | 4 | No (New) |
| Failure to Handle Identifier Query | 4 | No (New) |
| Score-Reasoning Disconnect | 4 | No (New) |
| Failure to resolve query ID | 4 | No (New) |
| Rating Scale Confusion | 3 | No (New) |
| Meta-Reasoning Confusion | 3 | No (New) |
| Score-reasoning contradiction | 3 | No (New) |
| Score Contradiction | 3 | No (New) |
| Score Disconnect | 3 | No (New) |
| Scale Mismatch | 3 | No (New) |
| Score Mapping Error | 3 | No (New) |
| Reasoning-Score Disconnect | 3 | No (New) |
| Misapplied Evaluation Criteria | 3 | No (New) |
| Internal Contradiction / Scale Confusion | 3 | No (New) |
| Convoluted Meta-Reasoning | 3 | No (New) |
| Scale Confusion | 3 | No (New) |
| Score Calibration Inconsistency | 3 | No (New) |
| Scale Range Mismatch | 3 | No (New) |
| Conflating Absence with an Answer | 3 | No (New) |
| Meta-reasoning Fallacy | 3 | No (New) |
| Failed to Recognize Document Identifier | 3 | No (New) |
| Dataset Artifact Misinterpretation | 3 | No (New) |
| Failure to Handle Query ID | 3 | No (New) |
| Task Confusion | 3 | No (New) |
| Rating Scale Violation | 3 | No (New) |
| Overthinking Meta-Question | 3 | No (New) |
| Failure to Recognize Document Identifier | 3 | No (New) |
| Failure to resolve entity identifier | 3 | No (New) |
| Failed Entity Resolution | 3 | No (New) |
| Treated Graded Scale as Binary | 2 | No (New) |
| Score mismatch with reasoning | 2 | No (New) |
| Equating Relevance with Answerability | 2 | No (New) |
| Scale Violation | 2 | No (New) |
| Score calibration error | 2 | No (New) |
| Flawed Task Logic | 2 | No (New) |
| Score/Reasoning Discrepancy | 2 | No (New) |
| Overthinking Negative Answerability | 2 | No (New) |
| Internal Reasoning Inconsistency | 2 | No (New) |
| Score Discrepancy / Scale Confusion | 2 | No (New) |
| Conflating Absence of Information with an Answer | 2 | No (New) |
| Scale Mapping Error | 2 | No (New) |
| Scale Non-Compliance | 2 | No (New) |
| Failure to handle identifier query | 2 | No (New) |
| Failure to Recognize Query Identifier | 2 | No (New) |
| Unrecognized Numeric Identifier | 2 | No (New) |
| Spurious Match / Hallucinated Relevance | 2 | No (New) |
| Failed to Recognize Identifier Query | 2 | No (New) |
| Miscalibrated Scoring | 2 | No (New) |
| Score-reasoning inconsistency | 2 | No (New) |
| Failure to resolve query identifier | 2 | No (New) |
| Entity Resolution Failure | 2 | No (New) |
| Literal Interpretation of Query Identifier | 2 | No (New) |
| Failure to Resolve Identifier | 2 | No (New) |
| Failure to Resolve Numeric Identifier | 2 | No (New) |
| Unrecognized Identifier Query | 2 | No (New) |
| Failure to Handle Query ID Artifact | 2 | No (New) |
| Flawed meta-reasoning | 1 | No (New) |
| Scoring Scale Misalignment | 1 | No (New) |
| Conflated Answerability with Relevance | 1 | No (New) |
| Inverted Answerability Logic | 1 | No (New) |
| Misapplied Scoring Rubric | 1 | No (New) |
| Factual error regarding document content | 1 | No (New) |
| Penalized Query Quality | 1 | No (New) |
| Treated Graded Relevance as Binary | 1 | No (New) |
| Misapplication of Rating Scale | 1 | No (New) |
| Treated Relevance as Binary Answerability | 1 | No (New) |
| Internal Contradiction between Reasoning and Score | 1 | No (New) |
| Scale Calibration | 1 | No (New) |
| Scale Boundary Error | 1 | No (New) |
| Scale Boundary Misunderstanding | 1 | No (New) |
| Faulty Meta-Reasoning | 1 | No (New) |
| Score Mismatch / Scale Confusion | 1 | No (New) |
| Formatting issue | 1 | No (New) |
| Output Contradiction | 1 | No (New) |
| Misinterpreting Negative Answerability | 1 | No (New) |
| Assumption of User Intent | 1 | No (New) |
| Internal Consistency Error | 1 | No (New) |
| Confused Relevance with Factual Correctness | 1 | No (New) |
| Reasoning-Verdict Mismatch | 1 | No (New) |
| Misunderstood Scoring Scale | 1 | No (New) |
| Confused Absence of Information with Valid Answer | 1 | No (New) |
| Task Misunderstanding | 1 | No (New) |
| Equated Negative Answer with Relevance | 1 | No (New) |
| Misunderstood Relevance Criteria | 1 | No (New) |
| Negative Evidence Fallacy | 1 | No (New) |
| Factually Inaccurate Dismissal | 1 | No (New) |
| Contradictory Score Output | 1 | No (New) |
| Score Mapping Mismatch | 1 | No (New) |
| Confusing absence of information with an answer | 1 | No (New) |
| Flawed Negative-Answer Logic | 1 | No (New) |
| Negative Answer Fallacy | 1 | No (New) |
| Score Calibration Discrepancy | 1 | No (New) |
| Hallucinated Task and Score Inconsistency | 1 | No (New) |
| Scoring Scale Error | 1 | No (New) |
| Score and Reasoning Mismatch | 1 | No (New) |
| Rubric Scale Misinterpretation | 1 | No (New) |
| Conflating Relevance with Sufficiency | 1 | No (New) |
| Ignored Topical Overlap | 1 | No (New) |
| Output Contradicts Reasoning | 1 | No (New) |
| Miscalibration of Grading Scale | 1 | No (New) |
| Perceived Ambiguity | 1 | No (New) |
| Score Calibration / Scale Mapping Error | 1 | No (New) |
| Miscalibration | 1 | No (New) |
| Scale miscalibration | 1 | No (New) |
| Scale Range Violation | 1 | No (New) |
| Misidentified Query | 1 | No (New) |
| Score/Reasoning Contradiction | 1 | No (New) |
| Mishandled Identifier Query | 1 | No (New) |
| Conflating Verifiability with Document Relevance | 1 | No (New) |
| Unrecognized Query Identifier | 1 | No (New) |
| Score-reasoning misalignment | 1 | No (New) |
| Mishandling Malformed/ID Query | 1 | No (New) |
| Failure to Handle Query Artifact | 1 | No (New) |
| Failure to Recognize ID / Entity Code | 1 | No (New) |
| Failure to Handle Malformed Query | 1 | No (New) |
| Overthinking Evaluation Criteria | 1 | No (New) |
| Overthinking / Meta-reasoning Trap | 1 | No (New) |
| Malformed Query Misinterpretation | 1 | No (New) |
| Misinterpreted Task Objective | 1 | No (New) |
| Failed Entity/Identifier Resolution | 1 | No (New) |
| Failure to Handle Query ID / Artifact | 1 | No (New) |
| Failed ID / Entity Mapping | 1 | No (New) |
| Failure to Handle Opaque Query | 1 | No (New) |
| Mishandling of Identifier Query | 1 | No (New) |
| Unrecognized Identifier Mapping | 1 | No (New) |
| Hallucinated match | 1 | No (New) |
| Failed to Recognize Entity Identifier | 1 | No (New) |
| Unrecognized Database Identifier | 1 | No (New) |
| Equated Absence of Information with Relevance | 1 | No (New) |
| Failure to Handle Opaque Query ID | 1 | No (New) |
| Unresolved Query ID | 1 | No (New) |
| Rubric Mapping Error | 1 | No (New) |
| Overthinking Task Meta-Structure | 1 | No (New) |
| Ignored Graded Relevance Scale | 1 | No (New) |
| Evaluated query quality instead of document relevance | 1 | No (New) |
| Conflating Factual Inaccuracy with Irrelevance | 1 | No (New) |
| Rubric Misapplication | 1 | No (New) |
| Flawed Verification Logic | 1 | No (New) |
| Misinterpreting Negative Verification as Relevance | 1 | No (New) |
| Over-scoring / Scale Miscalibration | 1 | No (New) |
| Overthinking and Output Inconsistency | 1 | No (New) |
| Score Mapping Discrepancy | 1 | No (New) |
| Evaluation Criterion Mismatch | 1 | No (New) |
| Contradictory Logic | 1 | No (New) |
| Conflating Negative Answer with Document Relevance | 1 | No (New) |
| Missed Relevant Information | 1 | No (New) |
| Evaluated Query Quality Instead of Relevance | 1 | No (New) |
| Fallacious Answerability Logic | 1 | No (New) |
| Scale Misunderstanding | 1 | No (New) |
| Meta-reasoning Confusion | 1 | No (New) |
| Confusing Topical Relevance with Answerability | 1 | No (New) |
| Score Calibration Failure | 1 | No (New) |
| External Knowledge Reliance | 1 | No (New) |
| Scale Floor Violation | 1 | No (New) |
| Score Inconsistency / Mapping Failure | 1 | No (New) |
| Score Mismatch / Output Inconsistency | 1 | No (New) |
| Reasoning-to-Score Contradiction | 1 | No (New) |
| Failed to Recognize ID Lookup | 1 | No (New) |
| Failure to Recognize Identifier Lookup | 1 | No (New) |
| Failure to Resolve Numeric/ID Query | 1 | No (New) |
| Failure to Handle Unexpanded Query ID | 1 | No (New) |
| Defaulted to Non-Zero Relevance | 1 | No (New) |
| Treating absence of information as relevance | 1 | No (New) |
| Failure to Resolve Query ID Artifact | 1 | No (New) |
| Failure on Query Artifact | 1 | No (New) |
| Ignored Identifier Lookup Context | 1 | No (New) |
| False Positive on Non-Semantic Query | 1 | No (New) |
| Failed Numerical Association | 1 | No (New) |
| Score Inconsistency / Scale Confusion | 1 | No (New) |
| Scoring Calibration Error | 1 | No (New) |
| Flawed Task Interpretation | 1 | No (New) |
| Failure to Resolve Domain-Specific Identifier | 1 | No (New) |
| Reasoning-Verdict Inconsistency | 1 | No (New) |
| Hallucinated Document Content | 1 | No (New) |
| Score Conversion Error | 1 | No (New) |
| Rating Scale Miscalibration | 1 | No (New) |
| Scale Boundary Violation | 1 | No (New) |
| Treated Absence of Information as an Answer | 1 | No (New) |
| Factual Misreading of Document | 1 | No (New) |
| Failure to Resolve Pronoun Ambiguity | 1 | No (New) |
| Equating Negative Answer with Relevance | 1 | No (New) |
| Binary Relevance Evaluation | 1 | No (New) |
| Overthinking / Meta-Reasoning Fallacy | 1 | No (New) |
| Reasoning-to-Score Inconsistency | 1 | No (New) |
| Incomplete Generation / Formatting Issue | 1 | No (New) |
| Evaluated Query Quality Instead of Document Relevance | 1 | No (New) |
| Task Reinterpretation | 1 | No (New) |
| Logic Inversion | 1 | No (New) |
| Flawed Relevance Logic | 1 | No (New) |
| Ignored Query | 1 | No (New) |
| Grading Criteria Confusion | 1 | No (New) |
| Failed to handle numerical identifier | 1 | No (New) |
| Identifier Resolution Failure | 1 | No (New) |
| Literal Matching on Query ID Artifact | 1 | No (New) |
| Failure to resolve numeric identifier | 1 | No (New) |
| Unresolved Query ID / Dataset Artifact | 1 | No (New) |
| Unrecognized Domain-Specific Identifier | 1 | No (New) |
| Failure in Entity Resolution | 1 | No (New) |
| Failure on Identifier-based Query | 1 | No (New) |
| Failure to Recognize Query Artifact | 1 | No (New) |
| Hallucinated Query / Prompt Contamination | 1 | No (New) |
| Failure to Recognize Identifier Context | 1 | No (New) |
| Failure to handle opaque identifier | 1 | No (New) |
| Failure to recognize identifier query | 1 | No (New) |
| Unrecognized Document Identifier | 1 | No (New) |
| Failure to Recognize ID/Entity Lookup | 1 | No (New) |
| Failure to Resolve Benchmark Query ID | 1 | No (New) |
| Failed to Resolve Entity Identifier | 1 | No (New) |
| False negative on identifier query | 1 | No (New) |
| Failure to recognize ID/code query | 1 | No (New) |
| Failed Entity Linking | 1 | No (New) |
| Failure to Recognize ID-based Match | 1 | No (New) |
| Failure to Map Query ID / Dataset Artifact | 1 | No (New) |
| Dataset Artifact / Query ID Failure | 1 | No (New) |
| Failure to Map Query Identifier | 1 | No (New) |
| Failure to recognize opaque identifier | 1 | No (New) |
| Misunderstood Task Framing | 1 | No (New) |
| Strict Lexical Matching on Opaque Query | 1 | No (New) |
| Ignored Document ID/Lookup Context | 1 | No (New) |
| Failure to recognize query identifier | 1 | No (New) |
| Over-crediting Absence of Evidence | 1 | No (New) |
| Failure to Recognize Query ID | 1 | No (New) |
| Failure to handle query ID artifact | 1 | No (New) |
| Query ID Misinterpretation | 1 | No (New) |
| Literal Query Matching on Query ID | 1 | No (New) |
| Failure to recognize document ID query | 1 | No (New) |
| Conflating negative answer with irrelevance | 1 | No (New) |
| Lexical mismatch on query identifier | 1 | No (New) |
| Unresolved Query Identifier Failure | 1 | No (New) |
| Failure to resolve entity code | 1 | No (New) |
| Failure to Handle Non-Semantic/ID Query | 1 | No (New) |
| Failure to Resolve Identifier Query | 1 | No (New) |
| Failed Identifier Mapping | 1 | No (New) |
| Failure to Recognize Domain-Specific Identifier | 1 | No (New) |
| Failure to Recognize Domain Identifier | 1 | No (New) |
| Failure to Handle ID Query | 1 | No (New) |
| Failed to Resolve Numeric Identifier | 1 | No (New) |
| Failure to Resolve Opaque Query ID | 1 | No (New) |
| Query ID Resolution Failure | 1 | No (New) |
| Overthinking Meta-Answerability | 1 | No (New) |
| Failed to resolve query ID | 1 | No (New) |
| Failure to Recognize Query ID Artifact | 1 | No (New) |
| Failure to recognize benchmark query ID | 1 | No (New) |
| Score Misalignment | 1 | No (New) |
| Flawed Meta-reasoning | 1 | No (New) |
| Misinterpreting Task Objective | 1 | No (New) |
| Misunderstood Identifier Query | 1 | No (New) |
| Failed to handle identifier query | 1 | No (New) |
| Failure to resolve numeric query identifier | 1 | No (New) |
| Query artifact misinterpretation | 1 | No (New) |

## Breakdown by Model Pair

### gemini-2.5-flash vs gemini-3.5-flash
| Category | Count |
|---|---|
| Overly Strict Relevance Threshold | 588 |
| Overly Strict Interpretation | 148 |
| Score-Reasoning Inconsistency | 127 |
| Hallucinated Requirement | 71 |
| Missing Reasoning | 56 |
| Ignored Nuance | 30 |
| Score-Reasoning Discrepancy | 24 |
| Hallucinated Query | 13 |
| Over-weighted specific aspect | 13 |
| Score-Reasoning Mismatch | 9 |
| Superficial Keyword Matching | 6 |
| Score Inconsistency | 6 |
| Internal Inconsistency | 6 |
| Reasoning-Output Inconsistency | 5 |
| Internal Contradiction | 5 |
| Meta-Reasoning Fallacy | 4 |
| Flawed Meta-Reasoning | 4 |
| Reasoning-Output Disconnect | 4 |
| Task Misinterpretation | 4 |
| Rubric Misinterpretation | 3 |
| Over-weighted keyword match | 3 |
| Meta-Reasoning Confusion | 2 |
| Score-reasoning contradiction | 2 |
| Score Contradiction | 2 |
| Rubric Miscalibration | 2 |
| Scale Misalignment | 2 |
| Reasoning-Score Inconsistency | 2 |
| Scoring Inconsistency | 2 |
| Scale Mismatch | 2 |
| Scoring Scale Confusion | 2 |
| Treated Graded Scale as Binary | 1 |
| Flawed meta-reasoning | 1 |
| Scoring Scale Misalignment | 1 |
| Conflated Answerability with Relevance | 1 |
| Inverted Answerability Logic | 1 |
| Misapplied Scoring Rubric | 1 |
| Factual error regarding document content | 1 |
| Penalized Query Quality | 1 |
| Reasoning-Output Mismatch | 1 |
| Score mismatch with reasoning | 1 |
| Rating Scale Confusion | 1 |
| Treated Graded Relevance as Binary | 1 |
| Equating Relevance with Answerability | 1 |
| Misapplication of Rating Scale | 1 |
| Score Disconnect | 1 |
| Reasoning-Score Contradiction | 1 |
| Over-weighted topical overlap | 1 |
| Score Mapping Inconsistency | 1 |
| Treated Relevance as Binary Answerability | 1 |
| Scale Calibration Error | 1 |
| Scale Violation | 1 |
| Score Calibration | 1 |
| Internal Contradiction between Reasoning and Score | 1 |
| Scale Calibration | 1 |
| Score Mismatch | 1 |
| Scale Boundary Error | 1 |
| Score calibration error | 1 |
| Over-crediting tangential relevance | 1 |
| Scale Boundary Misunderstanding | 1 |
| Faulty Meta-Reasoning | 1 |
| Score Mismatch / Scale Confusion | 1 |
| Formatting issue | 1 |
| Score/Reasoning Inconsistency | 1 |
| Output Contradiction | 1 |
| Misinterpreting Negative Answerability | 1 |
| Flawed Task Logic | 1 |
| Assumption of User Intent | 1 |
| Internal Consistency Error | 1 |
| Score Discrepancy | 1 |
| Confused Relevance with Factual Correctness | 1 |
| Score Mapping Error | 1 |
| Reasoning-Output Discrepancy | 1 |
| Reasoning-Output Contradiction | 1 |

### gemini-2.5-flash vs gemini-3.6-flash
| Category | Count |
|---|---|
| Overly Strict Relevance Threshold | 506 |
| Score-Reasoning Inconsistency | 193 |
| Overly Strict Interpretation | 99 |
| Hallucinated Requirement | 91 |
| Missing Reasoning | 90 |
| Ignored Nuance | 24 |
| Score-Reasoning Discrepancy | 24 |
| Score-Reasoning Mismatch | 23 |
| Over-weighted specific aspect | 11 |
| Reasoning-Output Inconsistency | 8 |
| Internal Contradiction | 8 |
| Flawed Meta-Reasoning | 7 |
| Reasoning-Score Inconsistency | 6 |
| Over-crediting tangential relevance | 6 |
| Hallucinated Query | 6 |
| Score Inconsistency | 5 |
| Internal Inconsistency | 5 |
| Reasoning-Output Mismatch | 4 |
| Task Misinterpretation | 4 |
| Reasoning-Score Discrepancy | 3 |
| Over-weighted keyword match | 3 |
| Reasoning-Output Contradiction | 3 |
| Reasoning-Output Disconnect | 3 |
| Conflating Absence with an Answer | 3 |
| Score Mismatch | 3 |
| Score/Reasoning Discrepancy | 2 |
| Overthinking Negative Answerability | 2 |
| Internal Reasoning Inconsistency | 2 |
| Conclusion-Score Mismatch | 2 |
| Score Miscalibration | 2 |
| Internal Contradiction / Scale Confusion | 2 |
| Reasoning-Score Contradiction | 2 |
| Convoluted Meta-Reasoning | 2 |
| Score Calibration | 2 |
| Scoring Scale Confusion | 2 |
| Scale Confusion | 2 |
| Scale Misalignment | 2 |
| Reasoning-Output Discrepancy | 2 |
| Score Calibration Inconsistency | 2 |
| Meta-Reasoning Fallacy | 2 |
| Scale Range Mismatch | 2 |
| Meta-reasoning Fallacy | 2 |
| Scale Non-Compliance | 2 |
| Score Mapping Inconsistency | 2 |
| Reasoning-Verdict Mismatch | 1 |
| Superficial Keyword Matching | 1 |
| Misunderstood Scoring Scale | 1 |
| Confused Absence of Information with Valid Answer | 1 |
| Task Misunderstanding | 1 |
| Equated Negative Answer with Relevance | 1 |
| Flawed Task Logic | 1 |
| Misunderstood Relevance Criteria | 1 |
| Negative Evidence Fallacy | 1 |
| Reasoning-Score Disconnect | 1 |
| Factually Inaccurate Dismissal | 1 |
| Score Discrepancy / Scale Confusion | 1 |
| Misapplied Evaluation Criteria | 1 |
| Contradictory Score Output | 1 |
| Score Mapping Mismatch | 1 |
| Score/Reasoning Inconsistency | 1 |
| Confusing absence of information with an answer | 1 |
| Rubric Miscalibration | 1 |
| Flawed Negative-Answer Logic | 1 |
| Negative Answer Fallacy | 1 |
| Score Calibration Discrepancy | 1 |
| Equating Relevance with Answerability | 1 |
| Conflating Absence of Information with an Answer | 1 |
| Hallucinated Task and Score Inconsistency | 1 |
| Scale Calibration Error | 1 |
| Meta-Reasoning Confusion | 1 |
| Scoring Scale Error | 1 |
| Scale Mapping Error | 1 |
| Score and Reasoning Mismatch | 1 |
| Rubric Scale Misinterpretation | 1 |
| Scale Mismatch | 1 |
| Conflating Relevance with Sufficiency | 1 |
| Ignored Topical Overlap | 1 |
| Score mismatch with reasoning | 1 |
| Output Contradicts Reasoning | 1 |
| Miscalibration of Grading Scale | 1 |
| Rating Scale Confusion | 1 |
| Rubric Misinterpretation | 1 |
| Score Disconnect | 1 |
| Perceived Ambiguity | 1 |
| Score Calibration / Scale Mapping Error | 1 |
| Miscalibration | 1 |
| Scale miscalibration | 1 |
| Scale Range Violation | 1 |
| Misidentified Query | 1 |
| Score/Reasoning Contradiction | 1 |

### gemini-3.5-flash vs gemini-3.8-flash
| Category | Count |
|---|---|
| Over-crediting tangential relevance | 197 |
| Score-Reasoning Inconsistency | 33 |
| Superficial Keyword Matching | 27 |
| Missing Reasoning | 20 |
| Hallucinated Requirement | 18 |
| Overly Strict Interpretation | 12 |
| Hallucinated Query | 8 |
| Overly Strict Relevance Threshold | 6 |
| Score-Reasoning Discrepancy | 6 |
| Ignored Nuance | 4 |
| Score-Reasoning Mismatch | 4 |
| Over-weighted keyword match | 3 |
| Reasoning-Output Discrepancy | 2 |
| Failed Identifier Resolution | 2 |
| Reasoning-Output Disconnect | 2 |
| Over-weighted topical overlap | 2 |
| Mishandled Identifier Query | 1 |
| Task Misinterpretation | 1 |
| Conflating Verifiability with Document Relevance | 1 |
| Reasoning-Score Inconsistency | 1 |
| Score Inconsistency | 1 |
| Unrecognized Query Identifier | 1 |
| Score-reasoning misalignment | 1 |
| Mishandling Malformed/ID Query | 1 |
| Failure to Handle Identifier Query | 1 |
| Literal Interpretation of Query ID | 1 |
| Scoring Scale Confusion | 1 |
| Meta-reasoning Fallacy | 1 |
| Failure to handle identifier query | 1 |
| Failure to Recognize Query Identifier | 1 |
| Failure to Handle Query Artifact | 1 |
| Failed Identifier Recognition | 1 |
| Identifier Mapping Failure | 1 |
| Score Mapping Inconsistency | 1 |
| Failure to Recognize ID / Entity Code | 1 |
| Internal Contradiction | 1 |
| Unrecognized Numeric Identifier | 1 |
| Failure to Resolve Query ID | 1 |
| Failure to Handle Malformed Query | 1 |
| Overthinking Evaluation Criteria | 1 |
| Overthinking / Meta-reasoning Trap | 1 |
| Malformed Query Misinterpretation | 1 |
| Misinterpreted Task Objective | 1 |
| Over-weighted specific aspect | 1 |

### gemini-3.5-flash vs gemini-3.7-flash
| Category | Count |
|---|---|
| Over-crediting tangential relevance | 189 |
| Superficial Keyword Matching | 26 |
| Score-Reasoning Inconsistency | 24 |
| Hallucinated Requirement | 20 |
| Missing Reasoning | 8 |
| Overly Strict Relevance Threshold | 8 |
| Ignored Nuance | 6 |
| Overly Strict Interpretation | 5 |
| Score-Reasoning Discrepancy | 4 |
| Hallucinated Query | 4 |
| Over-weighted keyword match | 3 |
| Score-Reasoning Mismatch | 3 |
| Over-weighted topical overlap | 3 |
| Failure to Recognize Identifier Query | 2 |
| Over-weighted specific aspect | 2 |
| Scoring Scale Confusion | 2 |
| Spurious Match / Hallucinated Relevance | 2 |
| Score Discrepancy | 1 |
| Failed Entity/Identifier Resolution | 1 |
| Failure to Handle Query ID / Artifact | 1 |
| Failed ID / Entity Mapping | 1 |
| Failure to Handle Opaque Query | 1 |
| Mishandling of Identifier Query | 1 |
| Unrecognized Identifier Mapping | 1 |
| Hallucinated match | 1 |
| Failed to Recognize Entity Identifier | 1 |
| Meta-Reasoning Fallacy | 1 |
| Failed Identifier Resolution | 1 |
| Failed to Recognize Document Identifier | 1 |
| Failed to Recognize Identifier Query | 1 |
| Dataset Artifact Misinterpretation | 1 |
| Unrecognized Database Identifier | 1 |
| Equated Absence of Information with Relevance | 1 |
| Failure to Handle Opaque Query ID | 1 |
| Failure to Handle Query ID | 1 |
| Reasoning-Output Inconsistency | 1 |
| Failure to Resolve Query ID | 1 |
| Score Inconsistency | 1 |
| Reasoning-Score Inconsistency | 1 |
| Unresolved Query ID | 1 |
| Failed Identifier Recognition | 1 |

### gemini-2.5-flash vs gemini-3.8-flash
| Category | Count |
|---|---|
| Overly Strict Relevance Threshold | 540 |
| Overly Strict Interpretation | 139 |
| Score-Reasoning Inconsistency | 119 |
| Hallucinated Requirement | 91 |
| Missing Reasoning | 63 |
| Ignored Nuance | 30 |
| Over-weighted specific aspect | 19 |
| Hallucinated Query | 18 |
| Score-Reasoning Mismatch | 13 |
| Score-Reasoning Discrepancy | 7 |
| Score Inconsistency | 6 |
| Scale Calibration Error | 6 |
| Score Mismatch | 5 |
| Flawed Meta-Reasoning | 5 |
| Task Misinterpretation | 5 |
| Over-weighted keyword match | 4 |
| Reasoning-Output Inconsistency | 4 |
| Internal Inconsistency | 3 |
| Score-Reasoning Disconnect | 3 |
| Internal Contradiction | 3 |
| Over-crediting tangential relevance | 2 |
| Superficial Keyword Matching | 2 |
| Conclusion-Score Mismatch | 2 |
| Rating Scale Violation | 2 |
| Score Miscalibration | 2 |
| Reasoning-Score Discrepancy | 2 |
| Scoring Scale Confusion | 2 |
| Score Calibration | 2 |
| Reasoning-Score Inconsistency | 2 |
| Reasoning-Output Disconnect | 2 |
| Rubric Mapping Error | 1 |
| Overthinking Task Meta-Structure | 1 |
| Ignored Graded Relevance Scale | 1 |
| Evaluated query quality instead of document relevance | 1 |
| Score/Reasoning Inconsistency | 1 |
| Meta-Reasoning Fallacy | 1 |
| Reasoning-Score Disconnect | 1 |
| Misapplied Evaluation Criteria | 1 |
| Task Confusion | 1 |
| Conflating Factual Inaccuracy with Irrelevance | 1 |
| Score calibration error | 1 |
| Rubric Misapplication | 1 |
| Overthinking Meta-Question | 1 |
| Flawed Verification Logic | 1 |
| Rating Scale Confusion | 1 |
| Misinterpreting Negative Verification as Relevance | 1 |
| Score Mapping Error | 1 |
| Miscalibrated Scoring | 1 |
| Over-scoring / Scale Miscalibration | 1 |
| Overthinking and Output Inconsistency | 1 |
| Reasoning-Score Contradiction | 1 |
| Score Mapping Discrepancy | 1 |
| Evaluation Criterion Mismatch | 1 |
| Internal Contradiction / Scale Confusion | 1 |
| Contradictory Logic | 1 |
| Conflating Negative Answer with Document Relevance | 1 |
| Missed Relevant Information | 1 |
| Evaluated Query Quality Instead of Relevance | 1 |
| Score-reasoning inconsistency | 1 |
| Treated Graded Scale as Binary | 1 |
| Fallacious Answerability Logic | 1 |
| Scale Misunderstanding | 1 |
| Meta-reasoning Confusion | 1 |
| Scale Violation | 1 |
| Confusing Topical Relevance with Answerability | 1 |
| Score Calibration Failure | 1 |
| External Knowledge Reliance | 1 |
| Score Mapping Inconsistency | 1 |
| Score Disconnect | 1 |
| Score Discrepancy | 1 |
| Scale Floor Violation | 1 |
| Scoring Inconsistency | 1 |
| Score Inconsistency / Mapping Failure | 1 |
| Score Contradiction | 1 |

### gemini-3.5-flash vs gemini-3.6-flash
| Category | Count |
|---|---|
| Over-crediting tangential relevance | 308 |
| Score-Reasoning Inconsistency | 75 |
| Missing Reasoning | 34 |
| Hallucinated Requirement | 22 |
| Superficial Keyword Matching | 20 |
| Score-Reasoning Discrepancy | 15 |
| Score-Reasoning Mismatch | 14 |
| Overly Strict Relevance Threshold | 8 |
| Overly Strict Interpretation | 6 |
| Over-weighted topical overlap | 5 |
| Score Inconsistency | 5 |
| Over-weighted keyword match | 5 |
| Reasoning-Output Disconnect | 4 |
| Flawed Meta-Reasoning | 4 |
| Reasoning-Output Discrepancy | 3 |
| Reasoning-Output Inconsistency | 3 |
| Ignored Nuance | 3 |
| Hallucinated Query | 3 |
| Overthinking Meta-Question | 2 |
| Reasoning-Output Mismatch | 2 |
| Literal Interpretation of Query ID | 1 |
| Conflating Absence of Information with an Answer | 1 |
| Failure to Recognize Identifier | 1 |
| Score Mismatch / Output Inconsistency | 1 |
| Score/Reasoning Inconsistency | 1 |
| Reasoning-to-Score Contradiction | 1 |
| Failure to handle identifier query | 1 |
| Failed to Recognize ID Lookup | 1 |
| Failure to Recognize Identifier Lookup | 1 |
| Failure to Resolve Numeric/ID Query | 1 |
| Score Miscalibration | 1 |
| Failure to Handle Unexpanded Query ID | 1 |
| Scoring Scale Confusion | 1 |
| Defaulted to Non-Zero Relevance | 1 |
| Treating absence of information as relevance | 1 |
| Identifier Mapping Failure | 1 |
| Failure to Resolve Query ID Artifact | 1 |
| Internal Inconsistency | 1 |
| Failure on Query Artifact | 1 |
| Ignored Identifier Lookup Context | 1 |
| Rubric Miscalibration | 1 |
| False Positive on Non-Semantic Query | 1 |
| Failed Numerical Association | 1 |
| Reasoning-Score Inconsistency | 1 |
| Score-reasoning inconsistency | 1 |
| Score Inconsistency / Scale Confusion | 1 |
| Reasoning-Output Contradiction | 1 |
| Scoring Calibration Error | 1 |
| Flawed Task Interpretation | 1 |
| Failure to Resolve Domain-Specific Identifier | 1 |
| Reasoning-Verdict Inconsistency | 1 |
| Failed Identifier Resolution | 1 |
| Failure to Recognize Identifier Query | 1 |
| Over-weighted specific aspect | 1 |

### gemini-2.5-flash vs gemini-3.7-flash
| Category | Count |
|---|---|
| Overly Strict Relevance Threshold | 564 |
| Overly Strict Interpretation | 113 |
| Score-Reasoning Inconsistency | 112 |
| Hallucinated Requirement | 88 |
| Missing Reasoning | 55 |
| Ignored Nuance | 21 |
| Over-weighted specific aspect | 18 |
| Hallucinated Query | 15 |
| Score-Reasoning Discrepancy | 11 |
| Score Inconsistency | 10 |
| Score-Reasoning Mismatch | 6 |
| Score Mismatch | 5 |
| Scoring Scale Confusion | 5 |
| Scale Calibration Error | 4 |
| Rubric Miscalibration | 3 |
| Over-crediting tangential relevance | 3 |
| Superficial Keyword Matching | 3 |
| Score Discrepancy | 2 |
| Task Confusion | 2 |
| Internal Inconsistency | 2 |
| Internal Contradiction | 2 |
| Score/Reasoning Inconsistency | 2 |
| Reasoning-Score Inconsistency | 2 |
| Reasoning-Output Discrepancy | 2 |
| Scale Misalignment | 2 |
| Hallucinated Document Content | 1 |
| Score Conversion Error | 1 |
| Rating Scale Miscalibration | 1 |
| Task Misinterpretation | 1 |
| Scale Boundary Violation | 1 |
| Treated Absence of Information as an Answer | 1 |
| Over-weighted keyword match | 1 |
| Misapplied Evaluation Criteria | 1 |
| Factual Misreading of Document | 1 |
| Scale Confusion | 1 |
| Scoring Inconsistency | 1 |
| Reasoning-Output Inconsistency | 1 |
| Scale Range Mismatch | 1 |
| Failure to Resolve Pronoun Ambiguity | 1 |
| Equating Negative Answer with Relevance | 1 |
| Binary Relevance Evaluation | 1 |
| Overthinking / Meta-Reasoning Fallacy | 1 |
| Score Discrepancy / Scale Confusion | 1 |
| Score-reasoning contradiction | 1 |
| Rating Scale Violation | 1 |
| Reasoning-to-Score Inconsistency | 1 |
| Miscalibrated Scoring | 1 |
| Incomplete Generation / Formatting Issue | 1 |
| Evaluated Query Quality Instead of Document Relevance | 1 |
| Task Reinterpretation | 1 |
| Score Mapping Error | 1 |
| Scale Mapping Error | 1 |
| Reasoning-Output Contradiction | 1 |
| Logic Inversion | 1 |
| Flawed Relevance Logic | 1 |
| Ignored Query | 1 |
| Grading Criteria Confusion | 1 |
| Score Calibration Inconsistency | 1 |

### gemini-3.6-flash vs gemini-3.8-flash
| Category | Count |
|---|---|
| Over-crediting tangential relevance | 87 |
| Superficial Keyword Matching | 47 |
| Score-Reasoning Inconsistency | 29 |
| Overly Strict Relevance Threshold | 24 |
| Overly Strict Interpretation | 20 |
| Hallucinated Requirement | 19 |
| Ignored Nuance | 17 |
| Over-weighted keyword match | 11 |
| Hallucinated Query | 10 |
| Missing Reasoning | 9 |
| Score-Reasoning Discrepancy | 4 |
| Score-Reasoning Mismatch | 4 |
| Flawed Meta-Reasoning | 3 |
| Failure to Recognize Identifier | 3 |
| Over-weighted specific aspect | 3 |
| Score/Reasoning Inconsistency | 2 |
| Identifier Mapping Failure | 2 |
| Dataset Artifact Misinterpretation | 2 |
| Failed Identifier Resolution | 2 |
| Failure to Resolve Identifier | 2 |
| Score Inconsistency | 2 |
| Literal Interpretation of Query ID | 2 |
| Failure to Resolve Query ID | 2 |
| Failure to Resolve Numeric Identifier | 2 |
| Failure to resolve query ID | 2 |
| Failure to Recognize Identifier Query | 2 |
| Task Misinterpretation | 1 |
| Failed to Recognize Document Identifier | 1 |
| Failed to handle numerical identifier | 1 |
| Identifier Resolution Failure | 1 |
| Failure to Recognize Document Identifier | 1 |
| Convoluted Meta-Reasoning | 1 |
| Failure to resolve query identifier | 1 |
| Entity Resolution Failure | 1 |
| Literal Matching on Query ID Artifact | 1 |
| Literal Interpretation of Query Identifier | 1 |
| Failure to resolve numeric identifier | 1 |
| Meta-Reasoning Fallacy | 1 |
| Unresolved Query ID / Dataset Artifact | 1 |
| Failure to Recognize Query Identifier | 1 |
| Unrecognized Domain-Specific Identifier | 1 |
| Failure in Entity Resolution | 1 |
| Failure to Handle Identifier Query | 1 |
| Failure on Identifier-based Query | 1 |
| Score-Reasoning Disconnect | 1 |
| Failure to Recognize Query Artifact | 1 |
| Failure to Handle Query ID | 1 |
| Hallucinated Query / Prompt Contamination | 1 |
| Failure to Recognize Identifier Context | 1 |
| Failure to handle opaque identifier | 1 |
| Failure to recognize identifier query | 1 |
| Unrecognized Document Identifier | 1 |
| Failure to Recognize ID/Entity Lookup | 1 |
| Failure to Resolve Benchmark Query ID | 1 |
| Reasoning-Output Mismatch | 1 |
| Failed to Resolve Entity Identifier | 1 |
| Unrecognized Identifier Query | 1 |
| Score Mapping Inconsistency | 1 |
| Failure to Handle Query ID Artifact | 1 |
| False negative on identifier query | 1 |
| Failure to recognize ID/code query | 1 |
| Failed Entity Linking | 1 |
| Failure to Recognize ID-based Match | 1 |
| Failure to Map Query ID / Dataset Artifact | 1 |
| Dataset Artifact / Query ID Failure | 1 |
| Failure to Map Query Identifier | 1 |
| Failure to recognize opaque identifier | 1 |
| Misunderstood Task Framing | 1 |
| Strict Lexical Matching on Opaque Query | 1 |

### gemini-3.6-flash vs gemini-3.7-flash
| Category | Count |
|---|---|
| Over-crediting tangential relevance | 96 |
| Superficial Keyword Matching | 56 |
| Overly Strict Relevance Threshold | 26 |
| Hallucinated Requirement | 23 |
| Score-Reasoning Inconsistency | 17 |
| Overly Strict Interpretation | 15 |
| Over-weighted keyword match | 14 |
| Hallucinated Query | 9 |
| Ignored Nuance | 9 |
| Missing Reasoning | 6 |
| Score Inconsistency | 5 |
| Failure to Recognize Identifier | 4 |
| Over-weighted topical overlap | 3 |
| Literal Interpretation of Query ID | 3 |
| Over-weighted specific aspect | 3 |
| Failure to resolve entity identifier | 3 |
| Failure to Resolve Query Identifier | 2 |
| Failure to Recognize Document Identifier | 2 |
| Identifier Mapping Failure | 2 |
| Failure to Recognize Identifier Query | 2 |
| Failed Identifier Recognition | 2 |
| Score-Reasoning Mismatch | 2 |
| Failed Entity Resolution | 2 |
| Failure to Resolve Query ID | 2 |
| Reasoning-Output Inconsistency | 1 |
| Score-Reasoning Discrepancy | 1 |
| Failure to Handle Query ID | 1 |
| Failure to resolve query identifier | 1 |
| Score Discrepancy | 1 |
| Ignored Document ID/Lookup Context | 1 |
| Failure to recognize query identifier | 1 |
| Reasoning-Score Disconnect | 1 |
| Over-crediting Absence of Evidence | 1 |
| Failure to Recognize Query ID | 1 |
| Failure to handle query ID artifact | 1 |
| Entity Resolution Failure | 1 |
| Query ID Misinterpretation | 1 |
| Literal Query Matching on Query ID | 1 |
| Failed to Recognize Identifier Query | 1 |
| Unrecognized Numeric Identifier | 1 |
| Failed to Recognize Document Identifier | 1 |
| Failure to recognize document ID query | 1 |
| Conflating negative answer with irrelevance | 1 |
| Lexical mismatch on query identifier | 1 |
| Unresolved Query Identifier Failure | 1 |
| Literal Interpretation of Query Identifier | 1 |
| Failure to resolve entity code | 1 |
| Failure to Handle Non-Semantic/ID Query | 1 |
| Failure to Resolve Identifier Query | 1 |
| Failed Identifier Resolution | 1 |
| Failed Identifier Mapping | 1 |
| Failure to Handle Identifier Query | 1 |
| Failure to Recognize Domain-Specific Identifier | 1 |
| Failure to Recognize Domain Identifier | 1 |
| Failure to Handle ID Query | 1 |
| Failed to Resolve Numeric Identifier | 1 |
| Failure to Resolve Opaque Query ID | 1 |
| Failure to resolve query ID | 1 |
| Failure to Handle Query ID Artifact | 1 |

### gemini-3.7-flash vs gemini-3.8-flash
| Category | Count |
|---|---|
| Over-crediting tangential relevance | 84 |
| Score-Reasoning Inconsistency | 32 |
| Missing Reasoning | 16 |
| Superficial Keyword Matching | 16 |
| Overly Strict Relevance Threshold | 14 |
| Hallucinated Requirement | 10 |
| Overly Strict Interpretation | 6 |
| Score-Reasoning Mismatch | 4 |
| Failure to Recognize Identifier Query | 4 |
| Failure to Resolve Query Identifier | 3 |
| Ignored Nuance | 3 |
| Score-Reasoning Discrepancy | 2 |
| Score Mapping Inconsistency | 2 |
| Hallucinated Query | 2 |
| Over-weighted keyword match | 2 |
| Query ID Resolution Failure | 1 |
| Reasoning-Output Inconsistency | 1 |
| Overthinking Meta-Answerability | 1 |
| Failed to resolve query ID | 1 |
| Failure to Recognize Query ID Artifact | 1 |
| Score Inconsistency | 1 |
| Failure to Handle Identifier Query | 1 |
| Failure to recognize benchmark query ID | 1 |
| Reasoning-Output Discrepancy | 1 |
| Score/Reasoning Inconsistency | 1 |
| Identifier Mapping Failure | 1 |
| Reasoning-Output Disconnect | 1 |
| Score Misalignment | 1 |
| Flawed Meta-reasoning | 1 |
| Misinterpreting Task Objective | 1 |
| Internal Inconsistency | 1 |
| Unrecognized Identifier Query | 1 |
| Misunderstood Identifier Query | 1 |
| Failed Identifier Recognition | 1 |
| Failed Identifier Resolution | 1 |
| Failure to resolve query ID | 1 |
| Over-weighted topical overlap | 1 |
| Failed Entity Resolution | 1 |
| Over-weighted specific aspect | 1 |
| Reasoning-Score Inconsistency | 1 |
| Failed to handle identifier query | 1 |
| Failure to resolve numeric query identifier | 1 |
| Query artifact misinterpretation | 1 |

## Raw Mapping Details

```json
{
  "Excessive strictness regarding specificity": "Overly Strict Interpretation",
  "Conflating Factual Inaccuracy with Irrelevance": "Conflating Factual Inaccuracy with Irrelevance",
  "Confused Relevance with Direct Answerability": "Overly Strict Interpretation",
  "Strict Answerability over Topical Relevance": "Overly Strict Interpretation",
  "Over-estimated Relevance": "Over-crediting tangential relevance",
  "Overly Harsh Scoring": "Overly Strict Relevance Threshold",
  "Binary Answerability Bias": "Overly Strict Relevance Threshold",
  "Over-penalized Partial Relevance": "Overly Strict Relevance Threshold",
  "Under-crediting partial relevance": "Overly Strict Relevance Threshold",
  "Identifier Mapping Failure": "Identifier Mapping Failure",
  "Failure to recognize partial/topical relevance": "Overly Strict Relevance Threshold",
  "Over-penalizing tangential relevance": "Overly Strict Relevance Threshold",
  "Scoring Scale Confusion": "Scoring Scale Confusion",
  "Over-weighting topical overlap": "Over-weighted topical overlap",
  "Misinterpreted Logical Disjunction": "Ignored Nuance",
  "Over-scrutinizing Ambiguity": "Overly Strict Interpretation",
  "Failure to Recognize Limited Relevance": "Overly Strict Relevance Threshold",
  "Over-penalizing Incomplete Information": "Hallucinated Requirement",
  "Over-weighted completeness over topical relevance": "Hallucinated Requirement",
  "Failure on Identifier Query": "Identifier Mapping Failure",
  "Demanding Excessive Depth": "Hallucinated Requirement",
  "Strict Lexical Matching Bias": "Over-weighted keyword match",
  "Overly Strict Completeness Requirement": "Hallucinated Requirement",
  "Over-penalized lack of exact terminology": "Over-weighted keyword match",
  "Over-demanding Completeness": "Hallucinated Requirement",
  "Superficial Match": "Superficial Keyword Matching",
  "Spurious Lexical Matching": "Superficial Keyword Matching",
  "False Positive on Irrelevant Content": "Over-crediting tangential relevance",
  "Ignored Nuance": "Ignored Nuance",
  "Failure to handle ID-based query": "Identifier Mapping Failure",
  "Literal Keyword Matching": "Superficial Keyword Matching",
  "Failure to recognize marginal relevance": "Overly Strict Relevance Threshold",
  "Dismissing Implicit Relevance": "Overly Strict Interpretation",
  "Rating scale mismatch": "Scoring Scale Confusion",
  "Over-strict threshold for marginal relevance": "Overly Strict Relevance Threshold",
  "Overly Punitive Scoring": "Overly Strict Relevance Threshold",
  "Score-Reasoning Misalignment": "Missing Reasoning",
  "Overly Strict Exact-Match Requirement": "Over-weighted keyword match",
  "Ignored Disjunctive Nuance": "Ignored Nuance",
  "Conflating Unanswerability with Irrelevance": "Overly Strict Interpretation",
  "Overly Strict Criteria": "Overly Strict Relevance Threshold",
  "Failure to Award Partial Relevance": "Overly Strict Relevance Threshold",
  "Score Calibration Error": "Scoring Scale Confusion",
  "Rewarding Referral or Negative Information": "Over-crediting tangential relevance",
  "Over-penalization of incomplete context": "Hallucinated Requirement",
  "Metric Confusion": "Scoring Scale Confusion",
  "Failure to Recognize Code/Identifier": "Identifier Mapping Failure",
  "Rigid Literalism": "Overly Strict Interpretation",
  "Failure to recognize minimal relevance": "Overly Strict Relevance Threshold",
  "Overly Strict Binary Judgment": "Overly Strict Relevance Threshold",
  "Confused Completeness with Relevance": "Overly Strict Interpretation",
  "Under-graded relevance": "Overly Strict Relevance Threshold",
  "Scale Non-Compliance": "Scale Non-Compliance",
  "Factual error regarding document content": "Factual error regarding document content",
  "Strict binary evaluation overlooking partial relevance": "Overly Strict Relevance Threshold",
  "Confusing Irrelevance with Answerability": "Overly Strict Interpretation",
  "Excessive strictness on explicit mentions": "Overly Strict Interpretation",
  "Over-penalized incomplete answer": "Overly Strict Interpretation",
  "Treating relevance as strict answerability": "Overly Strict Interpretation",
  "Overly strict criteria": "Overly Strict Interpretation",
  "Overthinking / Meta-Reasoning Fallacy": "Overthinking / Meta-Reasoning Fallacy",
  "Equating Unanswerability with Irrelevance": "Overly Strict Interpretation",
  "Over-penalizing missing specific details": "Over-weighted specific aspect",
  "Excessive Skepticism": "Overly Strict Interpretation",
  "Overly Strict Rejection of Incomplete Information": "Overly Strict Interpretation",
  "Failure to Recognize Graded/Partial Relevance": "Overly Strict Relevance Threshold",
  "Output Contradiction": "Output Contradiction",
  "Requirement of explicit mention": "Hallucinated Requirement",
  "Over-estimation of relevance": "Over-crediting tangential relevance",
  "Conflated Negative Answer with Unanswerability": "Ignored Nuance",
  "Demanded Explicit Definition": "Hallucinated Requirement",
  "Arbitrary Score Assignment": "Missing Reasoning",
  "Internal Contradiction": "Internal Contradiction",
  "Over-penalizing Lack of Lexical Overlap": "Superficial Keyword Matching",
  "Ignored Tangential Relevance": "Overly Strict Relevance Threshold",
  "Failure to Credit Topical Relevance": "Overly Strict Relevance Threshold",
  "Disregarded Partial Relevance": "Overly Strict Relevance Threshold",
  "Failure on Query Artifact": "Failure on Query Artifact",
  "Miscalibrated Rating Scale": "Overly Strict Relevance Threshold",
  "Hypercritical ambiguity penalty": "Overly Strict Interpretation",
  "Overly Strict Thresholding": "Overly Strict Relevance Threshold",
  "Strict Binary Thresholding": "Overly Strict Relevance Threshold",
  "Over-strict Relevance Threshold": "Overly Strict Relevance Threshold",
  "Disregarding Partial Relevance": "Overly Strict Relevance Threshold",
  "Over-penalized missing detail": "Over-weighted specific aspect",
  "Over-penalizing Temporal Relevance": "Ignored Nuance",
  "Overly Strict Matching Criterion": "Overly Strict Interpretation",
  "Misinterpretation of Question Intent": "Ignored Nuance",
  "Strict Answerability Requirement": "Hallucinated Requirement",
  "Score/Reasoning Contradiction": "Score/Reasoning Contradiction",
  "Conflating Partial Relevance with Non-Relevance": "Overly Strict Relevance Threshold",
  "Score Conversion Error": "Score Conversion Error",
  "Failed to Recognize Identifier": "Ignored Nuance",
  "All-or-Nothing Evaluation": "Overly Strict Relevance Threshold",
  "Over-reliance on exact keyword match": "Superficial Keyword Matching",
  "Ignoring Partial Relevance": "Overly Strict Relevance Threshold",
  "Demanding a complete answer": "Hallucinated Requirement",
  "Flawed Evaluation Logic": "Missing Reasoning",
  "Failure to connect related concepts": "Ignored Nuance",
  "Excessive Penalty for Incompleteness": "Overly Strict Interpretation",
  "Under-valued partial relevance": "Overly Strict Relevance Threshold",
  "Ignored partial relevance criteria": "Overly Strict Relevance Threshold",
  "Failure to identify complete irrelevance": "Over-crediting tangential relevance",
  "Conflating Absence of Information with an Answer": "Conflating Absence of Information with an Answer",
  "All-or-nothing grading": "Overly Strict Relevance Threshold",
  "Equating Non-Answerability with Irrelevance": "Overly Strict Relevance Threshold",
  "Conflating Graded Relevance with Direct Answerability": "Overly Strict Relevance Threshold",
  "Hallucinated topical link": "Over-weighted topical overlap",
  "Demanding Unwarranted Depth": "Hallucinated Requirement",
  "Failure to Handle Query ID Artifact": "Failure to Handle Query ID Artifact",
  "Dismissal of Partial Relevance": "Overly Strict Relevance Threshold",
  "Over-strict Binary Evaluation": "Overly Strict Relevance Threshold",
  "Strict keyword matching": "Over-weighted keyword match",
  "Over-penalizing Missing Specifics": "Over-weighted specific aspect",
  "Reasoning-Output Mismatch": "Reasoning-Output Mismatch",
  "Scale Floor Violation": "Scale Floor Violation",
  "Ignoring Topical Relevance": "Overly Strict Relevance Threshold",
  "Failure to Identify Domain Entity": "Ignored Nuance",
  "Conflating Topical Relevance with Answerability": "Overly Strict Relevance Threshold",
  "Conflating sufficiency with relevance": "Overly Strict Relevance Threshold",
  "Task Reinterpretation": "Task Reinterpretation",
  "Over-weighted missing terminology": "Over-weighted keyword match",
  "Demanded Excessive Elaboration": "Hallucinated Requirement",
  "Literal Matching on Query ID Artifact": "Literal Matching on Query ID Artifact",
  "Demanded Exact Keyword Match": "Over-weighted keyword match",
  "Misinterpreting Negative Answerability": "Misinterpreting Negative Answerability",
  "Over-penalizing marginal relevance": "Overly Strict Relevance Threshold",
  "Over-penalized lack of lexical match": "Over-weighted keyword match",
  "Hallucinated Ambiguity": "Hallucinated Requirement",
  "Over-weighted lexical mismatch": "Over-weighted keyword match",
  "Overestimating relevance": "Over-crediting tangential relevance",
  "Negative Evidence Fallacy": "Negative Evidence Fallacy",
  "Over-stringent Criteria": "Overly Strict Interpretation",
  "Dismissing partial relevance": "Overly Strict Relevance Threshold",
  "Excessive Penalty for Query Ambiguity": "Overly Strict Interpretation",
  "Over-penalization of Missing Information": "Overly Strict Relevance Threshold",
  "Conclusion-Score Mismatch": "Conclusion-Score Mismatch",
  "Overly Strict Evaluation of Marginal Relevance": "Overly Strict Relevance Threshold",
  "Threshold Calibration Error": "Overly Strict Relevance Threshold",
  "Spurious Relevance Detection": "Over-crediting tangential relevance",
  "Confusing Topical Relevance with Full Answerability": "Overly Strict Relevance Threshold",
  "Failed to handle identifier query": "Failed to handle identifier query",
  "Failure to Recognize Irrelevance": "Over-crediting tangential relevance",
  "Reasoning-Score Inconsistency": "Reasoning-Score Inconsistency",
  "Ignored Marginal Relevance": "Overly Strict Relevance Threshold",
  "Failure to credit marginal relevance": "Overly Strict Relevance Threshold",
  "Rubric Mapping Error": "Rubric Mapping Error",
  "Treated Graded Relevance as Binary Answerability": "Overly Strict Relevance Threshold",
  "Elevated Standard for Completeness": "Hallucinated Requirement",
  "Over-weighted Query Ambiguity": "Overly Strict Interpretation",
  "Ignored Scale Nuance": "Ignored Nuance",
  "Overthinking Task Requirements": "Hallucinated Requirement",
  "Failure to Recognize Query Artifact": "Failure to Recognize Query Artifact",
  "Failure to Recognize Query ID": "Failure to Recognize Query ID",
  "Failure to credit topical relevance": "Overly Strict Relevance Threshold",
  "Failure to Recognize Identifier Lookup": "Failure to Recognize Identifier Lookup",
  "Spurious Keyword Match": "Superficial Keyword Matching",
  "All-or-Nothing Scoring": "Overly Strict Relevance Threshold",
  "Over-penalized tangential relevance": "Overly Strict Relevance Threshold",
  "Over-strict evaluation": "Overly Strict Interpretation",
  "Reasoning-to-Score Discrepancy": "Missing Reasoning",
  "Hallucinated Query / Prompt Contamination": "Hallucinated Query / Prompt Contamination",
  "Spurious Relevance": "Over-crediting tangential relevance",
  "Failure to Handle Opaque Query ID": "Failure to Handle Opaque Query ID",
  "Unresolved Query ID / Dataset Artifact": "Unresolved Query ID / Dataset Artifact",
  "Failure to Recognize ID / Entity Code": "Failure to Recognize ID / Entity Code",
  "Overly Strict Requirement": "Hallucinated Requirement",
  "Dismissing Marginal Relevance": "Overly Strict Relevance Threshold",
  "Over-penalized Ambiguity": "Overly Strict Interpretation",
  "Overly Strict Inference Standard": "Overly Strict Interpretation",
  "Overestimated relevance": "Over-crediting tangential relevance",
  "Excessive Stringency": "Overly Strict Interpretation",
  "Strict matching": "Overly Strict Interpretation",
  "Treated Disjunctive Requirement as Conjunctive": "Overly Strict Interpretation",
  "Over-reliance on Explicit Mention": "Superficial Keyword Matching",
  "Confusing Relevance with Direct Answerability": "Hallucinated Requirement",
  "Conflating Negative Answerability with Relevance": "Overly Strict Interpretation",
  "Overly strict threshold for relevance": "Overly Strict Relevance Threshold",
  "Scale Miscalibration": "Ignored Nuance",
  "Overly Strict Standards": "Overly Strict Relevance Threshold",
  "Overly strict evaluation criteria": "Overly Strict Interpretation",
  "Over-weighted Lexical Mismatch": "Overly Strict Interpretation",
  "Strict Lexical Matching on Identifier Query": "Superficial Keyword Matching",
  "Over-penalized inaccuracy": "Overly Strict Interpretation",
  "Disregarded Topical Relevance": "Overly Strict Relevance Threshold",
  "Over-strict Grading Criteria": "Overly Strict Interpretation",
  "Score mapping error": "Missing Reasoning",
  "Hallucinated relevance without lexical match": "Over-crediting tangential relevance",
  "Demanded Excessive Granularity": "Hallucinated Requirement",
  "Failure to resolve entity identifier": "Failure to resolve entity identifier",
  "Strict lexical mismatch": "Overly Strict Interpretation",
  "All-or-nothing judgment": "Overly Strict Relevance Threshold",
  "Failed to Resolve Entity Identifier": "Failed to Resolve Entity Identifier",
  "Failure to recognize topical relevance": "Overly Strict Relevance Threshold",
  "Ignored Disjunctive Condition": "Ignored Nuance",
  "Evaluated Query Quality Instead of Relevance": "Evaluated Query Quality Instead of Relevance",
  "Score Inconsistency with Reasoning": "Missing Reasoning",
  "Over-penalizing Lack of Exact Terminology": "Over-weighted keyword match",
  "Dismissed marginal relevance": "Overly Strict Relevance Threshold",
  "Leniency Bias": "Over-crediting tangential relevance",
  "Defaulted to Non-Zero Relevance": "Defaulted to Non-Zero Relevance",
  "Pedantic / Over-strict Evaluation": "Overly Strict Interpretation",
  "Misinterpreting Negative Verification as Relevance": "Misinterpreting Negative Verification as Relevance",
  "Spurious Numeric Match": "Superficial Keyword Matching",
  "Underestimating Partial Relevance": "Overly Strict Relevance Threshold",
  "Over-weighted ambiguity": "Over-weighted specific aspect",
  "Ignoring topical relevance": "Overly Strict Interpretation",
  "Strict Binary Evaluation": "Overly Strict Relevance Threshold",
  "Score calibration error": "Score calibration error",
  "Assumed Latent Match": "Hallucinated Requirement",
  "Strict Lexical Over-reliance": "Over-weighted keyword match",
  "Demanded excessive detail": "Hallucinated Requirement",
  "Inverted Answerability Logic": "Inverted Answerability Logic",
  "Over-penalization of tangential relevance": "Overly Strict Relevance Threshold",
  "Conflated Answerability with Topical Relevance": "Overly Strict Interpretation",
  "Awarded Partial Credit for Indirect Information": "Over-crediting tangential relevance",
  "Ungrounded Inference": "Hallucinated Requirement",
  "Harsh Penalty for Ambiguity": "Overly Strict Interpretation",
  "All-or-nothing scoring": "Overly Strict Relevance Threshold",
  "Over-strict relevance criteria": "Overly Strict Relevance Threshold",
  "Ignored Graded Relevance": "Overly Strict Relevance Threshold",
  "Confusing Sufficiency with Relevance": "Overly Strict Interpretation",
  "Confusing absence of information with an answer": "Confusing absence of information with an answer",
  "Empty Reasoning": "Missing Reasoning",
  "Reasoning-to-Score Contradiction": "Reasoning-to-Score Contradiction",
  "Empty Response / Missing Reasoning": "Missing Reasoning",
  "Conflating Absence with an Answer": "Conflating Absence with an Answer",
  "Literal evaluation of query identifier": "Superficial Keyword Matching",
  "Over-penalizing lack of direct answer": "Overly Strict Interpretation",
  "Over-penalization of partial information": "Overly Strict Relevance Threshold",
  "Task Misunderstanding": "Task Misunderstanding",
  "Overly Strict Binary Interpretation": "Overly Strict Interpretation",
  "Unrecognized Entity Identifier": "Ignored Nuance",
  "Disqualified partial relevance": "Overly Strict Relevance Threshold",
  "Over-penalization": "Overly Strict Relevance Threshold",
  "Ignored Rubric Nuance": "Ignored Nuance",
  "Flawed meta-reasoning": "Flawed meta-reasoning",
  "Scale Misalignment": "Scale Misalignment",
  "Over-weighted query ambiguity": "Over-weighted specific aspect",
  "Strict Answerability vs Topical Relevance": "Overly Strict Interpretation",
  "Strict Keyword Matching": "Superficial Keyword Matching",
  "Over-penalizing Incompleteness": "Overly Strict Interpretation",
  "Equated Absence of Information with Relevance": "Equated Absence of Information with Relevance",
  "Score Inconsistency / Mapping Failure": "Score Inconsistency / Mapping Failure",
  "Overlooked Document Text": "Ignored Nuance",
  "Over-penalizing Missing Detail": "Overly Strict Interpretation",
  "Fallacious Answerability Logic": "Fallacious Answerability Logic",
  "Output Contradicts Reasoning": "Output Contradicts Reasoning",
  "Strict Lexical Matching on Query Artifact": "Superficial Keyword Matching",
  "Superficial Keyword Matching": "Superficial Keyword Matching",
  "Score Calibration Failure": "Score Calibration Failure",
  "Score/Reasoning Discrepancy": "Score/Reasoning Discrepancy",
  "All-or-nothing reasoning": "Overly Strict Relevance Threshold",
  "Binary/All-or-Nothing Judgment": "Overly Strict Relevance Threshold",
  "Over-penalized missing mechanism": "Hallucinated Requirement",
  "Flawed Logic / Negative Answer Fallacy": "Ignored Nuance",
  "Failure to resolve numeric query identifier": "Failure to resolve numeric query identifier",
  "Hallucinated Query / Premise": "Hallucinated Requirement",
  "Lexical Overlap Reliance": "Superficial Keyword Matching",
  "Meta-Reasoning Confusion": "Meta-Reasoning Confusion",
  "Overly Literal Interpretation": "Overly Strict Interpretation",
  "Over-penalized lack of specific answer": "Hallucinated Requirement",
  "Incomplete Reasoning": "Missing Reasoning",
  "Scale Calibration": "Scale Calibration",
  "Over-penalization of ambiguous phrasing": "Overly Strict Interpretation",
  "Overly Strict Evaluation Criteria": "Overly Strict Relevance Threshold",
  "Over-penalization of incomplete details": "Overly Strict Relevance Threshold",
  "Failure to Resolve Query ID Artifact": "Failure to Resolve Query ID Artifact",
  "Ignored Minimal Relevance": "Overly Strict Relevance Threshold",
  "Unrecognized Domain-Specific Identifier": "Unrecognized Domain-Specific Identifier",
  "Over-reliance on Exact Keyword Match": "Superficial Keyword Matching",
  "Over-rationalizing Relevance": "Over-crediting tangential relevance",
  "Over-penalizing ambiguity": "Overly Strict Interpretation",
  "Scoring Calibration Error": "Scoring Calibration Error",
  "Confusing Answerability with Topical Relevance": "Hallucinated Requirement",
  "Failure to credit topical/partial relevance": "Overly Strict Relevance Threshold",
  "Literal Interpretation of Query ID": "Literal Interpretation of Query ID",
  "Overly Pedantic Interpretation": "Overly Strict Interpretation",
  "Overthinking Question Semantics": "Overly Strict Interpretation",
  "Unrecognized Document Identifier": "Unrecognized Document Identifier",
  "Score-reasoning inconsistency": "Score-reasoning inconsistency",
  "External Knowledge Reliance": "External Knowledge Reliance",
  "Ignored marginal topical relevance": "Overly Strict Relevance Threshold",
  "Overthinking Meta-Answerability": "Overthinking Meta-Answerability",
  "Score Mismatch": "Score Mismatch",
  "Under-crediting Partial Relevance": "Overly Strict Relevance Threshold",
  "Under-weighting marginal topical relevance": "Overly Strict Relevance Threshold",
  "Strictness on Partial Relevance": "Overly Strict Relevance Threshold",
  "Score Calibration Inconsistency": "Score Calibration Inconsistency",
  "Missed Key Entity": "Ignored Nuance",
  "Confused Incompleteness with Irrelevance": "Overly Strict Relevance Threshold",
  "Over-weighting specific aspect": "Over-weighted specific aspect",
  "Misapplied Scoring Rubric": "Misapplied Scoring Rubric",
  "Over-penalized lack of detail": "Overly Strict Relevance Threshold",
  "Over-reliance on lexical match": "Superficial Keyword Matching",
  "Score Miscalibration": "Score Miscalibration",
  "Score-Reasoning Disconnect": "Score-Reasoning Disconnect",
  "Scale Calibration Error": "Scale Calibration Error",
  "Conflating Relevance with Direct Answerability": "Hallucinated Requirement",
  "Confusing Negative Answer with Non-Relevance": "Ignored Nuance",
  "Over-penalization of Ambiguity": "Overly Strict Interpretation",
  "Disregarded Marginal Relevance": "Overly Strict Relevance Threshold",
  "Over-penalizing lack of specificity": "Overly Strict Interpretation",
  "Equating partial relevance to irrelevance": "Overly Strict Relevance Threshold",
  "Strict thresholding on topical relevance": "Overly Strict Relevance Threshold",
  "Penalized Missing Alternative": "Hallucinated Requirement",
  "Meta-Reasoning Fallacy": "Meta-Reasoning Fallacy",
  "Overly Strict Matching": "Overly Strict Interpretation",
  "Hallucinated Requirement": "Hallucinated Requirement",
  "Score Contradiction": "Score Contradiction",
  "Flawed Meta-reasoning": "Flawed Meta-reasoning",
  "All-or-Nothing Assessment": "Overly Strict Relevance Threshold",
  "Ignored Topical Relevance": "Overly Strict Relevance Threshold",
  "Demanding excessive detail": "Overly Strict Interpretation",
  "Overly Strict Rubric Interpretation": "Overly Strict Interpretation",
  "Over-crediting absence of evidence": "Over-crediting tangential relevance",
  "Strict Lexical Matching / Query ID Sensitivity": "Superficial Keyword Matching",
  "Demanded Excessive Explicitness": "Overly Strict Interpretation",
  "Hallucinated Task/Requirement": "Hallucinated Requirement",
  "Over-reliance on literal semantic match": "Superficial Keyword Matching",
  "Failure to credit minimal topical relevance": "Overly Strict Relevance Threshold",
  "Demanded Affirmative Answer": "Hallucinated Requirement",
  "Unrecognized Database Identifier": "Unrecognized Database Identifier",
  "Failure to Recognize Related Concepts": "Ignored Nuance",
  "Overly strict evaluation standard": "Overly Strict Relevance Threshold",
  "Over-penalizing Query Ambiguity": "Overly Strict Interpretation",
  "Reinterpreting Query to Force Match": "Over-weighted topical overlap",
  "Excessive Penalty for Partial Relevance": "Overly Strict Relevance Threshold",
  "Failure to Recognize Document Identifier": "Failure to Recognize Document Identifier",
  "Dataset Artifact / Query ID Failure": "Dataset Artifact / Query ID Failure",
  "Equating Answerability with Relevance": "Overly Strict Interpretation",
  "Over-literal Interpretation": "Overly Strict Interpretation",
  "Score-Reasoning Mismatch": "Score-Reasoning Mismatch",
  "Score Disconnect": "Score Disconnect",
  "Flawed Task Logic": "Flawed Task Logic",
  "Overly Strict Extraction Requirement": "Hallucinated Requirement",
  "Binary Assumption": "Overly Strict Relevance Threshold",
  "Failure to Handle ID Query": "Failure to Handle ID Query",
  "Over-penalizing partial answer": "Overly Strict Relevance Threshold",
  "Over-weighted strict answerability": "Overly Strict Interpretation",
  "Over-penalizing Absence of Direct Answer": "Overly Strict Interpretation",
  "Strict Answerability Standard": "Overly Strict Interpretation",
  "Over-interpretation of ambiguous query": "Ignored Nuance",
  "Lenient Query Reinterpretation": "Over-crediting tangential relevance",
  "Overly Strict Threshold for Partial Relevance": "Overly Strict Relevance Threshold",
  "Overly Strict Evidence Standard": "Overly Strict Relevance Threshold",
  "Overthinking / Semantic Pedantry": "Overly Strict Interpretation",
  "Over-stringent relevance criteria": "Overly Strict Relevance Threshold",
  "Demanding Unreasonable Specificity": "Overly Strict Interpretation",
  "Overly Strict Scoring Threshold": "Overly Strict Relevance Threshold",
  "Equating relevance with complete answerability": "Overly Strict Interpretation",
  "Overly Strict Relevance Criteria": "Overly Strict Relevance Threshold",
  "Misunderstood Task Framing": "Misunderstood Task Framing",
  "Treated Graded Relevance as Binary": "Treated Graded Relevance as Binary",
  "Spurious Numerical Overlap": "Superficial Keyword Matching",
  "Ignoring marginal relevance": "Overly Strict Relevance Threshold",
  "Task Confusion": "Task Confusion",
  "Over-penalization for missing direct answer": "Overly Strict Interpretation",
  "Conflating relevance with answerability": "Overly Strict Interpretation",
  "Over-penalized missing information": "Overly Strict Interpretation",
  "Faulty Meta-Reasoning": "Faulty Meta-Reasoning",
  "Internal Contradiction / Scale Confusion": "Internal Contradiction / Scale Confusion",
  "Confusing Answerability with Graded Relevance": "Overly Strict Interpretation",
  "Misinterpreted Logical Operator": "Ignored Nuance",
  "Excessive Literalism": "Overly Strict Interpretation",
  "Confused Relevance with Factual Correctness": "Confused Relevance with Factual Correctness",
  "Meta-reasoning Fallacy": "Meta-reasoning Fallacy",
  "Failure to Handle Identifier Query": "Failure to Handle Identifier Query",
  "Under-credited partial relevance": "Overly Strict Relevance Threshold",
  "Unrecognized Identifier Query": "Unrecognized Identifier Query",
  "Superficial Number Matching": "Superficial Keyword Matching",
  "Reasoning-Output Contradiction": "Reasoning-Output Contradiction",
  "Failure to identify partial relevance": "Overly Strict Relevance Threshold",
  "Failure to resolve entity code": "Failure to resolve entity code",
  "Strict Threshold for Marginal Relevance": "Overly Strict Relevance Threshold",
  "Over-penalizing partial relevance": "Overly Strict Relevance Threshold",
  "Over-penalizing Marginal Relevance": "Overly Strict Relevance Threshold",
  "Conflating Relevance with Answerability": "Overly Strict Interpretation",
  "Reasoning-Output Discrepancy": "Reasoning-Output Discrepancy",
  "Confusing Answerability with Relevance": "Overly Strict Interpretation",
  "Failed to Credit Topical Relevance": "Overly Strict Relevance Threshold",
  "Excessively Strict Threshold": "Overly Strict Relevance Threshold",
  "Failure to Resolve Opaque Query ID": "Failure to Resolve Opaque Query ID",
  "Strict relevance threshold": "Overly Strict Relevance Threshold",
  "Over-weighted Lexical Match": "Over-weighted keyword match",
  "Spurious Relevance Inference": "Over-crediting tangential relevance",
  "Scale Mismatch": "Scale Mismatch",
  "Overestimating Relevance": "Over-crediting tangential relevance",
  "Ignored Document ID/Lookup Context": "Ignored Document ID/Lookup Context",
  "Dismissed Topical Relevance": "Overly Strict Relevance Threshold",
  "Equated Negative Answer with Relevance": "Equated Negative Answer with Relevance",
  "Overthinking Task Criteria": "Hallucinated Requirement",
  "Spurious Matching": "Superficial Keyword Matching",
  "Over-penalized Query Ambiguity": "Overly Strict Interpretation",
  "Hallucinated relevance": "Over-crediting tangential relevance",
  "Equating Negative Answer with Insufficient Information": "Overly Strict Interpretation",
  "Treated Partial Relevance as Irrelevant": "Overly Strict Relevance Threshold",
  "Literal Semantic Over-reliance": "Overly Strict Interpretation",
  "Literal interpretation of query artifact": "Ignored Nuance",
  "Treating Disjunctive Requirement as Conjunctive": "Hallucinated Requirement",
  "Overly Strict Threshold": "Overly Strict Relevance Threshold",
  "Disregard of marginal relevance": "Overly Strict Relevance Threshold",
  "Strict answerability over topical relevance": "Overly Strict Interpretation",
  "Excessive Standard of Completeness": "Overly Strict Interpretation",
  "Overly Strict Specificity Requirement": "Overly Strict Interpretation",
  "Failure to Recognize Graded Topical Relevance": "Ignored Nuance",
  "Over-weighted completeness over relevance": "Overly Strict Interpretation",
  "Conflating Unhelpfulness with Irrelevance": "Overly Strict Interpretation",
  "Over-penalized lack of direct answer": "Overly Strict Interpretation",
  "Over-penalization of Marginal Relevance": "Overly Strict Relevance Threshold",
  "Failure to Map Query Identifier": "Failure to Map Query Identifier",
  "Hallucinated Query Requirements": "Hallucinated Requirement",
  "All-or-Nothing Fallacy": "Overly Strict Relevance Threshold",
  "Ignored Grading Scale Nuance": "Ignored Nuance",
  "Overly Stringent Scoring": "Overly Strict Relevance Threshold",
  "Overly stringent criteria": "Overly Strict Relevance Threshold",
  "Demanding Completeness": "Overly Strict Interpretation",
  "Strict Literalism": "Overly Strict Interpretation",
  "Hallucinated Query Requirement": "Hallucinated Requirement",
  "Confused Answerability with Relevance": "Overly Strict Interpretation",
  "Evaluated Query Quality Instead of Document Relevance": "Evaluated Query Quality Instead of Document Relevance",
  "Failure in Entity Resolution": "Failure in Entity Resolution",
  "Reasoning-Score Discrepancy": "Reasoning-Score Discrepancy",
  "Over-penalized literal query mismatch": "Overly Strict Interpretation",
  "Treated Marginal Relevance as Irrelevant": "Overly Strict Relevance Threshold",
  "Excessive Strictness / Failure to Credit Partial Relevance": "Overly Strict Relevance Threshold",
  "Ignored Nuance of Partial Relevance": "Ignored Nuance",
  "Over-penalizing Missing Details": "Overly Strict Interpretation",
  "Failure to Recognize Query Identifier": "Failure to Recognize Query Identifier",
  "Over-reliance on lexical matching": "Superficial Keyword Matching",
  "Overly Strict Standard": "Overly Strict Relevance Threshold",
  "Over-weighted exact keyword match": "Over-weighted keyword match",
  "All-or-Nothing Judgment": "Overly Strict Relevance Threshold",
  "Failure to credit topical overlap": "Overly Strict Relevance Threshold",
  "False Positive Relevance": "Over-crediting tangential relevance",
  "Over-penalization of Incompleteness": "Overly Strict Interpretation",
  "Over-demanding criteria": "Overly Strict Relevance Threshold",
  "Hallucinated Task and Score Inconsistency": "Hallucinated Task and Score Inconsistency",
  "Confusing answerability with relevance": "Overly Strict Interpretation",
  "Demanded Explicit Answer": "Overly Strict Interpretation",
  "Overly literal interpretation": "Overly Strict Interpretation",
  "Misidentified Query": "Misidentified Query",
  "Ignored Marginal Topical Relevance": "Overly Strict Relevance Threshold",
  "Flawed Verification Logic": "Flawed Verification Logic",
  "Strict Semantic Matching": "Overly Strict Interpretation",
  "Presumed Missing Context": "Hallucinated Requirement",
  "Failure to resolve query identifier": "Failure to resolve query identifier",
  "Equating Relevance with Definitive Answerability": "Overly Strict Interpretation",
  "Over-penalization of marginal relevance": "Overly Strict Relevance Threshold",
  "Equating Insufficiency with Irrelevance": "Overly Strict Interpretation",
  "False positive relevance": "Over-crediting tangential relevance",
  "Overly Strict Interpretation": "Overly Strict Interpretation",
  "Failure to award marginal relevance": "Overly Strict Relevance Threshold",
  "Overly Strict Answerability Criterion": "Overly Strict Interpretation",
  "Over-penalization for missing explicit terminology": "Overly Strict Interpretation",
  "Failure to identify marginal relevance": "Overly Strict Relevance Threshold",
  "Ignored Graded Relevance Scale": "Ignored Graded Relevance Scale",
  "Failure to credit partial topical relevance": "Overly Strict Relevance Threshold",
  "Binary Relevance Evaluation": "Binary Relevance Evaluation",
  "Assumption of User Intent": "Assumption of User Intent",
  "Failure to recognize query identifier": "Failure to recognize query identifier",
  "Rubric Scale Misinterpretation": "Rubric Scale Misinterpretation",
  "Over-weighted specific constraint": "Over-weighted specific aspect",
  "Scale Confusion": "Scale Confusion",
  "Overlooked Relevant Information": "Ignored Nuance",
  "Failure to Recognize Marginal Relevance": "Overly Strict Relevance Threshold",
  "Conflating negative answer with irrelevance": "Conflating negative answer with irrelevance",
  "Over-weighted incompleteness": "Overly Strict Interpretation",
  "Internal Inconsistency": "Internal Inconsistency",
  "Evaluated query quality instead of document relevance": "Evaluated query quality instead of document relevance",
  "Overthinking Query Semantics": "Overly Strict Interpretation",
  "Ignored Graded Scale Nuance": "Ignored Nuance",
  "Literal Lexical Matching": "Superficial Keyword Matching",
  "Spurious Lexical Match": "Superficial Keyword Matching",
  "Rating Scale Miscalibration": "Rating Scale Miscalibration",
  "Spurious Relevance Assumption": "Over-crediting tangential relevance",
  "Over-penalizing missing specifics": "Overly Strict Interpretation",
  "Confusing Partial Relevance with Irrelevance": "Overly Strict Relevance Threshold",
  "Miscalibration": "Miscalibration",
  "Over-weighted complete answerability": "Overly Strict Interpretation",
  "Hallucinated Query Constraint": "Hallucinated Requirement",
  "Overestimating certainty": "Ignored Nuance",
  "Over-reliance on Lexical Overlap": "Over-weighted keyword match",
  "Demanded Unnecessary Specificity": "Hallucinated Requirement",
  "Confused Absence of Information with Valid Answer": "Confused Absence of Information with Valid Answer",
  "Penalized Query Quality": "Penalized Query Quality",
  "Overly Strict Literalism": "Overly Strict Interpretation",
  "Overly Stringent Relevance Threshold": "Overly Strict Relevance Threshold",
  "Failure to Identify Implicit Relevance": "Ignored Nuance",
  "Over-penalization from Hallucinated Requirement": "Hallucinated Requirement",
  "Treated Relevance as Binary Answerability": "Treated Relevance as Binary Answerability",
  "Under-scoring partial relevance": "Overly Strict Relevance Threshold",
  "Confusing Topical Relevance with Answerability": "Confusing Topical Relevance with Answerability",
  "Score Mismatch / Output Inconsistency": "Score Mismatch / Output Inconsistency",
  "Over-penalization / Excessive Strictness": "Overly Strict Interpretation",
  "Failed Numerical Association": "Failed Numerical Association",
  "Misapplied Evaluation Criteria": "Misapplied Evaluation Criteria",
  "Over-penalization of partial match": "Overly Strict Relevance Threshold",
  "Scale miscalibration": "Scale miscalibration",
  "Flawed Task Interpretation": "Flawed Task Interpretation",
  "Demanded Complete Coverage": "Overly Strict Interpretation",
  "Miscalibration of Grading Scale": "Miscalibration of Grading Scale",
  "Over-penalized ambiguous query": "Overly Strict Interpretation",
  "Incomplete Context Processing": "Ignored Nuance",
  "Failure to Distinguish Minimal Relevance from Irrelevance": "Overly Strict Relevance Threshold",
  "Score Inflation": "Over-crediting tangential relevance",
  "Conflating negative verification with high relevance": "Ignored Nuance",
  "Unrecognized Query Identifier": "Unrecognized Query Identifier",
  "Over-penalizing query ambiguity": "Overly Strict Interpretation",
  "Over-stringent threshold": "Overly Strict Relevance Threshold",
  "Dismissing Topical Relevance": "Overly Strict Interpretation",
  "Strict Binary Assessment": "Overly Strict Relevance Threshold",
  "Failed Identifier Mapping": "Failed Identifier Mapping",
  "Query ID Resolution Failure": "Query ID Resolution Failure",
  "Ignored Marginal Relevance Criteria": "Overly Strict Relevance Threshold",
  "Evaluating Document Quality Instead of Relevance": "Hallucinated Requirement",
  "Failure to Handle Query ID": "Failure to Handle Query ID",
  "Literal Keyword Bias": "Superficial Keyword Matching",
  "Binary Scoring / Ignored Marginal Relevance": "Overly Strict Relevance Threshold",
  "Strict Literal Matching on Query Artifact": "Superficial Keyword Matching",
  "Failed to Recognize ID Lookup": "Failed to Recognize ID Lookup",
  "Over-penalization of Lexical Mismatch": "Over-weighted keyword match",
  "Over-penalized lack of specificity": "Overly Strict Interpretation",
  "Failure to Identify Partial Relevance": "Overly Strict Relevance Threshold",
  "Excessively Strict Criterion": "Overly Strict Interpretation",
  "Miscalibrated Scoring": "Miscalibrated Scoring",
  "Over-penalized Lack of Keyword Match": "Over-weighted keyword match",
  "Failure to recognize opaque identifier": "Failure to recognize opaque identifier",
  "Dismissal of tangential relevance": "Overly Strict Relevance Threshold",
  "Over-weighted partial match": "Over-weighted topical overlap",
  "Spurious Relevance / Overly Lenient Scoring": "Over-crediting tangential relevance",
  "Conflating Implication with Specification": "Ignored Nuance",
  "Ignored Implicit Information": "Ignored Nuance",
  "Treated graded scale as binary": "Overly Strict Relevance Threshold",
  "Under-crediting Marginal Relevance": "Overly Strict Relevance Threshold",
  "Over-penalizing background relevance": "Overly Strict Relevance Threshold",
  "Spurious Association": "Over-weighted topical overlap",
  "Failed ID / Entity Mapping": "Failed ID / Entity Mapping",
  "Unresolved Query ID": "Unresolved Query ID",
  "Strict Lexical Matching": "Superficial Keyword Matching",
  "Demanded Explicit Terminology": "Over-weighted keyword match",
  "Failure to recognize benchmark query ID": "Failure to recognize benchmark query ID",
  "Literal Matching Bias": "Superficial Keyword Matching",
  "Evaluation against Hallucinated Query": "Hallucinated Requirement",
  "False negative on identifier query": "False negative on identifier query",
  "Overly Strict Completeness Standard": "Overly Strict Interpretation",
  "Query artifact misinterpretation": "Query artifact misinterpretation",
  "Over-weighted Incompleteness": "Overly Strict Interpretation",
  "Demanding Excessive Specificity": "Overly Strict Interpretation",
  "Failure to Recognize Partial Relevance": "Overly Strict Relevance Threshold",
  "Over-analyzed ambiguity": "Overly Strict Interpretation",
  "Ignored Partial/Topical Relevance": "Overly Strict Relevance Threshold",
  "Over-penalizing Lack of Depth": "Overly Strict Relevance Threshold",
  "Excessive strictness on answerability": "Overly Strict Relevance Threshold",
  "Overly Lenient Scoring": "Over-crediting tangential relevance",
  "Conflated Absence of Information with Answerability": "Ignored Nuance",
  "Over-analyzing Ambiguity": "Overly Strict Interpretation",
  "Excessive Rigidity": "Overly Strict Interpretation",
  "Over-penalized lack of explicit mention": "Overly Strict Interpretation",
  "Failed to recognize marginal relevance": "Overly Strict Relevance Threshold",
  "Incomplete Generation / Formatting Issue": "Incomplete Generation / Formatting Issue",
  "Over-penalization of Direct Answerability": "Overly Strict Relevance Threshold",
  "Over-weighted Direct Answer Requirement": "Hallucinated Requirement",
  "Flawed Logic": "Missing Reasoning",
  "Over-penalization of incomplete coverage": "Overly Strict Relevance Threshold",
  "Over-penalization of incomplete information": "Overly Strict Relevance Threshold",
  "Spurious Relevance Attribution": "Over-crediting tangential relevance",
  "Strict Semantic Matching on Query Artifact": "Overly Strict Interpretation",
  "Over-thinking Ambiguity": "Overly Strict Interpretation",
  "Dismissing partial topical relevance": "Overly Strict Relevance Threshold",
  "Misconstruing Negative Relevance as Partial Credit": "Over-crediting tangential relevance",
  "Hallucinated Evaluation Criteria": "Hallucinated Requirement",
  "Binary All-or-Nothing Evaluation": "Overly Strict Relevance Threshold",
  "Over-penalization of Incomplete Information": "Overly Strict Relevance Threshold",
  "Discounted partial relevance": "Overly Strict Relevance Threshold",
  "Treating Absence of Information as an Answer": "Ignored Nuance",
  "Over-penalized missing details": "Overly Strict Relevance Threshold",
  "Confusing Relevance with Full Answerability": "Overly Strict Relevance Threshold",
  "Hallucinated connection": "Over-crediting tangential relevance",
  "Score/Verdict Mismatch": "Missing Reasoning",
  "Strict/Binary Answer Requirement": "Hallucinated Requirement",
  "Superficial Pattern Matching": "Superficial Keyword Matching",
  "Failure to Handle Query Identifier": "Ignored Nuance",
  "Output Inconsistency": "Missing Reasoning",
  "Overly Stringent Standards": "Overly Strict Relevance Threshold",
  "Over-penalized Lack of Detail": "Overly Strict Relevance Threshold",
  "Conflating Topical Relevance with Direct Answerability": "Overly Strict Relevance Threshold",
  "Overly strict answerability standard": "Overly Strict Relevance Threshold",
  "Failure to Infer Implicit Information": "Overly Strict Interpretation",
  "Misinterpreted Task as Meta-Question": "Ignored Nuance",
  "Spurious Numeric Matching": "Superficial Keyword Matching",
  "Over-weighted explicit answer requirement": "Hallucinated Requirement",
  "False Positive on Irrelevant Query": "Over-crediting tangential relevance",
  "Undervaluation of Partial Relevance": "Overly Strict Relevance Threshold",
  "Keyword Matching Bias": "Over-weighted keyword match",
  "Scale Mapping Error": "Scale Mapping Error",
  "Ignored Nuance of Verification Task": "Ignored Nuance",
  "Failed to recognize minimal topical relevance": "Overly Strict Relevance Threshold",
  "Failure to recognize partial relevance": "Overly Strict Relevance Threshold",
  "Score/Reasoning Mismatch": "Missing Reasoning",
  "Score Mapping Error": "Score Mapping Error",
  "Over-strict relevance threshold": "Overly Strict Relevance Threshold",
  "Ungrounded Assumption": "Hallucinated Requirement",
  "Contradictory Logic": "Contradictory Logic",
  "Failure to handle opaque identifier": "Failure to handle opaque identifier",
  "Over-penalized partial information": "Overly Strict Relevance Threshold",
  "Rejection of Negative Answerability": "Ignored Nuance",
  "Penalized Missing Optional Requirement": "Hallucinated Requirement",
  "Failure to resolve numeric identifier": "Failure to resolve numeric identifier",
  "Overly Strict Answerability Threshold": "Overly Strict Relevance Threshold",
  "Excessive strictness": "Overly Strict Interpretation",
  "Over-penalization of query ambiguity": "Overly Strict Interpretation",
  "Confused Relevance with Answerability": "Overly Strict Interpretation",
  "Dismissed Minimal Relevance": "Overly Strict Relevance Threshold",
  "Failure to recognize identifier query": "Failure to recognize identifier query",
  "Over-penalizing incompleteness": "Overly Strict Relevance Threshold",
  "Over-reliance on Literal Match": "Superficial Keyword Matching",
  "Over-penalized Incomplete Information": "Overly Strict Relevance Threshold",
  "Overthinking task framing": "Overly Strict Interpretation",
  "Over-strict Semantic Matching": "Overly Strict Interpretation",
  "Score-reasoning contradiction": "Score-reasoning contradiction",
  "Spurious Concept Association": "Over-crediting tangential relevance",
  "Overly Strict Binary Evaluation": "Overly Strict Relevance Threshold",
  "Overly Strict Relevance Threshold": "Overly Strict Relevance Threshold",
  "Internal Contradiction between Reasoning and Score": "Internal Contradiction between Reasoning and Score",
  "Demanded Excessive Specificity": "Overly Strict Interpretation",
  "Conflating Negative Answer with Unanswerability": "Ignored Nuance",
  "Treated Relevance as Direct Answerability": "Overly Strict Interpretation",
  "Flawed Answerability Logic": "Ignored Nuance",
  "Overly strict criterion": "Overly Strict Interpretation",
  "Over-reliance on literal lexical match": "Superficial Keyword Matching",
  "Strict Lexical Overlap Failure": "Superficial Keyword Matching",
  "Ignored Partial Topical Relevance": "Overly Strict Relevance Threshold",
  "Over-penalization of Unanswerability": "Overly Strict Relevance Threshold",
  "Failure to assign partial credit": "Overly Strict Relevance Threshold",
  "Excessive Strictness": "Overly Strict Interpretation",
  "Strict Binary Answerability": "Overly Strict Relevance Threshold",
  "Conflated Unanswerability with Irrelevance": "Overly Strict Interpretation",
  "Failed to handle numerical identifier": "Failed to handle numerical identifier",
  "Overly Harsh Rejection": "Overly Strict Relevance Threshold",
  "Failed to Resolve Numeric Identifier": "Failed to Resolve Numeric Identifier",
  "Strict Answerability Bias": "Overly Strict Interpretation",
  "Over-lenient relevance scoring": "Over-crediting tangential relevance",
  "Over-penalization for missing core answer": "Overly Strict Relevance Threshold",
  "Over-penalized lack of full detail": "Overly Strict Relevance Threshold",
  "Hallucinated Document Content": "Hallucinated Document Content",
  "Pedantic Misinterpretation": "Overly Strict Interpretation",
  "Failed Entity/Identifier Resolution": "Failed Entity/Identifier Resolution",
  "Internal Consistency Error": "Internal Consistency Error",
  "Overly Strict Relevance Standard": "Overly Strict Relevance Threshold",
  "Over-penalization of Ambiguous Reference": "Overly Strict Interpretation",
  "Literal Query Interpretation": "Overly Strict Interpretation",
  "Factual Misreading of Document": "Factual Misreading of Document",
  "False Positive Matching": "Superficial Keyword Matching",
  "Failure to Resolve Numeric Identifier": "Failure to Resolve Numeric Identifier",
  "Failure to Resolve Domain-Specific Identifier": "Failure to Resolve Domain-Specific Identifier",
  "Conflating accuracy with relevance": "Overly Strict Interpretation",
  "Overly Strict Evaluation Criterion": "Overly Strict Relevance Threshold",
  "All-or-Nothing Standard": "Overly Strict Relevance Threshold",
  "Conflating Completeness with Relevance": "Overly Strict Interpretation",
  "Over-reliance on semantic overlap": "Over-weighted topical overlap",
  "Spurious Match / Partial Matching": "Superficial Keyword Matching",
  "Overlooked Topical Relationship": "Ignored Nuance",
  "Failure to credit tangential relevance": "Overly Strict Relevance Threshold",
  "Ignored topical relevance": "Ignored Nuance",
  "Overly harsh relevance threshold": "Overly Strict Relevance Threshold",
  "Spurious Number Matching": "Over-weighted keyword match",
  "Strict Lexical Matching on ID Query": "Superficial Keyword Matching",
  "Overlooked Relevant Entities": "Ignored Nuance",
  "Discounting Tangential Relevance": "Overly Strict Relevance Threshold",
  "Failed Entity Linking": "Failed Entity Linking",
  "Strict Lexical Overlap Bias": "Over-weighted keyword match",
  "Scoring Inconsistency": "Scoring Inconsistency",
  "Overly strict grading threshold": "Overly Strict Relevance Threshold",
  "Conflated partial relevance with irrelevance": "Overly Strict Relevance Threshold",
  "Mishandled Identifier Query": "Mishandled Identifier Query",
  "Over-estimated relevance for opaque query": "Over-weighted topical overlap",
  "Conflating Answerability with Topical Relevance": "Overly Strict Interpretation",
  "Score Inconsistency / Scale Confusion": "Score Inconsistency / Scale Confusion",
  "Excessively Strict Criteria": "Overly Strict Relevance Threshold",
  "Overly strict evaluation": "Overly Strict Relevance Threshold",
  "Over-penalized query ambiguity": "Overly Strict Interpretation",
  "Scale Boundary Violation": "Scale Boundary Violation",
  "Dismissing marginal relevance": "Overly Strict Relevance Threshold",
  "Over-penalized Unanswerability": "Overly Strict Interpretation",
  "Failure to handle query ID artifact": "Failure to handle query ID artifact",
  "Failure to Reward Partial Relevance": "Overly Strict Relevance Threshold",
  "Strict thresholding on marginal relevance": "Overly Strict Relevance Threshold",
  "False Positive on Noise Query": "Superficial Keyword Matching",
  "Over-penalization of negative constraint": "Ignored Nuance",
  "Overly Strict Information Requirement": "Hallucinated Requirement",
  "Logic Inversion": "Logic Inversion",
  "Over-generous Scoring": "Over-crediting tangential relevance",
  "Over-penalizing indirect relevance": "Overly Strict Relevance Threshold",
  "Hallucinated Specific Requirements": "Hallucinated Requirement",
  "Rewarding Negative Answer": "Ignored Nuance",
  "Too Strict Evaluation of Partial Relevance": "Overly Strict Relevance Threshold",
  "Failure to Recognize Topical Relevance": "Ignored Nuance",
  "Factually Inaccurate Dismissal": "Factually Inaccurate Dismissal",
  "Under-weighted partial relevance": "Overly Strict Relevance Threshold",
  "Over-weighted broad domain relevance": "Over-weighted topical overlap",
  "Over-strict Evaluation": "Overly Strict Relevance Threshold",
  "Overly Strict Threshold for Marginal Relevance": "Overly Strict Relevance Threshold",
  "Score Inconsistency": "Score Inconsistency",
  "Scale Boundary Misunderstanding": "Scale Boundary Misunderstanding",
  "Over-weighted negative constraint": "Over-weighted specific aspect",
  "Conflating Negative Answer with Document Relevance": "Conflating Negative Answer with Document Relevance",
  "Overly Strict Grading": "Overly Strict Relevance Threshold",
  "Treated Graded Scale as Binary": "Treated Graded Scale as Binary",
  "Spurious Relevance / Hallucinated Match": "Over-crediting tangential relevance",
  "Overscoring partial information": "Over-crediting tangential relevance",
  "Overly Strict Sufficiency Threshold": "Overly Strict Relevance Threshold",
  "Overly Strict Completeness Threshold": "Overly Strict Relevance Threshold",
  "Over-penalizing Brevity": "Overly Strict Relevance Threshold",
  "Dismissed Partial Relevance": "Overly Strict Relevance Threshold",
  "Over-penalized Missing Specifics": "Overly Strict Relevance Threshold",
  "Failure to Recognize Conceptual Overlap": "Superficial Keyword Matching",
  "Scale Misunderstanding": "Scale Misunderstanding",
  "Flawed Negative-Answer Logic": "Flawed Negative-Answer Logic",
  "Overthinking Negative Answerability": "Overthinking Negative Answerability",
  "Demanded explicit mention": "Overly Strict Interpretation",
  "Overly Harsh Grading": "Overly Strict Relevance Threshold",
  "Conflated Answerability with Relevance": "Conflated Answerability with Relevance",
  "Over-penalized Lexical Mismatch": "Superficial Keyword Matching",
  "Failure to Handle Ambiguity": "Ignored Nuance",
  "Ignored marginal relevance": "Overly Strict Relevance Threshold",
  "Over-strict completeness standard": "Overly Strict Relevance Threshold",
  "Over-stringent criteria": "Overly Strict Relevance Threshold",
  "Over-penalization of partial relevance": "Overly Strict Relevance Threshold",
  "Failure to reward topical relevance": "Overly Strict Relevance Threshold",
  "Over-interpretation of Ambiguous Query": "Overly Strict Interpretation",
  "Score-reasoning mismatch": "Missing Reasoning",
  "Overly Strict Answerability Standard": "Overly Strict Relevance Threshold",
  "Pedantic Interpretation": "Overly Strict Interpretation",
  "Equating Relevance with Answerability": "Equating Relevance with Answerability",
  "Strict lexical matching failure": "Superficial Keyword Matching",
  "Overly strict grading": "Overly Strict Relevance Threshold",
  "Failure to Resolve Entity Identifier": "Ignored Nuance",
  "Strict Literal Keyword Matching": "Superficial Keyword Matching",
  "Equating Negative Answer with Relevance": "Equating Negative Answer with Relevance",
  "Excessive Strictness on Specificity": "Overly Strict Relevance Threshold",
  "Over-penalized Lack of Specificity": "Overly Strict Relevance Threshold",
  "Overly strict interpretation": "Overly Strict Interpretation",
  "Failure to assign marginal relevance": "Overly Strict Relevance Threshold",
  "Literal Query Matching Failure": "Superficial Keyword Matching",
  "Hallucinated Intent": "Hallucinated Requirement",
  "Treated Disjunction as Conjunction": "Overly Strict Interpretation",
  "Dismissal of Marginal Relevance": "Overly Strict Relevance Threshold",
  "Over-penalizing answer completeness": "Overly Strict Relevance Threshold",
  "Conflating marginal relevance with total irrelevance": "Overly Strict Relevance Threshold",
  "Spurious Pattern Matching": "Superficial Keyword Matching",
  "Failure to Handle Query ID / Artifact": "Failure to Handle Query ID / Artifact",
  "Overly strict relevance criterion": "Overly Strict Relevance Threshold",
  "Ungrounded Relevance Assessment": "Hallucinated Requirement",
  "Conflating Direct Answerability with Relevance": "Overly Strict Interpretation",
  "Over-strict evaluation standard": "Overly Strict Relevance Threshold",
  "Under-valued partial information": "Overly Strict Relevance Threshold",
  "Over-reliance on lexical overlap": "Over-weighted keyword match",
  "Overly Strict Answer Requirement": "Hallucinated Requirement",
  "Misinterpreted Query Intent": "Ignored Nuance",
  "Failure to credit marginal topical relevance": "Overly Strict Relevance Threshold",
  "Over-penalized Missing Information": "Overly Strict Relevance Threshold",
  "Rigid keyword matching": "Superficial Keyword Matching",
  "Hallucinated Query / Evaluation Criteria": "Hallucinated Requirement",
  "Spurious Relevance / False Positive": "Over-crediting tangential relevance",
  "Internal Reasoning Inconsistency": "Internal Reasoning Inconsistency",
  "Failed to resolve query ID": "Failed to resolve query ID",
  "Unrecognized Identifier Mapping": "Unrecognized Identifier Mapping",
  "Failure to Award Partial Credit": "Overly Strict Relevance Threshold",
  "Lenient Scoring on Opaque Query": "Over-crediting tangential relevance",
  "Over-weighted specific aspect": "Over-weighted specific aspect",
  "Rubric Miscalibration": "Rubric Miscalibration",
  "Failure to Identify Complete Irrelevance": "Over-crediting tangential relevance",
  "Conflated Negative Answer with Irrelevance": "Overly Strict Interpretation",
  "Dismissed peripheral relevance": "Overly Strict Relevance Threshold",
  "Equating Relevance to Answerability": "Overly Strict Interpretation",
  "Conflating Absence of Information with Relevance": "Over-crediting tangential relevance",
  "Over-penalizing missing details": "Overly Strict Relevance Threshold",
  "Treated graded relevance as binary": "Overly Strict Relevance Threshold",
  "Reasoning-Verdict Contradiction": "Internal Reasoning Inconsistency",
  "Hallucinated Connection": "Hallucinated Requirement",
  "Overly harsh scoring": "Overly Strict Relevance Threshold",
  "Failure to Resolve Numeric/ID Query": "Failure to Resolve Numeric/ID Query",
  "Spurious partial match": "Superficial Keyword Matching",
  "Literal Query Matching": "Superficial Keyword Matching",
  "Hallucinated Context": "Hallucinated Requirement",
  "Failure to Resolve Pronoun Ambiguity": "Failure to Resolve Pronoun Ambiguity",
  "Strict Answerability Assumption": "Overly Strict Interpretation",
  "Over-penalizing missing information": "Overly Strict Relevance Threshold",
  "Failure to award partial relevance": "Overly Strict Relevance Threshold",
  "Overlooked Partial Relevance": "Overly Strict Relevance Threshold",
  "Rubric/Scale Misalignment": "Rubric Miscalibration",
  "Dismissed Tangential Relevance": "Overly Strict Relevance Threshold",
  "Discounting Partial Relevance": "Overly Strict Relevance Threshold",
  "Overly Strict Criterion": "Overly Strict Relevance Threshold",
  "Overly Strict Evaluation": "Overly Strict Relevance Threshold",
  "All-or-nothing evaluation": "Overly Strict Relevance Threshold",
  "Task Misinterpretation": "Task Misinterpretation",
  "Rating Scale Misalignment": "Rubric Miscalibration",
  "Misinterpretation of Answerability": "Overly Strict Interpretation",
  "Imposed Unnecessary Requirement": "Hallucinated Requirement",
  "Over-penalizing Missing Keywords": "Overly Strict Interpretation",
  "Failed to Recognize Document Identifier": "Failed to Recognize Document Identifier",
  "Over-analyzed Question Semantics": "Overly Strict Interpretation",
  "Overly strict relevance threshold": "Overly Strict Relevance Threshold",
  "Over-crediting Absence of Evidence": "Over-crediting Absence of Evidence",
  "Scoring Scale Misalignment": "Scoring Scale Misalignment",
  "Overly Strict QA Requirement": "Overly Strict Interpretation",
  "False Positive / Hallucinated Relevance": "Over-crediting tangential relevance",
  "Reasoning-Score Disconnect": "Reasoning-Score Disconnect",
  "Over-penalized implicit information": "Ignored Nuance",
  "Under-weighted Partial Relevance": "Overly Strict Relevance Threshold",
  "Missing Reasoning": "Missing Reasoning",
  "Keyword Mismatch Dismissal": "Superficial Keyword Matching",
  "Hallucinated Query": "Hallucinated Query",
  "Hallucinated Query Context": "Hallucinated Requirement",
  "Conflating Verifiability with Document Relevance": "Conflating Verifiability with Document Relevance",
  "Over-permissive Scoring": "Over-crediting tangential relevance",
  "Failure to Credit Minimal Relevance": "Overly Strict Relevance Threshold",
  "Score Mismatch / Scale Confusion": "Score Mismatch / Scale Confusion",
  "Query ID Misinterpretation": "Query ID Misinterpretation",
  "Conflating Irrelevance with a Valid Negative Answer": "Ignored Nuance",
  "Conflating Negative Answer with Irrelevance": "Ignored Nuance",
  "Over-strict criteria": "Overly Strict Interpretation",
  "Over-weighted Topical Overlap": "Over-weighted topical overlap",
  "Over-stringent relevance threshold": "Overly Strict Relevance Threshold",
  "Dismissed partial relevance": "Overly Strict Relevance Threshold",
  "Over-penalizing Ambiguity": "Overly Strict Interpretation",
  "Discounted Partial Relevance": "Overly Strict Relevance Threshold",
  "Conflated Negative Answer with Relevance": "Over-crediting tangential relevance",
  "Failed to Recognize Entity Identifier": "Failed to Recognize Entity Identifier",
  "Strict Answerability Criterion": "Overly Strict Interpretation",
  "Conflating Relevance with Full Answerability": "Overly Strict Interpretation",
  "Formatting issue": "Formatting issue",
  "Failure to Award Marginal Relevance": "Overly Strict Relevance Threshold",
  "Confusing Negative Verification with Relevance": "Over-crediting tangential relevance",
  "Score Misalignment": "Score Misalignment",
  "Confused Topical Relevance with Complete Answerability": "Overly Strict Interpretation",
  "Failure to credit minimal relevance": "Overly Strict Relevance Threshold",
  "Score Calibration": "Score Calibration",
  "Strict all-or-nothing standard": "Overly Strict Relevance Threshold",
  "Excessive Strictness Regarding Query Ambiguity": "Overly Strict Interpretation",
  "Failure to Recognize Domain Identifier": "Failure to Recognize Domain Identifier",
  "Score mismatch with reasoning": "Score mismatch with reasoning",
  "Misunderstood Disjunctive Requirement": "Ignored Nuance",
  "Overlooked Topical Relevance": "Overly Strict Relevance Threshold",
  "Conflating Answerability with Relevance": "Overly Strict Interpretation",
  "Strict Lexical Mismatch": "Superficial Keyword Matching",
  "Overly Harsh Evaluation": "Overly Strict Relevance Threshold",
  "Over-complicating evaluation criteria": "Overly Strict Interpretation",
  "Strict All-or-Nothing Evaluation": "Overly Strict Relevance Threshold",
  "Rubric Misapplication": "Rubric Misapplication",
  "Over-penalizing missing keywords": "Over-weighted keyword match",
  "Dataset Artifact Misinterpretation": "Dataset Artifact Misinterpretation",
  "Over-scoring / Scale Miscalibration": "Over-scoring / Scale Miscalibration",
  "Meta-reasoning Confusion": "Meta-reasoning Confusion",
  "Overthinking negative evidence": "Overly Strict Interpretation",
  "Ignored Implicit Evidence": "Ignored Nuance",
  "Lexical mismatch on query identifier": "Lexical mismatch on query identifier",
  "Strict Answerability Threshold": "Overly Strict Relevance Threshold",
  "Over-reliance on literal keyword matching": "Superficial Keyword Matching",
  "Over-penalizing Partial Relevance": "Overly Strict Relevance Threshold",
  "Over-stringent Evaluation": "Overly Strict Relevance Threshold",
  "Failure to Resolve Identifier": "Failure to Resolve Identifier",
  "Strict Completeness Requirement": "Hallucinated Requirement",
  "Over-penalization of missing details": "Hallucinated Requirement",
  "Overly Strict Scoring": "Overly Strict Relevance Threshold",
  "False Positive on Non-Semantic Query": "False Positive on Non-Semantic Query",
  "Failure to Handle Non-Semantic/ID Query": "Failure to Handle Non-Semantic/ID Query",
  "Failure to Resolve Identifier Query": "Failure to Resolve Identifier Query",
  "Overthinking Evaluation Criteria": "Overthinking Evaluation Criteria",
  "Under-scoring Marginal Relevance": "Overly Strict Relevance Threshold",
  "Over-penalized marginal relevance": "Overly Strict Relevance Threshold",
  "Score Mapping Inconsistency": "Score Mapping Inconsistency",
  "Hypercritical Query Ambiguity": "Overly Strict Interpretation",
  "Over-penalizing incomplete information": "Overly Strict Relevance Threshold",
  "Overly harsh scoring calibration": "Overly Strict Relevance Threshold",
  "Unwarranted Assumption and Score Contradiction": "Missing Reasoning",
  "Overly Strict Threshold / Ignored Marginal Relevance": "Overly Strict Relevance Threshold",
  "Conflating Relevance with Exact Answerability": "Overly Strict Interpretation",
  "Failure to Recognize Identifier": "Failure to Recognize Identifier",
  "Failed to Recognize Identifier Query": "Failed to Recognize Identifier Query",
  "Equated Negative Answer with Irrelevance": "Ignored Nuance",
  "Demanded Excessive Detail": "Hallucinated Requirement",
  "Over-penalized lack of explicit terms": "Over-weighted keyword match",
  "Flawed Meta-Logic": "Missing Reasoning",
  "Literal Keyword Mismatch": "Superficial Keyword Matching",
  "Over-strict Filtering on Ambiguous Query": "Overly Strict Interpretation",
  "Misinterpreting Task Objective": "Misinterpreting Task Objective",
  "Scoring Scale Error": "Scoring Scale Error",
  "Failure to Recognize Complete Irrelevance": "Over-crediting tangential relevance",
  "Malformed Query Misinterpretation": "Malformed Query Misinterpretation",
  "Failed Coreference Resolution": "Ignored Nuance",
  "Overthinking Ambiguity": "Overly Strict Interpretation",
  "Overly Strict Completeness Criteria": "Hallucinated Requirement",
  "Discounting topical relevance": "Overly Strict Relevance Threshold",
  "Over-penalizing brevity": "Hallucinated Requirement",
  "Under-weighting partial relevance": "Overly Strict Relevance Threshold",
  "Overly Strict Information Need": "Overly Strict Interpretation",
  "Failure to Recognize Identifier Context": "Failure to Recognize Identifier Context",
  "Over-strict lexical matching": "Overly Strict Interpretation",
  "Convoluted Meta-Reasoning": "Convoluted Meta-Reasoning",
  "Disregard of Partial Relevance": "Overly Strict Relevance Threshold",
  "Threshold Calibration": "Overly Strict Relevance Threshold",
  "Dismissing minimal topical relevance": "Overly Strict Relevance Threshold",
  "Overly strict grading criteria": "Overly Strict Relevance Threshold",
  "Spurious Numerical Match": "Superficial Keyword Matching",
  "Evaluated Answerability Instead of Relevance": "Hallucinated Requirement",
  "Misapplication of Rating Scale": "Misapplication of Rating Scale",
  "Unwarranted Partial Credit": "Over-crediting tangential relevance",
  "Score-Reasoning Contradiction": "Missing Reasoning",
  "Overestimated Relevance": "Over-crediting tangential relevance",
  "Overly Strict Grading Threshold": "Overly Strict Relevance Threshold",
  "Overly strict scoring": "Overly Strict Relevance Threshold",
  "Mishandling of Identifier Query": "Mishandling of Identifier Query",
  "Conflating answerability with topical relevance": "Hallucinated Requirement",
  "Misunderstood Query Intent": "Ignored Nuance",
  "Ignored Topical/Partial Relevance": "Overly Strict Relevance Threshold",
  "Score Mapping Mismatch": "Score Mapping Mismatch",
  "Lexical Overlap Bias": "Superficial Keyword Matching",
  "Spurious Relevance / Hallucinated Connection": "Superficial Keyword Matching",
  "Demanded excessive specificity": "Overly Strict Interpretation",
  "Reasoning-Score Mismatch": "Missing Reasoning",
  "Overlooked Information": "Ignored Nuance",
  "Perceived Ambiguity": "Perceived Ambiguity",
  "Ignoring Marginal Relevance": "Overly Strict Relevance Threshold",
  "Identifier Resolution Failure": "Identifier Resolution Failure",
  "Literal Interpretation of Query Identifier": "Literal Interpretation of Query Identifier",
  "Over-weighted Keyword Matching": "Over-weighted keyword match",
  "Overly Rigid Interpretation": "Overly Strict Interpretation",
  "Dismissed Marginal Relevance": "Overly Strict Relevance Threshold",
  "Failure to credit partial relevance": "Overly Strict Relevance Threshold",
  "Overly Strict Answerability Requirement": "Hallucinated Requirement",
  "Spurious Relevance Assignment": "Over-crediting tangential relevance",
  "Strict Grading / Failure to Award Partial Relevance": "Overly Strict Relevance Threshold",
  "Failure to Recognize ID-based Match": "Failure to Recognize ID-based Match",
  "Failure to Map Query ID / Dataset Artifact": "Failure to Map Query ID / Dataset Artifact",
  "Score Discrepancy / Scale Confusion": "Score Discrepancy / Scale Confusion",
  "Dismissal of marginal relevance": "Overly Strict Relevance Threshold",
  "Evaluation Criterion Mismatch": "Evaluation Criterion Mismatch",
  "Misinterpreting Query Intent": "Ignored Nuance",
  "Hallucinated Query Intent": "Hallucinated Requirement",
  "Overly strict relevance criteria": "Overly Strict Relevance Threshold",
  "Ignored Query": "Ignored Query",
  "Dismissed Relevant Entity": "Ignored Nuance",
  "Overly strict threshold for marginal relevance": "Overly Strict Relevance Threshold",
  "Spurious Token Matching": "Superficial Keyword Matching",
  "Over-reliance on Exact Keywords": "Superficial Keyword Matching",
  "Conflating completeness with relevance": "Hallucinated Requirement",
  "Failure to award partial credit": "Overly Strict Relevance Threshold",
  "Contradictory Score Output": "Contradictory Score Output",
  "Missing Reasoning / Generation Failure": "Missing Reasoning",
  "Over-penalized Missing Keyword": "Overly Strict Interpretation",
  "Overly Strict Keyword Matching": "Overly Strict Interpretation",
  "Spurious Match / Hallucinated Relevance": "Spurious Match / Hallucinated Relevance",
  "Overly strict lexical matching": "Overly Strict Interpretation",
  "Over-penalization of Implicit Information": "Overly Strict Interpretation",
  "Threshold Miscalibration": "Overly Strict Relevance Threshold",
  "Confused Answerability with Topical Relevance": "Hallucinated Requirement",
  "Excessive Strictness on Ambiguity": "Overly Strict Interpretation",
  "Over-weighted missing details": "Overly Strict Interpretation",
  "Strict Relevance Threshold": "Overly Strict Relevance Threshold",
  "Failure to distinguish minimal relevance from irrelevance": "Overly Strict Relevance Threshold",
  "Over-scoring Relevance": "Over-crediting tangential relevance",
  "Mishandling Malformed/ID Query": "Mishandling Malformed/ID Query",
  "Reasoning-to-Score Inconsistency": "Reasoning-to-Score Inconsistency",
  "Failure to Credit Partial Relevance": "Overly Strict Relevance Threshold",
  "Rating Scale Confusion": "Rating Scale Confusion",
  "Reasoning-Output Inconsistency": "Reasoning-Output Inconsistency",
  "Under-scoring Partial Relevance": "Overly Strict Relevance Threshold",
  "Failure to credit background relevance": "Overly Strict Relevance Threshold",
  "Reasoning-Output Disconnect": "Reasoning-Output Disconnect",
  "Overly Strict Interpretation of Numerical Query": "Overly Strict Interpretation",
  "Over-penalized Keyword Mismatch": "Overly Strict Interpretation",
  "Over-penalization of Partial Relevance": "Overly Strict Relevance Threshold",
  "Failure to handle identifier query": "Failure to handle identifier query",
  "Grading Criteria Confusion": "Grading Criteria Confusion",
  "Score-reasoning misalignment": "Score-reasoning misalignment",
  "Overly Strict Answerability Criteria": "Hallucinated Requirement",
  "Factual Contradiction": "Ignored Nuance",
  "Unresolved Query Identifier Failure": "Unresolved Query Identifier Failure",
  "Over-weighted Ambiguity": "Overly Strict Interpretation",
  "Hallucinated Entity Match": "Superficial Keyword Matching",
  "Overly Strict Evaluation Threshold": "Overly Strict Relevance Threshold",
  "Failure to recognize document ID query": "Failure to recognize document ID query",
  "Failed Domain Inference": "Ignored Nuance",
  "Ignored Query Aspect": "Ignored Nuance",
  "Hallucinated Semantic Connection": "Over-crediting tangential relevance",
  "Rating Scale Violation": "Rating Scale Violation",
  "Misunderstood Relevance Criteria": "Misunderstood Relevance Criteria",
  "Lexical Mismatch Bias": "Overly Strict Interpretation",
  "Over-strict matching criteria": "Overly Strict Interpretation",
  "False Positive on Irrelevant/Ambiguous Query": "Over-weighted topical overlap",
  "Overly Strict Filtering": "Overly Strict Relevance Threshold",
  "Hallucinated Criteria": "Hallucinated Requirement",
  "Strict Binary Judgment": "Overly Strict Relevance Threshold",
  "Overthinking Meta-Question": "Overthinking Meta-Question",
  "Hallucinated Relevance": "Over-crediting tangential relevance",
  "Misunderstood Scoring Scale": "Misunderstood Scoring Scale",
  "Strictness threshold too high": "Overly Strict Relevance Threshold",
  "Spurious Match": "Superficial Keyword Matching",
  "Over-strict evaluation criteria": "Overly Strict Interpretation",
  "Conflating Relevance with Sufficiency": "Conflating Relevance with Sufficiency",
  "Failure to recognize ID/code query": "Failure to recognize ID/code query",
  "Overly Strict Standard for Relevance": "Overly Strict Relevance Threshold",
  "Score Calibration Discrepancy": "Score Calibration Discrepancy",
  "Dismissing Partial Relevance": "Overly Strict Relevance Threshold",
  "Over-crediting Tangential Information": "Over-crediting tangential relevance",
  "Failure to Handle Opaque Query": "Failure to Handle Opaque Query",
  "Over-penalizing Temporal Mismatch": "Overly Strict Interpretation",
  "Hallucinated match": "Hallucinated match",
  "Score Discrepancy": "Score Discrepancy",
  "Failed to Recognize Partial Relevance": "Overly Strict Relevance Threshold",
  "Overly strict scoring threshold": "Overly Strict Relevance Threshold",
  "Scale Range Violation": "Scale Range Violation",
  "Over-penalizing missing detail": "Overly Strict Interpretation",
  "Overthinking and Output Inconsistency": "Overthinking and Output Inconsistency",
  "Equating Negative Answer with Irrelevance": "Ignored Nuance",
  "Binary / All-or-Nothing Evaluation": "Overly Strict Relevance Threshold",
  "Reasoning-Score Contradiction": "Reasoning-Score Contradiction",
  "Undervalued Partial Information": "Overly Strict Relevance Threshold",
  "Conflating Negative Answer with Relevance": "Ignored Nuance",
  "Failure to Handle Query Artifact": "Failure to Handle Query Artifact",
  "Confusing Relevance with Answerability": "Overly Strict Interpretation",
  "Failure to Apply Domain Inference": "Ignored Nuance",
  "Misunderstood Identifier Query": "Misunderstood Identifier Query",
  "Excessive Strictness / Overly Rigid Criteria": "Overly Strict Interpretation",
  "Overly Strict Lexical Matching": "Overly Strict Interpretation",
  "Overthinking Task Meta-Structure": "Overthinking Task Meta-Structure",
  "Miscalibrated Scoring Threshold": "Overly Strict Relevance Threshold",
  "Overly strict literal matching": "Overly Strict Interpretation",
  "Failure to Recognize Negative Answer Validity": "Ignored Nuance",
  "Conflating Negative Answer with Low Relevance": "Ignored Nuance",
  "Over-penalized incomplete information": "Overly Strict Interpretation",
  "Treating absence of information as relevance": "Treating absence of information as relevance",
  "Conflating Incompleteness with Irrelevance": "Overly Strict Relevance Threshold",
  "Over-penalization of ambiguity": "Overly Strict Interpretation",
  "Ignoring partial relevance": "Overly Strict Relevance Threshold",
  "Score/Reasoning Inconsistency": "Score/Reasoning Inconsistency",
  "Failure on Identifier-based Query": "Failure on Identifier-based Query",
  "Ignored partial relevance": "Overly Strict Relevance Threshold",
  "Over-strict threshold for minimal relevance": "Overly Strict Relevance Threshold",
  "Demanding Exhaustive Detail": "Hallucinated Requirement",
  "Spurious numeric match": "Superficial Keyword Matching",
  "Ignored Indirect Relevance": "Ignored Nuance",
  "Failure to reward marginal relevance": "Overly Strict Relevance Threshold",
  "Over-weighted Direct Answerability": "Overly Strict Interpretation",
  "Overly strict standard": "Overly Strict Relevance Threshold",
  "Scale Range Mismatch": "Scale Range Mismatch",
  "Overlooked Marginal Relevance": "Overly Strict Relevance Threshold",
  "Overthinking / Meta-reasoning Trap": "Overthinking / Meta-reasoning Trap",
  "Over-penalized Incompleteness": "Overly Strict Interpretation",
  "Conflating Topical Relevance with Complete Answerability": "Overly Strict Interpretation",
  "Rubric Misinterpretation": "Rubric Misinterpretation",
  "Failed Identifier Recognition": "Failed Identifier Recognition",
  "Spurious Substring Matching": "Superficial Keyword Matching",
  "Spurious Numerical Association": "Superficial Keyword Matching",
  "Over-penalization for incompleteness": "Overly Strict Relevance Threshold",
  "Assumed Relevance for Unmatched Query": "Over-crediting tangential relevance",
  "Demanded Explicit Detail": "Hallucinated Requirement",
  "Over-penalized incompleteness": "Overly Strict Relevance Threshold",
  "Over-reliance on lexical/semantic overlap": "Superficial Keyword Matching",
  "Over-penalized Incomplete Answer": "Overly Strict Relevance Threshold",
  "Overly strict threshold": "Overly Strict Relevance Threshold",
  "Conflating Answer Completeness with Relevance": "Overly Strict Interpretation",
  "Hallucinated Task": "Hallucinated Requirement",
  "Failure to Infer Contextual Referent": "Ignored Nuance",
  "Reasoning-Verdict Inconsistency": "Reasoning-Verdict Inconsistency",
  "Overly Strict Calibration": "Overly Strict Relevance Threshold",
  "Failure to Recognize Topical/Partial Relevance": "Overly Strict Relevance Threshold",
  "Failure to Recognize Domain-Specific Identifier": "Failure to Recognize Domain-Specific Identifier",
  "Over-penalized ambiguity": "Overly Strict Interpretation",
  "Over-penalized lack of semantic overlap": "Superficial Keyword Matching",
  "Failure to Resolve Query ID": "Failure to Resolve Query ID",
  "Ignored Partial Relevance": "Overly Strict Relevance Threshold",
  "Over-penalizing Topical Relevance": "Overly Strict Relevance Threshold",
  "Scale Violation": "Scale Violation",
  "Over-strict interpretation": "Overly Strict Interpretation",
  "Equating Absence of Information with Relevance": "Over-crediting tangential relevance",
  "Over-strict Explicit Evidence Requirement": "Hallucinated Requirement",
  "Overly Stringent Evaluation": "Overly Strict Relevance Threshold",
  "Conflating answerability with relevance": "Overly Strict Interpretation",
  "Entity Resolution Failure": "Entity Resolution Failure",
  "Confused Topical Relevance with Direct Answerability": "Overly Strict Interpretation",
  "Strict Answerability Filtering": "Overly Strict Relevance Threshold",
  "Over-penalizing missing aspects": "Over-weighted specific aspect",
  "Demanded Explicit Mention": "Hallucinated Requirement",
  "Binary Thinking": "Overly Strict Relevance Threshold",
  "Over-penalized partial relevance": "Overly Strict Relevance Threshold",
  "Strict all-or-nothing scoring": "Overly Strict Relevance Threshold",
  "Flawed Logic on Answerability": "Overly Strict Interpretation",
  "Score-Reasoning Inconsistency": "Score-Reasoning Inconsistency",
  "Hallucinated Evaluation Task": "Hallucinated Requirement",
  "Under-crediting Partial Information": "Overly Strict Relevance Threshold",
  "Empty Reasoning / Generation Failure": "Missing Reasoning",
  "Overly Strict Answerability": "Overly Strict Relevance Threshold",
  "Scale Boundary Error": "Scale Boundary Error",
  "Under-weighting topical relevance": "Overly Strict Relevance Threshold",
  "Failure to Recognize Identifier Query": "Failure to Recognize Identifier Query",
  "Score-Reasoning Discrepancy": "Score-Reasoning Discrepancy",
  "Failed Identifier Resolution": "Failed Identifier Resolution",
  "Overly Stringent Criteria": "Overly Strict Relevance Threshold",
  "Unrecognized Numeric Identifier": "Unrecognized Numeric Identifier",
  "Failed Entity Resolution": "Failed Entity Resolution",
  "Failed to recognize partial relevance": "Overly Strict Relevance Threshold",
  "Misinterpreted Evaluation Criteria": "Hallucinated Requirement",
  "Strict Lexical Matching on Opaque Query": "Strict Lexical Matching on Opaque Query",
  "Over-weighted lexical match": "Over-weighted keyword match",
  "Reasoning-Verdict Mismatch": "Reasoning-Verdict Mismatch",
  "Conflating Relevance with Completeness": "Overly Strict Interpretation",
  "Lexical Matching Bias": "Over-weighted keyword match",
  "Hallucinated Task/Query": "Hallucinated Requirement",
  "Keyword matching bias": "Over-weighted keyword match",
  "Failure to Resolve Benchmark Query ID": "Failure to Resolve Benchmark Query ID",
  "Score Calibration / Scale Mapping Error": "Score Calibration / Scale Mapping Error",
  "Negative Answer Fallacy": "Negative Answer Fallacy",
  "Overly strict evaluation threshold": "Overly Strict Relevance Threshold",
  "Overly Harsh Evaluation Criteria": "Overly Strict Interpretation",
  "Score and Reasoning Mismatch": "Score and Reasoning Mismatch",
  "Strict lexical matching bias": "Superficial Keyword Matching",
  "Overly Strict Relevance Criterion": "Overly Strict Interpretation",
  "Strict Answerability Assessment": "Overly Strict Interpretation",
  "Failure to resolve query ID": "Failure to resolve query ID",
  "Over-generous Relevance Assessment": "Over-crediting tangential relevance",
  "Score Mapping Discrepancy": "Score Mapping Discrepancy",
  "Misinterpreted Task Objective": "Misinterpreted Task Objective",
  "Literal Query Matching on Query ID": "Literal Query Matching on Query ID",
  "Over-inferred Relevance": "Over-crediting tangential relevance",
  "Equated Unanswerability with Zero Relevance": "Overly Strict Relevance Threshold",
  "Literal String Matching": "Superficial Keyword Matching",
  "Overly strict evaluation criterion": "Overly Strict Interpretation",
  "Treated Absence of Information as an Answer": "Treated Absence of Information as an Answer",
  "Failure to Handle Malformed Query": "Failure to Handle Malformed Query",
  "Strictness on marginal relevance": "Overly Strict Relevance Threshold",
  "Overly Strict Threshold for Minimal Relevance": "Overly Strict Relevance Threshold",
  "Flawed Relevance Logic": "Flawed Relevance Logic",
  "Failure to Recognize ID/Entity Lookup": "Failure to Recognize ID/Entity Lookup",
  "Failure to Resolve Query Identifier": "Failure to Resolve Query Identifier",
  "Failure to Credit Marginal Relevance": "Overly Strict Relevance Threshold",
  "Confused Relevance with Completeness": "Overly Strict Interpretation",
  "Failure to Recognize Minimal Relevance": "Overly Strict Relevance Threshold",
  "Over-penalization of Missing Details": "Overly Strict Interpretation",
  "Excessive penalty for incompleteness": "Overly Strict Interpretation",
  "Strict Binary Interpretation": "Overly Strict Relevance Threshold",
  "Failure to Handle Unexpanded Query ID": "Failure to Handle Unexpanded Query ID",
  "Hallucinated Task Context": "Hallucinated Requirement",
  "Ignored Identifier Lookup Context": "Ignored Identifier Lookup Context",
  "Conflating Partial Relevance with Irrelevance": "Overly Strict Relevance Threshold",
  "Missed Relevant Information": "Missed Relevant Information",
  "Failure to Recognize Query ID Artifact": "Failure to Recognize Query ID Artifact",
  "Over-penalizing topical relevance": "Overly Strict Interpretation",
  "Over-reliance on Lexical Matching": "Superficial Keyword Matching",
  "Overly Strict Specificity Standard": "Overly Strict Interpretation",
  "Confusing Incompleteness with Irrelevance": "Overly Strict Interpretation",
  "Flawed Meta-Reasoning": "Flawed Meta-Reasoning",
  "Ignored Topical Overlap": "Ignored Topical Overlap"
}
```
