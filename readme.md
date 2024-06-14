# Django YouTube Downloader

- Welcome to the Django YouTube Downloader!
- This is a web application built with Django that allows users to download videos from YouTube by simply providing a URL.

## Features

- **Simple UI**: A clean and straightforward interface for users to download YouTube videos.
- **Download Options**: Choose between different video resolutions to download.

## Usage

**Download a Video**:

- Paste the YouTube video URL in the input field.<br/><br/>
  ![1](https://private-user-images.githubusercontent.com/82939327/339661796-db7df3ed-63e6-42db-ba68-4ff0a140af07.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTgzNDczMzgsIm5iZiI6MTcxODM0NzAzOCwicGF0aCI6Ii84MjkzOTMyNy8zMzk2NjE3OTYtZGI3ZGYzZWQtNjNlNi00MmRiLWJhNjgtNGZmMGExNDBhZjA3LlBORz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjE0VDA2MzcxOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTAzNTY5NzAzMjcxZmU3MjQ4MjhmNTM3ZDBmMGVkMTdmZmI4MWZiNDk5MTUwYTIyMzYzNmNjNmY0OTFiMzY4MWMmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.f_GLdWZhcTsJuAtjpBVdQ6diyP0cCGQfuT_LFCYqzHo)
- Select the desired resolution and format.<br/><br/>
  ![2](https://private-user-images.githubusercontent.com/82939327/339661814-d019294e-e8e8-4a51-a5a6-dfe55a5609ea.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTgzNDczMzgsIm5iZiI6MTcxODM0NzAzOCwicGF0aCI6Ii84MjkzOTMyNy8zMzk2NjE4MTQtZDAxOTI5NGUtZThlOC00YTUxLWE1YTYtZGZlNTVhNTYwOWVhLlBORz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjE0VDA2MzcxOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTc0MTkwMDNlMTc3NDdkYjRlMjhlOTQ2NDBjOGM1NzQ5YmIzMGM4Nzc5Y2Y3ZDJlZDVjMWQyYzMxZThiM2RlYWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.igP1o4p2j5NlH_dijQwKTg3Vk41AmSpoH6s9PSa2yWA)
- Click on the "Download" button to start the download.<br/><br/>
  ![3](https://private-user-images.githubusercontent.com/82939327/339661827-d6957b11-0114-4dd3-bf80-2b6e2fcd906a.PNG?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTgzNDczMzgsIm5iZiI6MTcxODM0NzAzOCwicGF0aCI6Ii84MjkzOTMyNy8zMzk2NjE4MjctZDY5NTdiMTEtMDExNC00ZGQzLWJmODAtMmI2ZTJmY2Q5MDZhLlBORz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MTQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjE0VDA2MzcxOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTg4ODhlZGI4OWE2MzQyMzUwNWUxNDRkZjk2ZTNlNGMyMDI5OTNhN2RiODk4YjdkZjUzYWQ3NzI3M2YzMjYwZjUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.Nn3OnF2LDbfVvkoVEmiMZfT99LR7HnHXC6tzhXVhyYE)

Thank you for using Django YouTube Downloader! Happy downloading!