# music-test
音樂比對
branch: compare

使用的套件



現階段僅支持windows



1. 安裝ffmpeg library
能夠對音檔/ 影片進行解碼(decode)、編碼(encode)、轉碼().......

2. ffmpeg官網: https://www.ffmpeg.org/
Download
    windows
        Windows builds from gyan.dev
            點擊下載壓縮檔案

![image](https://user-images.githubusercontent.com/47851007/171563572-1e3c678b-20b8-4803-8f79-aa46261f4c8e.png)




3. 解壓縮內部的所有檔案至C:\users\xxxx\desktop\自定義folder"



4. 添加path進環境變數

![image](https://user-images.githubusercontent.com/47851007/171563523-516f9b8d-dd1a-4a97-82a3-a6622eeebe0b.png)


5. terminal測試是否安裝成功
ffmpeg -version

正確可跳出
![image](https://user-images.githubusercontent.com/47851007/171563614-e8a7d040-2935-4f6f-8082-8bee983263a2.png)


不正確的話則跳出紅字指令錯誤

6. 整理好spec_music的音樂檔不管.mp3 & .wav檔，皆放進自定義的資料夾內



7. 使用chrome套件Resource saver下載資源壓縮檔



8. 整理好資源包內的.mp3 & .wav檔，皆放進自定義的資料夾內(正確情況下_這裡的音檔數量會大於spec_music的數量)



9. 程式端_使用main.py
compare() 參數塞入上述處理好的資料夾位址

第一個參數為"正確SPEC_音樂folder"

第二個參數為"需要比較_音樂folder"

![image](https://user-images.githubusercontent.com/47851007/171563460-12afb212-8ac4-4679-ae0a-377056d41727.png)


10. windows會於desktop創建"Music_compare"資料夾，裡面包含重新轉檔的.mp3 & .wav(每跑一次程式會重建該資料夾)





11. 程式跑完後，一樣會於desktop創建"Music_log"，已.txt檔的形式記錄成功比對的檔案

