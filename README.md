# ACM_code
Password manager application

Click on the submitted link, it opens repository named ACM_code, then click on branches, and click on branch named "master"
Navigate that repository in PC using command prompt, then clone the repository,
Using cd ACM_code access that file
(make sure you have installed cryptography in your system, else type pip.install cryptograhy using cmd prompt)
Then type : python project.py
or first download it, open it in script mode of python IDLE. Save it and say Fn+F5 to run it.
1.Run the Script:
  
  When you execute the script, you will be prompted to enter your master username and password. The master username and password are stored in masterpswd.csv file.
  If the master username and password don't match then it prompts ACCESS DENIED

2. If login successful then it gives a menu 
  2.1. Add password
  2.2. View saved passwords
  2.3  Delete password
  2.4  Update Password

3. If you select option 1, you will be asked to provide:
  Account Name (eg Insta, Facebook)
  Username (associated with the account)
  Password - This password must meet the following criteria:
            Exactly 8 characters long.
            First 4 characters must be letters (A-Z or a-z)
            The 5th character must be @.
            The last 3 characters must be digits (0-9)
   Once entered, the password is encrypted and stored in passwords.csv file
4.If you select option 2, the program will retrieve all saved passwords from passwords.csv and display:
  Account Name
  Username
  Decrypted Password

5. If you select option 3, you'll be prompted to enter:
  Account Name
  Username
  If the account and username match an entry, the corresponding password will be deleted
  you will get a message saying "you'll be prompted"

4. If you select option 4, you’ll be prompted to enter:
  Account Name
  Username
  If the account and username exist, you'll be prompted to enter a new password (which must meet the same criteria as the original password).
  A message will be flashed : "Password updated successfully"

5. If any other choice then it says INVALID CHOICE
6. Finally the code ends
