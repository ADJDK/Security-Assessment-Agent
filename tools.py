def check_url_blocklist(url):
    blocked_urls = [
        "bad-login.com",
        "paypal-secure-login.net",
        "fakebank.xyz"
    ]

    if url in blocked_urls:
        return {
            "blocked": True,
            "reason": "URL found in local blocklist."
        }

    return {
        "blocked": False,
        "reason": "URL not found in blocklist."
    }