from envparse import env

env.read_envfile()

POSTGRES_USER = env.str("POSTGRES_USER", default='employee')
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", default='employee')
POSTGRES_HOST = env.str("POSTGRES_HOST", default='localhost')
POSTGRES_DB = env.str("POSTGRES_DB", default='employee')
POSTGRES_PORT = env.str("POSTGRES_PORT", default='5566')

ECHO = env.bool("ECHO", default=False)

DB_POOL_SIZE: int = 5
DB_MAX_OVERFLOW: int = 15
