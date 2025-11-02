from typing import List, Optional
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from api.core.models import Prompt

class PromptRepository:
    # CREATE
    async def create_prompt(self, db: AsyncSession, prompt: Prompt) -> Prompt:
        db.add(prompt)
        await db.commit()
        await db.refresh(prompt)
        return prompt

    # READ (One)
    async def get_prompt(self, db: AsyncSession, prompt_id: int) -> Optional[Prompt]:
        result = await db.execute(
            select(Prompt).where(Prompt.id == prompt_id, Prompt.status == 1)
        )
        return result.scalar_one_or_none()

    # READ (All)
    async def list_prompts(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Prompt]:
        result = await db.execute(
            select(Prompt).where(Prompt.status == 1).offset(skip).limit(limit)
        )
        return result.scalars().all()

    # UPDATE
    async def update_prompt(self, db: AsyncSession, prompt: Prompt) -> Prompt:
        db.add(prompt)
        await db.commit()
        await db.refresh(prompt)
        return prompt

    # DELETE (Soft delete)
    async def delete_prompt(self, db: AsyncSession, prompt: Prompt) -> None:
        prompt.status = 0
        prompt.last_updated = datetime.utcnow()
        db.add(prompt)
        await db.commit()