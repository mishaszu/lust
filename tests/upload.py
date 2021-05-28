import base64
import requests
import uuid

from pprint import pprint


def get_base_data(file: str) -> str:
    with open(file, "rb") as file:
        data = file.read()
        print(f"original {len(data)}")
        return base64.standard_b64encode(data).decode("utf-8")


def test_png_upload1():
    data = get_base_data("./samples/news.png")
    payload = {
        "format": "png",
        "data": data,
    }

    r = requests.post("http://127.0.0.1:7070/admin/create", json=payload)
    pprint(r.json())

    assert r.status_code == 200


def test_get_img1():
    r = requests.get(f"http://127.0.0.1:7070/images?file_id={uuid.uuid4()}")
    assert r.status_code == 404


def test_get_img2():
    r = requests.get(f"http://127.0.0.1:7070/images/{uuid.uuid4()}")
    assert r.status_code == 404


if __name__ == '__main__':
    test_png_upload1()
    test_get_img1()
    test_get_img2()
