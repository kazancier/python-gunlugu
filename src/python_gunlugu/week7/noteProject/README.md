noteProject :
Kullanıcı terminalden notlarını json dosyasına kayıt eder. Notlar date, subject, note ve keywords alanları ile kayıt olur.

Notlar json dosyasına kayıt edilir. Sözlük tercih edilmesinin sebebi notun herhangi bir alanına key ile ulaşılabilmesidir. Liste kullanılsa ve ilerleyen zamanda bir alan eklense indexler değişirdi. Örneğin index[1] ile bugün subjecte erişilebiliyorken, alan eklendikten sonra başka bir alan dönebilir.

write_note dosya_yolu olarak var olan bir klasör yolu verilirse False ve Bu bir klasör hata mesajı verilir. olmayan bir dosya yolu verilirse False ve Dosya yolu bulunamadı mesajı verir. İki farklı mesaj ile sorunun ne olduğu daha iyi anlaşılır.

create_note tuple döndürür. Bool, mesaj / sözlük.
Bool'u doğrudan koşul olarak kullanabilirsin.
Çağıran Bool'a bakmazsa jsona mesajı kaydedebilir.

Create_note subject olarak character girilmemişse (boşluk, satır başı vb) False ve Hata mesajı döner.,

read_note bir json dosyasını başarı ile okuyabilirse true ve jsondaki listeyi döndürür.
Hata alırsa: eğer dosya yolu bulnamadıysa boş false ve boş liste döndürür. eğer json dosyası bozuksa alternatif bir dosya adı ile kayıt eder.

note.json kullanıcının notları github 'a gitmesin diye gitignoreda var.  repo public olunca giren herkes kullanıcın notlarını görür

ilk sürümde olanlar :
Terminalden not kaydı.
Boş konu kontrolü.
json yoksa oluşturma.
jsonın dosya bulunamazsa kontrolü, klasörmü kontrolü

İlk sürümde olmayanlar :
Notların görüntülenmesi.
