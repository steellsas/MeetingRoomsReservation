# MeetingRoomsReservation
Project it is service for its employees which helps them to reserve company
meeting rooms. Each employee should be able to check each
room’s availability, book or cancel a reservation through an API

 Database schema:

 <img height="200" src="https://github.com/steellsas/MeetingRoomsReservation/blob/main/Document/MeetingRoom%20reservations.png" width="200"/>  


Project made with Django Rest Framework. 
 * Project features: 

 *     1. Create room reservation. Reservations title, room booked dates: from_date and to_date
         select Meeting room (room id) and select employees. Link  ../reservations/create/
 * 
        2. Cancel meeting room reservation. Removing meeting room reservations from Database.
        Need to give reservation id. Link ../reservations/cancel/<int:roombooking_id>
 *      3.Get meeting room reservations to filter by employee.Link /reservations/cancel/<int:roombooking_id>
 *      4. Get all meeting rooms reservations. Link ../reservations/room/all
 *      5  Get room reservations by room id. Link ../reservations/room/<int:room_id>
 *      6 Employee have first name, last name and account. Employes have relationshiip with User.
         Creating Employee must create account (Username,password. email)
 *       link: Link ..employee/register/
 *      7.  crate Meeting Room. review all meeting rooms 
 *          Link ../room/add/  or room/all/
 *      8 Autentications class using  : BasicAuthentication, SessionAuthentication
 *            login : using API rest_auth' ../rest-auth/login/
              logout :using API rest_auth' ../rest-auth/logout/
        
##Dependencies
● Docker 
● Python 3
● Django
● Django Rest Framework
● django-rest-auth
● PostgreSQL

##Installation
This project work in Docker container. 
  1. Install docker. Python 3, PostgreSQL to you computer.
  2. Create project directory, create Git repository. 
  3. Clone from GitHub  project : https://github.com/steellsas/MeetingRoomsReservation.git
  4. Migrate project : docker-compose run web Python manage.py migrate
  5. Build docker container: docker-compose build
  6. Start project : docker-compose up
  7. Create superuser for first connection.
  8. You can use this project


