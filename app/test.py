# def addition():
#     return 1 + 3

# a: int = addition()

# def print_addition(param1):
#     print(param1)
#     return param1

# # print_addition(a)

# d = {"na": "me", "surname": "none of your business", "sex": "yes please"}
# print(**d)

## ---------------- TEST CONNECTION TO ASTRA DB ------------------##
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config = {
    'secure_connect_bundle':
    'C:/Users/yo_laptop/Documents/dev/api_development/fastapi-scheduling/app/ignored/connect.zip'
}
auth_provider = PlainTextAuthProvider(
    'SflhQzbvOByNeMrCLPemobWa',
    'zMQDOQf0Lhriryk_CSHBv98HUPXcAtIYafbFUZ9DQUJNpDIvI9POIBLWtcgaQwTvZ6EU-SNUmk53,-Q,5ls3S-6.T0fdzozubUDz96inwwZ2+jffR3TZfsJSAUqMMZI,'
)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
    print(row[0])
else:
    print("An error occurred.")

## ---------------- TEST CONNECTION TO ASTRA DB ------------------##
