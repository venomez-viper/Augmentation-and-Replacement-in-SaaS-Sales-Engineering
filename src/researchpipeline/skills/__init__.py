"""Dynamic skills library for ResearchPipeline.

Provides a registry of reusable research/engineering/writing skills
that can be automatically matched to pipeline stages and injected
into LLM prompts.
"""

from researchpipeline.skills.schema import Skill
from researchpipeline.skills.registry import SkillRegistry

__all__ = ["Skill", "SkillRegistry"]
