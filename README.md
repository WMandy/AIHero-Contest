# AIHero-Contest
2019年10月第四范式举办的AIHero算法大赛  第一名
破解工商信息网站验证码，网址：http://www.gsxt.gov.cn/index.html  
### 验证码样式(根据文字语序点选）：  
![文字](https://github.com/WMandy/AIHero-Contest/blob/master/example_images/000000.png)
![文字](https://github.com/WMandy/AIHero-Contest/blob/master/example_images/000021.png)  
### 样本来源：  
1.爬虫， 
2.生成假数据
### 破解思路：  
1. 使用目标检测网络ssd检测验证码图像中的文字并切割成单字  
2. 使用分类网络识别单字，单字训练样本来源：实际切割单字图以及生成的假数据  
3. 使用语言模型seq2seq或ngram，按照语序组合单字（两种方案都尝试过，各有优缺，经测试ngram精度更高，最终版提交的ngram模型）  
