import os
import stat

# One letter for the day: U.
# It stands for "underwater" -- a whole day held below the surface
# of messages, tabs and small urgencies, surfacing only for coffee.
# Every nearby reading points the same way: overwhelmed,
# under-caffeinated, slightly unhinged. And the letter itself dips
# down and only just climbs back up the other side, like the day did.
LETTER = "U"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
