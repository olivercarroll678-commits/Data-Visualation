# IMPORTING LIBRARIES

import pandas as pd
import matplotlib.pyplot as plt

#####################################################
#
#   GETTING CSV FILE AND READING THE CSV
#
#####################################################

def load_data():
    """Automatically loads Task4a_Glenstar_data.csv from the local folder."""

    filename = "Task4a_Glenstar_data.csv"

################################################################################
#
#   IF THE FILE IS NOT FOUND THE PROGRAM WILL TELL THE USER FILE IS NOT FOUND
#
################################################################################

    try:
        return pd.read_csv(filename)

    except FileNotFoundError:
        print(f"Error: '{filename}' not found. Please place it in this folder.")
        return None


###############################################################
#
#   ALLOWS THE GRAPHS TO SEE INTO THE CSV DATA
#
###############################################################

global data
data = load_data()

###################################################################################################################################
#
#   OUTPUTS THE MAIN MENU AND CHECKS THE USER INPUT TO CHOOSE WHAT DATA THEY WANT VISUALISED
#
###################################################################################################################################

def main_menu():

    # Menu will run until a valid option is entered
    valid = False

    while valid == False:

        # Displays the menu
        print("-"*70)
        print("---------- Athlete Performance Analysis Module ------------- ")
        print("-"*70)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("1. Places achieved by athlete")
        print("-"*50)
        print("2. Overall percentage of placement ")
        print("-"*50)
        print("3. Prize money won by athlete")
        print("-"*50)
        print("4. Rule set data chart")
        print("-"*50)
        print("5. Prize money per rule set")
        print("-"*50)
        print("6. Athlete rule set average score")
        print("-"*50)
        print("7. Athlete rule set success rate")
        print("-"*50)
        print("8. EXIT PROGRAM")

        # User enters their menu choice
        choice = input('Enter your number selection here: ')

################################################################################
#
#   CHECKS IF THE USER ENTERED A NUMBER
#
################################################################################

        if choice.isdigit():

            # Converts the choice into an integer
            choice = int(choice)

################################################################################
#
#   CHECKS IF THE NUMBER IS BETWEEN 1 AND 8
#
################################################################################

            if 1 <= choice <= 8:

                # Ends the loop if valid
                valid = True

            else:

                # Error message if number is outside range
                print("Must be within the appropriate range (1-8)")

        else:

            # Error message if input is not a number
            print("Sorry, you did not enter a valid option")

    # Returns the valid menu choice
    return choice


###################################################################################################################################
#
#   GETS ALL ATHLETE NAMES FROM THE CSV FILE
#
###################################################################################################################################

def get_athlete_names():

################################################################################
#
#   READS THE CSV FILE
#
################################################################################

    df = pd.read_csv("Task4a_Glenstar_data.csv")

################################################################################
#
#   GETS UNIQUE ATHLETE NAMES FROM THE ATHLETE COLUMN
#
################################################################################

    athletes = df["Athlete"].unique().tolist()

################################################################################
#
#   OUTPUTS THE ATHLETE MENU AND VALIDATES USER INPUT
#
################################################################################

    valid = False

    while valid == False:

        print("-"*70)
        print("---------- Athlete Performance Analysis Module ------------- ")
        print("-"*70)
        print("")
        print("--------------------- Athlete Positions Menu --------------------- ")
        print("Select an athlete:")

################################################################################
#
#   DISPLAYS ALL ATHLETES WITH A NUMBER NEXT TO THEM
#
################################################################################

        for i in range(len(athletes)):
            print(i + 1, " ", athletes[i])

################################################################################
#
#   USER INPUT
#
################################################################################

        selection = input('Enter your number selection here: ')

################################################################################
#
#   CHECKS IF INPUT IS A NUMBER
#
################################################################################

        if selection.isdigit():

            # Converts the input into an integer
            selection = int(selection)

################################################################################
#
#   CHECKS IF NUMBER IS WITHIN THE RANGE OF ATHLETES
#
################################################################################

            if 1 <= selection <= len(athletes):

                # Ends loop if valid
                valid = True

            else:

                # Error message if outside range
                print("Must be within the appropriate range")

        else:

            # Error message if not a number
            print("Sorry, you did not enter a valid option")

