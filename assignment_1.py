emails = ['kwame@gmail.com', 'abena@gmail.com', 'omari@gmail.com']
print(emails)

emails.sort()

emails.append('Kofi@Gmail.com')

del emails[2]

print(len(emails))

final_emails = []
for i in range(len(emails)):
    final_emails.append(emails[i].lower())

print(final_emails)