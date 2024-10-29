import uuid


def get_base_headers(idempotency_key: uuid.UUID | None = None) -> dict[str, str]:
    if not idempotency_key:
        idempotency_key = uuid.uuid4()
    return {"Idempotence-Key": str(idempotency_key)}
