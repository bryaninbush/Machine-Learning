import joblib
from joblib import load
model_pretrained = load('trained_model.pkl')
import numpy as np

import requests
res_GRE = requests.get("https://masongre.blogspot.com/p/mason-gre-gre-mason-20-gre-gre-75-toeic.html")
res_TOEFL = requests.get("http://sk2toefl.blogspot.com/p/blog-page_94.html")

from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def formPage():
    return render_template('formPage.html')
 
@app.route("/submit", methods=['POST'])
def submit():
    if request.method == 'POST':
        form_data = request.form

        #University Rating	
        University_Rating_1 = ""
        University_Rating_2 = ""        
        University_Rating_3 = ""
        University_Rating_4 = ""
        University_Rating_5 = ""
        if int(form_data['University_Rating']) == 1:
            University_Rating_1 = 'selected'
        elif int(form_data['University_Rating']) == 2:
            University_Rating_2 = 'selected'
        elif int(form_data['University_Rating']) == 3:
            University_Rating_3 = 'selected'
        elif int(form_data['University_Rating']) == 4:
            University_Rating_4 = 'selected'
        else:
            University_Rating_5 = 'selected'

        #SOP
        SOP_1 = ""
        SOP_15 = ""
        SOP_2 = ""        
        SOP_25 = ""        
        SOP_3 = ""
        SOP_35 = ""
        SOP_4 = ""
        SOP_45 = ""
        SOP_5 = ""
        if float(form_data['SOP']) == 1:
            SOP_1 = 'selected'
        elif float(form_data['SOP']) == 1.5:
            SOP_15 = 'selected'        
        elif float(form_data['SOP']) == 2:
            SOP_2 = 'selected'
        elif float(form_data['SOP']) == 2.5:
            SOP_25 = 'selected'
        elif float(form_data['SOP']) == 3:
            SOP_3 = 'selected'
        elif float(form_data['SOP']) == 3.5:
            SOP_35 = 'selected'
        elif float(form_data['SOP']) == 4:
            SOP_4 = 'selected'
        elif float(form_data['SOP']) == 4.5:
            SOP_45 = 'selected'
        else:
            SOP_5 = 'selected'

        #LOR	
        LOR_1 = ""
        LOR_15 = ""
        LOR_2 = ""        
        LOR_25 = ""        
        LOR_3 = ""
        LOR_35 = ""
        LOR_4 = ""
        LOR_45 = ""
        LOR_5 = ""
        if float(form_data['LOR']) == 1:
            LOR_1 = 'selected'
        elif float(form_data['LOR']) == 1.5:
            LOR_15 = 'selected'        
        elif float(form_data['LOR']) == 2:
            LOR_2 = 'selected'
        elif float(form_data['LOR']) == 2.5:
            LOR_25 = 'selected'
        elif float(form_data['LOR']) == 3:
            LOR_3 = 'selected'
        elif float(form_data['LOR']) == 3.5:
            LOR_35 = 'selected'
        elif float(form_data['LOR']) == 4:
            LOR_4 = 'selected'
        elif float(form_data['LOR']) == 4.5:
            LOR_45 = 'selected'
        else:
            LOR_5 = 'selected'

        #判別式
        type_error = 1
        GRE_error = 1
        TOELF_error = 1
        CGPA_error = 1
        #ERROR
        #GRE Score
        if int(form_data['GRE_Score'])<260 or int(form_data['GRE_Score']) > 340:
            GRE_error = 0
        else:
            GRE_error = 1
        #TOELF Score
        if int(form_data['TOEFL_Score']) > 120 or int(form_data['TOEFL_Score']) < 0:
            TOELF_error = 0
        else:
            TOELF_error = 1
        #CGPA
        if float(form_data['CGPA']) <1 or float(form_data['CGPA']) >10:
            CGPA_error = 0
        else:
            CGPA_error = 1
        #type_error
        if GRE_error*TOELF_error*CGPA_error == 0:
            type_error = 0
        else:
            type_error = 1

        
        # ['GRE Score','TOEFL Score','University Rating','SOP','LOR','CGPA']
        result = model_pretrained.predict([[ int(form_data['GRE_Score']),int(form_data['TOEFL_Score']),int(form_data['University_Rating']),float(form_data['SOP']),float(form_data['LOR']),float(form_data['CGPA']) ]])

        # 顯示結果的內容
        list_str = ['你要確定ㄟ 是不是打錯了','你當我是塑膠嗎? 重填!!','無法計算:(']
        prob_high = ["https://p8.itc.cn/images01/20220314/87bc25570bd74f868479a17343f748ce.png",
                     "https://imgur.dcard.tw/djwljOXh.jpg"]

        prob_low = ["https://scontent.xx.fbcdn.net/v/t1.6435-9/98338109_264745994891850_3422489108369375232_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=8bfeb9&_nc_ohc=RKszYdW8zRoAX9p_3Dj&tn=G1ZDV4KozdSgdAg5&_nc_ht=scontent.ftpe7-1.fna&oh=00_AfBJ4yReAiW8bzGuH6yIjZfhsaiGpf79xAZAs-yPqWNYtg&oe=63D752FA&_nc_fr=ftpe7c01",
                    "https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1631263589133.jpg"]

        error = ["https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1655889030708.jpg",
                "https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1638117774102.jpg",
                "https://dvblobcdnjp.azureedge.net//Content/Upload/Popular/Images/2021-05/d0d8bc48-3f07-4614-8e17-5f96978b4e8d_m.jpg",
                "https://memeprod.ap-south-1.linodeobjects.com/user-template/82e491b6ae69721b75e0d2c13535bc5b.png",
                "https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1588745704333.jpg",
                "https://assets.juksy.com/files/articles/116580/800x_100_w-62d6632c3e6a1.jpg",
                "https://assets.matters.news/cover/bae637f8-4e0f-4a65-b1ba-cbb4a0dc34a4.jpeg"]

        # 設定梗圖來源格式
        graph_url = " "
        height = " "
        
        ad_str = " "
        adG_url = " "
        adT_url = " "
        
        # 判別輸入值是否錯誤
        if type_error == 1:
            prediction =  round(result[0],4)
            result_str = "你的入學機率是："

            # 發送廣告推薦
            if int(form_data['GRE_Score'])<300 and int(form_data['TOEFL_Score'])<71:
                ad_str = "為您推薦："
                adG_url = f'GRE四週全科密集班： {res_GRE.url}'
                adT_url = f'托福加強訓練： {res_TOEFL.url}'
            elif int(form_data['GRE_Score'])<300: #GRE廣告
                ad_str = "為您推薦："
                adG_url = f'GRE四週全科密集班： {res_GRE.url}'
            elif int(form_data['TOEFL_Score'])<71: #TOEFL廣告
                ad_str = "為您推薦："
                adT_url = f'托福加強訓練： {res_TOEFL.url}'
            else:
                ad_str = " "
                adG_url = " "
                adT_url = " "

            # 選梗圖
            if prediction < 0.3: #小機率
                graph_url = np.random.choice(prob_low)
                height = "200"
            elif prediction >0.8: #大機率
                graph_url = np.random.choice(prob_high)
                height = "200"
            else:
                graph_url = " "
                height = " "

        else:
            result_str = np.random.choice(list_str)
            prediction = " "
            graph_url = np.random.choice(error)
            height = "200"

        return render_template('formPage.html', 
        GRE_Score = form_data['GRE_Score'],
        TOEFL_Score = form_data['TOEFL_Score'],
        University_Rating_1 = University_Rating_1 ,University_Rating_2 = University_Rating_2 ,University_Rating_3 = University_Rating_3 ,University_Rating_4 = University_Rating_4 ,University_Rating_5 = University_Rating_5,
        SOP_1 = SOP_1, SOP_15 = SOP_15, SOP_2 = SOP_2, SOP_25 = SOP_25, SOP_3 = SOP_3, SOP_35 = SOP_35, SOP_4 = SOP_4, SOP_45 = SOP_45, SOP_5 = SOP_5,
        LOR_1 = LOR_1, LOR_15 = LOR_15, LOR_2 = LOR_2, LOR_25 = LOR_25, LOR_3 = LOR_3, LOR_35 = LOR_35, LOR_4 = LOR_4, LOR_45 = LOR_45, LOR_5 = LOR_5,
        CGPA = form_data['CGPA'],
        result_str = result_str,
        prediction = prediction,
        ad_str = ad_str,
        adT_url = adT_url,
        adG_url = adG_url,
        graph = "src="+graph_url,
        height = "height="+height)
 
if __name__ == "__main__":
    app.run()

