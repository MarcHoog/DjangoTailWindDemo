import dramatiq

@dramatiq.actor
def process_submission(content):
    print(f"Processed submission: {content}")
