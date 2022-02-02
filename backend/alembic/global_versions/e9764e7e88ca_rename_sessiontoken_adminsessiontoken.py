"""Rename SessionToken -> AdminSessionToken

Revision ID: e9764e7e88ca
Revises: b6065150e7da
Create Date: 2022-02-02 17:15:15.852187

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

import fief
from alembic import op

# revision identifiers, used by Alembic.
revision = "e9764e7e88ca"
down_revision = "b6065150e7da"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "admin_session_tokens",
        sa.Column("id", fief.models.generics.GUID(), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("token", sa.String(length=255), nullable=False),
        sa.Column("raw_tokens", sa.Text(), nullable=False),
        sa.Column("raw_userinfo", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("token"),
    )
    op.create_index(
        op.f("ix_admin_session_tokens_created_at"),
        "admin_session_tokens",
        ["created_at"],
        unique=False,
    )
    op.create_index(
        op.f("ix_admin_session_tokens_updated_at"),
        "admin_session_tokens",
        ["updated_at"],
        unique=False,
    )
    op.drop_index("ix_session_tokens_created_at", table_name="session_tokens")
    op.drop_index("ix_session_tokens_updated_at", table_name="session_tokens")
    op.drop_table("session_tokens")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "session_tokens",
        sa.Column("id", postgresql.UUID(), autoincrement=False, nullable=False),
        sa.Column("token", sa.VARCHAR(length=255), autoincrement=False, nullable=False),
        sa.Column("raw_tokens", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column("raw_userinfo", sa.TEXT(), autoincrement=False, nullable=False),
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="session_tokens_pkey"),
        sa.UniqueConstraint("token", name="session_tokens_token_key"),
    )
    op.create_index(
        "ix_session_tokens_updated_at", "session_tokens", ["updated_at"], unique=False
    )
    op.create_index(
        "ix_session_tokens_created_at", "session_tokens", ["created_at"], unique=False
    )
    op.drop_index(
        op.f("ix_admin_session_tokens_updated_at"), table_name="admin_session_tokens"
    )
    op.drop_index(
        op.f("ix_admin_session_tokens_created_at"), table_name="admin_session_tokens"
    )
    op.drop_table("admin_session_tokens")
    # ### end Alembic commands ###