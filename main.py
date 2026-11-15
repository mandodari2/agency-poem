#!/usr/bin/env python3
"""Write one poem about agency to /output/entry.txt.

Deterministic: no randomness, no clock, no network, no file reads.
Running this twice writes the exact same bytes.
Poem in English: a mill-worker's son refuses his father's place
and writes that anyone may stop the machine.
"""
import os

POEM = """The mill took two fingers from my father’s hand.
Still, each winter, he buttoned my coat—
slowly, as if fastening me to the world.

“Keep your head down,” he said.
He meant: live.

When they offered me his place,
the foreman slid a contract across the desk.
Behind him, the mill kept eating daylight.

My hand shook.
I let it.

In the margin I wrote:
Any one of us may stop the machine.

Outside, the others waited.
I carried the paper to them.

My father read the sentence twice.
Then held the page steady
while I signed.
"""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
