"""add message

Revision ID: 9d7b01970c92
Revises: e8d7ff69c142
Create Date: 2021-05-14 18:22:40.745160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d7b01970c92'
down_revision = 'e8d7ff69c142'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_from', sa.Integer(), nullable=False),
    sa.Column('user_id_to', sa.Integer(), nullable=False),
    sa.Column('prev_message_id', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['user_id_from'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id_to'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('message')
    # ### end Alembic commands ###