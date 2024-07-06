import subprocess as sp
import pymysql
import pymysql.cursors
import mysql.connector


def Get_Criminal_Record():
    """
    Function to implement option 3
    """
    try:
        cursor = con.cursor(buffered=True, dictionary=True)
        print("Below are all candidates with no criminal records(clean)\n")
        query = "SELECT c.Name FROM CANDIDATE c LEFT JOIN CRIMINAL_RECORDS cr ON c.CandidateID = cr.CandidateID WHERE cr.CriminalRecord = 'CLEAN'"

        # print(query)
        cursor.execute(query)
        con.commit()

        # Name = [Name[0] for Name in cursor.execute(query)]
        row = cursor.fetchone()
        while row:
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()

    except Exception as e:
        con.rollback()
        print("Failed to load database")
        print(">>>>>>>>>>>>>", e)

    print("Below are all candidates with criminal records\n")

    try:
        cursor = con.cursor(buffered=True, dictionary=True)
        query = "SELECT c.Name,cr.CriminalRecord FROM CANDIDATE c LEFT JOIN CRIMINAL_RECORDS cr ON c.CandidateID = cr.CandidateID WHERE cr.CriminalRecord <> 'CLEAN'"

        # print(query)
        cursor.execute(query)
        con.commit()
        # Name = [Name[0] for Name in cursor.execute(query)]
        count=0
        row = cursor.fetchone()
        while row:
            count+=1
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()
        if(count==0):
            print("No Entries\n")

    except Exception as e:
        con.rollback()
        print("Failed to load database")
        print(">>>>>>>>>>>>>", e)

    return


