import requests


def voyage(*data, address="127.0.0.1", port=5000):
    response = requests.get(f"http://{address}:{port}")
    json_resp = response.json()
    out = []
    for key, value in json_resp.items():
        match = 0
        for elem in value:
            if elem in data:
                match += 1
        if match > 0:
            out.append((key, match))
    return [y[0] for y in sorted(out, key=lambda x: (-x[1], x[0]))]