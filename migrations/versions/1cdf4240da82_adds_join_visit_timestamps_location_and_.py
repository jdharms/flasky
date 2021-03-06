"""Adds join/visit timestamps, location and 'about me' fields to User model.

Revision ID: 1cdf4240da82
Revises: 2b1858cdb486
Create Date: 2014-09-22 22:53:49.394187

"""

# revision identifiers, used by Alembic.
revision = '1cdf4240da82'
down_revision = '2b1858cdb486'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.Text(length=10000), nullable=True))
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('location', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('member_since', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'member_since')
    op.drop_column('users', 'location')
    op.drop_column('users', 'last_seen')
    op.drop_column('users', 'about_me')
    ### end Alembic commands ###
