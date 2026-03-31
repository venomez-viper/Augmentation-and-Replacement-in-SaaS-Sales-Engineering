"""Agent collaboration and knowledge sharing system.

Enables multiple ResearchPipeline instances to share research artifacts
(literature summaries, experiment results, code templates, review feedback)
through a file-system-based shared repository.
"""

from researchpipeline.collaboration.repository import ResearchRepository
from researchpipeline.collaboration.publisher import ArtifactPublisher
from researchpipeline.collaboration.subscriber import ArtifactSubscriber
from researchpipeline.collaboration.dedup import deduplicate_artifacts

__all__ = [
    "ResearchRepository",
    "ArtifactPublisher",
    "ArtifactSubscriber",
    "deduplicate_artifacts",
]
