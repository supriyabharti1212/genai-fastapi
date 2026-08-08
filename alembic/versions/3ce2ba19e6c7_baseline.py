"""baseline

Revision ID: 3ce2ba19e6c7
Revises: 
Create Date: 2026-08-08 21:21:37.671889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ce2ba19e6c7'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "chat_history",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("question", sa.Text(), nullable=False),
        sa.Column("answer", sa.Text(), nullable=False),
        sa.Column("model", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_index(
        "ix_chat_history_id",
        "chat_history",
        ["id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_chat_history_id", table_name="chat_history")
    op.drop_table("chat_history")