################################################################################
#
#   CORRECTS THE INDEX SO THE RIGHT ATHLETE IS CHOSEN
#
################################################################################

    chosen_athlete = athletes[selection - 1]

################################################################################
#
#   PRINTS THE CHOSEN ATHLETE TO CONFIRM SELECTION
#
################################################################################

    print("You have selected athlete:", chosen_athlete)

################################################################################
#
#   RETURNS THE CHOSEN ATHLETE
#
################################################################################

    return chosen_athlete
##########################################################################
#                                                                               
#   TO GET THE DATA RANGE FROM THE USER
#
##########################################################################
def get_date(start_end):
        #create a loop unless correct input is given
    flag = True
    
    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))

        # Make sure the data is in proper formating else it will not be accepted 
        try:
           pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return date

##########################################################################
#                                                                               
#   GET ALL REQUIRED DATA TO SHOW THE ATHLETE PLACEMENT
#
##########################################################################


def get_data_by_athlete_and_date(athlete, start_date, end_date):

    #reads the entire CSV 
    all = pd.read_csv("Task4a_Glenstar_data.csv")
    #focus on reading athlete data
    athlete_data = all.loc[all["Athlete"] == athlete].copy()
    #check date range for the athlete data and saves it as athlete data
    athlete_data["Date"]= pd.to_datetime(athlete_data["Date"], format="%d/%m/%Y", errors="raise")
    #checks the date range
    date_range = (athlete_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (athlete_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    #extracts the required data
    athlete_extract = athlete_data.loc[date_range]
    
    return athlete_extract

##########################################################################
#                                                                               
#   CALCULATES THE PLACE OF EACH ATHLETE AND SAVE THE TO BE DISPLAY LATER 
#
##########################################################################
def calculate_places (athlete_extract, athlete, start_date, end_date):
    gold = athlete_extract['Place'].value_counts().get("Gold")
    silver = athlete_extract['Place'].value_counts().get("Silver")
    bronze = athlete_extract['Place'].value_counts().get("Bronze")
    top = athlete_extract['Place'].value_counts().get("Top 10")
    no_place = athlete_extract['Place'].value_counts().get("Not Placed")


#############################################################################################################
#                                                                               
#   OUTPUT THE ATHLETE AND THERE PLACEMENT ALONG WITH HOW OFTEN THEY GET THAT PLACE 
#
#############################################################################################################

    print("Here is the break down of the performance of {} between {} and {}: ".format(athlete, start_date, end_date))
    print("Gold medals: ", gold)
    print("Silver medals:", silver)
    print("Bronze medals: ", bronze)
    print("Top 10: ", top)
    print("Not placed: ", no_place)

#################################################################################################
#                                                                               
#   PRODUCES A PIE CHART OF ALL OF THE PLACEMENTS NO MATTER ATHLETE AND OR SPORT 
#
#################################################################################################


def all_places(data):
    """Displays a pie chart of overall placement distribution."""
# get all the place data
    totals = data["Place"].value_counts()
# formats into a pie chart
    totals.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        figsize=(8, 8)
    )
#formats the title and lables
    plt.title("Overall Placement Distribution Across All Years")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()


#################################################################################################
#                                                                               
#   PRODUCES A BAR CHART OF THE PRIZE MONEY WON PER ATHLETE
#
#################################################################################################


def prize_money_won_per_athlete(data):

    """Generates a bar chart of prize money won per athlete."""

    #groups data by Athlete and prize money
    grouped_data = data.groupby("Athlete")["Prize Money"].sum()
    #kind of chart is what the line below does
    grouped_data.plot(kind="bar", figsize=(10, 6))
    #creates the chart 
    plt.title("Prize money Achieved Per Athlete")
    plt.xlabel("Athlete's name")
    plt.ylabel("Amount of money")
    plt.ticklabel_format(style='plain', axis='y')
    plt.tight_layout()
    plt.show()

    
#################################################################################################
#                                                                               
#   PRODUCES A BAR CHART ON THE WHAT EACH PERSON PLACED IN A RULE SET  
#
#################################################################################################


def athlete_rule_set_chart(data):
    """Displays athlete performance across rule sets."""
    #groups of by Athlete Rule set and Place 
    results = data.groupby(
        ["Athlete", "Rule Set"]
    )["Place"].value_counts().unstack(fill_value=0)
    # creates the chart type 
    results.plot(
        kind="bar",
        stacked=True,
        figsize=(14, 8)
    )
    #creating the chart
    plt.title("Athlete Performance by Rule Set")
    plt.xlabel("Athlete and Rule Set")
    plt.ylabel("Number of Results")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



#################################################################################################
#                                                                               
#   PRODUCES A BAR CHART OF MONEY PER RULE SET 
#
#################################################################################################



def prize_money_per_rule_set(data):
    #groups of by Athlete Rule set and Place 
    results = data.groupby(["Athlete", "Rule Set"])["Prize Money"].sum()
        # creates the chart type 
    results.plot(kind="bar", figsize=(10, 6))
     #creating the chart
    plt.title("Prize money Achieved Per Athlete")
    plt.xlabel("Athlete's name")
    plt.ylabel("Amount of money")
    plt.ticklabel_format(style='plain', axis='y')
    plt.tight_layout()
    plt.show()


#################################################################################################
#                                                                               
#   PRODUCES A BAR CHART RULE SET AVGERGE SCORE 
#
#################################################################################################


def athlete_rule_set_avg_score(data):
    """Shows average performance score per athlete per rule set."""

    # convert placements into numeric scores
    score_map = {
        "Gold": 4,
        "Silver": 3,
        "Bronze": 2,
        "Top 10": 1,
        "Not Placed": 0
    }

    temp = data.copy()
    temp["Score"] = temp["Place"].map(score_map)

    # group by athlete + rule set
    results = temp.groupby(["Athlete", "Rule Set"])["Score"].mean().unstack()

    # plot
    results.plot(kind="bar", figsize=(12, 6))

    plt.title("Average Athlete Performance Score by Rule Set")
    plt.xlabel("Athlete")
    plt.ylabel("Average Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


#################################################################################################
#                                                                               
#   PRDUCE A BAR CHART OF ATHLETE SUCCESS RATE
#
#################################################################################################

def athlete_rule_set_success_rate(data):
    """Shows percentage of medals (Gold/Silver/Bronze) per rule set."""

    temp = data.copy()

    # mark medals
    temp["Is Medal"] = temp["Place"].isin(["Gold", "Silver", "Bronze"])

    # group by rule set and athlete
    results = temp.groupby(["Athlete", "Rule Set"])["Is Medal"].mean().unstack()

    # convert to percentage
    results = results * 100

    # plot
    results.plot(kind="bar", figsize=(12, 6))

    plt.title("Athlete Medal Success Rate by Rule Set (%)")
    plt.xlabel("Athlete")
    plt.ylabel("Medal Percentage (%)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

##################################################################################################
#                                                                               
#   MAIN MENU THAT HOLDS ALL THE FUNCTIONS AND CALL THEM WHEN NEEDED 
#
#################################################################################################


main_menu_choice = main_menu()

if main_menu_choice == 1:
    athlete = get_athlete_names()
    start_date = get_date("start")
    end_date = get_date("end")
    athlete_extract = get_data_by_athlete_and_date(athlete, start_date, end_date)
    calculate_places (athlete_extract, athlete, start_date, end_date)

elif main_menu_choice == 2:
    all_places(data)

elif main_menu_choice == 3:
    prize_money_won_per_athlete(data)

elif main_menu_choice == 4:
    athlete_rule_set_chart(data)

elif main_menu_choice == 5:
    prize_money_per_rule_set(data)

elif main_menu_choice == 6:
    athlete_rule_set_avg_score(data)

elif main_menu_choice == 7:
    athlete_rule_set_success_rate(data)

elif main_menu_choice == 8:
    print("-"*50)
    print("EXITING PROGRAM")
    print("-"*50)




