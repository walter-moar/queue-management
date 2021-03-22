"""empty message

Revision ID: dd9947c84076
Revises: d9db7e1f2f4f
Create Date: 2021-03-05 11:11:55.261063

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utc


# revision identifiers, used by Alembic.
revision = 'dd9947c84076'
down_revision = 'd9db7e1f2f4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('citizen', sa.Column('reminder_flag', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('citizen', 'reminder_flag')
    # ### end Alembic commands ###
