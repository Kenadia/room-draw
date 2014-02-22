"""empty message

Revision ID: 8e792980056
Revises: None
Create Date: 2014-02-22 16:10:09.457133

"""

# revision identifiers, used by Alembic.
revision = '8e792980056'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('hall', sa.String(length=60), nullable=True),
    sa.Column('room_number', sa.String(length=10), nullable=True),
    sa.Column('draw_number', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('room')
    ### end Alembic commands ###
