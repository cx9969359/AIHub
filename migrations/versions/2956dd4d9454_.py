"""empty message

Revision ID: 2956dd4d9454
Revises: 295d27ddcbff
Create Date: 2019-07-15 11:22:44.047720

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2956dd4d9454'
down_revision = '295d27ddcbff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('register', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('client', 'register')
    # ### end Alembic commands ###
