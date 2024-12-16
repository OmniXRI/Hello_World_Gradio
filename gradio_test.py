import gradio as gr # 導入 Gradio 函式庫並令別名為 gr

# 定義 Gradio 輸出入處理函式 greet2()
# 輸入： name（字串）、is_morning（布林值）、temperature（數值）
# 輸出： "Good morning name, It is xx.x ℉ today"（字串）、攝氏溫度（數值）
def greet2(name, is_morning, temperature):
  salutation = "Good morning" if is_morning else "Good evening" # 若複選盒有勾選則輸出 "Good morning", 否則輸出 "Good evening"
  greeting = f"{salutation} {name}. It is {temperature} ℉ today" # 組合輸出用字串
  celsius = (temperature - 32) * 5 / 9 # 將華氏溫度轉成攝氏
  return greeting, round(celsius, 2) 

def launch_demo():
  # 建立輸人及輸出簡單應用介面
  # fn: 介面函數名稱
  # inputs: 輸人格式， 名字（字串）、是早上（複選盒）、華氏溫度（滑桿，最小值0，最大值100，預設值50）
  # outputs: 輸出格式，結果字串（標籤 Reslut）、結果溫度（標籤 攝氏（℃））
  demo = gr.Interface(
      fn=greet2,
      inputs=[gr.Textbox(placeholder="請輸入姓名", label="姓名"), "checkbox", gr.Slider(0, 100, value=50, label="華氏（℉）")], 
      outputs=[gr.Textbox(label="輸出"), gr.Textbox(label="攝氏（℃）")],
  )

  # 執行顯示介面
  demo.launch()
