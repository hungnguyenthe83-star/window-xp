import streamlit as st

# 1. Cấu hình giao diện chuẩn hóa cho khung hiển thị Streamlit Cloud
st.set_page_config(
    page_title="Windows XP Emulator", 
    page_icon="💾", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("📟 Trình Giả Lập Hệ Điều Hành Windows XP Luna")
st.caption("Mẹo: Nếu giao diện không hiển thị, hãy mở bằng tab ẩn danh (Incognito) để tránh bị chặn bởi các tiện ích trình duyệt.")

# 2. Toàn bộ mã nguồn giao diện hệ điều hành được đóng gói phẳng, loại bỏ f-string chống lỗi biên dịch
html_content = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Windows XP Professional</title>
    <style>
        body {
            margin: 0; padding: 0; overflow: hidden;
            font-family: 'Tahoma', 'Segoe UI', sans-serif;
            user-select: none; background: #0051e6;
        }
        #desktop {
            width: 100vw; height: 540px;
            background: url('https://wikimedia.org') center/cover no-repeat;
            position: relative; box-sizing: border-box; padding: 15px;
        }
        .desktop-icon {
            width: 85px; height: 75px; display: flex; flex-direction: column;
            align-items: center; justify-content: center; cursor: pointer;
            text-align: center; margin-bottom: 15px; border: 1px solid transparent; border-radius: 3px;
        }
        .desktop-icon:hover {
            background: rgba(43, 114, 245, 0.4); border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .desktop-icon span {
            color: white; font-size: 11px; margin-top: 5px; text-shadow: 1px 1px 2px rgba(0,0,0,0.9);
        }
        .svg-icon { width: 32px; height: 32px; }
        .window {
            position: absolute; width: 450px; height: 300px;
            background: #F1EEE4; border: 3px solid #0054E3;
            border-top-left-radius: 8px; border-top-right-radius: 8px;
            box-shadow: 3px 3px 12px rgba(0,0,0,0.4); display: none; flex-direction: column; z-index: 10;
        }
        .title-bar {
            background: linear-gradient(to bottom, #0058e6 0%, #0073ea 12%, #0058e6 88%, #0044b3 100%);
            height: 28px; display: flex; align-items: center; justify-content: space-between;
            padding: 0 8px; color: white; font-weight: bold; font-size: 12px; text-shadow: 1px 1px 1px rgba(0,0,0,0.5);
            border-top-left-radius: 5px; border-top-right-radius: 5px;
        }
        .window-buttons { display: flex; gap: 4px; }
        .win-btn {
            width: 21px; height: 21px; border-radius: 3px; cursor: pointer;
            font-weight: bold; font-size: 11px; display: flex; align-items: center; justify-content: center;
            color: white; border: 1px solid rgba(0,0,0,0.4); background: linear-gradient(to bottom, #2d7af4, #004cb3);
        }
        .btn-close { background: linear-gradient(to bottom, #e76043 0%, #e74322 15%, #b32d14 100%); }
        .win-btn:hover { filter: brightness(1.2); }
        .window-content {
            padding: 12px; flex-grow: 1; overflow: auto; font-size: 12px; color: #000;
            background: #FFF; margin: 4px; border: 1px solid #7F9DB9;
        }
        #taskbar {
            width: 100vw; height: 40px;
            background: linear-gradient(to bottom, #245edb 0%, #3f8cf3 9%, #245edb 18%, #1b4ca3 100%);
            position: absolute; bottom: 0; left: 0; display: flex;
            align-items: center; justify-content: space-between; z-index: 100; border-top: 1px solid #174291;
        }
        #start-btn {
            background: linear-gradient(to bottom, #388e3c 0%, #5cb85c 10%, #388e3c 90%, #225e25 100%);
            height: 100%; padding: 0 25px; display: flex; align-items: center; color: white;
            font-weight: bold; font-style: italic; font-size: 16px; cursor: pointer;
            border-top-right-radius: 8px; border-bottom-right-radius: 8px; box-shadow: 2px 0 5px rgba(0,0,0,0.4); border: none;
        }
        #start-btn:hover { filter: brightness(1.15); }
        #system-tray {
            background: linear-gradient(to bottom, #0c8df6 0%, #1ea1fc 9%, #0c8df6 18%, #045cb4 100%);
            height: 100%; padding: 0 15px; display: flex; align-items: center; color: white; font-size: 11px;
            border-left: 1px solid #084c8c;
        }
    </style>
</head>
<body>

    <div id="desktop">
        <!-- Icons ngoài màn hình chính bằng SVG vẽ nội địa -->
        <div class="desktop-icon" onclick="openWindow('my-computer')">
            <svg class="svg-icon" viewBox="0 0 24 24"><path fill="#ffca28" d="M19,17H5V7H19M19,5H5A2,2 0 0,0 3,7V17A2,2 0 0,0 5,19H19A2,2 0 0,0 21,17V7A2,2 0 0,0 19,5Z"/></svg>
            <span>My Computer</span>
        </div>

        <div class="desktop-icon" onclick="openWindow('internet-explorer')">
            <svg class="svg-icon" viewBox="0 0 24 24"><path fill="#0288d1" d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12A8,8 0 0,1 12,20A8,8 0 0,1 4,12A8,8 0 0,1 12,4Z"/></svg>
            <span>Internet Explorer</span>
        </div>

        <!-- Cửa sổ My Computer -->
        <div class="window" id="my-computer" style="left: 80px; top: 60px;">
            <div class="title-bar">
                <span>My Computer</span>
                <div class="window-buttons"><div class="win-btn btn-close" onclick="closeWindow('my-computer')">X</div></div>
            </div>
            <div class="window-content">
                <span style="color:#0054E3; font-weight:bold;">Hard Disk Drives</span><br><hr size="1" color="#D2CFBB">
                💽 Local Disk (C:) - 14.2 GB Free / 40.0 GB<br><br>
                <span style="color:#0054E3; font-weight:bold;">Devices with Removable Storage</span><br><hr size="1" color="#D2CFBB">
                💿 CD Drive (D:) - Empty
            </div>
        </div>

        <!-- Cửa sổ Internet Explorer -->
        <div class="window" id="internet-explorer" style="left: 180px; top: 120px;">
            <div class="title-bar">
                <span>Welcome to Microsoft Internet Explorer</span>
                <div class="window-buttons"><div class="win-btn btn-close" onclick="closeWindow('internet-explorer')">X</div></div>
            </div>
            <div class="window-content">
                <h3 style="color:#0044b3; margin-top:0;">Windows XP Emulator pro</h3>
                <p>Hệ điều hành giả lập Luna đã hoạt động ổn định tuyệt đối trên đám mây.</p>
                <p>Mã nguồn đã được giải phóng hoàn toàn khỏi các lỗi xung đột hệ thống.</p>
            </div>
        </div>
    </div>

    <!-- Thanh tác vụ dưới cùng -->
    <div id="taskbar">
        <button id="start-btn" onclick="alert('Hệ thống hoạt động tốt!')">start</button>
        <div id="system-tray">
            🔊&nbsp;<span id="clock">00:00 PM</span>
        </div>
    </div>

    <script>
        window.openWindow = function(id) { document.getElementById(id).style.display = 'flex'; }
        window.closeWindow = function(id) { document.getElementById(id).style.display = 'none'; }
        
        function updateClock() {
            const now = new Date();
            let hours = now.getHours();
            let minutes = now.getMinutes();
            let ampm = hours >= 12 ? 'PM' : 'AM';
            hours = hours % 12; hours = hours ? hours : 12;
            minutes = minutes < 10 ? '0'+minutes : minutes;
            document.getElementById('clock').innerText = hours + ':' + minutes + ' ' + ampm;
        }
        setInterval(updateClock, 1000);
        updateClock();
    </script>
</body>
</html>
"""

# 3. Kết xuất Iframe tĩnh (Không cho phép thanh cuộn làm hỏng cấu trúc màn hình)
st.components.v1.html(html_content, height=600, scrolling=False)



