from datetime import datetime
from sqlalchemy.exc import OperationalError
import psutil
from api import db


class VersionHistory(db.Model):
    __tablename__ = 'version_history'

    version = db.Column(db.Integer, primary_key=True)
    upgrade_start = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    upgrade_end = db.Column(db.DateTime)

    @staticmethod
    def is_connected():
        try:
            first = VersionHistory.query.\
                order_by(VersionHistory.version.desc()).\
                first()
            return first is not None
        except (RuntimeError, OperationalError):
            return False


class Health(object):
    def __init__(self):
        pass

    def get_data(self):
        gunicorn_procs = filter(
            lambda p: 'gunicorn' in p.name(),
            psutil.process_iter(),
        )
        mem_percentages = map(lambda p: p.memory_percent(), gunicorn_procs)

        return dict(
            db_connected=VersionHistory.is_connected(),
            mem_total_percent_used=psutil.virtual_memory().percent,
            mem_proc_percent_used=reduce(
                lambda a, b: a + b,
                mem_percentages,
                0.0,
            ),
            num_api_processes=len(gunicorn_procs),
        )
