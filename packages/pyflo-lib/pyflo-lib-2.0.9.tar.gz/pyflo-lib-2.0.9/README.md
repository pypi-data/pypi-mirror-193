## Python bitcoin library modified for FLO

### Installation
To install pyflo, 

    $ git clone https://github.com/ranchimall/pyflo
    $ cd pyflo
    $ sudo python3 setup.py install
    
### Dependencies

* Python 3.3.3+
* secp256k1


#### Message signing and verification 

Every message sent to the Blockchain is in hash format, and not in plain string. So we convert the message we are signing into a SHA256 hash before. 

```
>>> import pyflo

# ADDRESS GENERATION 
>>> a = pyflo.Address(address_type="P2PKH")
>>> a.address
'FTP7LL7QjhgKfqYX1pis18bCqEpZaGSRzZ'
>>> a.private_key.wif
'R8Gw2Mr3n2fY1ydB2X5gEehxHkdhboeUD6yw4wRtVKHaqAd9gdkK'
>>> a.private_key.hex
'16b6aca5ff6a3bf3a1332dd4edf87880b2883cb4fe16effd073e2e866aa141aa'
>>> a.public_key.hex
'033c30b269e2d5df229f3f0ce294b19c4f0a3a8d12280415ce41e7bd3784a619c4'

# CONVERT MESSAGE INTO SHA-256 HASH 
>>> pyflo.sha256(b'vivek'.hex())
b'\xa3\xdas\x97e\x01\x81,\xd7\xb8!\xa2\x0b\xfb\t\xaf\nj\x89\x1eA\x9c\xdf\xb7a\xfb\x19\xa9,\x91BB'
>>> pyflo.sha256(b'vivek'.hex()).hex()
'a3da73976501812cd7b821a20bfb09af0a6a891e419cdfb761fb19a92c914242'
>>> msg = b'vivek'.hex()
>>> msg_hash_hex = pyflo.sha256(msg).hex()
>>> msg_hash_bytes = pyflo.sha256(msg)
>>> msg
'766976656b'
>>> msg_hash_hex
'a3da73976501812cd7b821a20bfb09af0a6a891e419cdfb761fb19a92c914242'
>>> msg_hash_bytes
b'\xa3\xdas\x97e\x01\x81,\xd7\xb8!\xa2\x0b\xfb\t\xaf\nj\x89\x1eA\x9c\xdf\xb7a\xfb\x19\xa9,\x91BB'

# SIGN AND VERIFY THE MESSAGE 
>>> sig_msg_hex = pyflo.sign_message(msg_hash_hex, a.private_key.wif)
>>> pyflo.verify_signature(sig_msg_hex, a.public_key.hex, msg_hash_hex)
True

# SIGN AND VERIFY MESSAGE IN STANDARD OPERATION
>> pyflo.sign_message_standard_ops('vivek', a.private_key.wif)
'3045022039747449a6fbac008d04d763a3a62f2261d1c5a35ee6a21a8354d8757d27593802210085a4d4b9886de6d06c3563c97160c8d70f492ce56f9e00dbcd7276004369402e'
>> sig_msg_hex = pyflo.sign_message_standard_ops('vivek', a.private_key.wif)

# To verify the above signature, run the following in the console of any Standard Ops app 
>> sign_msg_hex = '3045022039747449a6fbac008d04d763a3a62f2261d1c5a35ee6a21a8354d8757d27593802210085a4d4b9886de6d06c3563c97160c8d70f492ce56f9e00dbcd7276004369402e'
>> a.public_key.hex = '033c30b269e2d5df229f3f0ce294b19c4f0a3a8d12280415ce41e7bd3784a619c4'
>> floCrypto.verifySign('vivek', sig_msg_hex, a.public_key.hex) 
true

```

The **sign_message_standard_ops** function verifies with [RanchiMall standard operations](https://github.com/ranchimall/Standard_Operations).
Things to note:
The function now takes 2 parameters -

1. Message in string ( not hex-encoded string)
2. Private key in wif (not bytes etc.)
The hex parameter has been removed as we are always returning hex in standard ops

New libraries used - hashlib
The elliptical curve folder, holds the code taken from starkbank ecdsa (MIT License)
no other additional dependencies

The signature generated with **sign_message_standard_ops** cannot be verified using purely Pyflo. Users can use the following API to verify signatures 

** Python **
``` 
import requests

url = 'https://flo-sign-validator.duckdns.org'
myobj = {'floID': floID,
            'pubKey': pubKey,
            'message': message,
            'sign': sign}

x = requests.post(url, json = myobj)
print(x.text)

```

** JavaScript **
``` 
fetch("https://flo-sign-validator.duckdns.org", {
  method: "POST",
  body: JSON.stringify({
    floID: floID,
    pubKey: pubKey,
    message: message,
    sign: sign
  }),
  headers: {
    "Content-type": "application/json; charset=UTF-8",
  },
})
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    console.log(data);
  })
  .catch((error) => console.error("Error:", error));

```

** PHP **
```
            function callAPI($method, $url, $data){
            $curl = curl_init();
            switch ($method){
                case "POST":
                    curl_setopt($curl, CURLOPT_POST, 1);
                    if ($data)
                        curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
                    break;
                case "PUT":
                    curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "PUT");
                    if ($data)
                        curl_setopt($curl, CURLOPT_POSTFIELDS, $data);                              
                    break;
                default:
                    if ($data)
                        $url = sprintf("%s?%s", $url, http_build_query($data));
            }
            // OPTIONS:
            curl_setopt($curl, CURLOPT_URL, $url);
            curl_setopt($curl, CURLOPT_HTTPHEADER, array(
                'APIKEY: 111111111111111111111',
                'Content-Type: application/json',
            ));
            curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
            // EXECUTE:
            $result = curl_exec($curl);
            curl_close($curl);
            return $result;
            }
            
            $floID = $_POST['floID'];
            $pubKey = $_POST['floPubKey'];
            $message = $_POST['message'];
            $signDataWithFlo = $_POST['signDataWithFlo'];
    
    
            $data_array =  array( "floID"        => $floID, "pubKey" => $pubKey, "message" => $message, "sign" => $signDataWithFlo  );
            $make_call = callAPI('POST', 'https://flo-sign-validator.duckdns.org', json_encode($data_array));
            $response = json_decode($make_call, true);
            
            print_r($response);

```
            
