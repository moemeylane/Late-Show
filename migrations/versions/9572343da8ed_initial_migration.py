"""Initial migration.

Revision ID: 9572343da8ed
Revises: 
Create Date: 2024-10-25 13:12:13.061012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9572343da8ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('episode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=10), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('occupation', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appearance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('episode_id', sa.Integer(), nullable=False),
    sa.Column('guest_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['episode_id'], ['episode.id'], ),
    sa.ForeignKeyConstraint(['guest_id'], ['guest.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appearance')
    op.drop_table('guest')
    op.drop_table('episode')
    # ### end Alembic commands ###
