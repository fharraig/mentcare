# mentcare

for testing:

sample json:

{
"PatientName": "Ross",
"PatientAdmitDate": "2021-09-06",
"PatientReleaseDate": "2021-10-15",
"PatientCondition": "broken leg",
"PatientClinician": "Dr. Beal",
"PatientStatus": "okay"
}

url: http://127.0.0.1:8000/manage/api/patients/

POST, GET, UPDATE, DELETE

for specific record, pass in ID in get /update/delete route

i.e. --> http://127.0.0.1:8000/manage/api/patients/6 will return 6th record in db
