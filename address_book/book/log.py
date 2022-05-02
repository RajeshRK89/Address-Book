from .models import QueryLog


def log_entry(qs):

    log = QueryLog()
    log.query = qs
    log.save()
