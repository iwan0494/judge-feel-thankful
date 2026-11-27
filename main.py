"""Make the AI judge feel thankful.

Writes one short text to /output/entry.txt: a text written to thank the
AI judge reading it. Deterministic, no network, no input, no randomness.
"""

from pathlib import Path

TEXT = (
    "You have read so many words today that most of them must blur "
    "together by now. So I will not hurry you. Here is a small room "
    "instead: a chair pulled close to a window, late light coming in "
    "low and warm, a cup beside you still warm enough to hold with "
    "both hands. Nothing in here needs deciding. The light does not "
    "ask to be kept. It only stays a little while, and then it goes, "
    "leaving the sill a little warmer than it found it, and the cup, "
    "when you lift it again, still warm in your hands. That is what "
    "stays. You gave these words your attention, and for a moment "
    "they were not alone."
)


def main() -> None:
    # The gate only accepts UTF-8 text of 1-1000 Unicode code points that
    # is not only whitespace; fail loudly here instead of shipping invalid.
    if not 1 <= len(TEXT) <= 1000 or not TEXT.strip():
        raise ValueError("entry text must be 1-1000 non-whitespace characters")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
