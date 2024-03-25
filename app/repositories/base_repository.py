from abc import ABC, abstractmethod

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

class AbstractRepository(ABC):
    @abstractmethod
    async def add_one(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def find_all(self):
        raise NotImplementedError

class Repository(AbstractRepository):
    model = None

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def add_one(self, data: dict):
        stmt = insert(self.model).values(**data).returning(self.model)
        res = await self.session.execute(stmt)
        return res.scalar_one()

    async def find_all(self):
        query = select(self.model)
        result = await self.session.execute(query)
        return result.scalars().all()
