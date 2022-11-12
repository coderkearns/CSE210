from game.card import Card


class Director:
    def __init__(self):
        self.first_card = Card()
        self.next_card = Card()

        self.is_playing = True
        self.score = 300

        self.guessed_lower = False

    def start_game(self):
        while self.is_playing:
            self.do_step_1()
            self.get_inputs()
            self.do_step_2()
            self.do_outputs()

            if self.score == 0:
                break

            self.is_playing = input("Play again? [y/N] ").lower() == "y"
            print()

    def do_step_1(self):
        self.first_card.draw()
        print(f"The card is: {self.first_card.value}")

    def get_inputs(self):
        higher_or_lower = input("Higher or lower? [H/l] ").lower()
        self.guessed_lower = higher_or_lower == "l"

    def do_step_2(self):
        self.next_card.draw()
        was_higher = self.first_card.is_higher_than(self.next_card)

        if self.guessed_lower:
            if not was_higher:
                self.score += 100
            else:
                self.score -= 75
        else:
            if was_higher:
                self.score += 100
            else:
                self.score -= 75

        if self.score < 0:
            self.score = 0

    def do_outputs(self):
        print(f"Next card was: {self.next_card.value}")
        print(f"You score is: {self.score}")
