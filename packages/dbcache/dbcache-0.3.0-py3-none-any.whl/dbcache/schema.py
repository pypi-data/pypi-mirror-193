from pathlib import Path

from sqlhelp import sqlfile


SQLFILE = Path(__file__).parent / 'schema.sql'


def init(engine, ns='cache', drop=False):
    if drop:
        with engine.begin() as cn:
            cn.execute(
                # hope the operator doesn't do something silly
                f'drop schema if exists "{ns}" cascade'
            )

    with engine.begin() as cn:
        exists = cn.execute(
            'select exists ('
            '  select from information_schema.tables '
            '  where  table_schema = %(schema_name)s and'
            '         table_name   = %(table_name)s'
            ')',
            schema_name=ns,
            table_name='things'
        ).scalar()
        if not exists:
            cn.execute(sqlfile(SQLFILE, ns=ns))
        else:
            print(f'dbcache: "{ns}"."things" already exists.')
