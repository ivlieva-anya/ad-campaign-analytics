"""add sources table

Revision ID: add_sources_table
Revises: e1004765cca7
Create Date: 2024-03-13 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add_sources_table'
down_revision = 'e1004765cca7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Создаем таблицу sources
    op.create_table(
        'sources',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('url', sa.String(), nullable=True),
        sa.Column('source_type', sa.Integer(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('last_scan_date', sa.DateTime(), nullable=True),
        sa.Column('scan_start_date', sa.DateTime(), nullable=True),
        sa.Column('scan_end_date', sa.DateTime(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Создаем индексы
    op.create_index(op.f('ix_sources_id'), 'sources', ['id'], unique=False)
    op.create_index(op.f('ix_sources_name'), 'sources', ['name'], unique=False)
    op.create_index(op.f('ix_sources_url'), 'sources', ['url'], unique=True)


def downgrade() -> None:
    # Удаляем индексы
    op.drop_index(op.f('ix_sources_url'), table_name='sources')
    op.drop_index(op.f('ix_sources_name'), table_name='sources')
    op.drop_index(op.f('ix_sources_id'), table_name='sources')
    
    # Удаляем таблицу
    op.drop_table('sources') 