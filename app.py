import os
import streamlit as st
import streamlit.components.v1 as components
from story_generator import template_generator
from story_store import load_stories, random_story, filter_stories
import io
import base64

# Try to import text-to-speech libraries
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False

try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False

st.set_page_config(page_title="Storytime for Kids", layout="wide")

def generate_audio(text: str):
    """Generate audio from text using Google TTS"""
    try:
        if GTTS_AVAILABLE:
            # Clean text for better speech
            clean_text = text.replace('🤖', '').replace('📝', '').strip()
            if len(clean_text) > 500:  # Limit length for better performance
                clean_text = clean_text[:500] + "."
            
            # Use Google Text-to-Speech
            tts = gTTS(text=clean_text, lang='en', slow=True)  # slow=True for children
            audio_buffer = io.BytesIO()
            tts.write_to_fp(audio_buffer)
            audio_buffer.seek(0)
            return audio_buffer.getvalue()
    except Exception as e:
        print(f"gTTS error: {e}")
        return None
    return None

def create_audio_player(text: str, key: str):
    """Create an audio player for the given text"""
    # Clean text for speech
    clean_text = text.replace('🤖', '').replace('📝', '').strip()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        # Google TTS option
        if st.button(f"🎵 Audio File", key=f"gtts_{key}"):
            try:
                with st.spinner("Generating audio..."):
                    audio_data = generate_audio(clean_text)
                    if audio_data:
                        st.audio(audio_data, format='audio/mp3')
                        st.success("🎵 Audio ready!")
                    else:
                        st.error("Audio generation failed. Check internet connection.")
            except Exception as e:
                st.error(f"Error: {e}")
    
    with col2:
        # Simple browser speech button
        if st.button(f"🗣️ Read Aloud", key=f"speech_{key}"):
            import json
            # Use a much simpler approach - create a unique HTML element
            speech_id = f"speech_container_{key}"
            
            # Properly escape text for JavaScript using JSON
            safe_text = json.dumps(clean_text)
            
            # Create a simple HTML component that triggers speech
            st.components.v1.html(f"""
            <div id="{speech_id}" style="padding: 10px;">
                <p style="color: green; font-weight: bold;">🎤 Reading story aloud...</p>
                <button onclick="stopReading()" style="background: #ff4757; color: white; border: none; padding: 8px 16px; border-radius: 5px; cursor: pointer;">
                    ⏹️ Stop Reading
                </button>
            </div>
            
            <script>
                // Wait for page to load
                setTimeout(function() {{
                    // Check if speech synthesis is supported
                    if ('speechSynthesis' in window) {{
                        // Cancel any existing speech
                        speechSynthesis.cancel();
                        
                        // Use properly escaped text
                        const textToSpeak = {safe_text};
                        
                        // Create speech utterance
                        const utterance = new SpeechSynthesisUtterance(textToSpeak);
                        
                        // Set speech parameters for children
                        utterance.rate = 0.8;
                        utterance.pitch = 1.1;
                        utterance.volume = 1.0;
                        
                        // Start speaking
                        speechSynthesis.speak(utterance);
                        
                        // Handle completion
                        utterance.onend = function() {{
                            document.getElementById("{speech_id}").innerHTML = 
                                '<p style="color: blue;">✅ Finished reading!</p>';
                        }};
                        
                        utterance.onerror = function(event) {{
                            document.getElementById("{speech_id}").innerHTML = 
                                '<p style="color: red;">❌ Speech failed: ' + event.error + '</p>';
                        }};
                    }} else {{
                        document.getElementById("{speech_id}").innerHTML = 
                            '<p style="color: red;">❌ Speech not supported in this browser</p>';
                    }}
                }}, 500);
                
                function stopReading() {{
                    speechSynthesis.cancel();
                    document.getElementById("{speech_id}").innerHTML = 
                        '<p style="color: orange;">⏹️ Speech stopped</p>';
                }}
            </script>
            """, height=100)

