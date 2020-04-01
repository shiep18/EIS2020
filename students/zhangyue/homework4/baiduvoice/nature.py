import requests
import json

APIKey = 'LuUwUnqxmZYd1pCuwmn1WyTL'
SecretKey = 'ZBsM5DV0IFAmYAQ1sAvOSYCGpqbgMqi2'


# 得到请求url
def get_url():
    url = 0
    # 通过API Key和Secret Key获取access_token
    AccessToken_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(
        APIKey, SecretKey)
    res = requests.post(AccessToken_url)  # 推荐使用post
    json_data = json.loads(res.text)
    # print(json.dumps(json_data, indent=4, ensure_ascii=False))
    if not json_data or 'access_token' not in json_data:
        print("获取AccessToken的json数据失败")
    else:
        accessToken = json_data['access_token']
        # 将得到的access_token加到请求url中
        url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/lexer?charset=UTF-8&access_token={}'.format(accessToken)
    return url


# 创建请求，获取数据
def get_address(url, text):
    address = ''  # 存储得到的地址
    body = {
        "text": text,
    }
    body2 = json.dumps(body)  # 将字典形式的数据转化为字符串,否则报错
    # 创建Header请求
    header = {
        'Content-Type': 'application/json'
    }
    res = requests.post(url, headers=header, data=body2)  # 推荐使用post
    json_data = json.loads(res.text)
    if not json_data or 'error_code' in json_data:
        # print(json.dumps(json_data, indent=4, ensure_ascii=False))
        print("获取关键词的Json数据失败")
    else:
        for item in json_data['items']:
            if item['ne'] == "LOC":
                # print(item['item'])
                address = item['item']
        return address


# def getCity(text):
#     url = "https://api.shenjian.io/nlp/lexer?appid=07e8d355ba0a44f0d9580b669eb2bfc3&text=" + text
#     res = requests.post(url)
#     info = dict(res.json())
#     info = dict(info)
#     infoItems = info["data"]["items"]
#
#     result = ""
#     for num in range(len(infoItems)):
#         if infoItems[num]["ne"] == "LOC":
#             result = infoItems[num]["item"]
#             break
#
#     if result == "":
#         return ""
#     else:
#         print("%s" % result)
#         return result


def getMusicName(text):
    url = "https://api.shenjian.io/nlp/lexer?appid=07e8d355ba0a44f0d9580b669eb2bfc3&text=" + text
    res = requests.post(url)
    info = dict(res.json())
    info = dict(info)
    infoItems = info["data"]["items"]
    # print(infoItems)
    result = ""
    for num in range(len(infoItems)):
        if infoItems[num]["item"] == "听" or infoItems[num]["item"] == "想听" or infoItems[num]["item"] == "要听" or \
                infoItems[num]["item"] == "首" or infoItems[num]["item"] == "一首":
            num += 1
            for j in range(len(infoItems) - num):
                result += infoItems[num + j]["item"]
            break
    print()
    return result


# print(getMusicName(""))

var = {"refresh_token": "25.68bcd1fc3ad5e07713d10f28d9361c53.315360000.1901118621.282335-19207919",
       "expires_in": 2592000,
       "session_key": "9mzdCy\/Yho89Xrp4JOQg56IOeGMxtpwfqXw2PNvyBQm3Tdj9W9Ya0KepVXgFpCciZp+vNjXNpTN4LftdM6Omt8eoUJKaFQ==",
       "access_token": "24.07973eb2289cc195e7de92d2516e8857.2592000.1588350621.282335-19207919",
       "scope": "public nlp_simnet nlp_wordemb nlp_comtag nlp_dnnlm_cn brain_nlp_lexer brain_all_scope brain_nlp_comment_tag brain_nlp_dnnlm_cn brain_nlp_word_emb_vec brain_nlp_word_emb_sim brain_nlp_sentiment_classify brain_nlp_simnet brain_nlp_depparser brain_nlp_wordembedding brain_nlp_dnnlm_cn_legacy brain_nlp_simnet_legacy brain_nlp_comment_tag_legacy brain_nlp_lexer_custom brain_nlp_keyword brain_nlp_topic brain_nlp_ecnet brain_nlp_emotion brain_nlp_comment_tag_custom brain_nlp_news_summary brain_nlp_sentiment_classify_custom brain_nlp_address wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test\u6743\u9650 vis-classify_flower lpq_\u5f00\u653e cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi qatest_scope1 fake_face_detect_\u5f00\u653eScope vis-ocr_\u865a\u62df\u4eba\u7269\u52a9\u7406 idl-video_\u865a\u62df\u4eba\u7269\u52a9\u7406",
       "session_secret": "b9aded2b082c36ba0a6017c8d1b432dc"}
