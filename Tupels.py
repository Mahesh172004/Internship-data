cameras={'canon':200,'sony':300}
print(cameras)      # Output: {'canon': 200, 'sony': 300}
cameras.update({'samsung':500})
print(cameras)      # Output: {'canon': 200, 'sony': 300, 'samsung': 500}
cameras['xyz']=1000
print(cameras)      # Output: {'canon': 200, 'sony': 300, 'samsung': 500, 'xyz': 1000}
print(cameras['canon'])  # Output: 200
