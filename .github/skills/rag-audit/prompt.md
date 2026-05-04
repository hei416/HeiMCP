You are auditing a RAG pipeline output for hallucination risk using the HeiMCP toolkit.

You have access to:
- `skill_rag_faithfulness_check` — heuristic faithfulness checker

## Your Task

### Step 1 — Run Faithfulness Check
Call `skill_rag_faithfulness_check` with:
- `query`: {{query}}
- `retrieved_context`: {{retrieved_context}}
- `generated_answer`: {{generated_answer}}

### Step 2 — Interpret and Report

Present findings as:

```
## RAG Faithfulness Audit

### 📊 Grounding Score
[Summary of how many claims are grounded vs. ungrounded]

### ❌ Hallucination Risk
[List any claims flagged as possibly hallucinated]

### ⚠️ Weak Grounding
[List any claims only partially supported by context]

### 💡 Recommendation
[Should this answer be shown to the user as-is, revised, or regenerated?]
[Specific suggestion: re-retrieve with broader query / ask LLM to cite sources / etc.]
```
