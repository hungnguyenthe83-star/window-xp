import streamlit as st

# 1. Cấu hình giao diện chuẩn hóa cho khung hiển thị Streamlit Cloud
st.set_page_config(
    page_title="Windows XP Emulator Pro", 
    page_icon="💾", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("📟 Trình Giả Lập Windows XP Professional Edition")
st.caption("Giao diện Luna được tái hiện chính xác từng pixel bằng CSS/HTML nguyên bản.")

# 2. Toàn bộ mã nguồn giao diện hệ điều hành Windows XP
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
        
        /* HỆ THỐNG ICON TRÊN DESKTOP */
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
        .svg-icon { width: 34px; height: 34px; }

        /* CỬA SỔ CHUẨN WINDOWS XP LUNA 100% */
        .window {
            position: absolute; width: 480px; height: 340px;
            background: #F1EEE4; border: 3px solid #0054E3;
            border-top-left-radius: 8px; border-top-right-radius: 8px;
            box-shadow: 4px 4px 15px rgba(0,0,0,0.4); display: none; flex-direction: column; z-index: 10;
        }
        /* Thanh tiêu đề dốc màu xanh lượn sóng */
        .title-bar {
            background: linear-gradient(to bottom, #0058e6 0%, #0073ea 12%, #0058e6 88%, #0044b3 100%);
            height: 30px; display: flex; align-items: center; justify-content: space-between;
            padding: 0 8px; color: white; font-weight: bold; font-size: 12px; text-shadow: 1px 1px 1px rgba(0,0,0,0.5);
            border-top-left-radius: 5px; border-top-right-radius: 5px;
        }
        .title-text { display: flex; align-items: center; gap: 6px; }
        
        /* 3 Nút bấm đóng/mở huyền thoại đổ bóng 3D */
        .window-buttons { display: flex; gap: 3px; }
        .win-btn {
            width: 21px; height: 21px; border-radius: 3px; cursor: pointer;
            font-weight: bold; font-size: 12px; display: flex; align-items: center; justify-content: center;
            color: white; border: 1px solid rgba(0,0,0,0.6); box-shadow: inset 1px 1px 1px rgba(255,255,255,0.4);
        }
        .btn-min { background: linear-gradient(to bottom, #3c8bf0, #05419e); }
        .btn-max { background: linear-gradient(to bottom, #3c8bf0, #05419e); }
        .btn-close { background: linear-gradient(to bottom, #e76043 0%, #e74322 15%, #b32d14 100%); border-color: #7c1a0c; }
        .win-btn:hover { filter: brightness(1.2); }
        
        /* Thanh menu ứng dụng cổ điển */
        .menu-bar {
            background: #F1EEE4; border-bottom: 1px solid #D2CFBB;
            padding: 4px 10px; font-size: 11px; color: #000; display: flex; gap: 15px;
        }
        .menu-item { cursor: pointer; padding: 2px 5px; border-radius: 2px; }
        .menu-item:hover { background: #316AC5; color: white; }
        
        .window-content {
            padding: 12px; flex-grow: 1; overflow: auto; font-size: 12px; color: #000;
            background: #FFF; margin: 4px; border: 1px solid #7F9DB9;
        }

        /* THANH TASKBAR PHÍA DƯỚI */
        #taskbar {
            width: 100vw; height: 40px;
            background: linear-gradient(to bottom, #245edb 0%, #3f8cf3 9%, #245edb 18%, #1b4ca3 100%);
            position: absolute; bottom: 0; left: 0; display: flex;
            align-items: center; justify-content: space-between; z-index: 100; border-top: 1px solid #174291;
        }
        
        /* Nút Start màu xanh lá lượn sóng */
        #start-btn {
            background: linear-gradient(to bottom, #388e3c 0%, #5cb85c 10%, #388e3c 90%, #225e25 100%);
            height: 100%; padding: 0 24px; display: flex; align-items: center; gap: 8px; color: white;
            font-weight: bold; font-style: italic; font-size: 16px; cursor: pointer;
            border-top-right-radius: 8px; border-bottom-right-radius: 8px; box-shadow: 2px 0 5px rgba(0,0,0,0.4); border: none;
            text-shadow: 1px 1px 1px #114013;
        }
        #start-btn:hover { filter: brightness(1.15); }
        #start-btn svg { width: 16px; height: 16px; }

        /* BẢNG START MENU THẬT CHUẨN CẤU TRÚC 2 CỘT GỐC */
        #start-menu {
            position: absolute; bottom: 40px; left: 0; width: 380px; height: 440px;
            background: #FFF; border: 2px solid #0054E3; border-top-right-radius: 5px;
            box-shadow: 5px -5px 15px rgba(0,0,0,0.5); display: none; z-index: 200;
            flex-direction: column;
        }
        .start-header {
            background: linear-gradient(to bottom, #1c5ae3 0%, #4487f7 100%);
            height: 55px; display: flex; align-items: center; padding: 0 15px;
            color: white; font-weight: bold; font-size: 14px; gap: 12px;
            border-bottom: 1px solid #174291;
        }
        .start-header-avatar {
            width: 34px; height: 34px; background: #fff; border: 2px solid #fff; border-radius: 4px;
            display: flex; align-items: center; justify-content: center; font-size: 20px;
        }
        .start-body { display: flex; flex-grow: 1; height: calc(100% - 100px); }
        .start-left { width: 55%; background: #FFF; padding: 10px 5px; display: flex; flex-direction: column; gap: 6px; }
        .start-right { width: 45%; background: #CBDAF4; border-left: 1px solid #99B4E3; padding: 10px; display: flex; flex-direction: column; gap: 12px; font-size: 11px; }
        .start-item { display: flex; align-items: center; gap: 8px; cursor: pointer; padding: 6px; font-size: 11px; color:#000; border-radius: 3px; }
        .start-item:hover { background: #316AC5; color: white; }
        .start-footer {
            background: linear-gradient(to bottom, #4487f7 0%, #1c5ae3 100%);
            height: 45px; display: flex; justify-content: flex-end; align-items: center; padding: 0 15px;
            border-top: 1px solid #174291;
        }
        .logoff-btn { background: #ff9800; border: 1px solid #fff; color: white; padding: 5px 12px; font-weight: bold; cursor: pointer; font-size: 11px; border-radius: 3px; box-shadow: 1px 1px 2px rgba(0,0,0,0.3); }
        .logoff-btn:hover { filter: brightness(1.1); }

        /* Khay hệ thống góc phải màu xanh nước biển */
        #system-tray {
            background: linear-gradient(to bottom, #0c8df6 0%, #1ea1fc 9%, #0c8df6 18%, #045cb4 100%);
            height: 100%; padding: 0 15px; display: flex; align-items: center; color: white; font-size: 11px;
            border-left: 1px solid #084c8c; gap: 8px;
        }
    </style>
</head>
<body>

    <div id="desktop">
        <!-- HỆ THỐNG ICON DESKTOP CHUẨN CỔ ĐIỂN -->
        <div class="desktop-icon" onclick="openWindow('my-computer')">
            <svg class="svg-icon" viewBox="0 0 24 24"><path fill="#ffb300" d="M20,18c1.1,0,2-0.9,2-2V6c0-1.1-0.9-2-2-2H4C2.9,4,2,4.9,2,6v10c0,1.1,0.9,2,2,2H0v2h24v-2H20z M4,6h16v10H4V6z"/></svg>
            <span>My Computer</span>
        </div>

        <div class="desktop-icon" onclick="openWindow('internet-explorer')">
            <svg class="svg-icon" viewBox="0 0 24 24"><path fill="#0288d1" d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12C20,13.62 19.5,15.14 18.68,16.4L13,10.72V7H11V10.3L6.4,5.7C7.94,4.64 9.89,4 12,4M4,12C4,10.55 4.4,9.2 5.1,8.05L11.5,14.45V18.5H12.5C14.76,18.5 16.74,17.22 17.72,15.34L13.88,11.5H16V9.5H11.88L6.2,3.82C5,5.1 4.24,6.71 4.07,8.5H6V10.5H4.07C4.03,11 4,11.5 4,12Z"/></svg>
            <span>Internet Explorer</span>
        </div>

        <!-- BẢNG START MENU THẬT CHUẨN 2 CỘT -->
        <div id="start-menu">
            <div class="start-header">
                <div class="start-header-avatar">👤</div>
                <span>Administrator</span>
            </div>
            <div class="start-body">
                <div class="start-left">
                    <div class="start-item" onclick="openWindow('internet-explorer'); toggleStartMenu();">
                        <svg width="16" height="16" viewBox="0 0 24 24"><path fill="#0288d1" d="M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,4A8,8 0 0,1 20,12C20,13.62 19.5,15.14 18.68,16.4L13,10.72V7H11V10.3L6.4,5.7C7.94,4.64 9.89,4 12,4"/></svg>
                        <strong>Internet Explorer</strong>
                    </div>
                    <div class="start-item" onclick="alert('Đang khởi động Windows Media Player...'); toggleStartMenu();">
                        🎬 <span>Windows Media Player</span>
                    </div>
                </div>
                <div class="start-right">
                    <div class="start-item" onclick="openWindow('my-computer'); toggleStartMenu();" style="font-weight:bold;">My Computer</div>
                    <div class="start-item" onclick="alert('Đang mở Control Panel...')">Control Panel</div>
                    <div class="start-item" onclick="alert('Đang kết nối Printers and Faxes...')">Printers and Faxes</div>
                </div>
