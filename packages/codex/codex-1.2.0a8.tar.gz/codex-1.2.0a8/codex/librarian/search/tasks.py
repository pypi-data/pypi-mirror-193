"""Libarian Tasks for searchd."""
from dataclasses import dataclass


@dataclass
class SearchIndexerTask:
    """Tasks for the search indexer."""

    pass


@dataclass
class SearchIndexRebuildIfDBChangedTask(SearchIndexerTask):
    """Task to check if the db is changed and schedule an update task."""

    pass


@dataclass
class SearchIndexUpdateTask(SearchIndexerTask):
    """Update the search index."""

    rebuild: bool


@dataclass
class SearchIndexOptimizeTask(SearchIndexerTask):
    """Optimize a fragmented index."""

    force: bool = False