# Simple CSS to make the app colorful and kid-friendly
st.markdown(
        """
        <style>
        .header { background: linear-gradient(90deg, #FFDEE9 0%, #B5FFFC 100%); padding:20px; border-radius:12px; text-align:center; }
        .big-title { font-size:42px; color:#3B3B98; font-weight:800; margin:0; }
        .subtitle { font-size:18px; color:#4A5568; margin:4px 0 0 0; }
            .emoji-large { font-size:120px; }
            /* Full-width story box with roomy padding for easy reading */
            .story-box { background: #FFFDF5; padding:20px; border-radius:18px; max-width:none; width:calc(100% - 40px); margin:8px auto; box-shadow: 0 8px 24px rgba(0,0,0,0.14); }
            .story-line { font-size:26px; line-height:1.6; color:#1a202c; margin:8px 0; }
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

# Initialize session state for storing generated stories
if 'generated_story' not in st.session_state:
    st.session_state.generated_story = None
if 'story_metadata' not in st.session_state:
    st.session_state.story_metadata = {}

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
            options=["(Random)", "Lion", "Elephant", "Gorilla", "Pig", "Monkey", "Bear", "Rabbit", "Duck", "Fox", "Turtle", 
                    "Cat", "Dog", "Panda", "Penguin", "Owl", "Frog", "Koala", "Zebra", "Giraffe", "Hippo", "Sheep", "Cow", "Horse", "Tiger", "Deer"],
        )
        use_ai = st.checkbox("Use AI Generation 🤖", value=True, help="Use AI to create unique stories, or uncheck for template-based stories")
        generate = st.button("Generate story")

    with right:
        # Placeholder for the generated story and animal badge
        story_area = st.container()

    if generate:
        # Show kid-friendly loader while generating story
        with story_area:
            # Create fun loading animation
            loading_container = st.empty()
            
            loading_messages = [
                "🌟 Creating your magical story...",
                "🎨 Painting adventures with words...", 
                "✨ Sprinkling story magic...",
                "📚 Gathering the perfect words...",
                "🦄 Adding some imagination...",
                "🎭 Setting up the characters...",
                "🌈 Making it extra special for you..."
            ]
            
            import random
            message = random.choice(loading_messages)
            
            loading_container.markdown(f"""
            <div style="text-align: center; padding: 40px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 20px; color: white;">
                <div style="font-size: 80px; margin-bottom: 20px;">
                    <span style="animation: bounce 1s infinite;">📖</span>
                    <span style="animation: bounce 1s infinite 0.1s;">✨</span>
                    <span style="animation: bounce 1s infinite 0.2s;">🎪</span>
                </div>
                <h2 style="margin: 0; font-size: 24px; font-weight: bold;">{message}</h2>
                <div style="margin-top: 20px;">
                    <div style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: white; margin: 0 4px; animation: pulse 1.5s ease-in-out infinite;"></div>
                    <div style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: white; margin: 0 4px; animation: pulse 1.5s ease-in-out infinite 0.3s;"></div>
                    <div style="display: inline-block; width: 8px; height: 8px; border-radius: 50%; background: white; margin: 0 4px; animation: pulse 1.5s ease-in-out infinite 0.6s;"></div>
                </div>
            </div>
            
            <style>
                @keyframes bounce {{
                    0%, 20%, 50%, 80%, 100% {{ transform: translateY(0); }}
                    40% {{ transform: translateY(-20px); }}
                    60% {{ transform: translateY(-10px); }}
                }}
                
                @keyframes pulse {{
                    0%, 100% {{ opacity: 0.3; transform: scale(0.8); }}
                    50% {{ opacity: 1; transform: scale(1.2); }}
                }}
            </style>
            """, unsafe_allow_html=True)
        
        # Generate the story and store in session state
        result = template_generator.generate_story(
            prompt='',
            child_name=child_name or None,
            favorite_animal=(None if favorite_animal == "(Random)" else favorite_animal),
            voice_friendly=False,
            use_llm=use_ai,
        )
        
        # Clear the loading animation
        loading_container.empty()
        
        # Store the story and metadata in session state
        st.session_state.generated_story = result
        st.session_state.story_metadata = {
            'child_name': child_name,
            'favorite_animal': favorite_animal,
            'use_ai': use_ai
        }

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
            emoji_map = {"Lion": "🦁", "Elephant": "🐘", "Gorilla": "🦍", "Pig": "🐷", "Monkey": "🐵", "Bear": "🐻", "Rabbit": "🐰", "Duck": "🦆", "Fox": "🦊", "Turtle": "🐢",
                        "Cat": "🐱", "Dog": "🐶", "Panda": "🐼", "Penguin": "🐧", "Owl": "🦉", "Frog": "🐸", "Koala": "🐨", "Zebra": "🦓", "Giraffe": "🦒", "Hippo": "🦛", 
                        "Sheep": "🐑", "Cow": "🐄", "Horse": "🐴", "Tiger": "🐅", "Deer": "🦌"}
            if chosen_animal:
                st.markdown(f"<div style='text-align:center; margin-bottom:10px;'><div style='font-size:80px; margin-bottom:5px;'>{emoji_map.get(chosen_animal, '')}</div><div style='font-size:22px; font-weight:700; margin-bottom:10px;'>Story about {chosen_animal} and {child_name}</div></div>", unsafe_allow_html=True)

            # Break sentences into readable paragraphs
            sentences = [s.strip() for s in result.split('. ') if s.strip()]
            story_html = ''.join(f'<p class="story-line">{sent.rstrip(".")}</p>' for sent in sentences)
            st.markdown(f'<div class="story-box">{story_html}</div>', unsafe_allow_html=True)
            
            # Add speech functionality
            st.write("---")
            st.subheader("🔊 Listen to Your Story")
            
            # Clean the story text for speech (remove emojis and special formatting)
            clean_story = result.replace('🤖', '').replace('📝', '').strip()
            
            # Simple one-click speech using components.v1.html
            import json
            safe_text = json.dumps(clean_story)
            
            components.html(f"""
            <div style="padding: 20px; text-align: center;">
                <button onclick="readStory()" 
                        style="background: linear-gradient(45deg, #FF6B6B, #4ECDC4); 
                               color: white; 
                               border: none; 
                               padding: 15px 30px; 
                               border-radius: 25px; 
                               cursor: pointer; 
                               font-size: 18px;
                               margin-right: 15px;
                               box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                               font-weight: bold;">
                    🗣️ Read Story Aloud
                </button>
                <button onclick="stopReading()" 
                        style="background: #FF4757; 
                               color: white; 
                               border: none; 
                               padding: 15px 30px; 
                               border-radius: 25px; 
                               cursor: pointer; 
                               font-size: 18px;
                               box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                               font-weight: bold;">
                    ⏹️ Stop
                </button>
                <div id="status" style="margin-top: 15px; font-size: 16px; font-weight: bold; color: #333;"></div>
            </div>
            
            <script>
                let currentUtterance = null;
                
                function readStory() {{
                    // Stop any current speech
                    if (speechSynthesis.speaking) {{
                        speechSynthesis.cancel();
                    }}
                    
                    // Check if speech synthesis is available
                    if (!('speechSynthesis' in window)) {{
                        document.getElementById('status').innerHTML = '❌ Speech not supported in this browser';
                        return;
                    }}
                    
                    // Get the story text
                    const storyText = {safe_text};
                    
                    if (!storyText || storyText.length === 0) {{
                        document.getElementById('status').innerHTML = '❌ No story to read';
                        return;
                    }}
                    
                    // Create speech utterance
                    currentUtterance = new SpeechSynthesisUtterance(storyText);
                    
                    // Set speech parameters for very gentle kid-friendly voice
                    currentUtterance.rate = 0.5;    // Very slow and gentle for little kids
                    currentUtterance.pitch = 1.5;   // Higher pitch for child-like voice
                    currentUtterance.volume = 0.8;  // Soft and gentle volume
                    
                    // Try to find the most child-like voice available
                    const voices = speechSynthesis.getVoices();
                    
                    // Look for child/young voices first, then female voices
                    const childVoice = voices.find(voice => 
                        voice.name.toLowerCase().includes('child') ||
                        voice.name.toLowerCase().includes('kid') ||
                        voice.name.toLowerCase().includes('young') ||
                        voice.name.toLowerCase().includes('junior') ||
                        voice.name.toLowerCase().includes('alex') ||  // Often young-sounding
                        voice.name.toLowerCase().includes('zoe') ||   // Child-like name
                        voice.name.toLowerCase().includes('alice') || // Often sounds young
                        voice.name.toLowerCase().includes('emma')     // Young-sounding name
                    );
                    
                    const femaleVoice = voices.find(voice => 
                        voice.name.toLowerCase().includes('samantha') ||
                        voice.name.toLowerCase().includes('karen') ||
                        voice.name.toLowerCase().includes('susan') ||
                        voice.name.toLowerCase().includes('victoria') ||
                        voice.name.toLowerCase().includes('allison') ||
                        voice.gender === 'female'
                    );
                    
                    // Prefer child voice, fallback to female voice
                    if (childVoice) {{
                        currentUtterance.voice = childVoice;
                    }} else if (femaleVoice) {{
                        currentUtterance.voice = femaleVoice;
                    }}
                    
                    // Set up event handlers
                    currentUtterance.onstart = function() {{
                        document.getElementById('status').innerHTML = '🎤 Reading your story...';
                    }};
                    
                    currentUtterance.onend = function() {{
                        document.getElementById('status').innerHTML = '✅ Finished reading!';
                        currentUtterance = null;
                    }};
                    
                    currentUtterance.onerror = function(event) {{
                        document.getElementById('status').innerHTML = '❌ Error: ' + event.error;
                        currentUtterance = null;
                    }};
                    
                    // Start speaking
                    speechSynthesis.speak(currentUtterance);
                }}
                
                function stopReading() {{
                    if (speechSynthesis.speaking) {{
                        speechSynthesis.cancel();
                        document.getElementById('status').innerHTML = '⏹️ Stopped reading';
                        currentUtterance = null;
                    }}
                }}
                
                // Test speech synthesis on page load
                window.onload = function() {{
                    if ('speechSynthesis' in window) {{
                        document.getElementById('status').innerHTML = '🔊 Ready to read your story!';
                    }} else {{
                        document.getElementById('status').innerHTML = '❌ Speech not supported in this browser';
                    }}
                }};
            </script>
            """, height=120)
    
    # Also display story from session state if no new story was generated
    elif st.session_state.generated_story:
        result = st.session_state.generated_story
        metadata = st.session_state.story_metadata
        
        # Show story from session state
        with story_area:
            # Display the stored story
            sentences = [s.strip() for s in result.split('. ') if s.strip()]
            story_html = ''.join(f'<p class="story-line">{sent.rstrip(".")}</p>' for sent in sentences)
            st.markdown(f'<div class="story-box">{story_html}</div>', unsafe_allow_html=True)
            
            # Add persistent speech functionality
            st.write("---")
            st.subheader("🔊 Listen to Your Story")
            
            clean_story = result.replace('🤖', '').replace('📝', '').strip()
            
            # Simple speech using components.v1.html
            import json
            safe_text = json.dumps(clean_story)
            
            components.html(f"""
            <div style="padding: 20px; text-align: center;">
                <button onclick="readPersistentStory()" 
                        style="background: linear-gradient(45deg, #FF6B6B, #4ECDC4); 
                               color: white; 
                               border: none; 
                               padding: 15px 30px; 
                               border-radius: 25px; 
                               cursor: pointer; 
                               font-size: 18px;
                               margin-right: 15px;
                               box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                               font-weight: bold;">
                    🗣️ Read Story Aloud
                </button>
                <button onclick="stopPersistentReading()" 
                        style="background: #FF4757; 
                               color: white; 
                               border: none; 
                               padding: 15px 30px; 
                               border-radius: 25px; 
                               cursor: pointer; 
                               font-size: 18px;
                               box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                               font-weight: bold;">
                    ⏹️ Stop
                </button>
                <div id="persistent-status" style="margin-top: 15px; font-size: 16px; font-weight: bold; color: #333;"></div>
            </div>
            
            <script>
                let persistentUtterance = null;
                
                function readPersistentStory() {{
                    if (speechSynthesis.speaking) {{
                        speechSynthesis.cancel();
                    }}
                    
                    if (!('speechSynthesis' in window)) {{
                        document.getElementById('persistent-status').innerHTML = '❌ Speech not supported in this browser';
                        return;
                    }}
                    
                    const storyText = {safe_text};
                    
                    if (!storyText || storyText.length === 0) {{
                        document.getElementById('persistent-status').innerHTML = '❌ No story to read';
                        return;
                    }}
                    
                    persistentUtterance = new SpeechSynthesisUtterance(storyText);
                    persistentUtterance.rate = 0.5;    // Very slow and gentle for little kids
                    persistentUtterance.pitch = 1.5;   // Higher pitch for child-like voice
                    persistentUtterance.volume = 0.8;  // Soft and gentle volume
                    
                    // Try to find the most child-like voice available
                    const voices = speechSynthesis.getVoices();
                    
                    // Look for child/young voices first, then female voices
                    const childVoice = voices.find(voice => 
                        voice.name.toLowerCase().includes('child') ||
                        voice.name.toLowerCase().includes('kid') ||
                        voice.name.toLowerCase().includes('young') ||
                        voice.name.toLowerCase().includes('junior') ||
                        voice.name.toLowerCase().includes('alex') ||
                        voice.name.toLowerCase().includes('zoe') ||
                        voice.name.toLowerCase().includes('alice') ||
                        voice.name.toLowerCase().includes('emma')
                    );
                    
                    const femaleVoice = voices.find(voice => 
                        voice.name.toLowerCase().includes('samantha') ||
                        voice.name.toLowerCase().includes('karen') ||
                        voice.name.toLowerCase().includes('susan') ||
                        voice.name.toLowerCase().includes('victoria') ||
                        voice.name.toLowerCase().includes('allison') ||
                        voice.gender === 'female'
                    );
                    
                    // Prefer child voice, fallback to female voice
                    if (childVoice) {{
                        persistentUtterance.voice = childVoice;
                    }} else if (femaleVoice) {{
                        persistentUtterance.voice = femaleVoice;
                    }}
                    
                    persistentUtterance.onstart = function() {{
                        document.getElementById('persistent-status').innerHTML = '🎤 Reading your story...';
                    }};
                    
                    persistentUtterance.onend = function() {{
                        document.getElementById('persistent-status').innerHTML = '✅ Finished reading!';
                        persistentUtterance = null;
                    }};
                    
                    persistentUtterance.onerror = function(event) {{
                        document.getElementById('persistent-status').innerHTML = '❌ Error: ' + event.error;
                        persistentUtterance = null;
                    }};
                    
                    speechSynthesis.speak(persistentUtterance);
                }}
                
                function stopPersistentReading() {{
                    if (speechSynthesis.speaking) {{
                        speechSynthesis.cancel();
                        document.getElementById('persistent-status').innerHTML = '⏹️ Stopped reading';
                        persistentUtterance = null;
                    }}
                }}
                
                // Initialize
                window.onload = function() {{
                    if ('speechSynthesis' in window) {{
                        document.getElementById('persistent-status').innerHTML = '🔊 Ready to read your story!';
                    }} else {{
                        document.getElementById('persistent-status').innerHTML = '❌ Speech not supported in this browser';
                    }}
                }};
            </script>
            """, height=120)


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
        emoji = {"Lion": "🦁", "Elephant": "🐘", "Gorilla": "🦍", "Pig": "🐷", "Monkey": "🐵", "Bear": "🐻", "Rabbit": "🐰", "Duck": "🦆", "Fox": "🦊", "Turtle": "🐢",
                "Cat": "🐱", "Dog": "🐶", "Panda": "🐼", "Penguin": "🐧", "Owl": "🦉", "Frog": "🐸", "Koala": "🐨", "Zebra": "🦓", "Giraffe": "🦒", "Hippo": "🦛", 
                "Sheep": "🐑", "Cow": "🐄", "Horse": "🐴", "Tiger": "🐅", "Deer": "🦌"}.get(animal.split()[0], '')
        st.markdown(f"<div style='text-align:center; margin-bottom:10px;'><div style='font-size:70px; margin-bottom:5px;'>{emoji}</div><div style='font-weight:700; font-size:18px; margin-bottom:8px;'>{animal}</div></div>", unsafe_allow_html=True)
        sentences = [s.strip() for s in chosen.get('story','').split('. ') if s.strip()]
        story_html = ''.join(f'<p class="story-line">{sent.rstrip(".")}</p>' for sent in sentences)
        st.markdown(f'<div class="story-box">{story_html}<p style="font-weight:700; margin-top:12px">Lesson: {chosen.get("lesson","")}</p></div>', unsafe_allow_html=True)
        
        # Add speech functionality for library stories
        st.write("---")
        st.subheader("🔊 Listen to This Story")
        library_story_text = f"{chosen.get('story','')} The lesson is: {chosen.get('lesson','')}"
        
        # Simple speech using components.v1.html
        import json
        safe_library_text = json.dumps(library_story_text)
        
        components.html(f"""
        <div style="padding: 20px; text-align: center;">
            <button onclick="readLibraryStory()" 
                    style="background: linear-gradient(45deg, #FF6B6B, #4ECDC4); 
                           color: white; 
                           border: none; 
                           padding: 15px 30px; 
                           border-radius: 25px; 
                           cursor: pointer; 
                           font-size: 18px;
                           margin-right: 15px;
                           box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                           font-weight: bold;">
                🗣️ Read Story Aloud
            </button>
            <button onclick="stopLibraryReading()" 
                    style="background: #FF4757; 
                           color: white; 
                           border: none; 
                           padding: 15px 30px; 
                           border-radius: 25px; 
                           cursor: pointer; 
                           font-size: 18px;
                           box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                           font-weight: bold;">
                ⏹️ Stop
            </button>
            <div id="library-status" style="margin-top: 15px; font-size: 16px; font-weight: bold; color: #333;"></div>
        </div>
        
        <script>
            let libraryUtterance = null;
            
            function readLibraryStory() {{
                if (speechSynthesis.speaking) {{
                    speechSynthesis.cancel();
                }}
                
                if (!('speechSynthesis' in window)) {{
                    document.getElementById('library-status').innerHTML = '❌ Speech not supported in this browser';
                    return;
                }}
                
                const storyText = {safe_library_text};
                
                if (!storyText || storyText.length === 0) {{
                    document.getElementById('library-status').innerHTML = '❌ No story to read';
                    return;
                }}
                
                libraryUtterance = new SpeechSynthesisUtterance(storyText);
                libraryUtterance.rate = 0.5;    // Very slow and gentle for little kids
                libraryUtterance.pitch = 1.5;   // Higher pitch for child-like voice
                libraryUtterance.volume = 0.8;  // Soft and gentle volume
                
                // Try to find the most child-like voice available
                const voices = speechSynthesis.getVoices();
                
                // Look for child/young voices first, then female voices
                const childVoice = voices.find(voice => 
                    voice.name.toLowerCase().includes('child') ||
                    voice.name.toLowerCase().includes('kid') ||
                    voice.name.toLowerCase().includes('young') ||
                    voice.name.toLowerCase().includes('junior') ||
                    voice.name.toLowerCase().includes('alex') ||
                    voice.name.toLowerCase().includes('zoe') ||
                    voice.name.toLowerCase().includes('alice') ||
                    voice.name.toLowerCase().includes('emma')
                );
                
                const femaleVoice = voices.find(voice => 
                    voice.name.toLowerCase().includes('samantha') ||
                    voice.name.toLowerCase().includes('karen') ||
                    voice.name.toLowerCase().includes('susan') ||
                    voice.name.toLowerCase().includes('victoria') ||
                    voice.name.toLowerCase().includes('allison') ||
                    voice.gender === 'female'
                );
                
                // Prefer child voice, fallback to female voice
                if (childVoice) {{
                    libraryUtterance.voice = childVoice;
                }} else if (femaleVoice) {{
                    libraryUtterance.voice = femaleVoice;
                }}
                
                libraryUtterance.onstart = function() {{
                    document.getElementById('library-status').innerHTML = '🎤 Reading story...';
                }};
                
                libraryUtterance.onend = function() {{
                    document.getElementById('library-status').innerHTML = '✅ Finished reading!';
                    libraryUtterance = null;
                }};
                
                libraryUtterance.onerror = function(event) {{
                    document.getElementById('library-status').innerHTML = '❌ Error: ' + event.error;
                    libraryUtterance = null;
                }};
                
                speechSynthesis.speak(libraryUtterance);
            }}
            
            function stopLibraryReading() {{
                if (speechSynthesis.speaking) {{
                    speechSynthesis.cancel();
                    document.getElementById('library-status').innerHTML = '⏹️ Stopped reading';
                    libraryUtterance = null;
                }}
            }}
            
            // Initialize
            window.onload = function() {{
                if ('speechSynthesis' in window) {{
                    document.getElementById('library-status').innerHTML = '🔊 Ready to read story!';
                }} else {{
                    document.getElementById('library-status').innerHTML = '❌ Speech not supported in this browser';
                }}
            }};
        </script>
        """, height=120)
