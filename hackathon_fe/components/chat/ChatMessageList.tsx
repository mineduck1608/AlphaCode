"use client";

type Message = {
  role: "user" | "assistant";
  content: string;
};

export default function ChatMessageList({
  messages,
  isLoading,
}: {
  messages: Message[];
  isLoading: boolean;
}) {
  return (
    <div className="flex-1 overflow-y-auto p-6 space-y-6">
      {messages.map((msg, i) => (
        <div
          key={i}
          className={`flex ${
            msg.role === "user" ? "justify-end" : "justify-start"
          }`}
        >
          <div
            className={`max-w-[75%] rounded-2xl px-4 py-2 text-sm ${
              msg.role === "user"
                ? "bg-[#4b5563] text-white"
                : "bg-[#2a2b32] text-gray-100"
            }`}
          >
            {msg.content}
          </div>
        </div>
      ))}

      {isLoading && (
        <div className="flex justify-start">
          <div className="bg-[#2a2b32] text-gray-400 text-sm px-4 py-2 rounded-2xl animate-pulse">
            Thinking...
          </div>
        </div>
      )}
    </div>
  );
}
