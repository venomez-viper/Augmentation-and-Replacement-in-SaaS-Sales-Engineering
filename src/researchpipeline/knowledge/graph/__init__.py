"""Research knowledge graph built on NetworkX.

Extracts entities (Papers, Methods, Datasets, Metrics) and relations
(CITES, EXTENDS, OUTPERFORMS) from literature and experiment results,
enabling research gap discovery and trend analysis.
"""

from researchpipeline.knowledge.graph.entities import Entity, EntityType
from researchpipeline.knowledge.graph.relations import Relation, RelationType
from researchpipeline.knowledge.graph.builder import KnowledgeGraphBuilder
from researchpipeline.knowledge.graph.query import KnowledgeGraphQuery

__all__ = [
    "Entity",
    "EntityType",
    "Relation",
    "RelationType",
    "KnowledgeGraphBuilder",
    "KnowledgeGraphQuery",
]
