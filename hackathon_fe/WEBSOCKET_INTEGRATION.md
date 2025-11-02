# WebSocket Chat Integration - Frontend

## 📦 Files Created

### 1. WebSocket Hook
**`app/lib/hooks/useWebSocket.ts`**
- Custom React hook để quản lý WebSocket connection
- Auto-reconnect khi bị disconnect
- Message parsing và state management
- Type-safe với TypeScript

### 2. Chat Component  
**`app/components/chat/Chat.tsx`**
- Standalone chat component với UI hoàn chỉnh
- Sử dụng `useWebSocket` hook
- Real-time messaging
- Connection status indicator

### 3. Connection Status
**`app/components/chat/ConnectionStatus.tsx`**
- Badge hiển thị trạng thái kết nối
- Visual indicator (green/yellow/red)

### 4. Updated ChatLayout
**`components/chat/ChatLayout.tsx`**
- Tích hợp WebSocket vào chat layout hiện có
- Thay thế mock API bằng real WebSocket connection
- Xử lý messages từ backend agent

## 🚀 Cách sử dụng

### Bước 1: Chạy Backend WebSocket Server

```powershell
cd d:\Code\Hackathon\AlphaCode\backend\api-gateway
python -m pip install -r requirements.txt
python main.py
```

Server sẽ chạy tại: `ws://localhost:8000/ws/chat`

### Bước 2: Chạy Frontend

```powershell
cd d:\Code\Hackathon\AlphaCode\hackathon_fe
npm run dev
```

Frontend sẽ chạy tại: `http://localhost:3000`

### Bước 3: Test Chat

1. Mở browser: `http://localhost:3000/chat`
2. Login nếu cần
3. ChatLayout sẽ tự động kết nối WebSocket
4. Gõ tin nhắn và gửi
5. Agent sẽ trả lời real-time qua WebSocket

## 💡 Features

### WebSocket Hook (`useWebSocket`)

```typescript
const { 
  messages,      // Danh sách messages
  connected,     // Trạng thái kết nối
  connecting,    // Đang kết nối
  sendMessage,   // Hàm gửi message
  connect,       // Kết nối thủ công
  disconnect,    // Ngắt kết nối
} = useWebSocket({
  url: 'ws://localhost:8000/ws/chat',
  autoConnect: true,
  reconnectInterval: 3000,
  maxReconnectAttempts: 5,
  onMessage: (msg) => console.log(msg),
});
```

### Message Format

Messages được parse tự động:

```typescript
interface Message {
  type: 'text' | 'error' | 'system' | 'typing';
  content: string;
  metadata?: Record<string, any>;
  timestamp: string;
  role?: 'user' | 'assistant' | 'system';
}
```

### Commands Available

Gõ trong chat:
- `ping` - Test connection
- `/help` - Show available commands
- `/history` - Show conversation history
- `/clear` - Clear history
- `/whoami` - Show session info

## 🔧 Configuration

Để đổi WebSocket URL, edit trong `ChatLayout.tsx`:

```typescript
const { connected, sendMessage: wsSendMessage } = useWebSocket({
  url: 'ws://your-server:port/ws/chat',  // <-- Đổi URL ở đây
  autoConnect: true,
  // ...
});
```

## 🎯 Architecture

```
Frontend (Next.js)
└── ChatLayout Component
    └── useWebSocket Hook
        └── WebSocket Connection
            ↕️
Backend (FastAPI)
└── /ws/chat endpoint
    └── ChatAgent
        └── Message Processing
```

## ✅ What's Working

- ✅ WebSocket connection từ frontend đến backend
- ✅ Real-time bi-directional messaging
- ✅ Auto-reconnect khi mất kết nối
- ✅ Message history persistence (localStorage)
- ✅ Agent commands (/help, /history, etc.)
- ✅ Connection status indicator
- ✅ Error handling & fallback messages

## 📝 Next Steps

1. **Thêm typing indicator**: Show khi agent đang typing
2. **File upload**: Gửi files qua WebSocket
3. **Multi-agent routing**: Chọn agent type khác nhau
4. **Message reactions**: Like/dislike messages
5. **Voice input**: Speech-to-text
6. **Stream responses**: Streaming text từ LLM

## 🐛 Troubleshooting

### WebSocket không kết nối được

1. Kiểm tra backend đang chạy:
   ```powershell
   curl http://localhost:8000/health
   ```

2. Kiểm tra URL đúng trong code:
   - Backend: `ws://localhost:8000/ws/chat`
   - Không phải `http://` mà là `ws://`

3. Check browser console cho errors

### Messages không hiển thị

1. Mở DevTools → Network → WS tab
2. Xem WebSocket messages
3. Kiểm tra message format

### Auto-reconnect không hoạt động

- Check `maxReconnectAttempts` trong hook config
- Xem console logs cho reconnect attempts

## 📚 References

- Backend README: `backend/api-gateway/README.md`
- WebSocket Hook: `app/lib/hooks/useWebSocket.ts`
- Chat Component: `app/components/chat/Chat.tsx`
