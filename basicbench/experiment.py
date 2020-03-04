from datetime import datetime, timezone
import uuid


class Experiment:

    def __init__(self, name: str) -> None:
        self._name = name
        self._created: datetime = datetime.utcnow()
        self._id: str = uuid.uuid4()

    @property
    def name(self) -> str:
        return self._name

    @property
    def id(self) -> str:
        return self._id

    @property
    def created(self) -> datetime:
        return self._created.astimezone(tz=None)