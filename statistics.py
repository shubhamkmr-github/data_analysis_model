def calculate_statistics(data):
    stats = {
        'mean': data.mean(),
        'median': data.median(),
        'mode': data.mode().iloc[0],
        'std_dev': data.std(),
        'correlation': data.corr()
    }
    return stats
