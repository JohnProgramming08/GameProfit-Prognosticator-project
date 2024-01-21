import tkinter as tk


#creating a class called GameProfit
class GameProfit:
  #setting up the initial variables for the class
  def __init__(self, money, time, goal):
    self.money = money
    self.time = time
    self.goal = goal
    self.money_minute = self.money / self.time

  #calculates money made every 15 minutes
  def calculate_money_15minutes(self):
    money_15minutes = self.money_minute * 15
    return money_15minutes

  #calculates money made every 30 minutes
  def calculate_money_30minutes(self):
    money_30minutes = self.money_minute * 30
    return money_30minutes

  #calculates money made every 60 minutes
  def calculate_money_60minutes(self):
    money_60minutes = self.money_minute * 60
    return money_60minutes

  #calculates how long it takes to earn desired funds
  def calculate_time(self):
    time_value = self.time
    money_value = self.money
    while self.money < self.goal:
      self.money += money_value
      self.time += time_value
    return self.time


#creating a class called MainWindow
class MainWindow:

  def __init__(self):
    #creating the root widget
    self.root = tk.Tk()
    self.root.config(bg="white")
    self.root.title("GameProfit Prognasticator")
    self.mode = "light"

  #creating all the frames for the program
  def frames(self):
    #creating the initial frames
    self.frame = tk.LabelFrame(self.root,
                               padx=5,
                               pady=5,
                               bg="light grey")
    self.frame.grid(row=1, column=0)

    self.frame2 = tk.LabelFrame(self.root,
                                padx=5,
                                pady=5,
                                bg="light grey")
    self.frame2.grid(row=3, column=0)

    self.frame3 = tk.LabelFrame(self.root,
                                padx=5,
                                pady=5,
                                bg="light grey")
    self.frame3.grid(row=5, column=0)

    self.frame4 = tk.LabelFrame(self.root,
                                padx=5,
                                pady=5,
                                bg="light grey")
    self.frame4.grid(row=0, column=0)

    self.frame5 = tk.LabelFrame(self.root,
                                padx=5,
                                pady=5,
                                bg="light grey",
                                text="SETTINGS")
    self.frame5.grid(row=0, column=0)

  #creating the intro screen
  def intro_frame4(self):
    #asking the user a question
    self.intro_question = tk.Label(self.frame4,
                                   text="Have you been here before?",
                                   bg="light grey")
    self.intro_question.grid(row=0, column=0, columnspan=2)

    #a command for the no button
    def noclick():
      no_button.destroy()
      yes_button.destroy()
      self.intro_question.destroy()

      #adding a description for the app
      description = tk.Label(
          self.frame4,
          text=
          "This is a program used for predicting the amount of money you can make \nin an amount of time using one method! \n \nIm currently studying GCSE computer science; this project was made \nso that i could practise using some of the skills i learned over \nthe six weeks holidays!",
          bg="light grey")
      description.grid(row=0, column=0)

      #creating a command for the next button
      def next_click():
        next_button.destroy()
        description.destroy()
        self.frame4.grid_forget()

        MainWindow.calculate_frame1(root_window)
        MainWindow.calculate_frame2(root_window)
        MainWindow.calculate_frame3(root_window)
        MainWindow.settings_frame5(root_window)

      #creating a next button
      next_button = tk.Button(self.frame4,
                              text="Next",
                              bg="cyan",
                              command=next_click)
      next_button.grid(row=1, column=0)

    #creating a no button
    no_button = tk.Button(self.frame4, text="NO", bg="cyan", command=noclick)
    no_button.grid(row=1, column=0)

    #creating a command for the yes button
    def yesclick():
      no_button.destroy()
      yes_button.destroy()
      self.intro_question.destroy()
      self.frame4.grid_forget()

      MainWindow.calculate_frame1(root_window)
      MainWindow.calculate_frame2(root_window)
      MainWindow.calculate_frame3(root_window)
      MainWindow.settings_frame5(root_window)

    #creating a yes button
    yes_button = tk.Button(self.frame4,
                           text="YES",
                           bg="cyan",
                           command=yesclick)
    yes_button.grid(row=1, column=1)

  #entries for the money and time
  def calculate_frame1(self):
    #adding an entry
    self.entry_description = tk.Label(self.frame,
                                      text="Money earned per use of method: ",
                                      bg="light grey")
    self.entry_description.grid(row=0, column=0)

    self.money_entry = tk.Entry(self.frame, width=25, borderwidth=2)
    #self.money_entry.insert(0, "100")
    self.money_entry.grid(row=1, column=0)

    #adding a column of nothingness
    self.space = tk.Label(self.frame, text="           ", bg="light grey")
    self.space.grid(row=0, column=1)

    #adding an entry
    self.entry_description2 = tk.Label(self.frame,
                                       text="How long the method takes(m): ",
                                       bg="light grey")
    self.entry_description2.grid(row=0, column=2)

    self.time_entry = tk.Entry(self.frame, width=25, borderwidth=2)
    #self.time_entry.insert(0, "10")
    self.time_entry.grid(row=1, column=2)

    #creating empty rows
    self.empty_row1 = tk.Label(self.root, text="", bg="white")
    self.empty_row1.grid(row=2, column=0)

    self.empty_row2 = tk.Label(self.root, text="", bg="white")
    self.empty_row2.grid(row=4, column=0)

  #money per 15 minutes to 1 hour
  def calculate_frame2(self):
    self.minutes15_label = tk.Label()
    self.minutes30_label = tk.Label()
    self.minutes60_label = tk.Label()

    #adding a command for the button
    def click2():
      #creates an object called funds
      money = int(self.money_entry.get())
      time = int(self.time_entry.get())
      funds = GameProfit(money, time, 0)

      #calculating money made per amount of time
      minutes15 = GameProfit.calculate_money_15minutes(funds)
      minutes30 = GameProfit.calculate_money_30minutes(funds)
      minutes60 = GameProfit.calculate_money_60minutes(funds)

      #deleting the previous calculation results
      self.minutes15_label.destroy()
      self.minutes30_label.destroy()
      self.minutes60_label.destroy()

      #light mode
      if self.mode == "light":
        #adds the calculated money per unit of time
        self.minutes15_label = tk.Label(self.frame2,
                                        text=minutes15,
                                        bg="white",
                                        fg="black")
        self.minutes15_label.grid(row=6, column=0)

        self.minutes30_label = tk.Label(self.frame2,
                                        text=minutes30,
                                        bg="white",
                                        fg="black")
        self.minutes30_label.grid(row=6, column=1)

        self.minutes60_label = tk.Label(self.frame2,
                                        text=minutes60,
                                        bg="white",
                                        fg="black")
        self.minutes60_label.grid(row=6, column=2)

      #dark mode
      elif self.mode == "dark":
        #adds the calculated money per unit of time
        self.minutes15_label = tk.Label(self.frame2,
                                        text=minutes15,
                                        bg="#5a5a5a",
                                        fg="white")
        self.minutes15_label.grid(row=6, column=0)

        self.minutes30_label = tk.Label(self.frame2,
                                        text=minutes30,
                                        bg="#5a5a5a",
                                        fg="white")
        self.minutes30_label.grid(row=6, column=1)

        self.minutes60_label = tk.Label(self.frame2,
                                        text=minutes60,
                                        bg="#5a5a5a",
                                        fg="white")
        self.minutes60_label.grid(row=6, column=2)

    #adding a calculate button
    self.calculate_button = tk.Button(self.frame2,
                                      text="Calculate Estimate",
                                      command=click2,
                                      bg="cyan")
    self.calculate_button.grid(row=3, column=1)

    #adding the three descriptions of the values below them
    self.money_title = tk.Label(self.frame2,
                                text="Money per 15 minutes:",
                                bg="light grey")
    self.money_title.grid(row=5, column=0)

    self.money_title2 = tk.Label(self.frame2,
                                 text="Money per 30 minutes:",
                                 bg="light grey")
    self.money_title2.grid(row=5, column=1)

    self.money_title3 = tk.Label(self.frame2,
                                 text="Money per 60 minutes:",
                                 bg="light grey")
    self.money_title3.grid(row=5, column=2)

  #calculating how long it will take to get desired funds
  def calculate_frame3(self):
    self.time_label = tk.Label()

    #adding an entry
    self.entry_description3 = tk.Label(
        self.frame3,
        text="How much money you are trying to get: ",
        bg="light grey")
    self.entry_description3.grid(row=0, column=0)

    self.money_goal_entry = tk.Entry(self.frame3, width=25, borderwidth=2)
    self.money_goal_entry.grid(row=1, column=0)

    #adding a command for the button
    def click3():
      #creating an object called funds
      money = int(self.money_entry.get())
      time = int(self.time_entry.get())
      goal = int(self.money_goal_entry.get())
      funds = GameProfit(money, time, goal)

      #calculating how long it will take to get the desired funds
      goal_time = GameProfit.calculate_time(funds)

      #deleting the results of the previous calculation
      self.time_label.destroy()

      #light mode
      if self.mode == "light":
        #adds the calculated time needed
        self.time_label = tk.Label(self.frame3,
                                   text=str(f"{goal_time} minutes"),
                                   bg="white",
                                   fg='black')
        self.time_label.grid(row=3, column=0)

      #dark mode
      elif self.mode == "dark":
        #adds the calculated time needed
        self.time_label = tk.Label(self.frame3,
                                   text=str(f"{goal_time} minutes"),
                                   bg="#5a5a5a",
                                   fg="white")
        self.time_label.grid(row=3, column=0)

    #creating a second calculate button
    self.calculate_button2 = tk.Button(self.frame3,
                                       text="Calculate Estimate",
                                       bg="cyan",
                                       command=click3)
    self.calculate_button2.grid(row=1, column=1)

    #adding a description of the value below it
    self.time_title = tk.Label(self.frame3,
                               text="Amount of time to get desired money: ",
                               bg="light grey")
    self.time_title.grid(row=2, column=0)

  #a dark and light button for the gui
  def settings_frame5(self):
    #creating a command for the settings button
    def settings_click():
      self.frame5.grid()

      #creating a command for the light button
      def light_click():
        self.mode = "light"
        #changes every widget to the light colour palette
        self.root.config(bg="white")
        self.frame.config(bg="light grey")
        self.frame2.config(bg="light grey")
        self.frame3.config(bg="light grey")
        self.frame5.config(bg="light grey")
        self.entry_description.config(bg="light grey")
        self.money_entry.config(bg="white")
        self.space.config(bg="light grey")
        self.entry_description2.config(bg="light grey")
        self.time_entry.config(bg="white")
        self.empty_row1.config(bg="white")
        self.empty_row2.config(bg="white")
        self.minutes15_label.config(bg="white", fg="black")
        self.minutes30_label.config(bg="white", fg="black")
        self.minutes60_label.config(bg="white", fg="black")
        self.calculate_button.config(bg="cyan")
        self.money_title.config(bg="light grey")
        self.money_title2.config(bg="light grey")
        self.money_title3.config(bg="light grey")
        self.entry_description3.config(bg="light grey")
        self.money_goal_entry.config(bg="white")
        self.time_label.config(bg="white", fg="black")
        self.calculate_button2.config(bg="cyan")
        self.time_title.config(bg="light grey")
        self.light_button.config(bg="cyan")
        self.dark_button.config(bg="cyan")
        self.destroy_button.config(bg="red")
        self.settings_button.config(bg="cyan")

      if self.mode == "light":
        #creating a light mode button
        self.light_button = tk.Button(self.frame5,
                                      text="Light Mode",
                                      bg="cyan",
                                      command=light_click)
        self.light_button.grid(row=0, column=0)

      elif self.mode == "dark":
        #creating a light mode button
        self.light_button = tk.Button(self.frame5,
                                      text="Light Mode",
                                      bg="dark cyan",
                                      command=light_click)
        self.light_button.grid(row=0, column=0)

      #creating a command for the dark button
      def dark_click():
        self.mode = "dark"
        #changes every widget to the dark colour palette
        self.root.config(bg="#5a5a5a")
        self.frame.config(bg="#8d8d8d")
        self.frame2.config(bg="#8d8d8d")
        self.frame3.config(bg="#8d8d8d")
        self.frame5.config(bg="#8d8d8d")
        self.entry_description.config(bg="#8d8d8d")
        self.money_entry.config(bg="white")
        self.space.config(bg="#8d8d8d")
        self.entry_description2.config(bg="#8d8d8d")
        self.time_entry.config(bg="white")
        self.empty_row1.config(bg="#5a5a5a")
        self.empty_row2.config(bg="#5a5a5a")
        self.minutes15_label.config(bg="#5a5a5a", fg="white")
        self.minutes30_label.config(bg="#5a5a5a", fg="white")
        self.minutes60_label.config(bg="#5a5a5a", fg="white")
        self.calculate_button.config(bg="dark cyan")
        self.money_title.config(bg="#8d8d8d")
        self.money_title2.config(bg="#8d8d8d")
        self.money_title3.config(bg="#8d8d8d")
        self.entry_description3.config(bg="#8d8d8d")
        self.money_goal_entry.config(bg="white")
        self.time_label.config(bg="#5a5a5a", fg="white")
        self.calculate_button2.config(bg="dark cyan")
        self.time_title.config(bg="#8d8d8d")
        self.light_button.config(bg="dark cyan")
        self.dark_button.config(bg="dark cyan")
        self.destroy_button.config(bg="dark red")
        self.settings_button.config(bg="dark cyan")

      if self.mode == "light":
        #creating a dark mode button
        self.dark_button = tk.Button(self.frame5,
                                     text="Dark Mode",
                                     bg="cyan",
                                     command=dark_click)
        self.dark_button.grid(row=0, column=1)

      elif self.mode == "dark":
        #creating a dark mode button
        self.dark_button = tk.Button(self.frame5,
                                     text="Dark Mode",
                                     bg="dark cyan",
                                     command=dark_click)
        self.dark_button.grid(row=0, column=1)

      #removes all of the widgets in settings
      def destroy_click():
        self.light_button.destroy()
        self.dark_button.destroy()
        self.destroy_button.destroy()
        self.frame5.grid_remove()

      if self.mode == "light":
        #creating a destroy button
        self.destroy_button = tk.Button(self.frame5,
                                        text="X",
                                        bg="red",
                                        command=destroy_click)
        self.destroy_button.grid(row=0, column=2)

      elif self.mode == "dark":
        #creating a destroy button
        self.destroy_button = tk.Button(self.frame5,
                                        text="X",
                                        bg="dark red",
                                        command=destroy_click)
        self.destroy_button.grid(row=0, column=2)

    #creating a settings button
    self.settings_button = tk.Button(self.root,
                                     text="Settings",
                                     bg="cyan",
                                     command=settings_click)
    self.settings_button.grid(row=0, column=0, stick="w")


#starting the main program
if __name__ == "__main__":
  root_window = MainWindow()
  MainWindow.frames(root_window)
  MainWindow.intro_frame4(root_window)
  tk.mainloop()

#implement exception handling and unit testing