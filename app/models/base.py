from sqlalchemy.ext.declarative import as_declarative, declared_attr

@as_declarative()
class Base:
    metadata = None
    id: int
    __name__: str

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()