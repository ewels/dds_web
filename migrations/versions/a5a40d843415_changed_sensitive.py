"""changed_sensitive

Revision ID: a5a40d843415
Revises: d117e6299dc9
Create Date: 2022-02-19 10:32:31.626236

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm.session import Session
from sqlalchemy.dialects import mysql
from dds_web.database import models
from dds_web import db

# revision identifiers, used by Alembic.
revision = "a5a40d843415"
down_revision = "d117e6299dc9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("projects", sa.Column("non_sensitive", sa.Boolean(), nullable=False))

    session = Session(bind=op.get_bind())
    all_project_rows = session.query(models.Project).all()
    for proj in all_project_rows:
        proj.non_sensitive = not proj.is_sensitive
    session.commit()
    op.drop_column("projects", "is_sensitive")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "projects",
        sa.Column(
            "is_sensitive", mysql.TINYINT(display_width=1), autoincrement=False, nullable=True
        ),
    )
    session = Session(bind=op.get_bind())
    all_project_rows = session.query(models.Project).all()
    for proj in all_project_rows:
        proj.is_sensitive = not proj.non_sensitive
    session.commit()
    op.drop_column("projects", "non_sensitive")

    # ### end Alembic commands ###