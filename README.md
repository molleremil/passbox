**PassBox**

<img width="599" alt="passbox_demo1" src="https://github.com/molleremil/passbox/assets/139823248/4c8e04fe-da40-43ab-a616-9d76870cd103">

------------------------------------------------------------------------------------------------------------------------------------------

**Note:** There are 2 version: `main.py` -> full version with all functionalities and `app.py` -> version without password leak check functionality.

------------------------------------------------------------------------------------------------------------------------------------------

In `main.py`, change the constant variable to your main/preferred email address, so you don't have to continuesly retype it. Or leave it as a blank string if you'd like to skip this feature.

<img width="303" alt="Screenshot 2024-02-05 at 21 42 35" src="https://github.com/molleremil/passbox/assets/139823248/472dad86-9402-4215-ab10-a3e273dbc5b0">

**Functionalities:**

  1. Generate strong and secure passwords (in connection to desired website) and save locally to a json file.
  2. Search through your database, to retrieve passwords for your desired sites effortlessly:
     <img width="598" alt="passbox_demo2" src="https://github.com/molleremil/passbox/assets/139823248/0fe932a6-332b-4c27-b545-4442709dc0e5">
     <img width="594" alt="passbox_demo3" src="https://github.com/molleremil/passbox/assets/139823248/add0b072-b6d9-4cfd-be35-6097eb73296b">
  3. Using the pwnedpasswords API, you can check if your password has been compromised. This method offers a very high level of security, as your password is encrypted with sha1 hash and the API utilizes K-anonymity, meaning only the first 5 characters of your hashed password are transmitted. Demo pictures:
     
     <img width="594" alt="passbox_demo4" src="https://github.com/molleremil/passbox/assets/139823248/4d0d102d-136f-4871-874f-4f311fba69d7">
     
     <img width="594" alt="passbox_demo5" src="https://github.com/molleremil/passbox/assets/139823248/1da9bf96-0926-4abf-b50a-ef906ad8a2d5">


     

