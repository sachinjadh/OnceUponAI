"OnceUponAI" Story Generation App

This small project demonstrates a zero-cost template-based story generator: no external models, fast and offline.

Files
- story_generator/
  - template_generator.py  # deterministic, zero-cost generator
- app.py                   # Streamlit UI
- smoke_test.py            # quick script to run the template generator
- requirements.txt         # optional dependencies for LLM and Streamlit

Quick run (template-only)

1. Python 3.8+ recommended.
2. Run the smoke test:

python3 smoke_test.py


Running options

- Template-only quick run (no external deps):

  python3 smoke_test.py

- Streamlit UI (template-only):

  pip install -r requirements.txt
  streamlit run app.py

New features

- Voice-friendly mode: check "Voice-friendly" in the UI to show the story as a sequence of very short lines — great for reading aloud or for text-to-speech.
- Small illustrations: animal emoji (🦁🐘🦍🐷🐵) are shown beside the animal name to make the story more engaging for toddlers.
- Simple vocabulary: choose the "simple" vocabulary level to get shorter, simpler words suitable for younger toddlers (1–2 years).

Tips to improve story quality:

- Prompt engineering: Provide a short context and a desired tone (e.g., "A whimsical bedtime story about an unlikely friendship, warm tone").
- Use the template generator for deterministic output; vary the random seed to get different stories.

Next steps (optional):

- Add caching of generated stories to avoid re-generating the same prompt repeatedly.
- Add more template variations, scenes, and small Markov-chain style continuation to increase variety while remaining zero-cost.
