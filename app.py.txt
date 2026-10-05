import streamlit as st

# Cấu hình giao diện khung Streamlit mở rộng không gian làm việc
st.set_page_config(page_title="Windows XP Emulator", page_icon="💾", layout="wide")

st.title("📟 Trình Giả Lập Hệ Điều Hành Windows XP")
st.write("Click vào các biểu tượng **My Computer** hoặc **Internet Explorer** để mở các cửa sổ hoài niệm!")

# Mã giao diện Windows XP (Được chuẩn hóa chuỗi văn bản thuần túy tránh lỗi biên dịch)
html_xp = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Windows XP Emulator</title>
    <style>
        body {
            margin: 0; padding: 0; overflow: hidden;
            font-family: 'Tahoma', sans-serif;
            user-select: none;
        }
        /* Hình nền đồi cỏ Bliss huyền thoại */
        #desktop {
            width: 100vw; height: 560px;
            background: url('https://wikimedia.org') center/cover no-repeat;
            position: relative;
            box-sizing: border-box;
            padding: 20px;
        }
        /* Các biểu tượng trên Desktop */
        .desktop-icon {
            width: 80px; height: 75px;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            cursor: pointer; text-align: center; margin-bottom: 15px;
            border: 1px solid transparent; border-radius: 3px;
        }
        .desktop-icon:hover {
            background: rgba(255, 255, 255, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.4);
        }
        .desktop-icon span {
            color: white; font-size: 11px; margin-top: 5px;
            text-shadow: 1px 1px 2px black;
        }
        .icon-img { font-size: 32px; }

        /* Cửa sổ ứng dụng (Windows) */
        .window {
            position: absolute; width: 400px; height: 280px;
            background: #ECE9D8; border: 3px solid #0055E6;
            border-top-left-radius: 7px; border-top-right-radius: 7px;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
            display: none; flex-direction: column;
            z-index: 10;
        }
        /* Thanh tiêu đề màu xanh XP */
        .title-bar {
            background: linear-gradient(to bottom, #0058e6 0%, #0073ea 12%, #0058e6 88%, #0044b3 100%);
            height: 30px; display: flex; align-items: center; justify-content: space-between;
            padding: 0 10px; color: white; font-weight: bold; font-size: 13px;
        }
        .close-btn {
            background: linear-gradient(to bottom, #e76043 0%, #e74322 12%, #b32d14 100%);
            border: 1px solid #7c1a0c; width: 21px; height: 21px; color: white;
            font-weight: bold; border-radius: 3px; cursor: pointer; text-align: center; line-height: 17px;
        }
        .close-btn:hover { filter: brightness(1.2); }
        .window-content { padding: 15px; flex-grow: 1; overflow: auto; font-size: 13px; color: #000; }

        /* THANH TASKBAR PHÍA DƯỚI */
        #taskbar {
            width: 100vw; height: 40px;
            background: linear-gradient(to bottom, #245edb 0%, #3f8cf3 9%, #245edb 18%, #1b4ca3 100%);
            position: absolute; bottom: 0; left: 0;
            display: flex; align-items: center; justify-content: space-between; z-index: 100;
        }
        /* Nút Start thần thánh */
        #start-btn {
            background: linear-gradient(to bottom, #388e3c 0%, #4caf50 10%, #388e3c 90%, #2e7d32 100%);
            height: 100%; padding: 0 25px; display: flex; align-items: center;
            color: white; font-weight: bold; font-style: italic; font-size: 16px;
            cursor: pointer; border-top-right-radius: 8px; border-bottom-right-radius: 8px;
            box-shadow: 2px 0 5px rgba(0,0,0,0.3); border: none;
        }
        #start-btn:hover { filter: brightness(1.1); }
        
        /* Khay hệ thống và đồng hồ */
        #system-tray {
            background: linear-gradient(to bottom, #0c8df6 0%, #1ea1fc 9%, #0c8df6 18%, #045cb4 100%);
            height: 100%; padding: 0 15px; display: flex; align-items: center;
            color: white; font-size: 12px; border-left: 1px solid #084c8c;
        }
    </style>
</head>
<body>

    <div id="desktop">
        <!-- Các Icon ngoài màn hình chính -->
        <div class="desktop-icon" onclick="openWindow('my-computer')">
            <div class="icon-img">🖥️</div>
            <span>My Computer</span>
        </div>
        <div class="desktop-icon" onclick="openWindow('internet-explorer')">
            <div class="icon-img">🌐</div>
            <span>Internet Explorer</span>
        </div>

        <!-- Cửa sổ My Computer -->
        <div class="window" id="my-computer" style="left: 60px; top: 50px;">
            <div class="title-bar">
                <span>My Computer</span>
                <button class="close-btn" onclick="closeWindow('my-computer')">X</button>
            </div>
            <div class="window-content">
                <strong>Ổ đĩa hệ thống:</strong><br><br>
                💽 Local Disk (C:) - 19.9 GB / 40 GB<br><br>
                💿 CD Drive (D:) - Empty
            </div>
        </div>

        <!-- Cửa sổ Internet Explorer -->
        <div class="window" id="internet-explorer" style="left: 180px; top: 100px; width: 450px;">
            <div class="title-bar">
                <span>Internet Explorer</span>
                <button class="close-btn" onclick="closeWindow('internet-explorer')">X</button>
            </div>
            <div class="window-content" style="background: white;">
                <h3 style="margin-top:0;">Welcome to Streamlit XP!</h3>
                <p>Hệ điều hành giả lập đang hoạt động hoàn hảo trên nền tảng đám mây.</p>
                <hr>
                <div style="display:flex; gap:5px;">
                    <input type="text" value="https://google.com" style="flex-grow:1; padding: 4px;" readonly> 
                    <button style="padding: 4px 10px; cursor:pointer;">Go</button>
                </div>
            </div>
        </div>
    </div>

    <!-- THANH TASKBAR -->
    <div id="taskbar">
        <button id="start-btn" onclick="alert('Hệ thống đang chạy mượt mà! Bấm các icon trên màn hình để trải nghiệm.')">start</button>
        <div id="system-tray">
            🕒&nbsp;<span id="clock">00:00 PM</span>
        </div>
    </div>

    <script>
        // Hàm mở cửa sổ ứng dụng
        window.openWindow = function(id) {
            document.getElementById(id).style.display = 'flex';
        }
        // Hàm đóng cửa sổ ứng dụng
        window.closeWindow = function(id) {
            document.getElementById(id).style.display = 'none';
        }

        // Cập nhật đồng hồ thời gian thực ở góc phải khay hệ thống
        function updateClock() {
            const now = new Date();
            let hours = now.getHours();
            let minutes = now.getMinutes();
            let ampm = hours >= 12 ? 'PM' : 'AM';
            hours = hours % 12;
            hours = hours ? hours : 12; 
            minutes = minutes < 10 ? '0'+minutes : minutes;
            document.getElementById('clock').innerText = hours + ':' + minutes + ' ' + ampm;
        }
        setInterval(updateClock, 1000);
        updateClock();
    </script>
</body>
</html>
"""

# Kích hoạt cấu phần Iframe hiển thị màn hình Windows XP độc lập
st.components.v1.html(html_xp, height=620, scrolling=False)
