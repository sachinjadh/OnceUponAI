# 🏗️ OnceUponAI - Application Architecture Diagram

## 📐 System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                           🌙 OnceUponAI Application                              │
├─────────────────────────────────────────────────────────────────────────────────┤
│                              Frontend Layer                                     │
├─────────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐           │
│  │   📱 Web UI     │    │  🎨 Components  │    │  🎪 Animations  │           │
│  │   (Streamlit)   │    │  HTML/CSS/JS    │    │  Loading &      │           │
│  │                 │    │  - Speech       │    │  Visual Effects │           │
│  │ • Generator Tab │    │  - Audio Player │    │  - Bounce Emojis│           │
│  │ • Library Tab   │    │  - Status       │    │  - Pulse Dots   │           │
│  │ • Kid-Friendly  │    │  - Controls     │    │  - Gradients    │           │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘           │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                            Application Layer                                    │
├─────────────────────────────────────────────────────────────────────────────────┤
│                              🐍 app.py                                         │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                        Main Streamlit App                               │   │
│  │                                                                         │   │
│  │  • Session State Management     • UI Component Rendering               │   │
│  │  • Tab Navigation              • Speech Integration                     │   │
│  │  • Loading Animations          • Error Handling                       │   │
│  │  • Story Display               • Audio Controls                       │   │
│  └─────────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                             Business Logic Layer                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐  │
│  │  🧠 Story Gen   │         │  📚 Story Store │         │  🗣️ Speech API  │  │
│  │  (Dual Engine)  │         │  Management     │         │  Integration    │  │
│  │                 │         │                 │         │                 │  │
│  │ • AI Generator  │◄────────┤ • Load Stories  │         │ • Voice Config  │  │
│  │ • Template Gen  │         │ • Filter/Search │         │ • Speech Control│  │
│  │ • Smart Routing │         │ • Random Select │         │ • Kid Optimize  │  │
│  │ • Error Handle  │         │ • JSON Parser   │         │ • Browser API   │  │
│  └─────────────────┘         └─────────────────┘         └─────────────────┘  │
│           │                            │                            │          │
│           ▼                            ▼                            ▼          │
│  ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐  │
│  │template_gen.py  │         │ story_store.py  │         │Web Speech API   │  │
│  └─────────────────┘         └─────────────────┘         └─────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              AI/ML Layer                                       │
├─────────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐  │
│  │  🤖 GPT-2 Model │         │  🧩 Transformers│         │  ⚡ Optimization │  │
│  │  Integration    │         │  Library        │         │  & Caching      │  │
│  │                 │         │                 │         │                 │  │
│  │ • Text Gen      │◄────────┤ • Model Loading │         │ • CPU Inference │  │
│  │ • Child-Safe    │         │ • Tokenization  │         │ • Timeout Handle│  │
│  │ • Prompt Eng    │         │ • Generation    │         │ • Fallback Logic│  │
│  │ • Story Format  │         │ • Post-Process  │         │ • Performance   │  │
│  └─────────────────┘         └─────────────────┘         └─────────────────┘  │
│           │                            │                            │          │
│           ▼                            ▼                            ▼          │
│  ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐  │
│  │  llm_generator  │         │ HuggingFace     │         │ CPU Optimized   │  │
│  │      .py        │         │ Transformers    │         │ Inference       │  │
│  └─────────────────┘         └─────────────────┘         └─────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              Data Layer                                        │
├─────────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐  │
│  │  📊 Stories DB  │         │  ⚙️ Config Data │         │  🎭 Templates   │  │
│  │  (JSON)         │         │  & Settings     │         │  & Fragments    │  │
│  │                 │         │                 │         │                 │  │
│  │ • Pre-written   │         │ • Voice Params  │         │ • Story Parts   │  │
│  │ • Story Library │         │ • UI Settings   │         │ • Animal Data   │  │
│  │ • Animal Meta   │         │ • Model Config  │         │ • Name Lists    │  │
│  │ • Moral Lessons │         │ • App Constants │         │ • Plot Elements │  │
│  └─────────────────┘         └─────────────────┘         └─────────────────┘  │
│           │                            │                            │          │
│           ▼                            ▼                            ▼          │
│  ┌─────────────────┐         ┌─────────────────┐         ┌─────────────────┐  │
│  │  stories.json   │         │ Streamlit State │         │ Template Arrays │  │
│  └─────────────────┘         └─────────────────┘         └─────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

## 🔄 Data Flow Architecture

