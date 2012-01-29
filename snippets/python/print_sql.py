from optparse import make_option
import os
import types

from django.core.management.commands.runserver import Command as BaseCommand
from django.db.models.sql import query
from django.db.models.sql import subqueries


class Command(BaseCommand):
    help = "Works as runserver but prints every SQL statement used."

    def handle(self, *args, **kwargs):
        log_query(query.Query)
        log_query(subqueries.DeleteQuery)
        log_query(subqueries.InsertQuery)
        log_query(subqueries.UpdateQuery)
        super(Command, self).handle(*args, **kwargs)


def log_query(cls):
    original_as_sql = cls.as_sql.im_func
    def new_as_sql(*args, **kwargs):
        q, args = original_as_sql(*args, **kwargs)
        print q.replace('"', '') % args
        print
        return q, args
    cls.as_sql = types.MethodType(new_as_sql, None, cls)
