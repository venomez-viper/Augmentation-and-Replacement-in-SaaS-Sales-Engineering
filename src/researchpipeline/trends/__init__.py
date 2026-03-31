"""Research trend tracking and automatic topic generation."""

from researchpipeline.trends.daily_digest import DailyDigest
from researchpipeline.trends.trend_analyzer import TrendAnalyzer
from researchpipeline.trends.opportunity_finder import OpportunityFinder
from researchpipeline.trends.auto_topic import AutoTopicGenerator
from researchpipeline.trends.feeds import FeedManager

__all__ = [
    "AutoTopicGenerator",
    "DailyDigest",
    "FeedManager",
    "OpportunityFinder",
    "TrendAnalyzer",
]
