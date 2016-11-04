import MySQLdb
import datetime
from sms_horizon import SmsHorizon

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="root",
                     db="gym_management")
# Production
# db = MySQLdb.connect(host="porovvasu.mysql.pythonanywhere-services.com",
#                      user="porovvasu",
#                      passwd="vasu1234",
#                      db="porovvasu$gym_management")

cur = db.cursor()

sms_horizon = SmsHorizon(user="porovvasu", api_key="bgeKApJ22wBgmuwNlKfr", main_url="http://smshorizon.co.in/api/sendsms.php?")


def send_sms_reminder(gyms):
    date_after_three_days = (datetime.datetime.today() + datetime.timedelta(days=3)).day

    for gym in gyms:
        # fetch fees amount , mobile number, first name of customer whose fees will be due in next days
        cur.execute("SELECT `phone`, `first_name`, DAY(`joining_date`), `fees_structure_id`, `fees_amount`, `fees_structure_type`"
                    "FROM management_gymmember a, management_feesstructure b WHERE a.fees_structure_id = b.id AND "
                    "DAY(`joining_date`) = '" + str(date_after_three_days) + "' AND a.gym_id = " + str(gym['gym_id']))

        for row in cur.fetchall():
            print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]) + " " + str(row[4]))
            mobile = row[0]
            first_name = row[1]
            fees_amount = row[4]
            fees_structure_type = row[5]
            message = "Hi {first_name},\n Your fees Rs.{fees_amount} will be due in three days for your Gym - {gym_name}, " \
                      "which is {fees_structure_type} fees.\n Happy Gyming! :)".format(first_name=str(first_name),
                                                                                       fees_amount=str(fees_amount),
                                                                                       gym_name=str(gym['gym_name']),
                                                                                       fees_structure_type=str(fees_structure_type))
            response = sms_horizon.send_sms(message=message, mobile=mobile)
            print (str(response))

    db.close()
    pass


def main():
    cur.execute("SELECT  b.`id`, `gym_name` FROM management_gymowner a, management_gym b "
                "WHERE a.id = b.gym_owner_id AND a.is_staff = '0'")

    gyms = []
    for row in cur.fetchall():
        gyms.append({"gym_id": row[0], "gym_name": row[1]})

    send_sms_reminder(gyms)

if __name__ == "__main__":
    main()

