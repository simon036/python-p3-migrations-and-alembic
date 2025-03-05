"""Empty Init

Revision ID: 2db2f3c4598c
Revises: d538e7a3a646
Create Date: 2025-03-05 14:31:06.718397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2db2f3c4598c'
down_revision: Union[str, None] = 'd538e7a3a646'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
