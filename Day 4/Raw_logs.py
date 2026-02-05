# Raw login logs with duplicate user IDs
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

# Convert list to set to keep only unique users
unique_users = set(raw_logs)

# Membership test
print("Is ID05 a unique user?", "ID05" in unique_users)

# Compare counts
print("Total log entries:", len(raw_logs))
print("Unique users:", len(unique_users))
