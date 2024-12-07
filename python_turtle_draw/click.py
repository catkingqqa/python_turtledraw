import tkinter as tk

def on_click(event):
    # 取得點擊位置，並以視窗中心為原點計算
    x_centered = event.x - window_width // 2
    y_centered = event.y - window_height // 2
    print(f"你點擊的位置是: ({x_centered}, {y_centered})")

# 設定視窗大小
window_width = 1280
window_height = 720

# 建立主視窗
root = tk.Tk()
root.title("中心為原點的點擊視窗")

# 設置視窗大小
root.geometry(f"{window_width}x{window_height}")

# 綁定點擊事件
root.bind("<Button-1>", on_click)  # 左鍵點擊

# 啟動主迴圈
root.mainloop()
