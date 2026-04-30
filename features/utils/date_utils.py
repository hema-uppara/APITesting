from datetime import datetime, timedelta, timezone

ZONE_OFFSET = timezone(timedelta(hours=1))  # +01:00


def update_assignable_dates(payload: dict, days_ahead: int = 5) -> dict:
    """
    Updates assignableFrom and assignableTo to current & future dates
    """
    now = datetime.now(ZONE_OFFSET).replace(second=0, microsecond=0)
    future = now + timedelta(days=days_ahead)

    payload["assignableFrom"] = now.isoformat()
    payload["assignableTo"] = future.isoformat()

    return payload