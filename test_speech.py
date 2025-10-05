#!/usr/bin/env python3

"""Simple test for speech functionality"""

import streamlit as st
import streamlit.components.v1 as components

st.title("🔊 Speech Test")

test_text = "Hello! This is a test of the speech functionality. The quick brown fox jumps over the lazy dog."

st.write("Click the button below to test browser speech:")

if st.button("🗣️ Test Speech"):
    st.write("Attempting to speak...")
    
    # Properly encode the text for JavaScript to avoid regex issues
    import json
    safe_text = json.dumps(test_text)  # This will properly escape the string
    
    # Simple HTML with speech synthesis
    components.html(f"""
    <div style="padding: 20px; background: #f0f2f6; border-radius: 10px;">
        <h3>🎤 Speech Test Active</h3>
        <p>Status: <span id="status">Starting...</span></p>
        <button onclick="stopSpeech()" style="background: #ff4757; color: white; border: none; padding: 10px 20px; border-radius: 5px;">
            ⏹️ Stop Speech
        </button>
    </div>
    
    <script>
        console.log("Speech test script loaded");
        
        // Function to update status
        function updateStatus(message) {{
            document.getElementById('status').textContent = message;
            console.log("Status:", message);
        }}
        
        // Check speech synthesis support
        if ('speechSynthesis' in window) {{
            updateStatus("Speech synthesis supported!");
            
            // Wait a bit for voices to load
            setTimeout(function() {{
                try {{
                    // Cancel any existing speech
                    speechSynthesis.cancel();
                    
                    // Use properly escaped text
                    const textToSpeak = {safe_text};
                    
                    // Create utterance
                    const utterance = new SpeechSynthesisUtterance(textToSpeak);
                    
                    // Set properties
                    utterance.rate = 0.8;
                    utterance.pitch = 1.0;
                    utterance.volume = 1.0;
                    
                    // Event handlers
                    utterance.onstart = function() {{
                        updateStatus("Speaking...");
                    }};
                    
                    utterance.onend = function() {{
                        updateStatus("Finished speaking!");
                    }};
                    
                    utterance.onerror = function(event) {{
                        updateStatus("Error: " + event.error);
                        console.error("Speech error:", event);
                    }};
                    
                    // Start speaking
                    speechSynthesis.speak(utterance);
                    updateStatus("Speech started...");
                    
                }} catch (error) {{
                    updateStatus("JavaScript error: " + error.message);
                    console.error("JS Error:", error);
                }}
            }}, 1000);
            
        }} else {{
            updateStatus("Speech synthesis not supported in this browser");
        }}
        
        // Stop function
        function stopSpeech() {{
            speechSynthesis.cancel();
            updateStatus("Speech stopped by user");
        }}
    </script>
    """, height=200)

st.write("---")
st.write("**Debug Info:**")
st.write("- Make sure you're using a modern browser (Chrome, Firefox, Safari, Edge)")
st.write("- Check that your browser allows audio/speech")
st.write("- Try clicking the test button and check the status message")
st.write("- If no sound, check your system volume and browser settings")