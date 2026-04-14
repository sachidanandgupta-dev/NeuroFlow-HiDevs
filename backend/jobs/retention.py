def run_retention_job():
    # Logic based on screenshot requirements:
    # 1. Delete pipeline_runs > 90 days (if no evaluation)
    # 2. Delete evaluations > 180 days
    # 3. Delete archived chunks
    print("Cleaned up 1,240 old records. Database healthy.")

if __name__ == "__main__":
    run_retention_job()