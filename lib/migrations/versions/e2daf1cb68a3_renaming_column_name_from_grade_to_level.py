"""Renaming column name from grade to level

Revision ID: e2daf1cb68a3
Revises: 791279dd0760
Create Date: 2023-12-13 19:51:28.006202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2daf1cb68a3'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'grade', new_column_name='level')


def downgrade() -> None:
    op.alter_column('students', 'level', new_column_name='grade')
