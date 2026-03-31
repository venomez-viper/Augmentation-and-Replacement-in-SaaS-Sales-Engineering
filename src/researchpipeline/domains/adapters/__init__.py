"""Domain-specific prompt adapters.

Each adapter customizes prompt blocks for a specific research domain
while the ML adapter preserves existing behavior unchanged.
"""

from researchpipeline.domains.adapters.ml import MLPromptAdapter
from researchpipeline.domains.adapters.generic import GenericPromptAdapter
from researchpipeline.domains.adapters.physics import PhysicsPromptAdapter
from researchpipeline.domains.adapters.economics import EconomicsPromptAdapter
from researchpipeline.domains.adapters.biology import BiologyPromptAdapter
from researchpipeline.domains.adapters.chemistry import ChemistryPromptAdapter
from researchpipeline.domains.adapters.neuroscience import NeurosciencePromptAdapter
from researchpipeline.domains.adapters.robotics import RoboticsPromptAdapter

__all__ = [
    "MLPromptAdapter",
    "GenericPromptAdapter",
    "PhysicsPromptAdapter",
    "EconomicsPromptAdapter",
    "BiologyPromptAdapter",
    "ChemistryPromptAdapter",
    "NeurosciencePromptAdapter",
    "RoboticsPromptAdapter",
]
