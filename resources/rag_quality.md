# RAG Faithfulness & Quality Standards

## Quality Dimensions

| Dimension | Question to Ask |
|---|---|
| **Faithfulness** | Does the answer only contain claims supported by retrieved context? |
| **Relevance** | Does the answer address the original query? |
| **Completeness** | Does the answer cover all key points available in context? |

## Hallucination Signals

- Specific numbers or dates **not present** in context
- Named entities **not mentioned** in context
- Causal claims not supported by context
- Confident assertions on topics absent from context

## Mitigation Strategies

1. Re-rank retrieved chunks by semantic similarity before generation
2. Ask the LLM to **cite specific passages** from context
3. Use an NLI cross-encoder for post-generation faithfulness scoring
4. Reduce temperature for factual / knowledge-retrieval queries
5. Use `[HALLUCINATED]` labelling in the prompt to surface issues explicitly

## Grounding Ratio Heuristic

A lightweight pre-filter before expensive NLI calls:
- **≥ 70% key terms** in context → likely grounded
- **40–70%** → weakly grounded, flag for review
- **< 40%** → hallucination risk, re-retrieve or reject
