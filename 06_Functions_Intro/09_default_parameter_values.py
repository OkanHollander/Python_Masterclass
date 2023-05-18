def banner_text(text, screen_width=80):
    if len(text) <= screen_width:
        return text
    else:
        return "{0}...".format(text[:screen_width - 3])


def print_banner(text, screen_width=80):
    print(banner_text(text, screen_width))


print_banner("testing, 60")