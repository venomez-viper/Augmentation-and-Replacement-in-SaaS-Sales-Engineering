"""Interactive Co-Pilot mode for human-AI research collaboration."""

from researchpipeline.copilot.modes import ResearchMode
from researchpipeline.copilot.controller import CoPilotController
from researchpipeline.copilot.feedback import FeedbackHandler
from researchpipeline.copilot.branching import BranchManager

__all__ = [
    "BranchManager",
    "CoPilotController",
    "FeedbackHandler",
    "ResearchMode",
]
