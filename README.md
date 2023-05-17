## account-authentication
## first things first
Run the program, "python3 mypass.py", simple right?
We can create an account by entering 1 into the input field, in this example I will be using the username: __hank__ AND the password: __hill__ 

<img width="681" alt="Screenshot 2023-05-16 at 9 31 48 PM" src="https://github.com/katstews/account-authentication/assets/112781868/355a71ed-1d00-4bfc-b3fe-074d13265f06">

## next step 
Sweet. We just successfully added our username and password into our mythical "database". Next step is to enter (2) to find our account info in the 'database'. We will do this by comparing our normal byte string with the hashed password in our db.txt file. We will be using __bcrypt__ to handle the hash comparisons. If we are successful, it should say, __Welcome Hank__ 

<img width="531" alt="Screenshot 2023-05-16 at 9 36 23 PM" src="https://github.com/katstews/account-authentication/assets/112781868/ca561a2e-4fe9-474b-a0e3-9ecc35f2ad7b">
<br/> 
another case to make sure it works, I will enter username: __hank__ with password: __propane__ ... 
<img width="531" alt="Screenshot 2023-05-16 at 9 36 23 PM" src="https://github.com/katstews/account-authentication/assets/112781868/72bf0de7-5335-4173-8265-22c0f8a39703">
it works! 
