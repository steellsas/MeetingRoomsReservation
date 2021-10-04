# MeetingRoomsReservation
Project it is service for its employees which helps them to reserve company
meeting rooms. Each employee should be able to check each
room’s availability, book or cancel a reservation through an API


###Project apps:

    employees
       crate Employee. EndPoint ../employee/register/
         Employee have first name, last name and account. Employes have relationshiip with User.
         Creating Employee must create account (Username,password. email)

    rooms
        crate Meeting Room. EndPoint ../room/add/
        get all Meeting Room. EndPoint ../room/all/
    reservations
        Create reservation. EndPoint .. /reservations/create/
        Get meeting room reservations. 
                EndPoint .. reservations/room/<int:room_id>
        Get meeting room reservationsto filter by employee
                EndPoint .. reservations/room/employee/<int:employee_id>
        Cancel reservation
             Removing meeting room reservations from Database.Need to give reservation id
             EmdPoint  .. reservations/cancel/<int:roombooking_id>
    Authentication
         For users authentication using :
              BasicAuthentication, SessionAuthentication
              
        login : using API rest_auth'
              Endpoint .. /rest-auth/login/
        logout :using API rest_auth'
               Endpoint ../rest-auth/logout/

##Dependencies


Describe any prerequisites, libraries, OS version, etc., needed before installing program.
ex. Windows 10
Installing
How/where to download your program
Any modifications needed to be made to files/folders
Executing program
How to run the program
Step-by-step bullets
code blocks for commands
