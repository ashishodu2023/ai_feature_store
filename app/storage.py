from google.cloud import bigtable

def store_features(table_name, feature_data):
    client = bigtable.Client()
    instance = client.instance("feature-store-instance")
    table = instance.table(table_name)

    for idx, row in feature_data.iterrows():
        row_key = f"feature-{idx}"
        row = table.row(row_key)
        row.set_cell("metadata", "name", row['Feature'])
        row.set_cell("metadata", "importance", str(row['Importance']))
        row.commit()
