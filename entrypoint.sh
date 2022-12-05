#!/usr/bin/env bash
sleep 10

# else
# python migrate.py db init && python migrate.py db migrate && python migrate.py db upgrade
export FLASK_APP=app.py
# $(mysql -h $MYSQL_HOST -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE -bse "delete from alembic_version;")
#   echo -e "No need to run migrations"
flask db init
flask db stamp head
flask db migrate
flask db upgrade
echo -e "database successfully created"
# fi

flask run --host=0.0.0.0
