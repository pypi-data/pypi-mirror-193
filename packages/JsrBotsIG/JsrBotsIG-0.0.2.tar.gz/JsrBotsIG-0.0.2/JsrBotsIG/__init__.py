import uuid
import string
import requests
import random
import time
import base64
from Cryptodome.Cipher import AES, PKCS1_v1_5
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes


def password_encrypt(password):
    resp = requests.get('https://i.instagram.com/api/v1/qe/sync/')
    publickeyid = int(resp.headers.get('ig-set-password-encryption-key-id'))
    publickey = resp.headers.get('ig-set-password-encryption-pub-key')
    session_key = get_random_bytes(32)
    iv = get_random_bytes(12)
    timestamp = str(int(time.time()))
    decoded_publickey = base64.b64decode(publickey.encode())
    recipient_key = RSA.import_key(decoded_publickey)
    cipher_rsa = PKCS1_v1_5.new(recipient_key)
    rsa_encrypted = cipher_rsa.encrypt(session_key)
    cipher_aes = AES.new(session_key, AES.MODE_GCM, iv)
    cipher_aes.update(timestamp.encode())
    aes_encrypted, tag = cipher_aes.encrypt_and_digest(password.encode("utf8"))
    size_buffer = len(rsa_encrypted).to_bytes(2, byteorder='little')
    payload = base64.b64encode(b''.join([
        b"\x01",
        publickeyid.to_bytes(1, byteorder='big'),
        iv,
        size_buffer,
        rsa_encrypted,
        tag,
        aes_encrypted
    ]))
    return payload.decode()

def generate_jazoest(symbols):
    amount = sum(ord(s) for s in symbols)
    return f'2{amount}'

