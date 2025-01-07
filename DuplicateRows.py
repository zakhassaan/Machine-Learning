# Check how many duplicate rows exist
duplicate_count = df.duplicated().sum()
print(f"Number of duplicates: {duplicate_count}")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Verify that duplicates have been removed
duplicate_count_after = df.duplicated().sum()
print(f"Number of duplicates after removal: {duplicate_count_after}")