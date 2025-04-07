"""add users table

Revision ID: 53b2627b77de
Revises: b3c45aa39281
Create Date: 2025-04-06 22:50:10.627618

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53b2627b77de'
down_revision: Union[str, None] = "a483662c5278"
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
