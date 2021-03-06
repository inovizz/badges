import csv
import random

from badges.models import User


from flask import url_for


def get_prefixer(url_prefix):
    def _url_for(*args, **kwargs):
        return url_prefix + url_for(*args, **kwargs)

    return _url_for

# TO BE REFACTORED
def bulk_update_speakers(csv_path: str):
    _404_speakers = []
    with open(csv_path) as f:
        rows = csv.DictReader(f, delimiter=",")

        for row in rows:
            a = User.find_by_booking_id(row["booking_id"])
            if not a:
                _404_speakers.append(row)
                continue

            a.set_type("speaker")

    if _404_speakers:
        print("The following speakers had no bookings")
        for s in _404_speakers:
            print(s)

# TO BE REFACTORED
def bulk_insert_attendees(csv_path: str):
    with open(csv_path, encoding='utf-8-sig') as f:
        rows = csv.DictReader(f, delimiter=",")
        for row in rows:
            a = User.find_by_email_id(row["email_id"])
            if a:
                print("User already existing")
                continue
            else:
                User.create(
                    email_id=row["email_id"],
                    fullname=row["fullname"],
                    twitter_id='dummy',
                    type=row.get("ticket_type", "Attendee"),
                )
                print(f"User with email {row['email_id']} created")

# TO BE REFACTORED
def bulk_export_attendee_tokens(csv_path: str):
    with open(csv_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["booking_id", "email", "token"])

        writer.writeheader()
        for attendee in User.query.all():
            writer.writerow(
                {
                    "booking_id": attendee.booking_id,
                    "email": attendee.email,
                    "token": attendee.token,
                }
            )

# TO BE REFACTORED
def bulk_insert_volunteer_spec(import_path: str, export_path: str):
    no_bookings = []
    booking_ids = []
    with open(import_path) as f:
        rows = csv.DictReader(f, delimiter=",")

        for row in rows:
            a = User.find_by_email(row["email"])
            if not a:
                no_bookings.append(row)
                continue

            User.create(
                booking_id=row["booking_id"],
                receipt_id=random.randint(1000, 9999),
                email=row["email"],
                fullname=row["fullname"],
            )

            booking_ids.append(row["booking_id"])

    with open(export_path, "w") as f:
        writer = csv.DictWriter(f, fieldnames=["booking_id", "email", "receipt_id"])

        writer.writeheader()
        for attendee in User.query.filter(User.booking_id.in_(booking_ids)):
            writer.writerow(
                {
                    "booking_id": attendee.booking_id,
                    "email": attendee.email,
                    "receipt_id": attendee.receipt_id,
                }
            )

    if no_bookings:
        print("The following volunteers have no bookings")
        for v in no_bookings:
            print(v)
