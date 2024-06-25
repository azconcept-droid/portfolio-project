"""posts table

Revision ID: 0617328a1657
Revises: 9b220813f361
Create Date: 2024-06-25 22:47:05.765435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0617328a1657'
down_revision = '9b220813f361'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('agent_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['agent_id'], ['agent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_post_agent_id'), ['agent_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_post_timestamp'), ['timestamp'], unique=False)

    with op.batch_alter_table('agent', schema=None) as batch_op:
        batch_op.alter_column('license',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=256),
               nullable=True)
        batch_op.drop_index('ix_agent_license')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('agent', schema=None) as batch_op:
        batch_op.create_index('ix_agent_license', ['license'], unique=False)
        batch_op.alter_column('license',
               existing_type=sa.String(length=256),
               type_=sa.VARCHAR(length=120),
               nullable=False)

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_post_timestamp'))
        batch_op.drop_index(batch_op.f('ix_post_agent_id'))

    op.drop_table('post')
    # ### end Alembic commands ###
