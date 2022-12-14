#!/bin/env python3
import os
from pathlib import Path


def template(temp):
    def inner(*args, **kwargs):
        return temp.format(*args, **kwargs)

    return inner


template_question = template(
    """> {question}

Answer here. Make sure to: (1) answer the question, (2) use code examples, (3) write at least 100 words, and (4) write in paragraph form.

"""
)


def generate_prepare():
    week_number = int(input("Week number? "))
    question = input("Question? ").strip()

    week_dir = Path(f"week{week_number}")
    prepare_dir = week_dir.joinpath("prepare")

    if not week_dir.exists():
        week_dir.mkdir()
        print(f"Creating directory '{week_dir}'")

    if not prepare_dir.exists():
        prepare_dir.mkdir()
        print(f"Creating directory '{prepare_dir}'")

    question_file = prepare_dir.joinpath("prepare.md")

    question_file.write_text(template_question(question=question))
    print(f"Creating file '{question_file}'")


def generate_teach():
    week_number = int(input("Week number? "))
    question = input("Question? ").strip()

    week_dir = Path(f"week{week_number}")
    teach_dir = week_dir.joinpath("teach")

    if not week_dir.exists():
        week_dir.mkdir()
        print(f"Creating directory '{week_dir}'")

    if not teach_dir.exists():
        teach_dir.mkdir()
        print(f"Creating directory '{teach_dir}'")

    question_file = teach_dir.joinpath("teach.md")

    question_file.write_text(template_question(question=question))
    print(f"Creating file '{question_file}'")


template_prove_readme = template(
    """# {assignment_name}

## Description

{description}

## Project Structure

```
prove/
├── game/
│   ├── <...other_files_here>
│   └── director.py
├── __main__.py
└── README.md
```

## Dependencies

- *no dependencies*

## Author

Carter Kearns (coder.kearns@gmail.com)

"""
)

template_prove_main = template(
    """\"""
Week {week_number}: {assignment_name}

Author: Carter Kearns
\"""
# Replace "game" with the folder name, "director" with the file name.
# See the dice-game template from week 2 for an example.
from game.director import Director

def main():
    director = Director()
    director.start_game()

if __name__ == "__main__":
    main()

"""
)


def generate_prove():
    week_number = int(input("Week number? "))
    assignment_name = input("Assignment name? ").strip().title()
    description = input("Description? ").strip().replace("\\n", "\n")

    week_dir = Path(f"week{week_number}")
    prove_dir = week_dir.joinpath("prove")

    if not week_dir.exists():
        week_dir.mkdir()
        print(f"Creating directory '{week_dir}'")

    if not prove_dir.exists():
        prove_dir.mkdir()
        print(f"Creating directory '{prove_dir}'")

    readme_file = prove_dir.joinpath("README.md")
    main_file = prove_dir.joinpath("__main__.py")

    readme_file.write_text(
        template_prove_readme(assignment_name=assignment_name, description=description)
    )
    print(f"Creating file '{readme_file}'")
    main_file.write_text(
        template_prove_main(assignment_name=assignment_name, week_number=week_number)
    )
    print(f"Creating file '{main_file}'")


def main():
    while True:
        attempt = input("(1) Prepare, (2) Teach, or (3) Prove? ")
        if attempt not in "123":
            continue

        if attempt == "1":
            generate_prepare()
        elif attempt == "2":
            generate_teach()
        elif attempt == "3":
            generate_prove()

        break


main()
