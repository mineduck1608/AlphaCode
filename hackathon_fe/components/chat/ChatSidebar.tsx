"use client";

import { Plus, MessageSquare, Settings } from "lucide-react";

export default function ChatSidebar() {
  return (
    <div className="w-64 bg-[#202123] flex flex-col p-3 border-r border-gray-800">
      <button className="flex items-center gap-2 text-sm text-gray-200 bg-[#343541] px-3 py-2 rounded-lg hover:bg-[#3e3f4b]">
        <Plus size={16} /> New chat
      </button>
      <div className="mt-4 flex-1 overflow-y-auto text-sm space-y-2">
        <div className="flex items-center gap-2 px-2 py-2 rounded-md hover:bg-[#2a2b32] cursor-pointer">
          <MessageSquare size={16} /> Project ideas
        </div>
        <div className="flex items-center gap-2 px-2 py-2 rounded-md hover:bg-[#2a2b32] cursor-pointer">
          <MessageSquare size={16} /> Study notes
        </div>
      </div>
      <div className="mt-auto border-t border-gray-800 pt-3">
        <button className="flex items-center gap-2 w-full text-sm text-gray-400 hover:text-gray-200">
          <Settings size={16} /> Settings
        </button>
      </div>
    </div>
  );
}
