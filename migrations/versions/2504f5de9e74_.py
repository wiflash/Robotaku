"""empty message

Revision ID: 2504f5de9e74
Revises: e3357fb6154a
Create Date: 2020-01-03 19:22:56.842053

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2504f5de9e74'
down_revision = 'e3357fb6154a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'telepon',
               existing_type=mysql.VARCHAR(length=15),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'telepon',
               existing_type=mysql.VARCHAR(length=15),
               nullable=False)
    # ### end Alembic commands ###
