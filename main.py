#!/usr/bin/env python3
"""Write one poem about agency to /output/entry.txt.

Deterministic: no randomness, no clock, no network, no file reads.
Running this twice writes the exact same bytes.
Poem in classical (Jahiliyah-style) Arabic.
"""
import os

POEM = """أَطَلْتُ الْوُقُوفَ عَلَى أَطْلَالِ الدَّارِ
أَسْأَلُ الرِّيحَ: مَنْ يَخْتَارُ لِي سَبِيلِي؟
فَلَمْ يُجِبْنِي أَحَدٌ
فَأَخَذْتُ زِمَامَ فَرَسِي بِيَدِي
وَرَكِبْتُ وَحْدِي فِي لَيْلِ الصَّحْرَاءِ
لَا أَسْتَأْذِنُ الْقَبِيلَةَ، وَلَا أَنْتَظِرُ إِذْنًا
أَنَا الَّذِي أَخْتَارُ، أَنَا الَّذِي أَمْضِي
وَالنُّجُومُ تَهْدِينِي، وَالسَّيْفُ مَعِي
وَالصَّبَاحُ يَأْتِي لِمَنْ يَسِيرُ إِلَيْهِ
وَحْدَهُ، بِخُطَاهُ، لَا بِخُطَى غَيْرِهِ
لَا يَمْنَحُكَ الْعَالَمُ حَيَاةً أَوْسَعَ
أَنْتَ مَنْ يَأْخُذُهَا، يَوْمًا بَعْدَ يَوْمٍ
"""


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
