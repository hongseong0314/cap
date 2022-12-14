crop_decoder_kr = {
    "00":"작물없음",
    "01":"고추",
    "02":"무",
    "03":"배추",
    "04":"애호박",
    "05":"양배추",
    "06":"오이",
    "07":"토마토",
    "08":"콩",
    "09":"파",
    "10":"호박",
}

crop_decoder_en = {
    "00":"no",
    "01":"pepper", #고추
    "02":"radish",#무
    "03":"napa", #배추
    "04":"squash", #애호박
    "05":"cabbage", #양배추
    "06":"cucumber", #오이
    "07":"tomato", #토마토
    "08":"bean", #콩
    "09":"onion", #파
    "10":"pumpkin", #호박
}

crop_aware_name_decoder = {
    0 : "고추 정상",
    1 : "고추탄저병",
    2 : "고추흰가루",
    3 : "무 정상", 
    4 : "무 검은무늬병",
    5 : "무 노균병",
    6 : "배추 정상",
    7 : "배추검은썩음병",
    8 : "배추노균병", 
    9 : "애호박 정상",
    10 : "애호박노균병",
    11 : "애호박흰가루",
    12 : "양배추 정상",
    13 : "양배추 균핵병",
    14 : "양배추 무름병",
    15 : "오이 정상",
    16 : "오이 노균병",
    17 : "오이 흰가루병",
    18 : "콩 정상",
    19 : "콩 불마름병",
    20 : "콩 점무늬병",
    21 : "토마토 정상",
    22 : "토마토 잎마름병",
    23 : "파 정상",
    24 : "파 검은무늬병",
    25 : "파 노균병",
    26 : "파 녹병",
    27 : "호박 정상",
    28 : "호박 노균병",
    29 : "호박 흰가루병",
    30 : "작물 없음",
}
name2encoder = {
    '고추 정상': 0,
    '고추탄저병': 1,
    '고추흰가루': 2,
    '무 정상': 3,
    '무 검은무늬병': 4,
    '무 노균병': 5,
    '배추 정상': 6,
    '배추검은썩음병': 7,
    '배추노균병': 8,
    '애호박 정상': 9,
    '애호박노균병': 10,
    '애호박흰가루': 11,
    '양배추 정상': 12,
    '양배추 균핵병': 13,
    '양배추 무름병': 14,
    '오이 정상': 15,
    '오이 노균병': 16,
    '오이 흰가루병': 17,
    '콩 정상': 18,
    '콩 불마름병': 19,
    '콩 점무늬병': 20,
    '토마토 정상': 21,
    '토마토 잎마름병': 22,
    '파 정상': 23,
    '파 검은무늬병': 24,
    '파 노균병': 25,
    '파 녹병': 26,
    '호박 정상': 27,
    '호박 노균병': 28,
    '호박 흰가루병': 29,
    '작물 없음': 30
 }


disease_aware_decoder = {
    "00":0,#"정상"
    "01":1,#"고추탄저병",
    "02":2,#"고추흰가루병",
    "03":4,#"무검은무늬병",
    "04":5,#"무노균병",
    "05":7,#"배추검은썩음병",
    "06":8,#"배추노균병",
    "07":10,#"애호박노균병",
    "08":11,#"에호박흰가루",
    "09":13,#"양배추균핵병",
    "10":14,#"양배추무름병",
    "11":16,#"오이노균병",
    "12":17,#"오이흰가루병",
    "13":19,#"콩불마름병",
    "14":20,#"콩점무늬병",
    "15":22,#"토마토잎마름병",
    "16":24,#"파검은무늬병",
    "17":25,#"파노균병",
    "18":26,#"파녹병",
    "19":28,#"호박노균병",
    "20":29,#"호박흰가루병",
}

crop_aware_decoder_kr = {
    "00":30,#"작물없음",
    "01":0,#"고추",
    "02":3,#"무",
    "03":6,#"배추",
    "04":9,#"애호박",
    "05":12,#"양배추",
    "06":15,#"오이",
    "07":21,#"토마토",
    "08":18,#"콩",
    "09":23,#"파",
    "10":27,#"호박",
}

crop_indexing = {
    0 : [30], #작물없음
    1 : [0,3], #고추
    2 : [3,6], #무
    3 : [6,9], #배추
    4 : [9,12], #애호박
    5 : [12,15], #양배추
    6 : [15,18], #오이
    7 : [21,23], #토마토
    8 : [18,21], #콩
    9 : [23,27], #파
    10 : [27,30] #호박
}

risks = {
    0 : "정상",
    1 : "초기",
    2 : "중기",
    3 : "말기",
}

area_dict = {
    0 :"구분없음",
    1 :"열매",
    2 :"꽃",
    3 :"잎",
    4 :"가지",
    5 :"줄기",
    6 :"뿌리",
    7: "해충",
}

# [0,3,6,9,12,15,18,21,23,27] 정상 index