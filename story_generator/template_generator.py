import random
from typing import Optional

# Try to import LLM generator - gracefully handle if dependencies missing
try:
    from .llm_generator import LLMGenerator
    LLM_AVAILABLE = True
except (ImportError, RuntimeError) as e:
    LLMGenerator = None
    LLM_AVAILABLE = False

CHARACTERS = [
    "Lion",
    "Elephant",
    "Gorilla",
    "Pig",
    "Monkey",
    "Bear",
    "Rabbit",
    "Duck",
    "Fox",
    "Turtle",
    "Cat",
    "Dog",
    "Panda",
    "Penguin",
    "Owl",
    "Frog",
    "Koala",
    "Zebra",
    "Giraffe",
    "Hippo",
    "Sheep",
    "Cow",
    "Horse",
    "Tiger",
    "Deer",
]

# Small emoji map to show alongside animals
EMOJI = {
    "Lion": "🦁",
    "Elephant": "🐘",
    "Gorilla": "🦍",
    "Pig": "🐷",
    "Monkey": "🐵",
    "Bear": "🐻",
    "Rabbit": "🐰",
    "Duck": "🦆",
    "Fox": "🦊",
    "Turtle": "🐢",
    "Cat": "🐱",
    "Dog": "🐶",
    "Panda": "🐼",
    "Penguin": "🐧",
    "Owl": "🦉",
    "Frog": "🐸",
    "Koala": "🐨",
    "Zebra": "🦓",
    "Giraffe": "🦒",
    "Hippo": "🦛",
    "Sheep": "🐑",
    "Cow": "🐄",
    "Horse": "🐴",
    "Tiger": "🐅",
    "Deer": "🦌",
}

LOCATIONS = [
    "in a cozy tree house",
    "by the gentle river",
    "under a starlit sky",
    "near a warm little cave",
    "on a soft grassy hill",
]

# Fun greeting lines used as the first line of the story
GREETINGS = [
    "waves a little hello!",
    "sends a big sleepy hug!",
    "twirls and says hi!",
    "gives a gentle wave to everyone!",
    "hums a happy hello!",
]

# Personalized greeting templates when child's name is available
PERSONAL_GREETINGS = [
    "says hello to {name} with a tiny wave!",
    "gives {name} a big sleepy hug!",
    "twirls and says hi to {name}!",
    "hums a happy hello just for {name}!",
    "winks and waves at {name}!",
]

SMALL_ACTIONS = [
    "said goodnight",
    "snuggled with a soft blanket",
    "brushed their teeth",
    "turned off the bright light",
    "gave a gentle hug",
    "tucked a tiny friend in",
    "waved to the sleepy moon",
    "hummed a little song",
    "wiped the tiny paws clean",
    "counted twinkly stars",
]

TECH_LESSONS = [
    "They put the tablet to sleep and charged it gently.",
    "They turn the light off to save sleepy power.",
    "They used the night-light softly so eyes can rest.",
    "They listened to quiet music and then the screen went dark.",
    "They said 'thank you' to the little robot who helps charge toys.",
    "They put toys away so the tablet can rest.",
    "They close the app and hugged their toy instead.",
    "They ask a grown-up to help with the charger.",
    "They used the dimmer so the room is calm.",
    "They kept screens small and soft before sleep.",
]

LIFE_LESSONS = [
    "Sharing a toy makes everyone smile.",
    "Saying goodnight helps you rest well.",
    "Brushing teeth keeps little teeth strong.",
    "Helping a friend makes the heart happy.",
    "A warm hug makes a cozy night.",
    "Taking turns is fair and fun.",
    "Listening helps friends feel heard.",
    "Being gentle keeps everyone safe.",
    "Kind words make the world bright.",
]

# Personalized life lesson templates (use when child_name is provided)
PERSONAL_LIFE_LESSONS = [
    "{name} sharing a toy makes everyone smile.",
    "{name}, saying goodnight helps you rest well.",
    "{name} brushing teeth keeps little teeth strong.",
    "{name}, helping a friend makes the heart happy.",
    "A warm hug makes a cozy night for {name}.",
    "{name}, taking turns is fair and fun.",
    "{name}, listening helps friends feel heard.",
    "Being gentle keeps everyone safe, {name}.",
    "Kind words make the world bright, {name}.",
]


