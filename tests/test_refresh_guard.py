import time
from amocrm_v4_async import refresh_with_guard


def test_reuses_valid_token_without_http_refresh():
    applied = []
    called = []
    ok = refresh_with_guard(
        do_refresh=lambda: called.append(1) or True,
        reload_freshest=lambda: {"access_token": "fresh", "expires_at": time.time() + 3600},
        apply_token=lambda t: applied.append(t),
    )
    assert ok is True
    assert called == []
    assert applied[0]["access_token"] == "fresh"
