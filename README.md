# 🌙 OnceUponAI - AI-Powered Storytelling for Kids

An interactive storytelling application that creates personalized stories for children using AI technology. Built with love for little ones, featuring engaging animations, kid-friendly speech synthesis, and a beautiful interface.

## ✨ Key Features

### 🤖 **Dual Story Generation**
- **AI-Powered Stories**: Uses GPT-2 model to generate unique, creative stories
- **Template Stories**: Fast, offline story generation as fallback
- **Smart Integration**: Seamlessly combines both approaches for reliability

### 🎭 **Personalization** 
- **Child's Name**: Stories can include the child's name for personal connection
- **25+ Animal Characters**: Lions, elephants, pandas, unicorns, and more!
- **Custom Prompts**: Add specific themes or elements to stories

### 🗣️ **Kid-Friendly Speech Synthesis**
- **Read Aloud**: One-click story narration with child-optimized voice settings
- **Gentle Voice**: Slow pace (0.5x), higher pitch (1.5x), soft volume for little ears
- **Smart Voice Selection**: Automatically finds child-like or female voices
- **Interactive Controls**: Easy start/stop buttons with visual feedback

### 🎨 **Beautiful Kid-Friendly Interface**
- **Colorful Design**: Gradient backgrounds and emoji-rich interface
- **Large Text**: Easy-to-read fonts sized for children
- **Animal Emojis**: Visual character representation (🦁🐘🦍🐷🐵)
- **Compact Layout**: Optimized spacing for better screen utilization

### 🎪 **Engaging Animations**
- **Story Loading**: Fun bouncing emojis with encouraging messages while AI generates
- **Visual Feedback**: Status indicators for all actions
- **Smooth Transitions**: Kid-friendly animations throughout

### 📚 **Story Library**
- **Pre-written Stories**: Curated collection of quality children's stories
- **Filtering**: Browse by animal character or get random stories
- **Moral Lessons**: Each story includes educational elements

## 🚀 Getting Started

### Prerequisites
- Python 3.8+ 
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sachinjadh/OnceUponAI.git
   cd OnceUponAI
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**
   - Navigate to `http://localhost:8501`
   - Start creating magical stories! ✨

## 🎯 How to Use

### Story Generator Tab
1. **Enter child's name** (optional) - makes stories personal
2. **Choose favorite animal** - from 25+ adorable options
3. **Select AI Generation** - toggle for AI vs template stories  
4. **Click "Generate story"** - watch the magical loading animation
5. **Enjoy the story** - beautifully formatted with large, readable text
6. **Read Aloud** - click the speech button for narration

### Stories Library Tab
1. **Browse by animal** - filter stories by character
2. **Random selection** - get surprise stories
3. **Read and listen** - same great speech features
4. **Learn lessons** - each story includes educational morals

## 🛠️ Technical Architecture

### Core Components
- **`app.py`**: Main Streamlit application with dual-tab interface
- **`story_generator/`**: Story generation modules
  - `template_generator.py`: Core story logic (template + AI)
  - `llm_generator.py`: GPT-2 AI integration
- **`story_store.py`**: Pre-written story library management
- **`stories.json`**: Curated story database

### AI Integration
- **Model**: GPT-2 via Hugging Face Transformers
- **Optimization**: Fast CPU inference with timeout handling
- **Prompts**: Structured prompts for child-appropriate content
- **Fallback**: Template generation if AI fails

### Speech Technology
- **Browser API**: Web Speech Synthesis for universal compatibility  
- **Voice Selection**: Smart algorithm to find child-friendly voices
- **Parameters**: Rate 0.5, Pitch 1.5, Volume 0.8 for optimal kid experience
- **Controls**: Non-blocking HTML/JavaScript implementation

## 🎨 Design Philosophy

### Child-Centered Design
- **Large, clear fonts** for developing reading skills
- **High contrast colors** for easy visibility  
- **Simple navigation** that kids can understand
- **Immediate feedback** for all interactions

### Parent-Friendly Features  
- **Safe content** - all stories are family-appropriate
- **Educational value** - stories include lessons and morals
- **Screen time optimization** - engaging but not addictive
- **Easy supervision** - clear interface for parents

## 🔧 Configuration Options

### Story Generation Settings
```python
# In template_generator.py
use_llm=True          # Enable AI generation
timeout=10            # AI generation timeout
fallback=True         # Use templates if AI fails
```

### Speech Settings  
```javascript
// Optimized for children
utterance.rate = 0.5;    # Very slow and clear
utterance.pitch = 1.5;   # Higher, friendlier pitch  
utterance.volume = 0.8;  # Gentle volume
```

## 📁 Project Structure
```
OnceUponAI/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── stories.json                    # Story database
├── story_store.py                  # Story library functions
├── story_generator/
│   ├── template_generator.py       # Core story generation
│   ├── llm_generator.py           # AI integration
│   └── __pycache__/
├── tests/
│   └── test_template_generator.py  # Unit tests
└── README.md                       # This file
```

## 🧪 Testing

### Run Tests
```bash
python -m pytest tests/
```

### Manual Testing
```bash
python smoke_test.py              # Test story generation
python test_speech.py             # Test speech functionality  
```

## 🌟 Features Highlights

### For Kids
- 🎭 **Personalized stories** with their name and favorite animals
- 🗣️ **Story narration** in gentle, child-friendly voices  
- 🎨 **Beautiful visuals** with large emojis and colorful design
- ⚡ **Instant gratification** with fast story generation
- 🎪 **Fun animations** during loading and interactions

### For Parents
- 📚 **Educational content** with moral lessons
- 🛡️ **Safe AI** - all content is child-appropriate  
- 📱 **Easy to use** - simple interface anyone can navigate
- 💾 **No data collection** - stories generated locally
- 🔊 **Volume control** - gentle audio levels

### For Developers
- 🧩 **Modular design** - easy to extend and modify
- 🤖 **AI integration** - ready for model upgrades  
- 🎨 **Modern UI** - Streamlit with custom HTML/CSS/JavaScript
- 🧪 **Well tested** - comprehensive test suite
- 📖 **Well documented** - clear code and comments

## 🚧 Future Enhancements

### Short Term
- [ ] **Voice selection dropdown** - let users choose specific voices
- [ ] **Story saving** - bookmark favorite generated stories  
- [ ] **More animals** - expand to 50+ character options
- [ ] **Story themes** - adventure, friendship, bedtime categories

### Long Term  
- [ ] **Story illustrations** - AI-generated images for stories
- [ ] **Multi-language support** - stories in different languages
- [ ] **User accounts** - save personalized preferences  
- [ ] **Mobile app** - native iOS/Android applications

## 🤝 Contributing

We welcome contributions! Please see our contributing guidelines:

1. **Fork the repository**
2. **Create feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit changes** (`git commit -m 'Add AmazingFeature'`)
4. **Push to branch** (`git push origin feature/AmazingFeature`)
5. **Open Pull Request**

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Hugging Face** - for the amazing Transformers library
- **Streamlit** - for the beautiful web framework
- **OpenAI** - for GPT-2 model architecture
- **Web Speech API** - for browser-based speech synthesis
- **All the parents and kids** who inspired this project!

---

Made with ❤️ for children everywhere. Happy storytelling! 📚✨