FUN_PARTS = [
    "They made a tiny dance with a twirl.",
    "A little giggle popped out like bubbles.",
    "They found a shiny pebble and counted it twice.",
    "A merry little tune played on a leaf.",
    "They made funny faces at the moon and it winked.",
    "They pretended the blanket was a magic cape.",
    "A sleepy yawn turned into a tiny smile.",
    "They blew a soft kiss to the stars.",
    "Someone whispered a silly riddle and everyone giggled.",
    "They clapped a tiny clap for being brave.",
]

# Map fun full sentences to a short action phrase used with the animal (verb phrase without leading subject)
FUN_ACTIONS = {
    "They made a tiny dance with a twirl.": "did a little dance",
    "A little giggle popped out like bubbles.": "giggled happily",
    "They found a shiny pebble and counted it twice.": "found a pebble",
    "A merry little tune played on a leaf.": "played a tiny tune",
    "They made funny faces at the moon and it winked.": "made funny faces",
    "They pretended the blanket was a magic cape.": "pretended the blanket was a cape",
    "A sleepy yawn turned into a tiny smile.": "yawned and smiled",
    "They blew a soft kiss to the stars.": "blew a kiss",
    "Someone whispered a silly riddle and everyone giggled.": "told a silly riddle and giggled",
    "They clapped a tiny clap for being brave.": "clapped for being brave",
}

# Final farewell appended to every story (default)
FAREWELL = "Goodnight — sweet dreams."


def _simple_word(s: str) -> str:
    """Map some words to simpler synonyms for younger toddlers."""
    replacements = {
        "cozy": "cozy",
        "gentle": "soft",
        "starlit": "starry",
        "little": "small",
        "soft": "soft",
        "said goodnight": "said night-night",
        "snuggled with a soft blanket": "snuggled with a blanket",
        "brushed their teeth": "brushed teeth",
        "turned off the bright light": "turned off the light",
        "gave a gentle hug": "gave a hug",
        "They put the tablet to sleep and charged it gently.": "They put the toy to sleep.",
        "They turn the light off to save sleepy power.": "They turned off the light.",
        "They used the night-light softly so eyes can rest.": "They used a night-light.",
        "They listened to quiet music and then the screen went dark.": "They listened to calm music.",
        "They said 'thank you' to the little robot who helps charge toys.": "They said thank you.",
        "They put toys away so the tablet can rest.": "They put toys away.",
        "They close the app and hugged their toy instead.": "They hugged their toy.",
        "They ask a grown-up to help with the charger.": "They asked for help.",
        "They used the dimmer so the room is calm.": "They turned lights low.",
        "They kept screens small and soft before sleep.": "They kept screens quiet.",
        "Sharing a toy makes everyone smile.": "Sharing makes friends.",
        "Saying goodnight helps you rest well.": "Saying night-night helps sleep.",
        "Brushing teeth keeps little teeth strong.": "Brushing teeth keeps teeth strong.",
        "Helping a friend makes the heart happy.": "Helping friends is nice.",
        "A warm hug makes a cozy night.": "A hug makes a happy night.",
        "Taking turns is fair and fun.": "Taking turns is fun.",
        "Listening helps friends feel heard.": "Listening helps friends.",
        "Being gentle keeps everyone safe.": "Being gentle is kind.",
        "Kind words make the world bright.": "Kind words are nice.",
        "They made a tiny dance with a twirl.": "They did a little dance.",
        "A little giggle popped out like bubbles.": "They giggled happily.",
        "They found a shiny pebble and counted it twice.": "They found a pebble.",
        "A merry little tune played on a leaf.": "A tiny tune played.",
        "They made funny faces at the moon and it winked.": "They made funny faces.",
        "They pretended the blanket was a magic cape.": "The blanket was a cape.",
        "A sleepy yawn turned into a tiny smile.": "A yawn became a smile.",
        "They blew a soft kiss to the stars.": "They blew a kiss.",
        "Someone whispered a silly riddle and everyone giggled.": "Someone told a riddle and they giggled.",
        "They clapped a tiny clap for being brave.": "They clapped for being brave.",
    }
    return replacements.get(s, s)


