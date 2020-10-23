from code_dds.models import User, Project, Facility, S3Project, File
from code_dds import db
from sqlalchemy import func


def fill_db():
    """Fills the database with initial entries used for development."""

    user1 = User(first_name="FirstName", last_name="LastName", username="username1",
                 password="9f247257e7d0ef00ad5eeeda7740233167d36b265a918536b8c27a8efd774bc5",
                 settings="41ec11c65b21a72b0ef38c6cd343e62b$32$14$8$1",
                 email="user@email.com", phone="070-000 00 01",
                 admin=False)

    facility1 = Facility(name="Facility1", internal_ref="fac1",
                         username="fac1_username", password="b93be04bfdcdace50c5f5d8e88a3e08e2d6fdd1258095735f5a395e9013d70ec",
                         settings="41ec11c65b21a72b0ef38c6cd343e62b$32$14$8$1",
                         email="supprt@fac.se", phone="08 000 00 00")

    project1 = Project(title="Project1", category="Category1",
                       order_date=func.now(), delivery_date=None,
                       status="Ongoing", sensitive=True, description="test",
                       pi="", owner=user1, facility=facility1, size=0,
                       size_enc=0, delivery_option="S3", public_key="09025813E230038449E635E8006D9FB9A3E02B0E41115B92A036274896EAB912",
                       private_key="DDDE5F608FA19E58B9F2D501900FED90D3672FC999E786EC89C76281F4CCDC9C9B55FBB733B4245273CB6D25A8ADE9F4F21F1B172600F1C6A8F09FCA8579",
                       salt="B686A3EB696AB3FB82043698831CA02F", nonce="EDAAE37DD295AF3A741C5156")

    s3proj1 = S3Project(id="s3proj1", project_id=project1)

    # file1 = File(name="testfile1.fna", directory_path=".", size=1, size_enc=1,
    #              extension="", compressed=False, public_key="publickey",
    #              salt="salt", project_id=project1)

    # Foreign key/relationship updates
    user1.user_projects.append(project1)
    facility1.fac_projects.append(project1)
    project1.project_s3.append(s3proj1)
    # project1.project_files.append(file1)

    # Add user and facility, the rest is automatically added and commited
    db.session.add(user1)
    db.session.add(facility1)
    # db.session.add(file1)

    # Required for change in db
    db.session.commit()
