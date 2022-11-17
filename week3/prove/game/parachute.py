PARACHUTE_ICONS = {
    5: """ ___
/   \\
-----
\   /
 \ /
  o
 /|\\
 / \\

^^^^^^^
""",
    4: """
/   \\
-----
\   /
 \ /
  o
 /|\\
 / \\

^^^^^^^
""",
    3: """

-----
\   /
 \ /
  o
 /|\\
 / \\

^^^^^^^
""",
    2: """


\   /
 \ /
  o
 /|\\
 / \\

^^^^^^^
""",
    1: """



 \ /
  o
 /|\\
 / \\

^^^^^^^
""",
    0: """




  x
 /|\\
 / \\

^^^^^^^
""",
}


def output_parachute(strings_left):
    """Prints the prototype icon matching the number of strings left"""
    print(PARACHUTE_ICONS[strings_left])
