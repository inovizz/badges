import csv

from badges.models import Attendee


def bulk_insert_attendees(csv_path: str):
    with open(csv_path) as f:
        rows = csv.DictReader(f, delimiter=",")

        for row in rows:
            Attendee.create(
                booking_id=row["booking_id"],
                email=row["email"],
                fullname=row["fullname"],
            )


def bulk_export_attendee_tokens(csv_path: str):
    with open(csv_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["booking_id", "email", "token"])

        writer.writeheader()
        for attendee in Attendee.query.all():
            writer.writerow(
                {
                    "booking_id": attendee.booking_id,
                    "email": attendee.email,
                    "token": attendee.token,
                }
            )