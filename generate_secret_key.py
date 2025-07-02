from django.core.management.utils import get_random_secret_key

print("Generated SECRET_KEY:")
print(get_random_secret_key())

# comments = [
#     "Hacked by root!",
#     "System failure at port 443",
#     "Access granted to 10.0.0.1",
#     "User admin logged in",
#     "HACKED by anonymous",
#     "admin logged out",
#     "Warning: brute-force attempt detected",
# ]
#
# hacked_lines = [c for c in comments if "hacked" in c.lower()]
# print("Hacked lines:")
# for line in hacked_lines:
#     print(line)
#
#
# lower_comments = [c.lower() for c in comments]