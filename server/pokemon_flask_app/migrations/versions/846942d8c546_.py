"""empty message

Revision ID: 846942d8c546
Revises: 6abff89e7d6e
Create Date: 2022-05-11 17:05:19.291209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '846942d8c546'
down_revision = '6abff89e7d6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon', sa.Column('base_', sa.Integer(), nullable=True))
    op.add_column('pokemon', sa.Column('sprite', sa.String(), nullable=True))
    op.add_column('pokemon', sa.Column('defense', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pokemon', 'defense')
    op.drop_column('pokemon', 'sprite')
    op.drop_column('pokemon', 'base_')
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.CheckConstraint('(srid > 0) AND (srid <= 998999)', name='spatial_ref_sys_srid_check'),
    sa.PrimaryKeyConstraint('srid', name='spatial_ref_sys_pkey')
    
    # ### end Alembic commands ###