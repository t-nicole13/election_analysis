'''counties = ["Arapahoe", "Denver", "Jefferson"]

for county in counties:
    print(county) '''


#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

'''for county in counties_dict:
    print(county)'''


'''for county, zip in counties_dict.items():
    print(county, zip)'''


'''for county in counties_dict.keys():
    print(county)'''

'''for zip in counties_dict.values():
    print(zip)'''

'''for county in counties_dict:
    print(counties_dict[county])'''


'''for county, registered_voter in counties_dict.items():
    #print(county + " county has " + str(registered_voter) + " registered voters.")
    print(f"{county} county has {registered_voter} registered voters.")'''


#Print each county and registered voter from the dictionary

'''for county, registered_voter in counties_dict.items():
    print(f"{county} county has {registered_voter:,} registered voters.")'''


#Print each county and registered voter from the dictionary

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for counties_dict in voting_data:
 
 # Create a filename variable to a direct or indirect path to the file.
# # As we perform the election analysis, we'll write data to this file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file. Add the newline escape sequence
#     txt_file.write("Counties in the Election\n_ _ _ _ _ _ _ _ _ _ _ _ _\nArapahoe\nDenver\nJefferson")


