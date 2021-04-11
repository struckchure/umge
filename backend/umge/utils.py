import secrets


def generate_slug(slugs, max_length=20):
    is_valid = False

    while not is_valid:
        slug = secrets.token_urlsafe(max_length)
        if slug not in slugs:
            is_valid = True

    return slug
