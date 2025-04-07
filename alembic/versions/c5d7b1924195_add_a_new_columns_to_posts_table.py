"""add a new columns to posts table

Revision ID: c5d7b1924195
Revises: b2428a74fc82
Create Date: 2025-04-06 23:31:07.970073

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5d7b1924195'
down_revision: Union[str, None] = 'b2428a74fc82'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("published", sa.Boolean(), 
                                     nullable= False, server_default= "True"))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True), 
                                     nullable= False, server_default= sa.text("NOW()")), )
    pass


def downgrade() -> None:
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
    pass
