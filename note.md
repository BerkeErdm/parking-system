python manage.py migrate
python manage.py startapp account

kullanıcı kaydetmek için
 - http://127.0.0.1:8000/api/account/signup   -> POST
   {
        first_name :'Berk', 
        last_name  :'Erdem', 
        email      :'berk@gmail.com' 
   }

- http://127.0.0.1:8000/api/getPark   -> GET

json 
    * dosya olarak json a.json 
    * server-client data taşıma 

#paylaşlım hosting 
#digitalocenal (cloud)
#http://abc.com/api/carparks/testabc      istediğin yerden istediğin yere bağlantısı 
#http://127.0.0.1/api/carparks/testabc     a -- a      aynı ağ
#http://192.168.1.29/api/carparks/testabc  a -- b    aynı ağ

# frond --> backend otopark  
# json 
# http://192.168.1.29/api/carparks/add  method --> POST
{ 
   "carpark_name" : "Test",
   "image" : "jkkkkk",
   "address" : "test mah. 23.sok izmir"
}
# http://192.168.1.29/api/carparks/delete/1  method -->GET

#sign up 
#http://192.168.1.29/api/account/signup
{
  "username" : "tekinpolat",
  "first_name" : "Tekin",
  "last_name" : "POLAT",
   ......
}

#CRUD
#ORM 
#SELECT * FROM abc 

INSERT INTO (parkName, districtName) VALUES('abc', 'test1')
INSERT INTO (parkName, districtName) VALUES('abc', 'test1'), ('def', 'test2')