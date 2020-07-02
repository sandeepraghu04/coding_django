## Django Coding Challenge - datamindedsolutions

### Main tasks in this Restaurant app - 

- A user able to create a restaurant. (Name, foodtype, address, rating etc.)

- A user able to obtain a list of restaurants.

- A user able to view details of a restaurant based on the restaurant they select from the list.

- A user able to edit and delete a restaurant.

- A user able to submit a rating for a restaurant.

- A user able to sort the list of restaurants by Highest Rating.

### Process to run Restaurant app -

- Clone or Download the repository

- In your python virtual env, run *'pip install -r requirements'*

- After environment setup, *make migrations and migrate changes*

- Now run the server with *python manage.py runserver*

- The server is up and running on *http://localhost:8000*

### Available Routes - 

- *http://localhost:8000/submit_restaurant* **POST** 

- *http://localhost:8000/get_restaurant* **GET** 

- *http://localhost:8000/modify_restaurant* **GET, PUT, DELETE**

- *http://localhost:8000/submit_rating* **POST**