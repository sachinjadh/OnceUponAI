import random

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


def generate_story(prompt: str = "", child_name: str | None = None, favorite_animal: str | None = None, voice_friendly: bool = False):
    """Generate a very short, toddler-friendly bedtime story.

    - prompt: optional small hint (e.g., favorite animal or toy)
    - seed: optional random seed for deterministic choices
    - voice_friendly: if True, return a list of short lines (good for reading aloud)
    - vocab: 'normal' or 'simple' (simpler words for younger toddlers)

    Returns: string (paragraph) by default or list[str] when voice_friendly=True.
    """
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
    return story
