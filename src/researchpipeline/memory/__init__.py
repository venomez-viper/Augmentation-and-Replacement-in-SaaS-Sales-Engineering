"""Persistent evolutionary memory system for ResearchPipeline.

Provides three categories of memory:
- **Ideation**: Research topics, hypotheses, and their outcomes.
- **Experiment**: Hyperparameters, architectures, and training tricks.
- **Writing**: Review feedback, paper structure patterns.

Each category supports semantic retrieval via embeddings, time-decay
weighting, and confidence scoring.
"""

from researchpipeline.memory.store import MemoryEntry, MemoryStore
from researchpipeline.memory.retriever import MemoryRetriever
from researchpipeline.memory.decay import time_decay_weight, confidence_update

__all__ = [
    "MemoryEntry",
    "MemoryStore",
    "MemoryRetriever",
    "time_decay_weight",
    "confidence_update",
]
