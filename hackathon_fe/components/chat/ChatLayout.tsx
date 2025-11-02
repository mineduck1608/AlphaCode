"use client";

import { useState } from "react";
import ChatSidebar from "./ChatSidebar";
import ChatHeader from "./ChatHeader";
import ChatMessageList from "./ChatMessageList";
import ChatInput from "./ChatInput";
import { mockSendMessage } from "@/lib/chatMockAPI";

// ✅ Khai báo type thống nhất cho toàn hệ thống
export type Message = {
  role: "user" | "assistant";
  content: string;
};

export default function ChatLayout() {
  // ✅ Gán type cho useState
  const [messages, setMessages] = useState<Message[]>([
    { role: "assistant", content: "Hi there 👋 How can I help you today?" },
  ]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async (text: string) => {
    if (!text.trim()) return;

    // ✅ ép type role về đúng union
    const newMessage: Message = { role: "user", content: text };
    setMessages((prev) => [...prev, newMessage]);
    setIsLoading(true);

    const reply = await mockSendMessage(text);
    setMessages((prev) => [
      ...prev,
      { role: "assistant", content: reply } as Message,
    ]);
    setIsLoading(false);
  };

  return (
    <div className="flex h-screen bg-[#111111] text-gray-200">
      <ChatSidebar />
      <div className="flex flex-col flex-1">
        <ChatHeader />
        <ChatMessageList messages={messages} isLoading={isLoading} />
        <ChatInput onSend={handleSend} />
      </div>
    </div>
  );
}
