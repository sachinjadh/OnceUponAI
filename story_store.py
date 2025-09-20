import json
import os
from typing import List, Dict, Optional

_STORIES_PATH = os.path.join(os.path.dirname(__file__), "stories.json")


def load_stories() -> List[Dict]:
    if not os.path.exists(_STORIES_PATH):
        return []
    with open(_STORIES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def random_story(stories: List[Dict]) -> Optional[Dict]:
    import random

    if not stories:
        return None
    return random.choice(stories)


def filter_stories(stories: List[Dict], animal: Optional[str] = None, lesson_contains: Optional[str] = None) -> List[Dict]:
    out = stories
    if animal:
        out = [s for s in out if animal.lower() in s.get("animal", "").lower()]
    if lesson_contains:
        out = [s for s in out if lesson_contains.lower() in s.get("lesson", "").lower()]
    return out
