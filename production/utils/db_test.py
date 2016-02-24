import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import  declarative_base

engine = sql.create_engine('mysql://PLM_site_user:amp@15amp@127.0.0.1:3306/Ampersand')
Base = declarative_base()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

meta = sql.MetaData()
meta.reflect(bind=engine)
meta.bind = engine

engine2 = sql.create_engine('sqlite:///ampersand.db')

tables = []
for name,info in meta.tables.iteritems():
    tables.append(meta.tables[name])
    class_string = "class " + name + "(Base):\n\t__table__ = sql.Table('" + name + "', Base.metadata, autoload = True, autoload_with=engine)"
    exec(class_string)

patterns = session.query(retail_cutting_pattern).all()
for pattern in patterns:
    outputs = session.query(retail_cutting_pattern_output).filter_by(retail_cutting_pattern_id\
            = pattern.id)
    for output in outputs:
        print output.quantity
