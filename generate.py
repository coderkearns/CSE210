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


template_prove_readme = template(
    """# {assignment_name}

## Description

{description}

## Project Structure

```
prove/
├── README.md
└── __main__.py
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
from .this

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
    is_prove = input("(1) Prepare or (2) Prove? [1] ").strip() == "2"
    if is_prove:
        generate_prove()
    else:
        generate_prepare()


main()
