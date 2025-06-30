# 2. მიმაგრებულ students.csv ფაილიდან წაიკითხეთ ინფორმაცია, გაფილტრეთ Grade-ის მიხედვით შემდეგნაირად:
#    ყველა სტუდენტი, რომელსაც 50-ზე ნაკლები ქულა აქვს შეინახეთ ახალ ფაილში(failed_students.csv)
#    ყველა სტუდენტი, რომელსაც 50-ზე მეტი ქულა აქვს შეინახეთ ახალ ფაილში(passed_students.csv)
#
#    ფაილებიდან ინფორმაციის წასაკითხად და ჩასაწერად აუცილებლად გამოიყენეთ DictReader და DictWriter!

import csv

with open('students.csv') as csvfile, open('passed_students.csv', 'w', newline='') as passed_students, open('failed_students.csv', 'w', newline='') as failed_students:
    reader = csv.DictReader(csvfile)
    # თავიდან მექანიკურად გავწერე ჰედერი და მერე დავგუგლე და ვნახე რო next აბრუნებს პირველ ხაზს მოცემული ცსვ ფაილიდან, რომელიც ჰედერი გამოდის.
    header = next(reader)
    writer = csv.DictWriter(passed_students, fieldnames=header)
    writer2 = csv.DictWriter(failed_students, fieldnames=header)
    writer.writeheader()
    writer2.writeheader()
    for row in reader:

        if int(row["Grade"]) >= 50:
            writer.writerow(row)
        else:
            writer2.writerow(row)



