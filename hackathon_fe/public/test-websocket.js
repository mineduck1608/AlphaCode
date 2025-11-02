/**
 * Quick Test - Kiểm tra WebSocket connection đơn giản
 * 
 * Chạy file này trong browser console để test connection
 */

console.log('🔧 Testing WebSocket Connection...');

// Close tất cả connections cũ
if (window.testWs) {
  window.testWs.close();
  console.log('Closed old connection');
}

// Tạo connection mới
const ws = new WebSocket('ws://localhost:8000/ws/chat');
window.testWs = ws;

ws.onopen = () => {
  console.log('✅ Connected!');
  console.log('Try: window.testWs.send("Hello")');
};

ws.onmessage = (event) => {
  console.log('📨 Received:', event.data);
  try {
    const data = JSON.parse(event.data);
    console.log('Parsed:', data);
  } catch (e) {
    console.log('Plain text:', event.data);
  }
};

ws.onerror = (error) => {
  console.error('❌ Error:', error);
};

ws.onclose = () => {
  console.log('🔌 Disconnected');
};

// Helper function
window.sendTest = (msg) => {
  if (window.testWs && window.testWs.readyState === WebSocket.OPEN) {
    window.testWs.send(msg);
    console.log('Sent:', msg);
  } else {
    console.error('WebSocket not connected!');
  }
};

console.log('Use: sendTest("your message")');
