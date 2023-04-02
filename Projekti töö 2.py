from tkinter import *
from tkinter import messagebox

class TripsTrapsTrull:
    def __init__(self, trips):
        self.trips = trips
        self.trips.title("Trips traps trull")

        self.praegune_mängija = "X"
        self.game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.player_scores = {"X": 0, "O": 0}  

        self.create_board()
        self.create_scoreboard()  

    def create_board(self):
        self.button_list = []
        for row in range(3):
            for col in range(3):
                button = Button(self.trips, text="", width=25, height=15,
                                command=lambda row=row, col=col: self.button_click(row, col))
                button.grid(row=row, column=col)
                self.button_list.append(button)
    
    def create_scoreboard(self):
        self.scoreboard = Label(self.trips, text=f"X: {self.player_scores['X']}  O: {self.player_scores['O']}")
        self.scoreboard.grid(row=3, column=0, columnspan=3)
    
    def update_scoreboard(self):
        self.scoreboard.configure(text=f"X: {self.player_scores['X']}  O: {self.player_scores['O']}")
    
    def button_click(self, row, col):
        if self.game_board[row][col] == "":
            self.game_board[row][col] = self.praegune_mängija
            self.button_list[row*3 + col].configure(text=self.praegune_mängija)
            
            if self.check_win():
                messagebox.showinfo("Võitja!", f"Mängija {self.praegune_mängija} võitis!")
                self.player_scores[self.praegune_mängija] += 1  # Update player score
                self.update_scoreboard()  # Update scoreboard
                self.reset_game()
            elif self.check_tie():
                messagebox.showinfo("Viik!", "See on viik!")
                self.reset_game()
            else:
                self.switch_player()
                
    def check_win(self):
        for i in range(3):
            if self.game_board[i][0] == self.game_board[i][1] == self.game_board[i][2] != "":
                return True
            elif self.game_board[0][i] == self.game_board[1][i] == self.game_board[2][i] != "":
                return True
        if self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] != "":
            return True
        elif self.game_board[2][0] == self.game_board[1][1] == self.game_board[0][2] != "":
            return True
        else:
            return False           
                
    def switch_player(self):
        if self.praegune_mängija == "X":
            self.praegune_mängija = "O"
        else:
            self.praegune_mängija = "X"
            
    def reset_game(self):
        self.current_player = "X"
        self.game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
        for button in self.button_list:
            button.configure(text="")
            
    
         
    def check_tie(self):
        for row in self.game_board:
            for cell in row:
                if cell == "":
                    return False
        return True
                
            
        
root = Tk()
mäng = TripsTrapsTrull(root)
root.mainloop()
