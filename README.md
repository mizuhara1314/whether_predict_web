# Weather-Prediction-System
幫大陸研究生做的空氣質量監測系統，讀取pm2.5csv數據並可視化和分析預測

# 使用技術：
  Python、Django、pandas、numpy、LSTM
  
# 簡介：
  可从pm25.csv中讀取數據訓練並做預測

# 運行
  1.在第一次執行 Django 專案之前，需要應用資料庫遷移：

  ```bash
 python manage.py migrate
```
 
  
  2.之後運行項目只需啟動 Django 伺服器:
  ```bash
  python manage.py runserver
```
# 未來改進 :
  可改成導入預訓練好的模型做預測取代每次點擊都要訓練完一次再預測，實時更新，以及串接天氣api取代數據集

# 收穫 :
透過dijango框架對環境變數文件跟環境(mode)設定的概念加深了
  
# 展示：
![image](https://github.com/user-attachments/assets/f157402d-c767-4bd8-82fc-a27859ce1b80)

![image](https://github.com/user-attachments/assets/c85389d4-d9ac-42be-b379-d1e6381af4d9)
![image](https://github.com/user-attachments/assets/670078b1-46f5-42ba-bf66-702e5e0971bb)
![image](https://github.com/user-attachments/assets/e79dccbc-c767-4af4-a380-127b412b21d4)