```
User Request Flow:
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│   👶   │───▶│   🎨   │───▶│   🧠   │───▶│   🤖   │───▶│   📚   │
│  Child  │    │   UI   │    │ Logic  │    │   AI   │    │ Story  │
│ Input   │    │Component│    │Engine  │    │ Model  │    │Output  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
     │              │              │              │              │
     │              │              │              │              ▼
     │              │              │              │         ┌─────────┐
     │              │              │              │         │   🗣️   │
     │              │              │              │         │ Speech  │
     │              │              │              │         │Synthesis│
     │              │              │              │         └─────────┘
     │              │              │              │
     │              │              │              ▼
     │              │              │         ┌─────────┐
     │              │              │         │   📝   │
     │              │              │         │Template │
     │              │              │         │Fallback │
     │              │              │         └─────────┘
     │              │              │
     │              │              ▼
     │              │         ┌─────────┐
     │              │         │   📊   │
     │              │         │ Session │
     │              │         │ State   │
     │              │         └─────────┘
     │              │
     │              ▼
     │         ┌─────────┐
     │         │   🎪   │
     │         │Loading  │
     │         │Animation│
     │         └─────────┘
     │
     ▼
┌─────────┐
│   ⚙️   │
│ Config  │
│ Input   │
└─────────┘
```

## 🏛️ Component Architecture

