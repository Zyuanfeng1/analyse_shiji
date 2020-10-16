import re
for i in range(130):
    with open(f'content{i+1}.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        s3 = re.sub(r"[0-9\s+\.\!\/_,$%^*()?;；:-【】+\"\']+|[+——！，;:。？、~@#￥%……&*（）]+", '', s)
        print(s3)
        with open(f'analysed_shiji_whole{i + 1}.txt', 'a+', encoding='utf-8') as f1:
            f1.write(s3)




