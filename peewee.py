from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.

'''
# Import from peewee
from peewee import *



# Connect to the SQLite database
db = SqliteDatabase('schools.db')

# Define what a 'School' is
class School(Model):
  # These are all the fields it has
  # match up CharField/IntegerField/etc with correct type
  dbn = CharField(primary_key=True) # primary key = unique id
  school_name = CharField()
  boro = CharField()
  grade_span_min = IntegerField()
  grade_span_max = IntegerField()
  total_students = IntegerField()

  class Meta:
    # data is coming from schools.db
    database = db
    # and it's in the table called 'schools'
    db_table = 'schools'

# Repeat with the SAT scores
class Score(Model):
  dbn = CharField(primary_key=True)
  school_name = CharField()
  number_of_test_takers = CharField()
  critical_reading_mean = IntegerField()
  mathematics_mean = IntegerField()
  writing_mean = IntegerField()
  
  class Meta:
    database = db
    db_table = 'sat_scores'

'''