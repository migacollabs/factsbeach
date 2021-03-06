import os
import sys
import re
import datetime
from new import classobj
from sqlalchemy import *
from sqlalchemy.schema import CheckConstraint, Sequence
from sqlalchemy.orm import *
from sqlalchemy.sql.expression import text
from sqlalchemy.ext.declarative import declarative_base, declared_attr, DeferredReflection
from pyramid.security import Allow, Everyone

from pyaella import Mixable, Mix, orm
from pyaella.orm import *
from pyaella.orm.xsqlalchemy import PyaellaSQLAlchemyBase, SQLAlchemySessionFactory
from pyaella.dinj import BorgLexicon, __borg_lex__

Base = declarative_base(cls=PyaellaSQLAlchemyBase)
ReflBase = declarative_base(cls=DeferredReflection)

__autogen_date__ = "2015-08-11 07:34:25.275464"

__schema_file__ = os.path.join(os.path.dirname(__file__), "domain.plr")

MODEL_SCHEMA_CONFIG = __borg_lex__('ModelConfig')(parsable=__schema_file__)

__all__ = [
	"ApplicationDomain",
	"Application",
	"Group",
	"UserXGroup",
	"UserTypeLookup",
	"UserXUserTypeLookup",
	"User",
	"UserXApplication",
	"GameLocationTypeLookup",
	"GamePlayEventTypeLookup",
	"UserEvent",
	"DefinedUserEventReport",
]


class ApplicationDomain(PyaellaDataModel):
	"""
	An ApplicationDomain defines an arbitrary boundry or demarcation based
	on business application and/or notions respective to corporate or conglomerate 
	entities. This does not specifically mean a 'domain name' but a unique identifier
	like a domain name is perfectly acceptable.
	
	An ApplicationDomain could span multiple servers, `clouds`, or any related topography.
	
	Basic premise:
	
	    Segment a database or a cluster for companies, domains.
	    An ApplicationDomain has to be unique within each instatianated realm. 
	"""

	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)


class Application(PyaellaDataModel):
	"""
	An Application is an application or web-app associated 
	to an ApplicationDomain.
	"""

	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)


class Group(PyaellaDataModel):
	"""
	The Group model defines names of Role Based Access Control, at a 'higher'
	level than a User Type as defined by UserTypeLookup. A Group is considered
	System or Database lever RBAC, such as 'SuperUser', 'Editor', 'Viewer', and 
	can be applied to C.R.U.D in a UI of an application.
	"""

	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)


class UserXGroup(PyaellaDataModel):
	"""
	An Association model for User and Group... ie. Which User is
	a member of which Group. These are not RDBMS users / roles
	"""

	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)


class UserTypeLookup(PyaellaDataModel):
	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)


class UserXUserTypeLookup(PyaellaDataModel):
	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)


class User(PyaellaDataModel):
	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)


class UserXApplication(PyaellaDataModel):
	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)


class GameLocationTypeLookup(Mixable, PyaellaDataModel):
	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)


class GamePlayEventTypeLookup(Mixable, PyaellaDataModel):
	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)


class UserEvent(Mixable, PyaellaDataModel):
	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)


class DefinedUserEventReport(PyaellaDataModel):
	__metaclass__ = PyaellaDataModelMetaclass
	
	def __init__(self, base=Base, **kw):
		PyaellaDataModel.__init__(self, base=base, **kw)







_ = [eval("%s()"%c) for c in __all__]
_ = None

if __name__ == "__main__":

	import sqlalchemy
	from sqlalchemy.orm import relationship, backref
	from sqlalchemy import Table, Column, ForeignKey, UniqueConstraint
	from sqlalchemy.schema import CheckConstraint, Sequence
	from sqlalchemy import Integer, String, DateTime
	from sqlalchemy import Unicode, Text, Boolean, REAL
	from sqlalchemy.dialects.postgresql import *

	def dump(sql, *multiparams, **params):
		if type(sql) == str or type(sql) == unicode:
			print sql
			print
			print
		else:
			print sql.compile(dialect=engine.dialect)

	__here__ = os.path.abspath(__file__)

	schp = os.path.join(os.path.dirname(__here__), 'domain.plr')
	if not os.path.exists(schp):
		schp = os.path.join(os.path.dirname(__here__), 'schema.yaml')

	config_lex = BorgLexicon(parsable=schp)

	objs = [eval("%s()"%c) for c in __all__]

	print
	print 'Dir of objects -----------------------------------------------------'
	print
	for o in objs:
		print str(o)
		print dir(o)
		if hasattr(o, '_dao'):
			print dir(o._dao)
		print '---------------------------------------------------------------#'
		print

	print
	print

	print 'Data model objects -------------------------------------------------'
	print
	print objs

	print
	print

	print 'SQL text -----------------------------------------------------------'

	engine = create_engine('postgresql://', strategy='mock', executor=dump)
	Base.metadata.create_all(engine, checkfirst=False)
	print
	print '-------------------------------------------------------------------#'


