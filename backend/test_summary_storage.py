"""Test script to verify summary and embedding storage in conversation table."""

import asyncio
from sqlalchemy import select
from api.core.db import async_session
from api.core.models import Conversation

async def check_conversations():
    """Check if any conversations have summary and embeddings."""
    async with async_session() as db:
        stmt = select(Conversation).where(Conversation.status == 1)
        result = await db.execute(stmt)
        conversations = result.scalars().all()
        
        print(f"\n📊 Total conversations: {len(conversations)}\n")
        
        for conv in conversations:
            print(f"{'='*60}")
            print(f"ID: {conv.id}")
            print(f"Name: {conv.name}")
            print(f"User ID: {conv.user_id}")
            print(f"Created: {conv.created_at}")
            print(f"Last Updated: {conv.last_updated}")
            print(f"\n✅ Has Summary: {bool(conv.summary)}")
            if conv.summary:
                print(f"   Length: {len(conv.summary)} chars")
                print(f"   Preview: {conv.summary[:200]}...")
            
            print(f"\n✅ Has Embedding: {bool(conv.summary_embedding)}")
            if conv.summary_embedding:
                print(f"   Dimensions: {len(conv.summary_embedding)}")
                print(f"   First 5 values: {conv.summary_embedding[:5]}")
            
            print(f"{'='*60}\n")
        
        # Count conversations with/without data
        with_summary = sum(1 for c in conversations if c.summary)
        with_embedding = sum(1 for c in conversations if c.summary_embedding)
        
        print(f"\n📈 Statistics:")
        print(f"   With Summary: {with_summary}/{len(conversations)}")
        print(f"   With Embedding: {with_embedding}/{len(conversations)}")

if __name__ == "__main__":
    asyncio.run(check_conversations())