def Add_Candidate():
    """
    Function to insert a new candidate into the CANDIDATE table
    """
    try:
        # Takes candidate details as input
        candidate = {}
        print("Enter new candidate's details: ")
        candidate["CandidateID"] = input("Candidate ID: ")
        candidate["CasteStatus"] = input("Caste Status: ")
        candidate["Age"] = int(input("Age: "))
        candidate["Gender"] = input("Gender: ")
        candidate["Name"] = input("Name: ")
        candidate["TotalFinancialAssets"] = int(
            input("Total Financial Assets: "))
        candidate["PartyID"] = input("PartyID: ")
        candidate["ContesterID"] = input("Contester ID (if any): ")

        cursor = con.cursor()

        # Execute the query to insert a new candidate into the CANDIDATE table
        query = "INSERT INTO CANDIDATE(CandidateID, CasteStatus,Age, Gender, Name, TotalFinancialAssets, PartyID, ContesterID) VALUES('%s', '%s', '%d', '%s', '%s', '%d', '%s', %s)" % (
            candidate["CandidateID"], candidate["CasteStatus"], candidate["Age"], candidate["Gender"], candidate["Name"], candidate["TotalFinancialAssets"], candidate["PartyID"], candidate["ContesterID"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def Add_VOTE():
    """
    Function to insert a new candidate into the CANDIDATE table
    """
    try:
        # Takes candidate details as input
        vote = {}
        print("Enter new vote details: ")
        vote["VoteID"] = input("Vote ID: ")
        vote["VoterID"] = input("Voter ID: ")
        vote["ElectionID"] = input("Election ID: ")
        vote["CandidateID"] = input("Candidate ID: ")

        cursor = con.cursor()

        # Execute the query to insert a new candidate into the CANDIDATE table
        query = "INSERT INTO VOTE(VoteID,VoterID,ElectionID,CandidateID) VALUES('%s', '%s','%s', '%s')" % (
            vote["VoteID"], vote["VoterID"], vote["ElectionID"], vote["CandidateID"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def Add_PARTY():
    """
    Function to insert a new candidate into the CANDIDATE table
    """
    try:
        # Takes candidate details as input
        party = {}
        print("Enter new party's details: ")
        party["PartyID"] = input("Party ID: ")
        party["PartyName"] = input("Party Name: ")
        party["PartyMembership"] = int(input("Party Membership: "))
        party["PartySymbol"] = input("Party Symbol: ")
        party["PoliticalPosition"] = input("Political Position: ")

        cursor = con.cursor()

        # Execute the query to insert a new candidate into the CANDIDATE table
        query = "INSERT INTO PARTY(PartyID,PartyName,PartyMembership,PartySymbol,PoliticalPosition) VALUES('%s', '%s', '%d', '%s', '%s')" % (
            party["PartyID"], party["PartyName"], party["PartyMembership"], party["PartySymbol"], party["PoliticalPosition"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def Total_budget() :
    try:
        election_id = input("enter the election id for the particular year :")
        cursor = con.cursor(buffered=True, dictionary=True)
        
        query = f"SELECT SUM(Amount) AS TotalBudgetAllocated FROM BUDGET WHERE ElectionID = '{election_id}';"
        cursor.execute(query)
        con.commit()
        # Name = [Name[0] for Name in cursor.execute(query)]
        count=0
        row = cursor.fetchone()
        while row:
            count+=1
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()
        if(count==0):
            print("No Entries\n")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
        
    return
        

def Get_Candidate_minmax_age():
    try:
        cursor = con.cursor(buffered=True, dictionary=True)
        query_max_age = "SELECT c.Name,c.Age AS MaximumAge FROM CANDIDATE c WHERE c.AGE = (SELECT MAx(Age) AS MaximumAge FROM CANDIDATE);"
        cursor.execute(query_max_age)
        con.commit()
        # Name = [Name[0] for Name in cursor.execute(query)]
        row = cursor.fetchone()
        count=0
        while row:
            count+=1
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()
        if(count==0):
            print("No Entries\n")
 
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    
    try:
        query_min_age = "SELECT c.Name,c.Age AS MinimumAge FROM CANDIDATE c WHERE c.AGE = (SELECT MIN(Age) AS MinimumAge FROM CANDIDATE);"
        cursor.execute(query_min_age)
        con.commit()
        # Name = [Name[0] for Name in cursor.execute(query)]
        count=0
        row = cursor.fetchone()
        while row:
            count+=1
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()
        if(count==0):
            print("No Entries\n")
        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    
    return

def Party_information():
    try:
        name = input("Enter name of party you want info about: ")
        cursor = con.cursor(buffered=True,dictionary=True)
        print("Below are all voter with age as given in input\n")
        query = f"SELECT v.PartyID,v.PartySymbol,v.PoliticalPosition FROM PARTY v WHERE v.PartyID = '{name}';"
        
        # print(query)
        cursor.execute(query)
        con.commit()

        # Name = [Name[0] for Name in cursor.execute(query)]
        count=0
        row = cursor.fetchone()
        while row:
            count+=1
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone() 
        if(count==0):
            print("No Entries\n")
          

    except Exception as e:
        con.rollback()
        print("Failed to load database")
        print(">>>>>>>>>>>>>", e)
        
    return

def Constituency_info() :
    try:
        cursor = con.cursor(buffered=True,dictionary=True)
        print("Urban constituencies are:\n")
        query = ("SELECT * FROM CONSTITUENCY c WHERE c.ConstituencyType = 'Urban' GROUP BY c.ConstituencyID;")
        cursor.execute(query)
        con.commit()

        # Name = [Name[0] for Name in cursor.execute(query)]
        count=0
        row = cursor.fetchone()
        while row:
            count+=1
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone() 
        if(count==0):
            print("No Entries\n")

    except Exception as e:
        con.rollback()
        print("Failed to load database")
        print(">>>>>>>>>>>>>", e)
        
    try:
        cursor = con.cursor(buffered=True,dictionary=True)
        print("Rural constituencies are:\n")
        query = ("SELECT * FROM CONSTITUENCY c WHERE c.ConstituencyType = 'Rural' GROUP BY c.ConstituencyID;")
        cursor.execute(query)
        con.commit()

        # Name = [Name[0] for Name in cursor.execute(query)]
        count=0
        row = cursor.fetchone()
        while row:
            count+=1
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()    
        if(count==0):
            print("No Entries\n")
    
    except Exception as e:
        con.rollback()
        print("Failed to load database")
        print(">>>>>>>>>>>>>", e)
        
    return
    
def Voter_age():
     
    try:
        age = input("age: ")
        cursor = con.cursor(buffered=True,dictionary=True)
        print("Below are all voter with age as given in input\n")
        query = f"SELECT * FROM VOTER v WHERE v.Age = '{age}';"
        
        # print(query)
        cursor.execute(query)
        con.commit()

        # Name = [Name[0] for Name in cursor.execute(query)]
        count=0
        row = cursor.fetchone()
        while row:
            count+=1
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone() 
        if(count==0):
            print("No Entries\n")
          

    except Exception as e:
        con.rollback()
        print("Failed to load database")
        print(">>>>>>>>>>>>>", e)
        
    return

def More_than_budget():
    try:
        # Take election ID as input from the user
        election_id = input("Enter the Election ID: ")

        # Take threshold amount as input from the user
        threshold_amount = int(input("Enter the minimum campaign spending threshold: "))

        cursor = con.cursor(buffered=True, dictionary=True)
        print(f"Below are all parties that spent more than {threshold_amount} on their campaigns in {election_id}\n")
        query = f"SELECT B.PartyID, P.PartyName, SUM(B.Amount) AS TotalCampaignSpending FROM BUDGET B JOIN PARTY P ON B.PartyID = P.PartyID WHERE B.ElectionID = '{election_id}' GROUP BY B.PartyID, P.PartyName HAVING TotalCampaignSpending > {threshold_amount};"

        cursor.execute(query)
        con.commit()

        count=0
        row = cursor.fetchone()
        while row:
            count+=1
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()
        if(count==0):
            print("No Entries\n")
            
    except Exception as e:
        con.rollback()
        print("Failed to load database")
        print(">>>>>>>>>>>>>", e)
    
    return

def Reserved_constituencies():

    try:
        cursor = con.cursor(buffered=True, dictionary=True)
        print("Below are all reserved constituencies\n")
        query = "SELECT * FROM CONSTITUENCY WHERE ReservedStatus = 'Yes' GROUP BY ConstituencyID;"


        # print(query)
        cursor.execute(query)
        con.commit()

        # Name = [Name[0] for Name in cursor.execute(query)]
        count=0
        row = cursor.fetchone()
        while row:
            count+=1
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()
        if(count==0):
            print("No Entries\n")

    except Exception as e:
        con.rollback()
        print("Failed to load database")
        print(">>>>>>>>>>>>>", e)
    
    return

def Budget_constituency() :
    try:
        cursor = con.cursor(buffered=True, dictionary=True)
        election_id = input("Enter election id: ")
        query = (f"SELECT CONSTITUENCY.ConstituencyID,CONSTITUENCY.ConstituencyName,CONSTITUENCY.IncumbentCandidate,SUM(BUDGET.AMOUNT) AS TotalAmount,CANDIDATE.PartyID AS Incumbent_Party,BUDGET.PartyID AS Budget_Party FROM CONSTITUENCY INNER JOIN BUDGET ON CONSTITUENCY.ConstituencyID = BUDGET.ConstituencyID INNER JOIN CANDIDATE ON CONSTITUENCY.IncumbentCandidate = CANDIDATE.CandidateID WHERE BUDGET.ElectionID = '{election_id}' GROUP BY CONSTITUENCY.ConstituencyID, CONSTITUENCY.ConstituencyName, CONSTITUENCY.IncumbentCandidate, CANDIDATE.PartyID,BUDGET.PartyID;")
        cursor.execute(query)
        con.commit()

        # Name = [Name[0] for Name in cursor.execute(query)]
        count=0
        row = cursor.fetchone()
        while row:
            count+=1
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()
        if(count==0):
            print("No Entries\n")

    except Exception as e:
        con.rollback()
        print("Failed to load database")
        print(">>>>>>>>>>>>>", e)
    
    return

def delete_party_from_coalition():
    try:
        # Take Coalition ID as input from the user
        coalition_id = input("Enter the Coalition ID: ")

        # Take Party ID as input from the user
        party_id = input("Enter the Party ID to remove from the coalition: ")

        cursor = con.cursor(buffered=True, dictionary=True)

        # Check if the party is a member of the specified coalition
        check_query = f"SELECT * FROM COALITION_MEMBERS WHERE CoalitionID = '{coalition_id}' AND PartyID = '{party_id}';"
        cursor.execute(check_query)

        if cursor.rowcount > 0:
            # If the party is a member, proceed with the deletion
            delete_query = f"DELETE FROM COALITION_MEMBERS WHERE CoalitionID = '{coalition_id}' AND PartyID = '{party_id}';"
            cursor.execute(delete_query)
            con.commit()
            print(f"Party {party_id} has been removed from Coalition {coalition_id}.")
        else:
            print(f"Party {party_id} is not a member of Coalition {coalition_id}.")

    except Exception as e:
        con.rollback()
        print("Failed to delete party from coalition.")
        print("Error:", e)
        
    return
def update_criminal_record():
    try:
        # Take Candidate Name as input from the user
        candidate_name = input("Enter the Candidate ID: ")

        cursor = con.cursor(buffered=True, dictionary=True)

        # Check if the candidate exists
        check_query = f"SELECT * FROM CRIMINAL_RECORDS WHERE CandidateID = '{candidate_name}';"
        cursor.execute(check_query)

        if cursor.rowcount > 0:
            # If the candidate exists, take new criminal record as input
            new_criminal_record = input("Enter the new Criminal Record: ")

            # Update the criminal record
            update_query = f"UPDATE CRIMINAL_RECORDS SET CriminalRecord = '{new_criminal_record}' WHERE CandidateID = '{candidate_name}';"
            cursor.execute(update_query)
            con.commit()
            print(f"Criminal record for candidate {candidate_name} has been updated to '{new_criminal_record}'.")
        else:
            print(f"Candidate {candidate_name} does not have a criminal record.")

    except Exception as e:
        con.rollback()
        print("Failed to update criminal record.")
        print("Error:", e)
    return

def update_financial_assets_by_name():
    try:
        # Take Candidate Name as input from the user
        candidate_name = input("Enter the Candidate Name: ")

        cursor = con.cursor(buffered=True, dictionary=True)

        # Check if the candidate exists
        check_query = f"SELECT * FROM CANDIDATE WHERE Name = '{candidate_name}';"
        cursor.execute(check_query)

        if cursor.rowcount > 0:
            # If the candidate exists, take new financial assets value as input
            new_financial_assets = int(input("Enter the new Total Financial Assets: "))

            # Update the financial assets
            update_query = f"UPDATE CANDIDATE SET TotalFinancialAssets = {new_financial_assets} WHERE Name = '{candidate_name}';"
            cursor.execute(update_query)
            con.commit()
            print(f"Total Financial Assets for candidate {candidate_name} has been updated to {new_financial_assets}.")
        else:
            print(f"Candidate {candidate_name} does not exist.")

    except Exception as e:
        con.rollback()
        print("Failed to update financial assets.")
        print("Error:", e)

    return
    
def update_coalition_name():
    try:
        # Take Coalition ID as input from the user
        coalition_id = input("Enter the Coalition ID: ")

        cursor = con.cursor(buffered=True, dictionary=True)

        # Check if the coalition exists
        check_query = f"SELECT * FROM COALITION WHERE CoalitionID = '{coalition_id}';"
        cursor.execute(check_query)

        if cursor.rowcount > 0:
            # If the coalition exists, take new coalition name as input
            new_coalition_name = input("Enter the new Coalition Name: ")

            # Update the coalition name
            update_query = f"UPDATE COALITION SET CoalitionName = '{new_coalition_name}' WHERE CoalitionID = '{coalition_id}';"
            cursor.execute(update_query)
            con.commit()
            print(f"Coalition name for Coalition ID {coalition_id} has been updated to {new_coalition_name}.")
        else:
            print(f"Coalition with ID {coalition_id} does not exist.")

    except Exception as e:
        con.rollback()
        print("Failed to update coalition name.")
        print("Error:", e)
    
    return

def candidate_vote_analysis():
    try:
        # Take input for Candidate ID and Constituency ID
        candidate_id = input("Enter Candidate ID: ")
        # constituency_id = input("Enter Constituency ID: ")

        cursor = con.cursor(buffered=True, dictionary=True)

        # SQL Query
        query = f"""
            SELECT
                c.CandidateID,
                c.PartyID,
                c.Gender,
                c.Age,
                c.CasteStatus,
                c.Name,
                COUNT(IF(v.CandidateID IS NOT NULL, 1, NULL)) AS Number_of_Votes,
                COALESCE(co.ConstituencyID, 'No Vote') AS ConstituencyID,
                COALESCE(co.ConstituencyName, 'No Vote') AS ConstituencyName
            FROM
                CANDIDATE AS c
            LEFT JOIN
                VOTE AS v ON v.CandidateID = c.CandidateID
            LEFT JOIN
                VOTER AS vr ON vr.VoterID = v.VoterID
            LEFT JOIN
                CONSTITUENCY AS co ON co.ConstituencyID = vr.ConstituencyID
            WHERE
                c.CandidateID = '{candidate_id}'
            GROUP BY
                c.CandidateID, ConstituencyID, ConstituencyName
            ORDER BY
                Number_of_Votes DESC;
        """

        cursor.execute(query)
        con.commit()

        # Fetch all the rows
        rows = cursor.fetchall()

        # Print the results
        count=0
        for row in rows:
            count+=1
            print(row)

        if(count==0):
            print("No Entries\n")
            
    except Exception as e:
        con.rollback()
        print("Failed to execute the query.")
        print("Error:", e)


    return

def delete_entry_from_vote():
    try:
        # Take Vote ID as input from the user
        vote_id = input("Enter the Vote ID: ")
        
        cursor = con.cursor(buffered=True, dictionary=True)

        # Check if the party is a member of the specified coalition
        check_query = f"SELECT * FROM VOTE WHERE VoteID = '{vote_id}';"
        cursor.execute(check_query)

        if cursor.rowcount > 0:
            # If the party is a member, proceed with the deletion
            delete_query = f"DELETE FROM VOTE WHERE VoteID = '{vote_id}';"
            cursor.execute(delete_query)
            con.commit()
            print(f"Vote {vote_id} has been removed.")
        else:
            print(f"Vote {vote_id} is not a valid vote.")

    except Exception as e:
        con.rollback()
        print("Failed to delete vote from coalition.")
        print("Error:", e)
        
    return

def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if (ch == 1):
        Add_Candidate()
    elif (ch == 2):
        Add_PARTY()
    elif (ch == 3):
        Add_VOTE()
    elif (ch == 4):
        Get_Criminal_Record()
    elif (ch == 5):
        Voter_age()
    elif (ch == 6):
        Get_Candidate_minmax_age()
    elif (ch == 7):
        Total_budget()
    elif (ch == 8):
        Constituency_info()
    elif (ch == 9):
        Party_information()
    elif (ch == 10):
        More_than_budget()
    elif (ch == 11):
        Reserved_constituencies()
    elif (ch == 12):
        Budget_constituency()
    elif (ch == 13):
        delete_party_from_coalition()
    elif(ch==14):
        update_criminal_record()
    elif(ch==15):
        update_financial_assets_by_name()
    elif(ch==16):
        update_coalition_name()
    elif(ch==17):
        candidate_vote_analysis()
    elif(ch==18):
        delete_entry_from_vote()


    else:
        print("Error: Invalid Option")





while (1):
    tmp = sp.call('clear', shell=True)

    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password_1 = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = mysql.connector.connect(
            user=username,
            password=password_1,
            host='localhost',
            database='VeriBallot'
        )

        if con.is_connected():
            print("Connected to MySQL database")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while (1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Option 1 - Add a new Candidate")  # Hire an Employee
                print("2. Option 2 - Add a new Party")  # Fire an Employee
                print("3. Option 3 - Add vote")  # Promote Employee
                # Employee Statistics
                print("4. Option 4 - Select candidates with no criminal record and display candidates with their criminal records")
                print("5. Option 5 - Select voters with a given age")
                print("6. Option 6 - Minimum and maximum ages of contesting candidate")
                print("7. Option 7 - Total Budget allocated in a year")
                print("8. Option 8 - Get Constituency info based on its type")
                print("9. Option 9 - Get Party information")
                print("10. Option 10 - Retrieve the names of all parties that spent more than a certain amount on their campaigns for a specific election. ")
                print("11. Option 11 - Show the reserved constituencies")
                print("12. Option 12 - Budget constituencies analysis")
                print("13. Option 13 - Delete A Particular Party from a Coalition")
                print("14. Option 14 - Update A Criminal Record")
                print("15. Option 15 - Update Financial Assets of A Candidate")
                print("16. Option 16 - Update Name of a new Coalition")
                print("17. Option 17 - Analysis to see which candidate received how many votes in which constituency")
                print("18. Option 18 - Delete Entry from Vote")
                print("19. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 19:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")