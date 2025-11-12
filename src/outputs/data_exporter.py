thonimport json

def export_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)