from datetime import datetime, timezone
from types import SimpleNamespace

from src.ingestion.rss_ingest import RSSIngestService


class DummyMetrics:
    def record_histogram(self, *args, **kwargs):
        pass

    def increment_counter(self, *args, **kwargs):
        pass


class DummyEvents:
    async def log_event(self, *args, **kwargs):
        pass


def _service() -> RSSIngestService:
    return RSSIngestService(DummyMetrics(), DummyEvents())


def test_episode_id_is_deterministic_for_same_inputs():
    service = _service()
    publish_date = datetime(2025, 1, 1, tzinfo=timezone.utc)

    first = service._build_episode_id("GUID-1", "https://cdn/a.mp3", "Title", publish_date)
    second = service._build_episode_id("guid-1", " https://cdn/a.mp3 ", "title", publish_date)

    assert first == second


def test_extract_episode_uses_fallback_guid_for_missing_guid():
    service = _service()
    entry = {
        "title": "No Guid Episode",
        "link": "https://example.com/episodes/1",
        "published": "Tue, 19 Nov 2024 10:00:00 GMT",
        "enclosures": [{"href": "https://cdn.example.com/1.mp3"}],
    }

    episode = service._extract_episode_metadata(entry)

    assert episode is not None
    assert len(episode.guid) == 64
    assert len(episode.episode_id) == 64


def test_feed_metadata_deduplicates_and_orders_episodes():
    service = _service()
    older = {
        "id": "dup-guid",
        "title": "Duplicate Episode",
        "enclosures": [{"href": "https://cdn.example.com/dup.mp3"}],
        "published_parsed": (2024, 1, 1, 0, 0, 0, 0, 0, 0),
    }
    newer = {
        "id": "dup-guid",
        "title": "Duplicate Episode",
        "enclosures": [{"href": "https://cdn.example.com/dup.mp3"}],
        "published_parsed": (2024, 1, 2, 0, 0, 0, 0, 0, 0),
    }
    unique = {
        "id": "unique-guid",
        "title": "Unique Episode",
        "enclosures": [{"href": "https://cdn.example.com/unique.mp3"}],
        "published_parsed": (2024, 1, 3, 0, 0, 0, 0, 0, 0),
    }

    parsed_feed = SimpleNamespace(
        feed={"title": "Show", "description": "Desc", "author": "Author"},
        entries=[older, newer, unique],
    )

    metadata = service._extract_feed_metadata(parsed_feed, "https://example.com/feed.xml")

    assert len(metadata.episodes) == 2
    assert metadata.episodes[0].guid == "unique-guid"
    assert metadata.episodes[1].publish_date == datetime(2024, 1, 2, tzinfo=timezone.utc)
