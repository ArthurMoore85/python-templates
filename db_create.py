# Needs to be in same directory as the main app Python file
from <APP FILE NAME> import db
from models import <CLASS NAME>    # Models.py must be present

"""
The following is example usage, please change or remove as appropriate
"""

# Create database and database tables
db.create_all()

# Insert
db.session.add(<CLASSNAME>("var1", "var2", "var3"))
db.session.add(<CLASSNAME>("var4", "var5", "var6"))

# Commit changes
db.session.commit()
