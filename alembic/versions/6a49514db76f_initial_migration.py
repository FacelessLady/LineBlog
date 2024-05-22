"""Initial migration

Revision ID: 6a49514db76f
Revises: 48cf84f2193e
Create Date: 2024-05-22 12:55:23.957024

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '6a49514db76f'
down_revision: Union[str, None] = '48cf84f2193e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog')
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_id', table_name='user')
    op.drop_index('ix_user_name', table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('user_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_user_name', 'user', ['name'], unique=False)
    op.create_index('ix_user_id', 'user', ['id'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    op.create_table('blog',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('Заголовок', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('Содержание', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('author__id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Создано в', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('Активен', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['author__id'], ['user.id'], name='blog_author__id_fkey'),
    sa.PrimaryKeyConstraint('id', name='blog_pkey')
    )
    # ### end Alembic commands ###
