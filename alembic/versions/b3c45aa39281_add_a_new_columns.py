"""add a new columns

Revision ID: b3c45aa39281
Revises: 118bf733b3a0
Create Date: 2025-04-06 22:10:32.073801

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b3c45aa39281'
down_revision: Union[str, None] = '118bf733b3a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("content",sa.String(),nullable= False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
