import boto3
import json
import psycopg2
from hashlib import sha256
from decimal import Decimal
import decimal

# Create an SQS client with a custom session
sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-east-1', aws_access_key_id='', aws_secret_access_key='')

# Replace 'your-queue-name' with the actual queue name
queue_url = 'http://localhost:4566/000000000000/login-queue'

# Connect to the PostgreSQL database
db_params = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    while True:
        # Receive messages from the SQS queue
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=5
        )

        if 'Messages' not in response:
            print("No more messages to process. Exiting.")
            break

        for message in response['Messages']:
            message_body = message['Body']
            json_data = json.loads(message_body)

            if 'user_id' in json_data:
                try:
                    app_version_parts = json_data.get('app_version', '0.0').split('.')
                    major_version = int(app_version_parts[0])
                    minor_version = int(app_version_parts[1]) if len(app_version_parts) > 1 else 0
                    patch_version = int(app_version_parts[2]) if len(app_version_parts) > 2 else 0
                    app_version_decimal = Decimal(f'{major_version}.{minor_version}.{patch_version}')
                except decimal.InvalidOperation:
                    app_version_decimal = Decimal('0.0')

                # Hash the device_id and ip using SHA-256
                hashed_device_id = sha256(json_data.get('device_id', '').encode()).hexdigest()
                hashed_ip = sha256(json_data.get('ip', '').encode()).hexdigest()

                insert_statement = (
                    "INSERT INTO user_logins "
                    "(user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) "
                    "VALUES (%s, %s, %s, %s, %s, %s, current_date);"
                )

                values = (
                    json_data.get('user_id', ''),
                    json_data.get('device_type', ''),
                    hashed_ip,
                    hashed_device_id,
                    json_data.get('locale', ''),
                    app_version_decimal
                )

                try:
                    cursor.execute(insert_statement, values)
                    connection.commit()
                    print("Inserted data into PostgreSQL:", values)
                except psycopg2.Error as e:
                    print("Error inserting data:", e)

            # Delete the processed message from the SQS queue
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )

except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Database connection closed.")
