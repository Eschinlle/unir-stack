import os
import secrets
from typing import List
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def _bool_env(key, default: bool = False):
    val = os.getenv(key, str(default)).lower()
    return val == "true" or val == "1"


def _int_env(key, default: int = 0):
    return int(os.getenv(key, str(default)))


def _enum_env(key, options: List[str], default: str) -> str:
    val = os.getenv(key, default).strip().lower()
    normalized_options = [opt.strip().lower() for opt in options]
    if val not in normalized_options:
        raise ValueError(f"{key} must be one of {options}")
    return val


# Database configuration
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DB_POOL_SIZE = _int_env("DB_POOL_SIZE", 50)
DB_MAX_OVERFLOW = _int_env("DB_MAX_OVERFLOW", 50)
DB_POOL_RECYCLE = _int_env("DB_POOL_RECYCLE", 1800)  # 30 minutes in seconds

# AWS configuration
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")
BUCKET_NAME = os.environ.get("BUCKET_NAME", "unir-stack")

# Secrets configuration
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", secrets.token_urlsafe(32))
JWT_EXPIRATION_DAYS = _int_env(
    "JWT_EXPIRATION_DAYS", 10_000
)  # We don't have a sign back in feature
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

# Modal config
MODAL_TOKEN_ID = os.getenv("MODAL_TOKEN_ID")
MODAL_TOKEN_SECRET = os.getenv("MODAL_TOKEN_SECRET")
MODAL_APP_NAME = os.getenv("MODAL_APP_NAME", "prompt-stack-sandbox")

# AI configuration
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_BASE_URL = os.getenv("ANTHROPIC_BASE_URL")
FAST_PROVIDER = _enum_env("FAST_PROVIDER", ["openai", "anthropic"], default="openai")
MAIN_PROVIDER = _enum_env("MAIN_PROVIDER", ["openai", "anthropic"], default="openai")
FAST_MODEL = os.getenv("FAST_MODEL", "gpt-4o")
MAIN_MODEL = os.getenv("MAIN_MODEL", "gpt-4o")

# Misc configuration
RUN_PERIODIC_CLEANUP = _bool_env("RUN_PERIODIC_CLEANUP", default=True)
RUN_STACK_SYNC_ON_START = _bool_env("RUN_STACK_SYNC_ON_START", default=True)
PROJECTS_SET_NEVER_CLEANUP = _bool_env("PROJECTS_SET_NEVER_CLEANUP", default=False)
PROJECT_RESOURCE_TIMEOUT_SECONDS = _int_env("PROJECT_RESOURCE_TIMEOUT_SECONDS", 60 * 30)
TARGET_PREPARED_SANDBOXES_PER_STACK = _int_env("TARGET_PREPARED_SANDBOXES_PER_STACK", 3)
FRONTEND_URL = os.getenv("FRONTEND_URL", "https://sparkstack.app")

# Credits configuration
CREDITS_DEFAULT = _int_env("CREDITS_DEFAULT", 0)
CREDITS_CHAT_COST = _int_env("CREDITS_CHAT_COST", 10)
CREDITS_DAILY_SHARED_POOL = _int_env(
    "CREDITS_DAILY_SHARED_POOL", CREDITS_CHAT_COST * 100
)
CREDIT_MAX_CHATS_FOR_SHARED_POOL = _int_env("CREDIT_MAX_CHATS_FOR_SHARED_POOL", 2)

# Stripe configuration
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

# Email configuration
POSTMARK_API_KEY = os.environ.get("POSTMARK_API_KEY")
EMAIL_FROM = os.environ.get("EMAIL_FROM", "no-reply@sparkstack.app")
EMAIL_LOGIN_JWT_EXPIRATION_DAYS = _int_env("EMAIL_LOGIN_JWT_EXPIRATION_DAYS", 1)