def generate_story(prompt: str = "", child_name: str | None = None, favorite_animal: str | None = None, voice_friendly: bool = False, use_llm: bool = True):
    """Generate a very short, toddler-friendly bedtime story.

    - prompt: optional small hint (e.g., favorite animal or toy)
    - child_name: optional child's name to personalize the story
    - favorite_animal: preferred animal character
    - voice_friendly: if True, return a list of short lines (good for reading aloud)
    - use_llm: if True, use AI generation; if False, use template-based generation

    Returns: string (paragraph) by default or list[str] when voice_friendly=True.
    """
    # Check if LLM is requested and available
    if use_llm and LLM_AVAILABLE:
        return _generate_story_llm(prompt, child_name, favorite_animal, voice_friendly)
    elif use_llm and not LLM_AVAILABLE:
        print("Warning: LLM requested but not available. Falling back to template generation.")
    
    # Fall back to template-based generation
    return _generate_story_template(prompt, child_name, favorite_animal, voice_friendly)


def _generate_story_llm(prompt: str = "", child_name: str | None = None, favorite_animal: str | None = None, voice_friendly: bool = False):
    """Generate story using LLM (AI-powered generation)."""
    try:
        # Initialize the LLM generator
        generator = LLMGenerator(model_name="gpt2")
        
        # Determine the character first
        character = None
        if favorite_animal:
            character = favorite_animal
        elif prompt and any(animal.lower() in prompt.lower() for animal in CHARACTERS):
            for animal in CHARACTERS:
                if animal.lower() in prompt.lower():
                    character = animal
                    break
        else:
            character = random.choice(CHARACTERS)
        
        # Build a structured prompt that follows the exact template pattern
        if child_name and child_name.strip():
            story_prompt = f"{character} waves hello to {child_name.strip()} with a warm smile. {character} teaches that being kind and sharing makes everyone happy. {character} plays games, dances around, and makes silly faces that make everyone giggle. {character} talks gently to {child_name.strip()} about their day and gives them a cozy hug. Now it's time for {child_name.strip()} to rest and sleep peacefully. Goodnight dear {child_name.strip()}, have the sweetest dreams."
        else:
            story_prompt = f"{character} waves hello with a warm smile. {character} teaches that being kind and sharing makes everyone happy. {character} plays games, dances around, and makes silly faces that make everyone giggle. Now it's time to rest and sleep peacefully. Goodnight, have the sweetest dreams."
        
        # Generate the story with better parameters
        # Calculate input length in tokens
        input_tokens = generator.tokenizer.encode(story_prompt)
        input_length = len(input_tokens)
        
        generated_text = generator.generate(
            prompt=story_prompt,
            max_length=input_length + 50,  # Shorter for faster generation
            temperature=0.7,  # Balanced creativity
        )
        
        # The generated text includes our prompt, so we'll use it all as the story
        story = generated_text.strip()
        
        # Clean up the generated text
        story = _clean_generated_story(story, child_name, favorite_animal)
        
        # Add AI generation indicator (just icon)
        story = f"🤖 {story}"
        
        # Format for voice-friendly output if requested
        if voice_friendly:
            sentences = [s.strip() for s in story.split('.') if s.strip()]
            return [s + '.' for s in sentences if s]
        
        return story
        
    except Exception as e:
        print(f"Error generating LLM story: {e}. Falling back to template generation.")
        return _generate_story_template(prompt, child_name, favorite_animal, voice_friendly)