### Frontend Components
```
┌─────────────────────────────────────────────────────────────────┐
│                        Frontend Layer                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ Generator   │  │   Library   │  │   Speech    │             │
│  │    Tab      │  │    Tab      │  │  Controls   │             │
│  │             │  │             │  │             │             │
│  │ • Name      │  │ • Filter    │  │ • Read      │             │
│  │ • Animal    │  │ • Browse    │  │ • Stop      │             │
│  │ • AI Toggle │  │ • Random    │  │ • Status    │             │
│  │ • Generate  │  │ • Display   │  │ • Voice Sel │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │               Story Display Area                        │   │
│  │                                                         │   │
│  │ • Animal Emoji (80px/70px)                             │   │
│  │ • Story Title                                          │   │
│  │ • Story Content (Large Font, Easy Reading)            │   │
│  │ • Loading Animation (Bouncing Emojis)                 │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Backend Services
```
┌─────────────────────────────────────────────────────────────────┐
│                      Backend Services                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐                    │
│  │  Story Engine   │    │  Speech Engine  │                    │
│  │  ┌───────────┐  │    │  ┌───────────┐  │                    │
│  │  │    AI     │  │    │  │  Browser  │  │                    │
│  │  │ GPT-2 Gen │  │    │  │ Speech API│  │                    │
│  │  └───────────┘  │    │  └───────────┘  │                    │
│  │  ┌───────────┐  │    │  ┌───────────┐  │                    │
│  │  │ Template  │  │    │  │   Voice   │  │                    │
│  │  │Generator  │  │    │  │ Selection │  │                    │
│  │  └───────────┘  │    │  └───────────┘  │                    │
│  └─────────────────┘    └─────────────────┘                    │
│                                                                 │
│  ┌─────────────────┐    ┌─────────────────┐                    │
│  │   Data Store    │    │  State Manager  │                    │
│  │  ┌───────────┐  │    │  ┌───────────┐  │                    │
│  │  │ Stories   │  │    │  │  Session  │  │                    │
│  │  │ Database  │  │    │  │   State   │  │                    │
│  │  └───────────┘  │    │  └───────────┘  │                    │
│  │  ┌───────────┐  │    │  ┌───────────┐  │                    │
│  │  │Templates  │  │    │  │Story Cache│  │                    │
│  │  │& Config   │  │    │  │& Metadata │  │                    │
│  │  └───────────┘  │    │  └───────────┘  │                    │
│  └─────────────────┘    └─────────────────┘                    │
└─────────────────────────────────────────────────────────────────┘
```

## 🔧 Technology Stack

### Core Technologies
```
┌──────────────────────────────────────────────────────────┐
│                    Tech Stack                           │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  🌐 Frontend:                                           │
│  ├── Streamlit (Web Framework)                         │
│  ├── HTML5/CSS3 (Custom Components)                    │
│  ├── JavaScript (Speech & Animations)                  │
│  └── Responsive Design                                  │
│                                                          │
│  🐍 Backend:                                            │
│  ├── Python 3.8+ (Core Language)                      │
│  ├── Streamlit Components (UI Framework)               │
│  ├── Session State Management                          │
│  └── Error Handling & Logging                          │
│                                                          │
│  🤖 AI/ML:                                              │
│  ├── HuggingFace Transformers (GPT-2)                 │
│  ├── Torch (ML Framework)                              │
│  ├── CPU Optimization                                   │
│  └── Prompt Engineering                                 │
│                                                          │
│  🗣️ Speech:                                             │
│  ├── Web Speech API (Browser Native)                   │
│  ├── Custom Voice Selection                            │
│  ├── Kid-Optimized Parameters                          │
│  └── Cross-Browser Compatibility                       │
│                                                          │
│  📊 Data:                                               │
│  ├── JSON (Story Database)                             │
│  ├── In-Memory Caching                                 │
│  ├── Template Arrays                                    │
│  └── Configuration Management                           │
└──────────────────────────────────────────────────────────┘
```

## 🚀 Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Deployment View                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 Local Development                       │   │
│  │                                                         │   │
│  │  📱 Browser ◄──── HTTP ────► 🖥️ Streamlit Server       │   │
│  │  (Client)        8501        (Python Process)          │   │
│  │                                                         │   │
│  │  Features:                   Features:                  │   │
│  │  • Interactive UI            • Story Generation         │   │
│  │  • Speech Synthesis          • AI Integration           │   │
│  │  • Animations               • Data Management          │   │
│  │  • Responsive Design        • Session Handling         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │               Production Deployment                     │   │
│  │                                                         │   │
│  │  🌐 Users ◄── HTTPS ──► 🔒 Load Balancer              │   │
│  │                              │                          │   │
│  │                              ▼                          │   │
│  │                         🐳 Container                   │   │
│  │                         (Docker/K8s)                   │   │
│  │                              │                          │   │
│  │                              ▼                          │   │
│  │                    ┌─────────────────┐                 │   │
│  │                    │ Streamlit Apps  │                 │   │
│  │                    │ (Multi-Instance)│                 │   │
│  │                    └─────────────────┘                 │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

## 📈 Performance & Scalability

### System Metrics
```
┌─────────────────────────────────────────────────────────────┐
│                   Performance Profile                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ⚡ Response Times:                                        │
│  ├── UI Load: < 2s                                        │
│  ├── Template Story: < 1s                                 │
│  ├── AI Story: 5-15s                                      │
│  └── Speech Start: < 0.5s                                 │
│                                                             │
│  💾 Memory Usage:                                          │
│  ├── Base App: ~50MB                                      │
│  ├── GPT-2 Model: ~500MB                                  │
│  ├── Session Data: ~1-5MB                                 │
│  └── Total: ~550MB                                        │
│                                                             │
│  🔄 Scalability:                                           │
│  ├── Concurrent Users: 10-50 (single instance)           │
│  ├── Stories/Hour: 200-1000                               │
│  ├── CPU Intensive: AI Generation                         │
│  └── Horizontally Scalable                                │
└─────────────────────────────────────────────────────────────┘
```

## 🔒 Security & Safety

### Child Safety Features
```
┌─────────────────────────────────────────────────────────────┐
│                   Safety Architecture                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🛡️ Content Safety:                                        │
│  ├── Curated Story Templates                              │
│  ├── AI Content Filtering                                 │
│  ├── No External API Calls                                │
│  └── Family-Friendly Prompts                              │
│                                                             │
│  🔐 Privacy Protection:                                    │
│  ├── No Data Collection                                   │
│  ├── Local Processing Only                                │
│  ├── No User Registration                                 │
│  └── Session-Based Storage                                │
│                                                             │
│  ⚙️ Technical Security:                                    │
│  ├── Input Validation                                     │
│  ├── Error Handling                                       │
│  ├── Timeout Protection                                   │
│  └── Resource Limits                                      │
└─────────────────────────────────────────────────────────────┘
```

## 🎯 Key Design Patterns

1. **🔄 Dual-Engine Pattern**: AI + Template fallback for reliability
2. **🎭 Session State Pattern**: Persistent story display without reruns  
3. **🎪 Progressive Enhancement**: Basic functionality + enhanced features
4. **🧩 Component Composition**: Modular UI components
5. **⚡ Lazy Loading**: Load heavy AI models only when needed
6. **🛡️ Graceful Degradation**: Fallback to templates if AI fails
7. **🎨 Child-First Design**: All decisions prioritize kid experience

---

*This architecture supports the OnceUponAI mission: Creating magical, safe, and educational storytelling experiences for children through modern AI technology.* ✨📚👶