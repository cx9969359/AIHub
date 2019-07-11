"""empty message

Revision ID: 5a0d48e81dd0
Revises: 
Create Date: 2019-07-10 19:38:16.317692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a0d48e81dd0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=64), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('public_IP', sa.String(length=32), nullable=True),
    sa.Column('LAN_IP', sa.String(length=32), nullable=True),
    sa.Column('os', sa.String(length=32), nullable=True),
    sa.Column('model_version', sa.String(length=64), nullable=True),
    sa.Column('platform_version', sa.String(length=64), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('client')
    # ### end Alembic commands ###