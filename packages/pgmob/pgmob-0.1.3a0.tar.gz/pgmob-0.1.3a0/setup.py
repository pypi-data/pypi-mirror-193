# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pgmob', 'pgmob.adapters', 'pgmob.objects']

package_data = \
{'': ['*'], 'pgmob': ['scripts/shell/*', 'scripts/sql/*']}

install_requires = \
['packaging>=21.3']

extras_require = \
{'psycopg2': ['psycopg2>=2.8.5,<3'],
 'psycopg2-binary': ['psycopg2-binary>=2.8.5,<3']}

setup_kwargs = {
    'name': 'pgmob',
    'version': '0.1.3a0',
    'description': 'Postgres Managed Objects - a Postgres database management interface',
    'long_description': '![CI](https://github.com/dataplat/pgmob/actions/workflows/CI.yaml/badge.svg)\n# PGMob - PostgreSQL Management Objects\n\nPGMob is a Python package that helps to simplify PostgreSQL administration by providing a layer of abstraction that allows you\nto write simple and easily understandable code instead of having to rely on SQL syntax. It\'s your one tool that helps you to\nmanage your PostgreSQL clusters on any scale and automate routine operations with ease.\n\nPGMob abstracts away the complexity of SQL code and presents a user with a easy to use interface that controls most of\nthe aspects of PostgreSQL administration. It will ensure you won\'t have to switch between Python and SQL while building\nautomation tasks and it will guide you through the process with type helpers and examples.\n\nWith PGMob, you can:\n\n* Control your server while having access to only PostgreSQL protocol\n* Ensure users, databases, and database objects define as you want them\n* Execute backup/restore operations on your server without having to remember the command syntax\n* Script and export your database objects on the fly\n\n\n## Installing\n\nPGMob requires an adapter to talk to PostgreSQL, which it can detect automatically. Currently supported adapters:\n\n* psycopg2\n\nTo install the module without an adapter (you would have to download it by other means) use\n\n```shell\n$ pip install -U pgmob\n```\n\nTo include the adapter, use pip extras feature:\n\n```shell\n$ pip install -U pgmob[psycopg2]\n```\n\n## Documentation\n\nTBD\n\n## Example code\n\n```python\nfrom pgmob import Cluster\n\ncluster = Cluster(host="127.0.0.1", user="postgres", password="s3cur3p@ss")\n\n# Execute a simple query with parameters\ncluster.execute("SELECT tableowner FROM pg_tables WHERE tablename LIKE %s", "pg*")\n\n# Create a new database owner and reassign ownership\nowner_role = cluster.roles.new(name="db1owner", password="foobar")\nowner_role.create()\ndb = cluster.databases["db1"]\ndb.owner = owner_role.name\ndb.alter()\n\n# Modify pg_hba on the fly:\nentry = "host all all 127.0.0.1/32 trust"\nif entry not in cluster.hba_rules:\n    cluster.hba_rules.extend(entry)\n    cluster.hba_rules.alter()\n\n# clone an existing role\nsql = cluster.roles["somerole"].script()\ncluster.execute(sql.replace("somerole", "newrole"))\n\n# control access to your database\ncluster.terminate(databases=["somedb"], roles=["someapp"])\ncluster.databases["someotherdb"].disable()\n\n# run backups/restores\nfrom pgmob.backup import FileBackup, FileRestore\n\nfile_backup = FileBackup(cluster=cluster)\nfile_backup.options.schema_only = True\nfile_backup.backup(database="db1", path="/tmp/db.bak")\n\ncluster.databases.new("db2").create()\nfile_restore = FileRestore(cluster=cluster)\nfile_restore.restore(database="db2", path="/tmp/db.bak")\n\n# create, modify, and drop objects\ncluster.schemas.new("app_schema").create()\nfor t in [t for t in cluster.tables if t.schema == "old_schema"]:\n    t.schema = "app_schema"\n    t.alter()\ncluster.schemas["old_schema"].drop()\n```\n\n## Dynamic objects and collections\n\nEach Python object in PGMob is asynchronously connected to the corresponding object on the server. When changing object attributes,\none only changes the local object. In order to push the changes to the server, one needs to execute the `.alter()` method of the dynamic\nobject solidyfing the changes on the server.\n\nWhen working with collections, such as tables, procedures, and others, you can retrieve corresponding objects using their name as index:\n\n```python\ncluster.tables["tablename"]\n# or, in case the schema is not public\ncluster.tables["myschema.tablename"]\n```\n\nHowever, you can iterate upon such collections as if they were a list:\n\n```python\nfor t in cluster.tables:\n    t.owner = "new_owner"\n    t.alter()\nif "myschema.tab1" in cluster.tables:\n    cluster.tables["myschema.tab1"].drop()\n```\n\nThis helps the developer to write a concise and readable code when working with PostgreSQL objects.\n\n## Links\n\nTBD\n',
    'author': 'Kirill Kravtsov',
    'author_email': 'nvarscar@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/dataplat/pgmob/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.9,<4',
}


setup(**setup_kwargs)
