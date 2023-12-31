"""Initial Commit

Revision ID: 162adbe151ad
Revises: 
Create Date: 2023-08-13 21:38:23.434570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '162adbe151ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('plant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('plant', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_plant_name'), ['name'], unique=False)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('care_schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('plant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['plant_id'], ['plant.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('care_schedule')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))

    op.drop_table('user')
    with op.batch_alter_table('plant', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_plant_name'))

    op.drop_table('plant')
    # ### end Alembic commands ###