def _clean_generated_story(story: str, child_name: Optional[str] = None, favorite_animal: Optional[str] = None) -> str:
    """Clean up and structure the LLM-generated story to follow the proper format."""
    if not story:
        return "Once upon a time, there was a gentle friend who wished everyone sweet dreams. Goodnight!"
    
    # Remove any unwanted content
    story = story.strip()
    
    # Split into sentences and clean them up
    sentences = [s.strip() for s in story.split('.') if s.strip()]
    
    # Filter sentences to keep only the structured parts (first 6 sentences max)
    # Structure: greeting, lesson, fun, talk to kid, sleep, goodbye
    structured_sentences = []
    
    for sentence in sentences[:6]:  # Only take first 6 sentences
        # Skip sentences that seem off-topic or unstructured
        lower_sent = sentence.lower()
        
        # Keep sentences that match our structure patterns
        if any(pattern in lower_sent for pattern in [
            'waves hello', 'teaches', 'being kind', 'sharing', 
            'plays games', 'dances', 'silly faces', 'giggle',
            'talks gently', 'about their day', 'cozy hug',
            'time for', 'rest', 'sleep', 'goodnight', 'sweet dreams'
        ]):
            structured_sentences.append(sentence)
        elif len(structured_sentences) < 6:  # Accept first 6 sentences even if they don't match perfectly
            structured_sentences.append(sentence)
    
    # Ensure minimum structure
    if len(structured_sentences) < 4:
        # Add missing parts if too short
        character_name = favorite_animal if favorite_animal else "Lion"
        if child_name and child_name.strip():
            if len(structured_sentences) == 0:
                structured_sentences.append(f"{character_name} waves hello to {child_name.strip()} with a warm smile")
            if len(structured_sentences) == 1:
                structured_sentences.append(f"{character_name} teaches that being kind and sharing makes everyone happy")
            if len(structured_sentences) == 2:
                structured_sentences.append(f"{character_name} plays games, dances around, and makes silly faces that make everyone giggle")
            if len(structured_sentences) == 3:
                structured_sentences.append(f"{character_name} talks gently to {child_name.strip()} about their day and gives them a cozy hug")
        else:
            if len(structured_sentences) == 0:
                structured_sentences.append(f"{character_name} waves hello with a warm smile")
            if len(structured_sentences) == 1:
                structured_sentences.append(f"{character_name} teaches that being kind and sharing makes everyone happy")
            if len(structured_sentences) == 2:
                structured_sentences.append(f"{character_name} plays games, dances around, and makes silly faces that make everyone giggle")
    
    # Reconstruct the story
    story = '. '.join(structured_sentences)
    if not story.endswith('.'):
        story += '.'
    
    # Ensure it ends with proper goodnight
    if not any(ending in story.lower() for ending in ["goodnight", "sweet dreams"]):
        if child_name and child_name.strip():
            story += f" Goodnight {child_name.strip()}, sweet dreams!"
        else:
            story += " Goodnight, sweet dreams!"
    
    return story


