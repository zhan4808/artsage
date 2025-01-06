from google.cloud import bigquery

def query_met_dataset(limit=1000):
    """
    Query the Met dataset for a subset of images with metadata.
    """
    client = bigquery.Client()
    query = f"""
    SELECT objectID, primaryImage, title, artistDisplayName, objectName, objectURL
    FROM `bigquery-public-data.met_dataset.met_objects`
    WHERE primaryImage IS NOT NULL
    LIMIT {limit}
    """
    query_job = client.query(query)
    return query_job.to_dataframe()