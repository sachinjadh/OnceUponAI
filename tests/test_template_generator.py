from story_generator.template_generator import generate_story


def test_generate_story_returns_string():
    s = generate_story(prompt="test", seed=1)
    assert isinstance(s, str)
    assert len(s) > 0
