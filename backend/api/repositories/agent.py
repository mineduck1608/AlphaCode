from typing import List, Optional
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from api.core.models import Agent

class AgentRepository:
    # CREATE
    async def create_agent(self, db: AsyncSession, agent: Agent) -> Agent:
        db.add(agent)
        await db.commit()
        await db.refresh(agent)
        return agent

    # READ (One)
    async def get_agent(self, db: AsyncSession, agent_id: int) -> Optional[Agent]:
        result = await db.execute(
            select(Agent).where(Agent.id == agent_id, Agent.status == 1)
        )
        return result.scalar_one_or_none()

    # READ (All)
    async def list_agents(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Agent]:
        result = await db.execute(
            select(Agent).where(Agent.status == 1).offset(skip).limit(limit)
        )
        return result.scalars().all()

    # UPDATE
    async def update_agent(self, db: AsyncSession, agent: Agent) -> Agent:
        db.add(agent)
        await db.commit()
        await db.refresh(agent)
        return agent

    # DELETE (Soft delete)
    async def delete_agent(self, db: AsyncSession, agent: Agent) -> None:
        agent.status = 0
        agent.last_updated = datetime.utcnow()
        db.add(agent)
        await db.commit()