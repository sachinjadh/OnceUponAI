from story_generator.template_generator import generate_story


def main():
    print("Running smoke test for template generator...")
    s = generate_story(prompt="A tiny hero", seed=42)
    print("Generated story:\n")
    print(s)


if __name__ == "__main__":
    main()
