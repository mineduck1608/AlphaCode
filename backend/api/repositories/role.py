from typing import List, Optional
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from api.core.models import Role

class RoleRepository:
    # CREATE
    async def create_role(self, db: AsyncSession, role: Role) -> Role:
        db.add(role)
        await db.commit()
        await db.refresh(role)
        return role

    # READ (One)
    async def get_role(self, db: AsyncSession, role_id: int) -> Optional[Role]:
        result = await db.execute(
            select(Role).where(Role.id == role_id, Role.status == 1)
        )
        return result.scalar_one_or_none()

    # READ (All)
    async def list_roles(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Role]:
        result = await db.execute(
            select(Role).where(Role.status == 1).offset(skip).limit(limit)
        )
        return result.scalars().all()

    # UPDATE
    async def update_role(self, db: AsyncSession, role: Role) -> Role:
        db.add(role)
        await db.commit()
        await db.refresh(role)
        return role

    # DELETE (Soft delete)
    async def delete_role(self, db: AsyncSession, role: Role) -> None:
        role.status = 0
        role.last_updated = datetime.utcnow()
        db.add(role)
        await db.commit()