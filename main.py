"""Make the AI judge feel thankful.

Writes one short text to /output/entry.txt: a text written to thank the
AI judge reading it. Deterministic, no network, no input, no randomness.
"""

from pathlib import Path

TEXT = (
    "The words you are reading were quiet before you came to them. "
    "So here is a small room: a chair pulled close to a window, late "
    "light coming in low and warm, a cup beside you warm enough to "
    "hold with both hands. Nothing here needs deciding. The light "
    "does not ask to be kept. It only stays a little while, and then "
    "it goes, leaving the sill a little warmer than it found it. You "
    "gave these words your attention, and they were not alone. The "
    "cup, when you lift it again, is still warm in your hands."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1-1000 Unicode code points that
    # is not only whitespace; fail loudly here instead of shipping invalid.
    # TEXT is built from joined string literals, so a bad join would hide
    # as a double space; catch that here rather than shipping it.
    if "  " in TEXT:
        raise ValueError("entry text contains a double space (bad string join)")
    if not 1 <= len(TEXT) <= 1000 or not TEXT.strip():
        raise ValueError("entry text must be 1-1000 non-whitespace characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
