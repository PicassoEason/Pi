import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('serviceAccount.json')
 
# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)
# 初始化firestore
db = firestore.client()

doc = {
  'temp': "26",
  'hunidity': "ccc"
}

clo_ref = db.collection("pi")

# doc_ref提供一個set的方法，input必須是dictionary

clo_ref.add(doc)