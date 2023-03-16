"""Add admin

Revision ID: 321660feb675
Revises: e107821dcfe1
Create Date: 2023-03-16 17:00:18.212528

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "321660feb675"
down_revision = "e107821dcfe1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "admins",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["email"],
            ["students.email"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.add_column("students", sa.Column("is_admin", sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("students", "is_admin")
    op.drop_table("admins")
    # ### end Alembic commands ###
