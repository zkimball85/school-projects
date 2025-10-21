#Get all the necessary information from the user

winning_team_points = int(input("Enter the leading team's points: "))
losing_team_points = int(input("Enter the trailing team's points: "))
possession = input('Which team has possession of the ball? (leading/trailing): ').strip().lower()
time_remaining = int(input('Enter the time remaining in seconds: '))

#1. Calculate the point difference (the lead)

lead = winning_team_points - losing_team_points

#2. Subtract 3 points from the lead

adjusted_lead = lead - 3

#3. Adjust for ball possession

if possession == 'leading':
    adjusted_lead += 0.5
elif possession == 'trailing':
    adjusted_lead -= 0.5

#4. Check if the lead is too small for the formula to work

if adjusted_lead > 0:

#5. Square the result

    final_value = adjusted_lead ** 2
    
#6. Compare the squared value to the time remaining

    if final_value > time_remaining:
        print('The lead is safe!')
    else:
        print('The lead is NOT safe!')
else:
    print('The lead is NOT safe!')