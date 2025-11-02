"use client";

import { useState } from "react";
import { Paperclip, Mic, Send } from "lucide-react";

export default function ChatInput({
  onSend,
}: {
  onSend: (text: string) => void;
}) {
  const [input, setInput] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;
    onSend(input);
    setInput("");
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="border-t border-gray-800 bg-[#1e1f24] p-4 flex items-center gap-3"
    >
      <button
        type="button"
        className="text-gray-400 hover:text-gray-200 p-2 rounded-md hover:bg-[#2a2b32]"
      >
        <Paperclip size={18} />
      </button>
      <input
        className="flex-1 bg-transparent text-gray-200 text-sm outline-none placeholder-gray-500"
        placeholder="Send a message..."
        value={input}
        onChange={(e) => setInput(e.target.value)}
      />
      <button
        type="button"
        className="text-gray-400 hover:text-gray-200 p-2 rounded-md hover:bg-[#2a2b32]"
      >
        <Mic size={18} />
      </button>
      <button
        type="submit"
        className="bg-[#10a37f] text-white px-3 py-2 rounded-md hover:bg-[#0e8f6d]"
      >
        <Send size={16} />
      </button>
    </form>
  );
}
