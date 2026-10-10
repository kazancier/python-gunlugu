import json

from ekranResmiProjesi import json_yaz


def test_json_success(tmp_path):
    hareketler ="["
    """
    with open(tmp_path/"gunluk.json", "w", encoding="utf-8" ) as file:
            json.dump(hareketler, file, ensure_ascii=False, indent=4)

    """
    dosya = tmp_path / "gunluk.json"
    dosya.write_text("[]")
    
    assert json_yaz("E","EkranResmi001.png","Notlar.png",dosya) == True
    print(tmp_path)
