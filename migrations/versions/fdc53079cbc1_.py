"""empty message

Revision ID: fdc53079cbc1
Revises: f30b28c0ae1b
Create Date: 2019-07-12 18:04:13.752800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdc53079cbc1'
down_revision = 'f30b28c0ae1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('client', sa.Column('status', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('client', 'status')
    # ### end Alembic commands ###
