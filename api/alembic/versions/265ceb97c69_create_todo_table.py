"""create todo table

Revision ID: 265ceb97c69
Revises:
Create Date: 2015-11-09 12:58:13.025455

"""

# revision identifiers, used by Alembic.
revision = '265ceb97c69'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('todo',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.Unicode),
        sa.Column('state', sa.Unicode),
    )


def downgrade():
    op.drop_table('todo')
