# Teacher Panel Service
This is one of the services of the Software-Engineering-1402-02 multiservices project.
## What functionalities does this service provide?
- Allowing users to register as teachers.
- Allowing teachers to create English Learning courses for students.
- The courses include a title, objectives and a poster to represent the content of course.
- The courses include video files which are teacher's uploaded videos.
- The courses include exams that contain 4 option questions provided by teacher. 
- The questions of exams include a category to represent the type of question.
## Implementation parts of this service
1.First part which is a ASP.NET API responsible for database interactions and data transfer.
2.Seconde part which is the projct's Django core server responsible for creating and rendering views
based on the data that was retrieved from ASP.NET API.
## How do the different parts interact with each other?
Django core server uses HTTP requests to retrieve data from the API.
### Further explanation
Some of the UI files(html css js) are from a free template that are changed to meet our requirements.