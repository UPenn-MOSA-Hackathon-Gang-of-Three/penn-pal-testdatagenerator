'''
Create a program to generate test datasets of mentor and mentees to use for testing the Penn-Pal's matching algorithm.

How to use:
1) Download the Faker package
2) In Line 32, update name of the output csv file.
3) In Line 52, change the value to the number of entries that you would like in your test data set.
4) Run the program.

'''
import csv
import random
from faker import Faker

fake_data = Faker()

# uncomment this if you want to generate the same dataset, else will produce different set each time this is run
# Faker.seed(0)

# to adjust available options adjust
mentorMentee = ("Mentor", "Mentee")
gender = ("Male", "Female")
certification = ("CPA", "CIA", "CISA", "PMP", "CPA, CIA", "CPA, CISA", "CIA, CISA", "CRMA", "CFE", "CFE, CIA")
yesNo = ("Yes", "No")
genderPreference = ("Male", "Female", "No preference")
skills = ("Leadership", "Certification", "Networking", "Interviewing", "Communication", "Strategic Thinking")
timezones = ("GMT+0:00", "GMT+1:00", "GMT+2:00", "GMT+3:00", "GMT+03:07",
             "GMT+03:30", "GMT+4:00", "GMT+4:30", "GMT+5:00", "GMT+5:30",
             "GMT+5:45", "GMT+6:00", "GMT+6:30", "GMT+7:00", "GMT+8:00",
             "GMT+8:45", "GMT+9:00", "GMT+9:30", "GMT+10:00", "GMT+10:30",
             "GMT+11:00", "GMT+11:30", "GMT+12:00", "GMT+12:45", "GMT+13:00",
             "GMT+14:00", "GMT-12:00", "GMT-11:00", "GMT-10:00", "GMT-9:30",
             "GMT-9:00", "GMT-8:00", "GMT-7:00", "GMT-6:00", "GMT-5:00",
             "GMT-4:30", "GMT-4:00", "GMT-3:30", "GMT-3:00", "GMT-2:00",
             "GMT-1:00")

# create a csv file with column headings
with open('test_data_set.csv', 'w', newline='') as csvfile:
    fieldnames = ["Name",
                  "Mentor or Mentee",
                  "Email Address",
                  "Phone Number",
                  "Gender",
                  "Company",
                  "Job Title",
                  "Time Zone",
                  "Location",
                  "Certification(s)",
                  "Years of Experience",
                  "Multiple Mentors or Mentees",
                  "Mentor or Mentee gender preference",
                  "Skills offered or required"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # selects random value for each of the attributes
    # to adjust number of mentors/mentees change range(X) value in output
    for _ in range(100):
        writer.writerow({'Name': fake_data.name(),
                         'Mentor or Mentee': random.choice(mentorMentee),
                         'Email Address': fake_data.email(),
                         'Phone Number': fake_data.phone_number(),
                         'Gender': random.choice(gender),
                         'Company': fake_data.company(),
                         'Job Title': fake_data.job(),
                         'Time Zone': random.choice(timezones),
                         'Location': fake_data.country(),
                         'Certification(s)': random.choice(certification),
                         'Years of Experience': random.randint(1, 50),
                         'Multiple Mentors or Mentees': random.choice(yesNo),
                         'Mentor or Mentee gender preference': random.choice(genderPreference),
                         'Skills offered or required': random.choice(skills)})

    csv_fake_data = csv.writer(csvfile)
