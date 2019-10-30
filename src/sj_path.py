#환경변수 지정
#다른폴더라도 같은 폴더처럼 인식하게 해줌.
import sys

#window - crawler
sys.path.insert(0,'./')
sys.path.insert(0,'../../')
sys.path.insert(0,'./sj_crawling')
sys.path.insert(0,'./login')
sys.path.insert(0,'./etc')
sys.path.insert(0,'./list')
sys.path.insert(0,'./dbs/mongo')
#IML Tokenizer
sys.path.insert(0,'./etc/IML_Tokenizer/src')
sys.path.insert(0, '../../IML_Tokenizer/src/')
#IML AI
sys.path.insert(0, '../../SJ_AI/src')
#Server
sys.path.insert(0,'/home/iml/')
sys.path.insert(0,'/home/iml/SOOJLE/')
sys.path.insert(0,'/home/iml/SJ_Auth')
sys.path.insert(0,'/home/iml/SJ_AI/src')
sys.path.insert(0,'/home/iml/IML_Tokenizer/src/')
#server - crawler
sys.path.insert(0,'/home/iml/SOOJLE_Crawler/')
sys.path.insert(0,'/home/iml/SOOJLE_Crawler/src/')
sys.path.insert(0,'/home/iml/SOOJLE_Crawler/src/login/')
sys.path.insert(0,'/home/iml/SOOJLE_Crawler/src/sj_crawling/')
sys.path.insert(0,'/home/iml/SOOJLE_Crawler/src/etc/')
sys.path.insert(0,'/home/iml/SOOJLE_Crawler/src/list/')
sys.path.insert(0,'/home/iml/SOOJLE_Crawler/src/dbs/mongo/')