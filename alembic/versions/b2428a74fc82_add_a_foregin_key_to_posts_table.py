"""add a Foregin-Key to posts table

Revision ID: b2428a74fc82
Revises: 53b2627b77de
Create Date: 2025-04-06 23:12:34.968524

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b2428a74fc82'
down_revision: Union[str, None] = '53b2627b77de'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("creator_id",sa.Integer(),nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table= "users",
                          local_cols=["creator_id"],remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts","creator_id")
    pass
