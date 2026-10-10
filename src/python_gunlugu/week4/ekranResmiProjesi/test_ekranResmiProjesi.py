import json

from ekranResmiProjesi import json_yaz


def test_json_defect(tmp_path):
  
    dosya = tmp_path / "gunluk.json"
    dosya.write_text("[")
    
    assert json_yaz("E","EkranResmi001.png","Notlar.png",dosya) == False
    

def test_json_success(tmp_path):
  
    
    dosya = tmp_path / "gunluk.json"
    dosya.write_text("[]")
    
    assert json_yaz("E","EkranResmi001.png","Notlar.png",dosya) == True
    

def test_json_exists(tmp_path):
    
    dosya = tmp_path /" "
    assert json_yaz("E","EkranResmi001.png","Notlar.png",dosya) == True
    
