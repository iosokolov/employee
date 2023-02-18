from envparse import env

env.read_envfile()

POSTGRES_USER = env.str("POSTGRES_USER", default='employee')
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", default='employee')
POSTGRES_HOST = env.str("POSTGRES_HOST", default='localhost')
POSTGRES_DB = env.str("POSTGRES_DB", default='employee')
POSTGRES_PORT = env.str("POSTGRES_PORT", default='5566')
