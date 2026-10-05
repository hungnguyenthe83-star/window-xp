import streamlit as st

# Cấu hình giao diện Streamlit mở rộng tối đa
st.set_page_config(page_title="Microsoft Windows XP Professional", page_icon="💾", layout="wide")

st.title("📟 Trình Giả Lập Windows XP Professional")
st.write("Click vào các biểu tượng **My Computer** hoặc **Internet Explorer** để trải nghiệm giao diện chuẩn hệ điều hành Luna!")

# Bộ mã HTML/CSS/JS tự vẽ đồ họa SVG nội địa để tránh lỗi đường dẫn mạng
html_xp_clean = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Windows XP Professional</title>
    <style>
        body {
            margin: 0; padding: 0; overflow: hidden;
            font-family: 'Tahoma', 'Segoe UI', sans-serif;
            user-select: none;
            background: #0051e6;
        }
        /* Màn hình Desktop với ảnh nền Bliss độ phân giải cao */
        #desktop {
            width: 100vw; height: 560px;
            background: url('https://wikimedia.org') center/cover no-repeat;
            position: relative;
            box-sizing: border-box;
            padding: 15px;
        }
        
        /* Hệ thống Icon ngoài màn hình chính */
        .desktop-icon {
            width: 85px; height: 75px;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            cursor: pointer; text-align: center; margin-bottom: 15px;
            border: 1px solid transparent; border-radius: 3px;
        }
        .desktop-icon:hover {
            background: rgba(43, 114, 245, 0.4);
            border: 1px solid rgba(255, 255, 255, 0.3);
        }
        .desktop-icon span {
            color: white; font-size: 11px; margin-top: 5px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.9);
        }
        .svg-icon { width: 32px; height: 32px; }

        /* CỬA SỔ WINDOWS XP CHUẨN ĐẾN TỪNG PIXEL */
        .window {
            position: absolute; width: 460px; height: 320px;
            background: #F1EEE4; border: 3px solid #0054E3;
            border-top-left-radius: 8px; border-top-right-radius: 8px;
            box-shadow: 3px 3px 12px rgba(0,0,0,0.4);
            display: none; flex-direction: column; z-index: 10;
        }
        /* Thanh tiêu đề dốc màu xanh lượn sóng */
        .title-bar {
            background: linear-gradient(to bottom, #0058e6 0%, #0073ea 12%, #0058e6 88%, #0044b3 100%);
            height: 28px; display: flex; align-items: center; justify-content: space-between;
            padding: 0 8px; color: white; font-weight: bold; font-size: 12px;
            text-shadow: 1px 1px 1px rgba(0,0,0,0.5);
            border-top-left-radius: 5px; border-top-right-radius: 5px;
        }
        .title-text { display: flex; align-items: center; gap: 6px; }
        .window-buttons { display: flex; gap: 4px; }
        
        /* 3 Nút bấm đóng/mở huyền thoại */
        .win-btn {
            width: 21px; height: 21px; border-radius: 3px; cursor: pointer;
            font-weight: bold; font-size: 11px; display: flex; align-items: center; justify-content: center;
            color: white; border: 1px solid rgba(0,0,0,0.4);
        }
        .btn-min { background: linear-gradient(to bottom, #2d7af4, #004cb3); }
        .btn-max { background: linear-gradient(to bottom, #2d7af4, #004cb3); }
        .btn-close {
            background: linear-gradient(to bottom, #e76043 0%, #e74322 15%, #b32d14 100%);
            border-color: #7c1a0c; font-size: 12px;
        }
        .win-btn:hover { filter: brightness(1.2); }
        
        .menu-bar {
            background: #F1EEE4; border-bottom: 1px solid #D2CFBB;
            padding: 3px 10px; font-size: 11px; color: #000; display: flex; gap: 12px;
        }
        .menu-item:hover { background: #316AC5; color: white; cursor: pointer; }
        
        .window-content {
            padding: 12px; flex-grow: 1; overflow: auto;
            font-size: 12px; color: #000; background: #FFF; margin: 4px;
            border: 1px solid #7F9DB9;
        }

        /* THANH TASKBAR PHÍA DƯỚI */
        #taskbar {
            width: 100vw; height: 40px;
            background: linear-gradient(to bottom, #245edb 0%, #3f8cf3 9%, #245edb 18%, #1b4ca3 100%);
            position: absolute; bottom: 0; left: 0;
            display: flex; align-items: center; justify-content: space-between; z-index: 100;
            border-top: 1px solid #174291;
        }
        
        /* Nút Start màu xanh lá lượn sóng */
        #start-btn {
            background: linear-gradient(to bottom, #388e3c 0%, #5cb85c 10%, #388e3c 90%, #225e25 100%);
            height: 100%; padding: 0 25px; display: flex; align-items: center; gap: 6px;
            color: white; font-weight: bold; font-style: italic; font-size: 16px;
            cursor: pointer; border-top-right-radius: 8px; border-bottom-right-radius: 8px;
            box-shadow: 2px 0 5px rgba(0,0,0,0.4); border: none;
            text-shadow: 1px 1px 1px #114013;
        }
        #start-btn:hover { filter: brightness(1.15); }

        /* BẢNG START MENU THẬT CHIA 2 CỘT */
        #start-menu {
            position: absolute; bottom: 40px; left: 0; width: 380px; height: 440px;
            background: #FFF; border: 2px solid #0054E3; border-top-right-radius: 5px;
            box-shadow: 5px -5px 15px rgba(0,0,0,0.5); display: none; z-index: 200;
            flex-direction: column;
        }
        .start-menu-header {
            background: linear-gradient(to bottom, #1c5ae3 0%, #4487f7 100%);
            height: 50px; display: flex; align-items: center; padding: 0 15px;
            color: white; font-weight: bold; font-size: 14px; gap: 10px;
        }
        .start-menu-body { display: flex; flex-grow: 1; height: calc(100% - 95px); }
        .start-left { width: 55%; background: #FFF; padding: 10px; display: flex; flex-direction: column; gap: 10px; }
        .start-right { width: 45%; background: #CBDAF4; border-left: 1px solid #99B4E3; padding: 10px; display: flex; flex-direction: column; gap: 12px; font-size: 11px; }
        .start-item { display: flex; align-items: center; gap: 8px; cursor: pointer; padding: 4px; font-size: 11px; color:#000; }
        .start-item:hover { background: #316AC5; color: white; }
        .start-menu-footer {
            background: linear-gradient(to bottom, #4487f7 0%, #1c5ae3 100%);
            height: 45px; display: flex; justify-content: flex-end; align-items: center; padding: 0 15px;
        }
        .logoff-btn { background: #ff9800; border: 1px solid #fff; color: white; padding: 4px 12px; font-weight: bold; cursor: pointer; font-size: 11px; border-radius: 2px; }

        /* Khay hệ thống và đồng hồ */
        #system-tray {
            background: linear-gradient(to bottom, #0c8df6 0%, #1ea1fc 9%, #0c8df6 18%, #045cb4 100%);
            height: 100%; padding: 0 15px; display: flex; align-items: center;
            color: white; font-size: 11px; border-left: 1px solid #084c8c; gap: 12px;
        }
    </style>
</head>
<body>

    <div id="desktop">
        <!-- Icons ngoài desktop vẽ hoàn toàn bằng mã đồ họa SVG -->
        <div class="desktop-icon" onclick="openWindow('my-computer')">
            <svg class="svg-icon" viewBox="0 0 24 24"><path fill="#007acc" d="M4,6H20V16H4V6M2,4A2,2 0 0,0 0,6V16A2,2 0 0,0 2,18H10V20H8V22H16V20H14V18H22A2,2 0 0,0 24,16V6A2,2 0 0,0 22,4H2M4,8H20V14H4V8Z"/></svg>
            <span>My Computer</span>
        </div>
        <div class="desktop-icon" onclick="openWindow('internet-explorer')">
            <svg class="svg-icon" viewBox="0 0 24 24"><path fill="#008080" d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12C20,13.62 19.5,15.14 18.68,16.4L13,10.72V7H11V10.3L6.4,5.7C7.94,4.64 9.89,4 12,4M4,12C4,10.55 4.4,9.2 5.1,8.05L11.5,14.45V18.5H12.5C14.76,18.5 16.74,17.22 17.72,15.34L13.88,11.5H16V9.5H11.88L6.2,3.82C5,5.1 4.24,6.71 4.07,8.5H6V10.5H4.07C4.03,11 4,11.5 4,12Z"/></svg>
            <span>Internet Explorer</span>
        </div>

        <!-- BẢNG START MENU CHUẨN -->
        <div id="start-menu">
            <div class="start-menu-header">
                <svg width="24" height="24" viewBox="0 0 24 24"><path fill="#fff" d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4M12,18c-2.67,0-8,1.34-8,4v-2c0-2.66,5.33-4,8-4s8,1.34,8,4v2C20,19.34 14.67,18 12,18Z"/></svg>
                <span>Administrator</span>
            </div>
            <div class="start-menu-body">
                <div class="start-left">
                    <div class="start-item" onclick="openWindow('internet-explorer'); toggleStartMenu();">
                        <strong>Internet Explorer</strong>
                    </div>
                    <div class="start-item" onclick="alert('Mở Windows Media Player...'); toggleStartMenu();">
                        <span>Windows Media Player</span>
                    </div>
                </div>
                <div class="start-right">
                    <div class="start-item" onclick="openWindow('my-computer'); toggleStartMenu();" style="font-weight:bold;">My Computer</div>
                    <div class="start-item" onclick="alert('Đang truy cập Control Panel...')">Control Panel</div>
                </div>
            </div>
            <div class="start-menu-footer">
                <button class="logoff-btn" onclick="location.reload()">Turn Off Computer 🔴</button>
            </div>
        </div>

        <!-- CỬA SỔ MY COMPUTER CHUẨN LUNA -->
        <div class="window" id="my-computer" style="left: 100px; top: 60px;">
            <div class="title-bar">
                <div class="title-text">
                    <span>My Computer</span>
                </div>
                <div class="window-buttons">
                    <div class="win-btn btn-min">0</div>
                    <div class="win-btn btn-max">🗖</div>


