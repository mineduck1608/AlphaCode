/**
 * Chat Component - AI Agent Chat Interface
 * 
 * Component để chat với AI agent qua WebSocket
 */

'use client';

import { useState, useRef, useEffect } from 'react';
import { useWebSocket, type Message } from '@/app/lib/hooks/useWebSocket';
import { Send, Loader2, Circle } from 'lucide-react';
import { cn } from '@/app/lib/utils';

interface ChatProps {
  websocketUrl?: string;
  className?: string;
  placeholder?: string;
  welcomeMessage?: string;
}

export function Chat({
  websocketUrl = 'ws://localhost:8000/ws/chat',
  className,
  placeholder = 'Nhập tin nhắn... (thử gõ /help)',
  welcomeMessage,
}: ChatProps) {
  const [input, setInput] = useState('');
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const { messages, connected, connecting, sendMessage, connect, disconnect } = useWebSocket({
    url: websocketUrl,
    autoConnect: false,
    onOpen: () => {
      console.log('Chat connected!');
    },
    onError: (error) => {
      console.error('Chat connection error:', error);
    },
  });

  // Auto scroll to bottom khi có tin nhắn mới
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  // Focus input khi connected
  useEffect(() => {
    if (connected) {
      inputRef.current?.focus();
    }
  }, [connected]);

  const handleSend = () => {
    const text = input.trim();
    if (!text || !connected) return;

    sendMessage(text);
    setInput('');
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const renderMessage = (message: Message, index: number) => {
    const isUser = message.role === 'user';
    const isSystem = message.type === 'system';
    const isError = message.type === 'error';

    return (
      <div
        key={index}
        className={cn(
          'flex w-full mb-4',
          isUser ? 'justify-end' : 'justify-start'
        )}
      >
        <div
          className={cn(
            'max-w-[80%] rounded-lg px-4 py-2 break-words',
            isUser && 'bg-blue-500 text-white',
            isSystem && 'bg-yellow-50 text-yellow-800 border border-yellow-200',
            isError && 'bg-red-50 text-red-800 border border-red-200',
            !isUser && !isSystem && !isError && 'bg-gray-100 text-gray-900'
          )}
        >
          <div className="text-sm">{message.content}</div>
          <div className="text-xs opacity-70 mt-1">
            {new Date(message.timestamp).toLocaleTimeString('vi-VN', {
              hour: '2-digit',
              minute: '2-digit',
            })}
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className={cn('flex flex-col h-full bg-white rounded-lg shadow-lg', className)}>
      {/* Header */}
      <div className="flex items-center justify-between px-6 py-4 border-b">
        <div className="flex items-center gap-3">
          <div className="relative">
            <div className="w-10 h-10 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center text-white font-bold">
              AI
            </div>
            <Circle
              className={cn(
                'absolute -bottom-1 -right-1 w-4 h-4',
                connected ? 'fill-green-500 text-green-500' : 'fill-gray-400 text-gray-400'
              )}
            />
          </div>
          <div>
            <h3 className="font-semibold text-gray-900">AI Agent Chat</h3>
            <p className="text-xs text-gray-500">
              {connecting && 'Đang kết nối...'}
              {connected && 'Đang hoạt động'}
              {!connecting && !connected && 'Chưa kết nối'}
            </p>
          </div>
        </div>

        <button
          onClick={() => (connected ? disconnect() : connect())}
          className={cn(
            'px-4 py-2 rounded-lg text-sm font-medium transition-colors',
            connected
              ? 'bg-red-500 hover:bg-red-600 text-white'
              : 'bg-green-500 hover:bg-green-600 text-white'
          )}
        >
          {connecting && <Loader2 className="w-4 h-4 animate-spin" />}
          {!connecting && (connected ? 'Ngắt kết nối' : 'Kết nối')}
        </button>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto px-6 py-4">
        {!connected && !connecting && messages.length === 0 && (
          <div className="flex flex-col items-center justify-center h-full text-center text-gray-500">
            <div className="w-16 h-16 rounded-full bg-gray-100 flex items-center justify-center mb-4">
              <Send className="w-8 h-8 text-gray-400" />
            </div>
            <p className="text-lg font-medium">Chào mừng đến với AI Chat</p>
            <p className="text-sm mt-2">
              {welcomeMessage || 'Click "Kết nối" để bắt đầu chat với AI agent'}
            </p>
          </div>
        )}

        {messages.map((message, index) => renderMessage(message, index))}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="px-6 py-4 border-t">
        <div className="flex gap-2">
          <input
            ref={inputRef}
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder={placeholder}
            disabled={!connected}
            className={cn(
              'flex-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
              !connected && 'bg-gray-50 cursor-not-allowed'
            )}
          />
          <button
            onClick={handleSend}
            disabled={!connected || !input.trim()}
            className={cn(
              'px-6 py-2 rounded-lg font-medium transition-colors flex items-center gap-2',
              connected && input.trim()
                ? 'bg-blue-500 hover:bg-blue-600 text-white'
                : 'bg-gray-300 text-gray-500 cursor-not-allowed'
            )}
          >
            <Send className="w-4 h-4" />
            Gửi
          </button>
        </div>
        
        {connected && (
          <div className="mt-2 text-xs text-gray-500">
            Nhấn <kbd className="px-2 py-1 bg-gray-100 rounded">Enter</kbd> để gửi
          </div>
        )}
      </div>
    </div>
  );
}
