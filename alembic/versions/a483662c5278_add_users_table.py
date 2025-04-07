"""add users table

Revision ID: a483662c5278
Revises: b3c45aa39281
Create Date: 2025-04-06 22:34:36.818786

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a483662c5278'
down_revision: Union[str, None] = 'b3c45aa39281'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
      sa.Column("id",sa.Integer(),primary_key=True,nullable=False),
      sa.Column("email", sa.String() , nullable= False , unique= True),
      sa.Column("password",sa.String(), nullable= False),
      sa.Column("created_at",sa.TIMESTAMP(timezone=True), nullable=False, server_default= sa.text("now()"))
      )
    pass


def downgrade() -> None:
    op.drop_table("users")
    pass
