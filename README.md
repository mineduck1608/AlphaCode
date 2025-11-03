# 🚀 AlphaCode - AI-Powered Requirements Engineering Assistant

<div align="center">

![AlphaCode Logo](hackathon_fe/public/logo2.png)

**An intelligent chatbot system for Requirements Engineering with real-time WebSocket communication**

[![Next.js](https://img.shields.io/badge/Next.js-16.0-black?logo=next.js)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-316192?logo=postgresql)](https://www.postgresql.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?logo=typescript)](https://www.typescriptlang.org/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://www.python.org/)

[Features](#features) • [Architecture](#architecture) • [Installation](#installation) • [Team](#team)

</div>

---

## 📋 Mô Tả Dự Án

**AlphaCode** là một hệ thống trợ lý AI thông minh chuyên biệt cho lĩnh vực **Requirements Engineering** (Kỹ thuật Yêu cầu). Dự án được phát triển với mục tiêu hỗ trợ các nhóm phát triển phần mềm trong việc:

- 📝 **Thu thập và phân tích yêu cầu**: Tự động phân tích và chuẩn hóa các yêu cầu từ người dùng
- 🤖 **Tương tác thời gian thực**: Giao tiếp với AI Agent qua WebSocket với typing indicator
- 📊 **Sinh Context Diagram**: Tự động tạo sơ đồ ngữ cảnh từ các yêu cầu đã phân tích
- 💬 **Chat History Management**: Lưu trữ và quản lý lịch sử hội thoại
- 🔗 **Share Conversations**: Chia sẻ các cuộc trò chuyện qua link công khai
- 🎨 **Modern UI/UX**: Giao diện tối hiện đại với theme xanh dương chuyên nghiệp

### 🎯 Use Case Chính

```
User → Input Requirements → AI Analysis → Generate Context Diagram
                ↓
          Store in Database
                ↓
          Share Results
```

---

## ✨ Features

### 🎨 Frontend Features

- ✅ **Real-time Chat Interface** với WebSocket
- ✅ **Typing Indicator** - Hiển thị khi AI đang trả lời
- ✅ **Message History** - Lưu trữ local và database
- ✅ **Share Conversation** - Tạo link chia sẻ công khai
- ✅ **Dual Tabs Sidebar** - Recent & Shared conversations
- ✅ **Preview Panel** - Xem kết quả phân tích
- ✅ **Dark Blue Theme** - Giao diện chuyên nghiệp
- ✅ **Responsive Design** - Tương thích mọi thiết bị
- ✅ **Authentication** - Login/Logout system

### 🔧 Backend Features

- ✅ **FastAPI WebSocket Server** - Real-time bidirectional communication
- ✅ **AI Agent System** - Chat agent với Google Gemini
- ✅ **Session Management** - Quản lý phiên làm việc
- ✅ **Database Integration** - PostgreSQL với SQLAlchemy ORM
- ✅ **RESTful API** - Full CRUD operations
- ✅ **CORS Middleware** - Cross-origin support
- ✅ **Error Handling** - Comprehensive error management
- ✅ **MCP Integration** - Model Context Protocol support

---

## 🏗️ Architecture & Technology Stack

### 📐 System Architecture Overview

```
                    ┌─────────────────────────────────────────────┐
                    │          Frontend (Next.js 16)              │
                    │  ┌──────────────┐    ┌──────────────┐      │
                    │  │ Chat UI      │    │ Share UI     │      │
                    │  │ Components   │    │ Components   │      │
                    │  └──────────────┘    └──────────────┘      │
                    │           │                  │              │
                    │           ▼                  ▼              │
                    │  ┌────────────────────────────────┐        │
                    │  │   WebSocket Hook Manager       │        │
                    │  │  (useWebSocket.ts)            │        │
                    │  └────────────────────────────────┘        │
                    └─────────────┬───────────────────────────────┘
                                  │ WebSocket + REST API
                                  ▼
                    ┌─────────────────────────────────────────────┐
                    │       Backend (FastAPI + Uvicorn)           │
                    │  ┌──────────────────────────────────┐      │
                    │  │    WebSocket Server              │      │
                    │  │   /ws/chat endpoint              │      │
                    │  └──────────────────────────────────┘      │
                    │           │                                 │
                    │           ▼                                 │
                    │  ┌──────────────────────────────────┐      │
                    │  │   Chat Agent (Orchestrator)      │      │
                    │  │   - Google Gemini 2.0 Flash      │      │
                    │  │   - Session Management           │      │
                    │  │   - Function Calling Router      │      │
                    │  └──────────────────────────────────┘      │
                    │           │                                 │
                    │           ▼                                 │
                    │  ┌─────────────────────────────────────┐   │
                    │  │   MCP (Model Context Protocol)      │   │
                    │  │        Multi-Agent System           │   │
                    │  └─────────────────────────────────────┘   │
                    │     │      │        │        │        │    │
                    └─────┼──────┼────────┼────────┼────────┼────┘
                          │      │        │        │        │
                ┌─────────┴──┐ ┌─┴──┐ ┌──┴───┐ ┌──┴───┐ ┌─┴────┐
                │ Collector  │ │Anal│ │Requi │ │Report│ │Vector│
                │   Agent    │ │yzer│ │rement│ │ er   │ │Search│
                └────────────┘ └────┘ └──────┘ └──────┘ └──────┘
                          │                                   │
                          ▼                                   ▼
                    ┌─────────────────┐             ┌──────────────┐
                    │   PostgreSQL    │             │  ChromaDB    │
                    │   Database      │             │  (Vectors)   │
                    └─────────────────┘             └──────────────┘
```

### 🔧 Technology Stack

#### **Frontend Technologies**

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Framework** | Next.js | 16.0.1 | App Router, SSR, API Routes |
| **Language** | TypeScript | 5.x | Type-safe development |
| **Styling** | Tailwind CSS | 4.x | Utility-first CSS framework |
| **UI Library** | Lucide React | Latest | Beautiful icon components |
| **State Management** | React Hooks | 19.x | useState, useEffect, useCallback, useRef |
| **Real-time Communication** | WebSocket API | Native | Bidirectional client-server communication |
| **HTTP Client** | Fetch API | Native | RESTful API calls |
| **Routing** | Next.js App Router | 16.0 | File-based routing system |
| **Data Persistence** | LocalStorage | Browser API | Client-side chat history caching |

**Frontend Architecture Patterns:**
- **Custom Hooks**: `useWebSocket` for WebSocket state management
- **Component Composition**: Modular, reusable components
- **Server Components**: Static generation where possible
- **Client Components**: Interactive UI with "use client" directive

#### **Backend Technologies**

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| **Framework** | FastAPI | 0.104.1 | High-performance async web framework |
| **Language** | Python | 3.11+ | Backend logic and AI integration |
| **ASGI Server** | Uvicorn | 0.24.0 | WebSocket + HTTP server |
| **Database** | PostgreSQL | 16.x | Relational data storage |
| **ORM** | SQLAlchemy | 2.0+ | Async database operations |
| **Migration Tool** | Alembic | Latest | Database schema versioning |
| **AI Model** | Google Gemini | 2.0 Flash | Large Language Model for chat |
| **Embeddings** | Google Gemini | text-embedding-004 | Vector embeddings for search |
| **Vector DB** | ChromaDB | Latest | Semantic search storage |
| **Protocol** | MCP (Model Context Protocol) | Custom | Multi-agent communication via STDIO |

**Backend Architecture Patterns:**
- **Async/Await**: Non-blocking I/O operations
- **Dependency Injection**: FastAPI's built-in DI system
- **Repository Pattern**: Data access abstraction
- **Service Layer**: Business logic separation
- **Multi-Agent System**: MCP-based microservices

### 🤖 Multi-Agent System (MCP Architecture)

AlphaCode sử dụng **Model Context Protocol (MCP)** để orchestrate multiple specialized AI agents:

```
                   ┌──────────────────────────┐
                   │   Chat Agent             │
                   │   (Main Orchestrator)    │
                   │   - Gemini 2.0 Flash     │
                   │   - Function Calling     │
                   └────────────┬─────────────┘
                                │
                                │ Routes to appropriate agent
                                │
            ┌───────────────────┼───────────────────┐
            │                   │                   │
            ▼                   ▼                   ▼
    ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
    │  Collector   │   │   Analyzer   │   │ Requirement  │
    │   Agent      │→  │    Agent     │→  │    Agent     │
    └──────────────┘   └──────────────┘   └──────────────┘
            │                   │                   │
            └───────────────────┴───────────────────┘
                                │
                                ▼
                        ┌──────────────┐
                        │   Reporter   │
                        │    Agent     │
                        └──────────────┘
                                │
                                ▼
                        ┌──────────────┐
                        │  Validator   │
                        │    Agent     │
                        └──────────────┘
```

#### **MCP Agents Details**

**1. 📥 Collector Agent** (`mcp_collector`)
- **Purpose**: Thu thập và chuẩn hóa requirements
- **Functions**:
  - `ingest_raw`: Nhận raw text input
  - `normalize`: Chuẩn hóa format
  - `extract_stories`: Trích xuất user stories
- **Technology**: Python + Gemini API
- **Prompt**: `prompts/collector.yml`

**2. 🔍 Analyzer Agent** (`mcp_analyzer`)
- **Purpose**: Phân tích chất lượng requirements
- **Functions**:
  - `analyze_requirement`: Phát hiện vấn đề (ambiguity, conflicts)
  - `analyze_stories`: Phân tích user stories
  - `suggest_improvements`: Đề xuất cải thiện
- **Detection**: Ambiguity, Incompleteness, Non-testable statements
- **Technology**: Python + Gemini API
- **Prompt**: `prompts/analyzer.yml`

**3. 📋 Requirement Agent** (`mcp_requirement`)
- **Purpose**: Xác định và ưu tiên requirements
- **Functions**:
  - `identify_requirements`: Xác định core requirements
  - `prioritize`: Tính priority score
- **Scoring Logic**:
  - Length-based scoring
  - Keyword detection (critical, must, should)
  - Acceptance criteria presence
- **Technology**: Python + Gemini API
- **Prompt**: `prompts/requirement.yml`

**4. 📊 Reporter Agent** (`mcp_reporter`)
- **Purpose**: Sinh Context Diagram và báo cáo
- **Functions**:
  - `generate_report`: Tạo Mermaid diagram
- **Output**:
  - Context Diagram (Mermaid syntax)
  - Requirements summary
  - Actor identification
- **Technology**: Python + Gemini API
- **Prompt**: `prompts/reporter.yml`

**5. ✅ Validator Agent** (`mcp_validator`)
- **Purpose**: Validate chất lượng output
- **Functions**:
  - `validate_requirements`: Kiểm tra structure
  - `validate_report`: Kiểm tra completeness
  - `llm_check`: LLM-based validation
- **Technology**: Python + Gemini API

**6. 🔎 Vector Search Agent** (`mcp_vector`)
- **Purpose**: Semantic search và similarity matching
- **Functions**:
  - `ingest`: Lưu documents với embeddings
  - `search`: Tìm kiếm semantic với top_k results
- **Technology**: ChromaDB + Gemini Embeddings
- **Model**: `text-embedding-004`

#### **MCP Communication Flow**

```python
# Example: User sends requirements
User: "I want a login system with OAuth"
  ↓
ChatAgent (Orchestrator)
  ↓
1. Collector.ingest_raw() → Normalize text
  ↓
2. Collector.extract_stories() → ["As a user, I want to login..."]
  ↓
3. Analyzer.analyze_stories() → Detect issues, suggest improvements
  ↓
4. Requirement.identify_requirements() → Extract core requirements
  ↓
5. Requirement.prioritize() → Assign priority scores
  ↓
6. Reporter.generate_report() → Create Context Diagram (Mermaid)
  ↓
7. Validator.validate_report() → Ensure quality
  ↓
Response: Context Diagram + Analysis Results
```

### 🎯 Core Features Architecture

#### **1. Real-time Chat System**

**Frontend Flow:**
```typescript
User Input → ChatInput Component
           ↓
     useWebSocket Hook
           ↓
  WebSocket.send(message)
           ↓
     Backend WebSocket
           ↓
  ChatAgent.handle_message()
           ↓
     MCP Agent Pipeline
           ↓
  Response via WebSocket
           ↓
  ChatMessageList renders
```

**Key Components:**
- `useWebSocket.ts`: WebSocket lifecycle management
- `ChatLayout.tsx`: Main container với session state
- `TypingIndicator.tsx`: Real-time agent typing status
- `ChatMessageList.tsx`: Message rendering với streaming effect

#### **2. Share Conversation System**

**Architecture:**
```
User clicks "Share Chat"
        ↓
ShareDialog Component
        ↓
generateShareLink() API
        ↓
Create SharedConversation record
        ↓
Generate unique share URL
        ↓
Public route: /share/[shareId]
        ↓
Read-only view với message history
```

**Components:**
- `ShareDialog.tsx`: Modal để generate/revoke links
- `SharedConversationsList.tsx`: Danh sách conversations đã share
- `/share/[shareId]/page.tsx`: Public share viewer

#### **3. Session Management**

**Backend:**
```python
WebSocket Connection
        ↓
SessionManager.register()
        ↓
Assign unique session_id
        ↓
Create ChatAgent instance
        ↓
Store in active_sessions dict
        ↓
Handle messages per session
        ↓
SessionManager.unregister() on disconnect
```

**Features:**
- Session-based agent instances
- Conversation history per session
- Auto-cleanup on disconnect
- Session statistics tracking

### 💾 Data Flow

```
┌─────────────────────────────────────────────────────────┐
│                    User Action                          │
└───────────────────────┬─────────────────────────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │   Frontend State Management   │
        │   - React useState            │
        │   - LocalStorage caching      │
        └───────────────┬───────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │   WebSocket Communication     │
        │   - Bidirectional messaging   │
        │   - JSON message format       │
        └───────────────┬───────────────┘
                        │
                        ▼
        ┌───────────────────────────────┐
        │    Backend API Layer          │
        │    - FastAPI endpoints        │
        │    - WebSocket handler        │
        └───────────────┬───────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
┌──────────────┐              ┌──────────────┐
│ Service Layer│              │ MCP Adapter  │
│ - Business   │              │ - Agent      │
│   Logic      │              │   Routing    │
└──────┬───────┘              └──────┬───────┘
       │                             │
       ▼                             ▼
┌──────────────┐              ┌──────────────┐
│ Repository   │              │ MCP Agents   │
│ - Data Access│              │ - STDIO      │
└──────┬───────┘              │   Protocol   │
       │                      └──────────────┘
       ▼
┌──────────────┐
│  PostgreSQL  │
│  Database    │
└──────────────┘
```

---

## 🚀 Installation

### Prerequisites

- **Node.js** 18+ và npm/yarn
- **Python** 3.11+
- **PostgreSQL** 16+
- **Git**

### 1️⃣ Clone Repository

```bash
git clone https://github.com/mineduck1608/AlphaCode.git
cd AlphaCode
```

### 2️⃣ Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env

# Edit .env with your configuration:
# - DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/alphacode
# - GENAI_API_KEY=your_google_gemini_api_key
# - LLM_MODEL=gemini-1.5-flash

# Run database migrations
alembic upgrade head

# Fix message column if needed
python fix_message_column.py

# Start backend server
python run.py
# or
uvicorn api.main:app --reload --port 8000
```

Backend sẽ chạy tại: `http://localhost:8000`

WebSocket endpoint: `ws://localhost:8000/ws/chat`

### 3️⃣ Frontend Setup

```bash
# Navigate to frontend
cd hackathon_fe

# Install dependencies
npm install
# or
yarn install

# Setup environment variables
cp .env.example .env.local

# Edit .env.local (optional for ngrok)
# NEXT_PUBLIC_API_URL=http://localhost:8000
# NEXT_PUBLIC_WS_URL=ws://localhost:8000

# Start development server
npm run dev
# or
yarn dev
```

Frontend sẽ chạy tại: `http://localhost:3000`

### 4️⃣ Database Setup

```sql
-- Create PostgreSQL database
CREATE DATABASE alphacode;

-- Create user (optional)
CREATE USER alphacode_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE alphacode TO alphacode_user;
```

---

## 🎮 Usage

### 1. Truy cập ứng dụng

Mở trình duyệt và truy cập: `http://localhost:3000`

### 2. Login (Mock)

- Email: `test@example.com`
- Password: bất kỳ

### 3. Bắt đầu Chat

1. Click "New Chat" để tạo cuộc trò chuyện mới
2. Nhập yêu cầu của bạn vào ô chat
3. AI Agent sẽ phản hồi với typing indicator
4. Lịch sử chat tự động lưu

## 👥 Team

<table>
  <tr>
    <th>Họ Tên</th>
    <th>MSSV</th>
    <th>Email</th>
    <th>Số Điện Thoại</th>
  </tr>
  <tr>
    <td><b>Võ Huy Hoàng</b></td>
    <td>SE184022</td>
    <td>hoangvhse184022@fpt.edu.vn</td>
    <td>0913428487</td>
  </tr>
  <tr>
    <td><b>Đặng Minh Đức</b></td>
    <td>SE183990</td>
    <td>ducdmse183990@fpt.edu.vn</td>
    <td>0977300916</td>
  </tr>
  <tr>
    <td><b>Đặng Thành Ngọc</b></td>
    <td>SE183959</td>
    <td>ngocdtse183959@fpt.edu.vn</td>
    <td>0846410449</td>
  </tr>
  <tr>
    <td><b>Đặng Chu Quốc Khánh</b></td>
    <td>SE183880</td>
    <td>khanhdcqse183880@fpt.edu.vn</td>
    <td>0364339088</td>
  </tr>
  <tr>
    <td><b>Võ Khắc Xuân Nguyên</b></td>
    <td>SE183970</td>
    <td>nguyenvkxse183970@fpt.edu.vn</td>
    <td>0982784074</td>
  </tr>
</table>

---

## 🐛 Troubleshooting

### Common Issues

#### 1. WebSocket Connection Failed

```bash
# Check if backend is running
curl http://localhost:8000/health

# Check WebSocket endpoint
wscat -c ws://localhost:8000/ws/chat
```

#### 2. Database Connection Error

```bash
# Verify PostgreSQL is running
psql -U postgres -c "SELECT version();"

# Check database exists
psql -U postgres -l | grep alphacode

# Test connection
psql -U alphacode_user -d alphacode -c "SELECT 1;"
```

#### 3. Message Content Too Long Error

```sql
-- Run this SQL to fix VARCHAR(255) → TEXT
ALTER TABLE message ALTER COLUMN content TYPE TEXT;
```

```bash
# Or run the Python script
cd backend
python fix_message_column.py
```

#### 4. CORS Error

Đảm bảo backend có CORS middleware:

```python
# In api/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📝 Development

### Running Tests

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd hackathon_fe
npm test
```

### Code Formatting

```bash
# Backend (Python)
black backend/
isort backend/

# Frontend (TypeScript)
cd hackathon_fe
npm run lint
npm run format
```

### Database Migrations

```bash
cd backend

# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

---

## 🔮 Future Enhancements

- [ ] User authentication với JWT
- [ ] File upload support
- [ ] Voice input/output
- [ ] Multi-language support
- [ ] Export chat history to PDF
- [ ] Advanced analytics dashboard
- [ ] Team collaboration features
- [ ] Integration với Jira/GitHub
- [ ] Mobile app (React Native)
- [ ] Docker containerization

---

## 📄 License

This project is developed for educational purposes as part of SEAL Hackathon Contest

---

## 🙏 Acknowledgments

- **FPT University** - For providing the learning environment
- **Google Gemini** - For AI capabilities
- **FastAPI** - For excellent WebSocket support
- **Next.js** - For modern React framework
- **Vercel** - For deployment platform

---

## 📞 Contact & Support

For questions, issues, or contributions:

- **Repository**: [github.com/mineduck1608/AlphaCode](https://github.com/mineduck1608/AlphaCode)
- **Issues**: [github.com/mineduck1608/AlphaCode/issues](https://github.com/mineduck1608/AlphaCode/issues)

---

<div align="center">

**Made with ❤️ by AlphaCode Team**

⭐ Star us on GitHub if you find this project helpful!

</div>