class Instagram:
    def __init__(self,User,Password):
        self.user = User
        self.passw=Password
    def Login(self):
        g1=requests.get('https://i.instagram.com/api/v1/accounts/login/').cookies
        mid=g1['mid']
        PigeonSession=f'UFS-{str(uuid.uuid4())}-0'
        IgDeviceId=uuid.uuid4()
        IgFamilyDeviceId=uuid.uuid4()
        a1=''.join(random.choices(string.ascii_lowercase+string.digits,k=16))
        AndroidID=f'android-{a1}'
        a2=''.join(random.choices(string.digits,k=6))
        useragent=f'Instagram 270.2.0.24.82 Android (30/11; 320dpi; 720x1513; Xiaomi/POCO; {a2}MI; angelicain; mt6765; en_IN; 447588991)'
        self.Blockversion='8948ffb7f08f55034a99187fec38b9d26b830b435c286c2fc879b5cac9b25569'
        headers = {
            'Host': 'i.instagram.com',
            'X-Ig-App-Locale': 'en_IN',
            'X-Ig-Device-Locale': 'en_IN',
            'X-Ig-Mapped-Locale': 'en_US',
            'X-Pigeon-Session-Id': str(PigeonSession),
            'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),
            'X-Ig-Bandwidth-Speed-Kbps': f'{random.randint(1000, 9999)}.000',
            'X-Ig-Bandwidth-Totalbytes-B': f'{random.randint(10000000, 99999999)}',
            'X-Ig-Bandwidth-Totaltime-Ms': f'{random.randint(10000, 99999)}',
            'X-Bloks-Version-Id': self.Blockversion,
            'X-Ig-Www-Claim': '0',
            'X-Bloks-Is-Layout-Rtl': 'false',
            'X-Ig-Device-Id':str(IgDeviceId),
            'X-Ig-Family-Device-Id': str(IgFamilyDeviceId),
            'X-Ig-Android-Id': str(AndroidID),
            'X-Ig-Timezone-Offset': '19800',
            'X-Ig-Nav-Chain': f'LoginLandingFragment:login_landing:1:warm_start:{round(time.time(), 3)}::',
            'X-Fb-Connection-Type': 'WIFI',
            'X-Ig-Connection-Type': 'WIFI',
            'X-Ig-Capabilities': '3brTv10=',
            'X-Ig-App-Id': '567067343352427',
            'Priority': 'u=3',
            'User-Agent': str(useragent),
            'Accept-Language': 'en-IN, en-US',
            'X-Mid': str(mid),
            'Ig-Intended-User-Id': '0',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Fb-Http-Engine': 'Liger',
            'X-Fb-Client-Ip': 'True',
            'X-Fb-Server-Cluster': 'True',
        }
        data = {
            'signed_body': 'SIGNATURE.{"jazoest":"'+str(generate_jazoest(str(IgFamilyDeviceId)))+'","country_codes":"[{\\"country_code\\":\\"91\\",\\"source\\":[\\"default\\"]}]","phone_id":"'+str(IgFamilyDeviceId)+'","enc_password":"#PWD_INSTAGRAM:0:'+str(round(time.time()))+':'+str(self.passw)+'","username":"'+str(self.user)+'","adid":"'+str(uuid.uuid4())+'","guid":"'+str(IgDeviceId)+'","device_id":"'+str(AndroidID)+'","google_tokens":"[]","login_attempt_count":"0"}',
        }
        response = requests.post('https://i.instagram.com/api/v1/accounts/login/', headers=headers, data=data)
        self.response = response
        self.mid = mid
        self.PigeonSession = PigeonSession
        self.IgDeviceId = IgDeviceId
        self.IgFamilyDeviceId = IgFamilyDeviceId
        self.AndroidID = AndroidID
        self.UserAgent = useragent

        if 'ig-set-authorization' in response.headers:
            self.sessionid=response.headers['ig-set-authorization'].split(':')[2]

            self.userid = response.headers['ig-set-ig-u-ds-user-id']
            if response.headers['ig-set-ig-u-rur'] == '':
                headers = {
                    'x-ig-app-locale': 'en_IN',
                    'x-ig-device-locale': 'en_IN',
                    'x-ig-mapped-locale': 'en_US',
                    'x-pigeon-rawclienttime': str(round(time.time(), 3)),
                    'x-ig-bandwidth-speed-kbps':  f'{random.randint(10000000, 99999999)}',
                    'x-ig-bandwidth-totalbytes-b': f'{random.randint(10000000, 99999999)}',
                    'x-ig-bandwidth-totaltime-ms': f'{random.randint(10000, 99999)}',
                    'x-bloks-version-id': self.Blockversion,
                    'x-ig-www-claim': '0',
                    'x-bloks-is-layout-rtl': 'false',
                    'x-ig-device-id': str(IgDeviceId),
                    'x-ig-family-device-id': str(IgFamilyDeviceId),
                    'x-ig-android-id': str(AndroidID),
                    'x-ig-timezone-offset': '19800',
                    'x-fb-connection-type': 'WIFI',
                    'x-ig-connection-type': 'WIFI',
                    'x-ig-capabilities': '3brTv10=',
                    'x-ig-app-id': '567067343352427',
                    'priority': 'u=3',
                    'user-agent': self.UserAgent,
                    'accept-language': 'en-IN, en-US',
                    'authorization': f'Bearer IGT:2:{self.sessionid}',
                    'x-mid': self.mid,
                    'ig-u-ds-user-id': self.userid,
                    'ig-intended-user-id': self.userid,
                    'x-fb-http-engine': 'Liger',
                    'x-fb-client-ip': 'True',
                    'x-fb-server-cluster': 'True',
                }
                params = {
                    'product_types': 'content_appreciation,digital_collectibles',
                }

                response1 = requests.get(
                    'https://b.i.instagram.com/api/v1/creators/partner_program/get_monetization_products_gating/',
                    params=params,
                    headers=headers,
                )
                self.xclaim = response1.headers['x-ig-set-www-claim']
                self.igrur = response1.headers['ig-set-ig-u-rur'].split(':')[1]
                self.igid = response1.headers['ig-set-ig-u-shbid'].split(',')[0]

            else:

                self.igrur = response.headers['ig-set-ig-u-rur'].split(':')[1]
                self.xclaim = response.headers['x-ig-set-www-claim']
                
            value = {
                "status":"ok",
                'BlockVersion': self.Blockversion,
                "username": self.user,
                "password": self.passw,
                "FamilyDeviceID": str(self.IgFamilyDeviceId),
                "AndroidID": str(self.AndroidID),
                "DeviceID": str(self.IgDeviceId),
                'UserAgent': str(self.UserAgent),
                'PigeonSession': str(self.PigeonSession),
                "AuthToken":str(self.sessionid),
                "UID":str(self.userid),
                "X-Mid": str(self.mid),
                'igrur': str(self.igrur),
                'xclaim': str(self.xclaim),
                'igid':str(self.igid),
            }
        elif response.json()["message"] != "":
            value = {
                "message":response.json()["message"],
                "status":"fail"
            }
        else:
            value = {
                "message":"Username or Password is Wrong",
                "status":"fail"
        }
            
        return value