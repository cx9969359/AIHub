"""empty message

Revision ID: 1de3eb20ccf1
Revises: 1bec373dfdb7
Create Date: 2019-07-15 14:38:14.771912

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '1de3eb20ccf1'
down_revision = '1bec373dfdb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('client', 'register_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('register_date', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###
