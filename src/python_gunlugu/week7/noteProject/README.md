noteProject :
Kullanıcı terminalden notlarını json dosyasına kayıt eder. Notlar date, subject, note ve keywords alanları ile kayıt olur.

Notlar json dosyasına kayıt edilir. Sözlük tercih edilmesinin sebebi notun herhangi bir alanına key ile ulaşılabilmesidir. Liste kullanılsa ve ilerleyen zamanda bir alan eklense indexler değişirdi. Örneğin index[1] ile bugün subjecte erişilebiliyorken, alan eklendikten sonra başka bir alan dönebilir.

create_note tuple döndürür. Bool, mesaj / sözlük.
Bool'u doğrudan koşul olarak kullanabilirsin.
Çağıran Bool'a bakmazsa jsona mesajı kaydedebilir.

Create_note subject olarak character girilmemişse (boşluk, satır başı vb) False döner

İlk sürümde olmayanlar :
Notların görüntülenmesi.
