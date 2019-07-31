# For more details, see
# http://docs.sqlalchemy.org/en/latest/orm/tutorial.html#declare-a-mapping
from anthill.framework.db import db
from anthill.framework.utils import timezone
from anthill.framework.utils.asynchronous import as_future
from anthill.platform.api.internal import InternalAPIMixin
from anthill.platform.auth import RemoteUser
from sqlalchemy_utils.types import JSONType


class ApplicationVersion(db.Model):
    __tablename__ = 'application_versions'
    __table_args__ = (
        db.UniqueConstraint('app_name', 'app_version'),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_name = db.Column(db.String(128), nullable=False)
    app_version = db.Column(db.String(128), nullable=False)
    build_id = db.Column(db.Integer, db.ForeignKey('builds.id'))
    build = db.relationship('Build')


class Build(InternalAPIMixin, db.Model):
    __tablename__ = 'builds'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=timezone.now)
    description = db.Column(db.String(512), nullable=False)
    # file = db.Column(db.FileType(), nullable=False)
    payload = db.Column(JSONType, nullable=False, default={})
    enabled = db.Column(db.Boolean, nullable=False, default=True)

    async def get_user(self) -> RemoteUser:
        data = await self.internal_request('login', 'get_user', user_id=self.user_id)
        return RemoteUser(**data)
