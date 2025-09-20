import os
import streamlit as st
from story_generator import template_generator
from story_store import load_stories, random_story, filter_stories

st.set_page_config(page_title="Storytime for Kids", layout="wide")

# Simple CSS to make the app colorful and kid-friendly
st.markdown(
        """
        <style>
        .header { background: linear-gradient(90deg, #FFDEE9 0%, #B5FFFC 100%); padding:20px; border-radius:12px; text-align:center; }
        .big-title { font-size:42px; color:#3B3B98; font-weight:800; margin:0; }
        .subtitle { font-size:18px; color:#4A5568; margin:4px 0 0 0; }
            .emoji-large { font-size:120px; }
            /* Full-width story box with roomy padding for easy reading */
            .story-box { background: #FFFDF5; padding:28px; border-radius:18px; max-width:none; width:calc(100% - 64px); margin:12px auto; box-shadow: 0 8px 24px rgba(0,0,0,0.14); }
            .story-line { font-size:28px; line-height:1.8; color:#1a202c; margin:10px 0; }
            @media (max-width: 600px) {
                .story-line { font-size:26px; }
                .emoji-large { font-size:96px; }
                .story-box { width:calc(100% - 32px); padding:18px; }
            }
        </style>
        <div class="header">
            <div class="big-title">🌙 Storytime</div>
            <div class="subtitle">Short, gentle tales for little ones</div>
        </div>
        """,
        unsafe_allow_html=True,
)

# Top-level tabs: Generator and Stories Library
# Top-level tabs: Generator and Stories Library
tab = st.tabs(["Generator", "Stories Library"])

stories_data = load_stories()

# -------- Generator tab (two-column layout) --------
with tab[0]:
    st.header("Make a story")
    left, right = st.columns([1, 2], gap="large")

    with left:
        st.subheader("Controls")
        child_name = st.text_input("Child's name (optional)", "")
        favorite_animal = st.selectbox(
            "Favorite animal (optional)",
            options=["(Random)", "Lion", "Elephant", "Gorilla", "Pig", "Monkey", "Bear", "Rabbit", "Duck", "Fox", "Turtle"],
        )
        generate = st.button("Generate story")

    with right:
        # Placeholder for the generated story and animal badge
        story_area = st.container()

    if generate:
        # Generate the story
        # No prompt input: pass empty prompt; favorite_animal will guide character selection
        result = template_generator.generate_story(
            prompt='',
            child_name=child_name or None,
            favorite_animal=(None if favorite_animal == "(Random)" else favorite_animal),
            voice_friendly=False,
        )

        # Determine the chosen character to show emoji/name
        chosen_animal = None
        # First, prefer the favorite_animal selectbox if a real animal was chosen
        if favorite_animal and favorite_animal != "(Random)":
            chosen_animal = favorite_animal

        # If still unknown, try to guess from the generated story text
        if not chosen_animal:
            for a in ["Lion","Elephant","Gorilla","Pig","Monkey","Bear","Rabbit","Duck","Fox","Turtle"]:
                if a.lower() in result.lower():
                    chosen_animal = a
                    break

        with story_area:
            # show big emoji and name if available
            emoji_map = {"Lion": "🦁", "Elephant": "🐘", "Gorilla": "🦍", "Pig": "🐷", "Monkey": "🐵", "Bear": "🐻", "Rabbit": "🐰", "Duck": "🦆", "Fox": "🦊", "Turtle": "🐢"}
            if chosen_animal:
                st.markdown(f"<div style='text-align:center'><div style='font-size:120px'>{emoji_map.get(chosen_animal, '')}</div><div style='font-size:28px; font-weight:800'>Story about {chosen_animal} and {child_name}</div></div>", unsafe_allow_html=True)

            # Break sentences into readable paragraphs
            sentences = [s.strip() for s in result.split('. ') if s.strip()]
            story_html = ''.join(f'<p class="story-line">{sent.rstrip(".")}</p>' for sent in sentences)
            st.markdown(f'<div class="story-box">{story_html}</div>', unsafe_allow_html=True)


# -------- Stories Library (card grid) --------
with tab[1]:
    st.header("Stories Library")
    animals = sorted({s.get("animal", "").split()[0] for s in stories_data if s.get("animal")})
    # Simplified library: choose animal or pick random (single dropdown)
    animals_options = ["All"] + animals
    chosen_animal = st.selectbox("Choose animal", options=animals_options)

    filtered = filter_stories(stories_data, animal=None if chosen_animal == "All" else chosen_animal)
    if st.button("Random story from library"):
        chosen = random_story(filtered)
    else:
        # show the first matching story for the selected animal (or the first overall)
        chosen = None
        if filtered:
            chosen = filtered[0]

    if chosen:
        st.subheader(chosen.get('title',''))
        animal = chosen.get('animal','')
        emoji = {"Lion": "🦁", "Elephant": "🐘", "Gorilla": "🦍", "Pig": "🐷", "Monkey": "🐵", "Bear": "🐻", "Rabbit": "🐰", "Duck": "🦆", "Fox": "🦊", "Turtle": "🐢"}.get(animal.split()[0], '')
        st.markdown(f"<div style='text-align:center'><div style='font-size:96px'>{emoji}</div><div style='font-weight:700'>{animal}</div></div>", unsafe_allow_html=True)
        sentences = [s.strip() for s in chosen.get('story','').split('. ') if s.strip()]
        story_html = ''.join(f'<p class="story-line">{sent.rstrip(".")}</p>' for sent in sentences)
        st.markdown(f'<div class="story-box">{story_html}<p style="font-weight:700; margin-top:12px">Lesson: {chosen.get("lesson","")}</p></div>', unsafe_allow_html=True)
