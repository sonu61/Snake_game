from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.hideturtle()

        self.update_scoreboard()


    def update_scoreboard(self):

        self.write(f"Score: {self.score}", font=("Arial", 12, "bold"), align='center')

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER !!!", font=("Arial", 12, "bold"), align='center')

    def score_increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