def _generate_story_template(prompt: str = "", child_name: str | None = None, favorite_animal: str | None = None, voice_friendly: bool = False):
    """Template-based story generation (original logic)."""
    # Always use non-deterministic randomness (no seed)

    # If prompt mentions a known character (animal), prefer that character
    def _extract_animal_from_prompt(p: str) -> str | None:
        if not p:
            return None
        p_low = p.lower()
        for c in CHARACTERS:
            if c.lower() in p_low:
                return c
        # simple variants like 'lion toy' or 'my elephant' -> check words
        words = [w.strip(".,!?:;\n\t\r") for w in p_low.split()]
        for c in CHARACTERS:
            if c.lower() in words:
                return c
        return None

    prompt_animal = _extract_animal_from_prompt(prompt)
    fav_animal = None
    if favorite_animal:
        # try to match favorite to known characters
        fav_low = favorite_animal.strip().lower()
        for c in CHARACTERS:
            if c.lower() in fav_low or fav_low in c.lower():
                fav_animal = c
                break

    # Priority: favorite animal -> prompt animal -> random
    if fav_animal is not None:
        character = fav_animal
    elif prompt_animal is not None:
        character = prompt_animal
    else:
        character = random.choice(CHARACTERS)
    location = random.choice(LOCATIONS)
    action = random.choice(SMALL_ACTIONS)
    tech = random.choice(TECH_LESSONS)
    # Choose life lesson (personalized if name present)
    if child_name:
        # Fill name into a personal template
        life = random.choice(PERSONAL_LIFE_LESSONS).format(name=child_name.strip())
    else:
        life = random.choice(LIFE_LESSONS)
    fun = random.choice(FUN_PARTS)

    def _strip_leading_they(s: str) -> str:
        # If sentence starts with 'They ' remove it for 'X says ...' phrasing
        if not s:
            return s
        s_stripped = s.strip()
        low = s_stripped.lower()
        if low.startswith("they "):
            no_they = s_stripped[len("They "):]
            # Capitalize first char for nicer sentence
            return no_they[0].upper() + no_they[1:] if no_they else no_they
        return s_stripped

    # Add emoji to the character name for visual cue
    emoji = EMOJI.get(character, "")

    # Keep sentences short and simple
    lines = []

    # First line: fun greeting from the animal (personalized if child_name present)
    if child_name and child_name.strip():
        greet = random.choice(PERSONAL_GREETINGS).format(name=child_name.strip())
    else:
        greet = random.choice(GREETINGS)

    first = f"{emoji} {character} {greet}" if emoji else f"{character} {greet}"
    # Second line: place the animal in a cozy location or small action
    second = f"{emoji} {character} {location}." if emoji else f"{character} {location}."
    lines.append(first)
    lines.append(second)

    # Use normal vocabulary by default
    life_frag = life
    tech_frag_full = tech

    tech_frag = _strip_leading_they(tech_frag_full)

    # Animal speaks the life lesson and the tech lesson (shortened)
    lines.append(f"{character} says {life_frag.rstrip('.') }.")
    lines.append(f"{character} says {tech_frag.rstrip('.') }.")

    # Add a small fun line to keep the story playful — animal acts the fun part
    # Prefer a normalized short action from FUN_ACTIONS; fall back to a stripped fragment
    fun_action = FUN_ACTIONS.get(fun)
    if not fun_action:
        # use the original fun fragment and strip leading 'They'
        fun_frag_full = fun
        fun_action = _strip_leading_they(fun_frag_full)
        # make lowercase verb-phrase if it starts with a capitalized noun like 'A '
        fun_action = fun_action[0].lower() + fun_action[1:] if fun_action and fun_action[0].isupper() else fun_action

    # Ensure no trailing period on action before composing
    action_text = fun_action.rstrip('.')
    lines.append(f"{character} {action_text}.")

    # Optionally add the prompt as a small personal line.
    # If the prompt is just the animal (or contains the animal), avoid duplicating it.
    if prompt:
        # Keep prompt short for toddlers
        # Skip adding if prompt mostly just names the character
        skip_prompt_line = False
        if prompt_animal is not None:
            # If prompt equals the animal or is a short phrase containing just the animal, skip
            p_stripped = prompt.strip().lower()
            if p_stripped == character.lower() or p_stripped.endswith(character.lower()) or character.lower() in p_stripped.split():
                # very short prompts like 'lion' or 'my lion' -> skip
                if len(p_stripped.split()) <= 3:
                    skip_prompt_line = True

        if not skip_prompt_line:
            lines.append(f"They thought about {prompt}.")

    # If we have a child's name, add a warm personal line including the name and chosen animal
    if child_name:
        name_clean = child_name.strip()
        if name_clean:
            lines.append(f"{character} waved a little hello to {name_clean}.")

    # Always use normal vocabulary (no mapping step)

    # Remove any existing bedtime/goodnight lines to avoid duplicates
    def _is_goodnight_line(s: str) -> bool:
        if not s:
            return False
        low = s.lower()
        return "goodnight" in low or "night-night" in low or "night night" in low

    lines = [l for l in lines if not _is_goodnight_line(l)]

    # Append a fixed farewell as the final line. Personalize when child_name is present.
    if child_name and child_name.strip():
        lines.append(f"Goodnight, {child_name.strip()} — sweet dreams.")
    else:
        lines.append(FAREWELL)

    # Combine into a tiny bedtime story (3-6 short sentences)
    if voice_friendly:
        return lines

    story = " ".join(lines)
    
    # Add template generation indicator (just icon)
    story = f"📝 {story}"
    
    return story
