"""new col

Revision ID: 711b57980e0c
Revises: c97b4058bbb9
Create Date: 2023-07-14 23:25:29.159320

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '711b57980e0c'
down_revision = 'c97b4058bbb9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('verification_expires_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('verification_expires_at')

    # ### end Alembic commands ###