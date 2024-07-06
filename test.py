import subprocess as sp
import pymysql
import pymysql.cursors
import mysql.connector


def option2():
    """
     Function to implement option 2
     """


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


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
        row = cursor.fetchone()
        while row:
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()

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
        row = cursor.fetchone()
        while row:
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()
 
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
        while row:
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()
 
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    
    try:
        query_min_age = "SELECT c.Name,c.Age AS MinimumAge FROM CANDIDATE c WHERE c.AGE = (SELECT MIN(Age) AS MinimumAge FROM CANDIDATE);"
        cursor.execute(query_min_age)
        con.commit()
        # Name = [Name[0] for Name in cursor.execute(query)]
        row = cursor.fetchone()
        while row:
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()
        
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
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
        row = cursor.fetchone()
        while row:
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone() 
          

    except Exception as e:
        con.rollback()
        print("Failed to load database")
        print(">>>>>>>>>>>>>", e)
        
    return

def Reserved_constituencies():

    try:
        cursor = con.cursor(buffered=True, dictionary=True)
        print("Below are all candidates with no criminal records(clean)\n")
        query = "SELECT * FROM CONSTITUENCY WHERE ReservedStatus = 'Yes';"


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

        row = cursor.fetchone()
        while row:
            print(row)  # Process the fetched row as needed
            row = cursor.fetchone()

    except Exception as e:
        con.rollback()
        print("Failed to load database")
        print(">>>>>>>>>>>>>", e)
    
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
    # Selection
    
    elif (ch == 8):
        Reserved_constituencies()
    elif (ch == 9):
        More_than_budget()
        
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



                
                # Selection
                print("8. Option 8 - Show the reserved constituencies")
                
                # Update
                
                # Delete

                #analysis 
                print("9. Option 9 - Retrieve the names of all parties that spent more than a certain amount on their campaigns for a specific election. ")


                
                print("10. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 8:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")