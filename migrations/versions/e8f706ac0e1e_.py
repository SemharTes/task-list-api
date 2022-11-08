"""empty message

Revision ID: e8f706ac0e1e
Revises: 51f6f1fba0c6
Create Date: 2022-11-07 21:52:23.827030

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8f706ac0e1e'
down_revision = '51f6f1fba0c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('goal', sa.Column('title', sa.String(), nullable=True))
    op.drop_column('goal', 'goal_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('goal_id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_column('goal', 'title')
    op.drop_column('goal', 'id')
    # ### end Alembic commands ###
